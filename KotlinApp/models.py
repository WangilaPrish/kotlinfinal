from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=100)
    yob = models.DateField()
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateTimeField()
    department = models.CharField(max_length=30)
    doctor = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Account(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title