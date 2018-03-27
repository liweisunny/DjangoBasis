from django.db import models

# Create your models here.
class UserInfo(models.Model):
    class Meta:
        db_table='user_info'
    username=models.CharField(max_length=30,blank=True)
    password=models.CharField(max_length=30,blank=True)

