from django.db import models

# Create your models here.

class UserList(models.Model) :
     name = models.CharField(max_length = 250)
     address = models.CharField(max_length = 500)
     
     

     




