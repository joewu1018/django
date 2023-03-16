from django.db import models

# Create your models here.
class student(models.Model):
    stuName= models.CharField(max_length=50,null=False)
    stuID = models.CharField(max_length=10,null=False)
    stuSex=models.CharField(max_length=2,default="M",null=False)
    stuBirth=models.DateField(null=False)
    stuEmail=models.EmailField(max_length=100,blank=True,default="")
    stuPhone=models.CharField(max_length=20,blank=True,default="")
    stuAddress=models.CharField(max_length=255,blank=True,default="")


    def __str__(self):
        return self.stuName