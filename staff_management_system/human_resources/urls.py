from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet

# Created a router and registered viewsets with it.
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'employees', EmployeeViewSet, basename='employee')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]