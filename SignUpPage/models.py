from django.db import models
from django.contrib.auth.models import User
class Index(models.Model):
    username=models.CharField(max_length=120, null=True, blank=True)
    fname=models.CharField(max_length=120, null=True, blank=True)
    lname=models.CharField(max_length=120, null=True, blank=True)
    email=models.CharField(max_length=120, null=True, blank=True)
    password1=models.CharField(max_length=120, null=True, blank=True)
    password2=models.CharField(max_length=120, null=True, blank=True)
    state=models.CharField(max_length=120, null=True, blank=True)
    address=models.CharField(max_length=120, null=True, blank=True)
    pincode=models.IntegerField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.name
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg' , upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'