from django.db import models
from django.utils import timezone


class Dog(models.Model):
    name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    description = models.TextField(blank=True)
    guardian = models.ForeignKey('Guardian', blank=True, null=True, on_delete=models.SET_NULL)
    fixed = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} (Dog)'


class Guardian(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.name} (Guardian)'


class Payment(models.Model):
    sum = models.FloatField()
    currency = models.CharField(max_length=5)
    datetime = models.DateTimeField(default=timezone.now)
    payer = models.TextField(blank=True)
    purpose = models.ManyToManyField(Dog, blank=True)

    def __str__(self):
        return f'{self.sum} {self.currency}'


