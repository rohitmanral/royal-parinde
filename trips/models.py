from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Trip(models.Model):

    destination = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    location = RichTextField()
    key_place = RichTextField()
    price = models.IntegerField()
    meal = models.CharField(max_length=255)
    accomodation = models.CharField(max_length=255)
    transport = models.CharField(max_length=255)
    pick_drop = models.CharField(max_length=255)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.destination
