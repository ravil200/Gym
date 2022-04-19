from django.db import models

class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Classes(models.Model):
    class_name = models.CharField(max_length=255)
    trainer_name = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    class_image = models.ImageField()

    def __str__(self) -> str:
        return self.class_name

class Schedules(models.Model):
    name = models.ForeignKey(Classes, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self) -> str:
        return self.name 

class Contact(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name