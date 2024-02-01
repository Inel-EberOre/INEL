from django.db import models

# from django.contrib.auth.models import User -> Ya no trabajamos con User sino con AbstractUser
from django.contrib.auth.models import AbstractUser

# AbstractUser (campos)
# username
# first_name
# last_name
# email
# password
# groups
# user_permissions
# is_staff
# is_active
# is_superuser
# last_login
# date_joined

# #AbstractBaseUser (campos)
# id
# password
# last_login

class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    def has_shipping_address(self):
        return self.shipping_address is not None

class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Si un usuario se elimina que también se elimine el registro Profile
    bio = models.TextField()