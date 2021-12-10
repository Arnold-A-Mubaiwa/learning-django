# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import  Pet,Vaccine

@admin.register(Pet)
class PetAdmin (admin.ModelAdmin):
    list_display =['name','species','breed','age','sex']

admin.site.register(Vaccine)