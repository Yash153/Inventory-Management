from django.db import models
from django.db.models.deletion import CASCADE

class LocationModel(models.Model):
    dt = models.DateTimeField(auto_now_add = True,null=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    location = models.ForeignKey(LocationModel, on_delete=CASCADE)
    name = models.CharField(max_length=255)
    dt = models.DateTimeField(auto_now_add = True,null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class MovementModel(models.Model):
    dt = models.DateTimeField(auto_now_add = True,null=True)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
