from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('',views.product_page,name='product_page')
]