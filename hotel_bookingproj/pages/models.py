from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(default=0)
    state = models.CharField(max_length=2)
    zip = models.PositiveIntegerField(default=0)
    comments = models.TextField()	
    name1 = models.CharField(max_length=50)
    cnumber = models.PositiveIntegerField(default=0)
    expm = models.CharField(max_length=50)
    expy = models.PositiveIntegerField(default=0)
    cvv = models.PositiveIntegerField(default=0)
    arrive = models.DateTimeField()
    depart = models.DateTimeField()
    guest = models.PositiveIntegerField(default=0)
    rooms = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name