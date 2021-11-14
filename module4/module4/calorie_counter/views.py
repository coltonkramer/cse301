from django.shortcuts import render
from django.http import HttpResponse
from .models import Foods
from calorie_counter.models import Foods

def calorie_counter(request):
    if request.method == "POST":
        food = request.POST['food']
        calories = request.POST['calories']
        print(food, calories)
        ins = Foods(food=food, calories=calories)
        ins.save()

    food_list = Foods.objects.all()
    context = {
        'author': 'Colton Kramer',
        'food_list': food_list,
    }
    return render(request, 'counter/home.html', context)


def about(request):
        return render(request, 'counter/about.html', {'title': 'About'})
