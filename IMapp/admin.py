from django.contrib import admin
from django.contrib.admin.decorators import register
from django.shortcuts import render
from .models import ProductModel,LocationModel,MovementModel

admin.site.register(ProductModel)
admin.site.register(LocationModel)
admin.site.register(MovementModel)
