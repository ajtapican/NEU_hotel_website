from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(default=False)
    zip = models.PositiveIntegerField(default=False)

    def __str__(self):
        return self.name