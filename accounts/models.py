from django.db import models

# Create your models here.
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class Country(models.Model):
    name = models.CharField(max_length=100, default='c')

    def __str__(self):
        return ("{}".format(self.name))


class City(models.Model):
    name = models.CharField(max_length=100 ,default='c')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return ("{} ({})".format(self.name, self.country.name))


class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, default='g')
    age = models.IntegerField(default=0)
    country = models.IntegerField(default=1)
    city = models.IntegerField(default=1)

    def __str__(self):
        return ("{} ({} {})".format(self.user.email, self.user.first_name, self.user.last_name))


class Sale(models.Model):
    product = models.CharField(max_length=50, default='p')
    revenue = models.CharField(max_length=50, default='p')
    sales_number = models.IntegerField(default=0)