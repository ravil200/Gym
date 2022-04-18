from tabnanny import verbose
from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name 

class Classes(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.title