from django.contrib import admin
from .models import *


class Animals_admin(admin.ModelAdmin):
    list_display = 'name'


class breed_Admin(admin.ModelAdmin):
    list_display = ('animal', 'name')


admin.site.register(Animal)
admin.site.register(Breed)
# admin.site.register(Animal_data)
