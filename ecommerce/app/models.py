from django.db import models

# Create your models here.
class Users(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=250)
    name=models.CharField(max_length=35)
    last_login=models.DateTimeField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['email','password']
    
    def __str__(self):
        return self.email
