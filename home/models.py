from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email
    
    
    
class Plus(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=14)
    title=models.CharField(max_length=255)
    content=models.TextField()

    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return self.title + " by " + self.name
