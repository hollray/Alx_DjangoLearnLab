from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Department(models.Model):
    """
    Represents a department within the company.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Role(models.Model):
    """
    Model representing different roles in the organization.
    """
    # Using choices to restrict the available roles
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('HR Staff', 'HR Staff'),
        ('Customized', 'Customized'),
    )
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    """
    Custom User model to add a 'role' field.
    This model inherits all fields from Django's AbstractUser.
    """
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Employee(models.Model):
    """
    Represents an employee, linked to a department.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profile(models.Model):
    """
    A user profile model to hold additional information.
    This model has a one-to-one relationship with the custom user model.
    """
    # This field now correctly references the custom user model using AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
