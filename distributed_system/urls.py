from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_order/', views.add_order, name='add_order'),
]
