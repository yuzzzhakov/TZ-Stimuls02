from django.db import models
from PIL import Image
from django.utils import timezone


class Dog(models.Model):
    name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    image = models.ImageField(default='default.jpg', upload_to='dog_pics')
    description = models.TextField(blank=True)
    guardian = models.ForeignKey('Guardian', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} (Dog)'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Guardian(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()


class Payment(models.Model):
    sum = models.FloatField()
    currency = models.CharField(max_length=5)
    datetime = models.DateTimeField(default=timezone.now)
    payer = models.TextField(blank=True)
    purpose = models.ManyToManyField(Dog)


