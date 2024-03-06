from django.db import models

class Outlet(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    flavors = models.TextField()  
    
    def __str__(self):
        return self.name