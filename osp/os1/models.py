from django.db import models
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# Create your models here.
class User(models.Model):
    rows=models.IntegerField()
    columns=models.IntegerField()
    max_allocation_matrix=models.CharField(max_length=128)
    allocation_matrix=models.CharField(max_length=128)
    available_vector=models.CharField(max_length=128)
    available_vector1=models.CharField(max_length=128)
