"""IMproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from IMapp.views import delete_location, delete_product, product, location, movement, stock, add_product, add_location, view_product, view_location, edit_product, save_changes_product, edit_location, save_changes_location, movement, movementhistory, stock_location, stock_product, delete_location, delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product, name="product"),
    path('stock/', stock, name="stock"),
    path('product/', product, name="product"),
    path('location/', location, name="location"),
    path('movement/', movement, name="movement"),
    path('product/add_product/', add_product, name="add_product"),
    path('add_product/', add_product, name="add_product"),
    path('location/add_location/', add_location, name="add_location"),
    path('view/<int:id>',view_product, name="view_product"),
    path('product/view/<int:id>',view_product, name="view_product"),
    path('location/view/<int:id>',view_location, name="view_location"),
    path('product/edit/<int:id>',edit_product, name="edit_product"),
    path('edit/<int:id>',edit_product, name="edit_product"),
    path('product/edit/save_changes_product', save_changes_product, name="save_changes_product"),
    path('edit/save_changes_product', save_changes_product, name="save_changes_product"),
    path('location/edit/<int:id>', edit_location, name="edit_location"),
    path('location/edit/save_changes_location', save_changes_location, name="save_changes_location"),
    path("product/edit/delete/<int:id>", delete_product, name="delete_product"),
    path("location/edit/delete/<int:id>", delete_location, name="delete_location"),
    path('movement/', movement, name="movement"),
    path("stock/", stock, name="stock"),
    path("movementhistory/", movementhistory, name="movementhistory"),
    path("stock_location/", stock_location, name="stock_location"),
    path("stock_product/", stock_product, name="stock_product"),

]
