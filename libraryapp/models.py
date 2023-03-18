from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=50)      
    def __str__(self):
          return self.name                           


class Users(models.Model):
    name = models.CharField(max_length=50)                                 
    surname = models.CharField(max_length=50)   
    email = models.CharField(max_length=50)      
    username = models.CharField(max_length=50) 
    password = models.CharField(max_length=50) 
    books=models.ForeignKey(Books,on_delete=models.CASCADE,null=True)

    def __str__(self):
             return f"{self.name} {self.surname}"