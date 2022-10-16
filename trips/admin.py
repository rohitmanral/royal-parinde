from django.contrib import admin
from . models import Trip

from django.utils. html import format_html

# Register your models here.


class TripAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Trip Image'
    list_display= ('id','thumbnail','destination', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'destination',)
    list_editable= ('is_featured',)

admin.site.register(Trip, TripAdmin)
