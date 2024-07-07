from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('', views.home, name="home"),
    #Add product
    path('add_product', views.add_product, name="add_product"),
    #View the product individually
    path('product/<str:product_id>', views.product, name="product"),
    #Edit product
    path('edit_product', views.edit_product, name="edit_product"),
    #Delete product
    path('delete_product/<str:product_id>', views.delete_product, name="delete_product")
]
