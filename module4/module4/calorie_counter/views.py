from django.shortcuts import render
from django.http import HttpResponse
from .models import Foods

def calorie_counter(request):
    food_list = Foods.objects.all()
    context = {
        'author': 'Colton Kramer',
        'food_list': food_list
    }
    return render(request, 'counter/home.html', context)

# , {'food_list': food_list}

def about(request):
        return render(request, 'counter/about.html', {'title': 'About'})
