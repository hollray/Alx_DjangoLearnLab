from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Department, Employee, Role
from .serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.


# --- Custom Permission Classes ---
# These classes will check the user's role and grant or deny access accordingly.
# The user's role is expected to be an attribute of the User model.
class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access a view.
    """
    def has_permission(self, request, view):
        # A user has admin permission if their role is 'Admin'.
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'Admin'
        
class IsHRStaff(permissions.BasePermission):
    """
    Custom permission to only allow HR Staff users to view (read-only) data.
    """
    def has_permission(self, request, view):
        # HR Staff can only perform safe methods (GET, HEAD, OPTIONS).
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'HR Staff'


class IsCustomized(permissions.BasePermission):
    """
    Custom permission for a customized role.
    - Can view records (safe methods).
    - Can create new staff (POST).
    """
    def has_permission(self, request, view):
        # Customized users can perform safe methods and POST requests.
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'Employee'


# --- ViewSets with Permissions Applied ---
# These ViewSets use a `permission_classes` list to apply the new security rules.
# The order of the classes matters, so `IsAuthenticated` is checked first.
class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed, created, edited, or deleted.
    - Only Admin has full access (CRUD).
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    # Department-related actions are restricted to Admin users only.
    # The `permission_classes` list handles this for all methods.
   

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed, created, edited, or deleted.
    - Admin: Full access (CRUD).
    - HR Staff: Read-only access.
    - Customized: Read and Create access.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin | IsHRStaff | IsCustomized]

    def get_permissions(self):
        """
        Instantiate and return the list of permissions that this view requires.
        This method allows for more granular control over permissions.
        """
        if self.action in ['list', 'retrieve']:
            # All roles can list and retrieve employees.
            self.permission_classes = [permissions.IsAuthenticated, IsAdmin | IsHRStaff | IsCustomized]
        elif self.action == 'create':
            # Only Admin and Customized roles can create.
            self.permission_classes = [permissions.IsAuthenticated, IsAdmin | IsCustomized]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Only Admin can update or destroy.
            self.permission_classes = [permissions.IsAuthenticated, IsAdmin]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in self.permission_classes]




