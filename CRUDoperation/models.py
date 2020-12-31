from django.db import models

class EmpDetails(models.Model):
    empname = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100) 
    occupation = models.CharField(max_length= 100)
    salary = models.IntegerField()
    class Meta:
        db_table ="Employee"  