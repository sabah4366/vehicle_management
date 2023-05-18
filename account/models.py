
from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group
class User(AbstractUser):
    USER_TYPES = [
        ('super_admin', 'Super Admin'),
        ('admin_user', 'Admin User'),
        ('user', 'User'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES,default='user')
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_set',
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )
