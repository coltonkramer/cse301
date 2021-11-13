from django.urls import path
from . import views



urlpatterns = [
    path('home', views.calorie_counter, name='calorie_counter'),
    path('about', views.about, name='calorie_counter_about'),

]

