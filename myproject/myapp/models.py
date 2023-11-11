from django.db import models

# Create your models here.
class Contact(models.Model):
    sno =models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    phone =models.CharField(max_length=13)
    Email =models.CharField(max_length=100)
    Content =models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
          return "Message from " + self.name 

class Blogs(models.Model):
    sno =models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    authname=models.CharField(max_length=50)
    slug = models.CharField(max_length=150)
    img=models.ImageField(upload_to='pics',blank=True,null=True)
    timeStamp=models.DateTimeField(blank=True)
    def __str__(self) :
        return f'Uploaded by  {self.authname}' 