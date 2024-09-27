
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('shopping/', views.im_hungry),
    path('index/', views.index)
]