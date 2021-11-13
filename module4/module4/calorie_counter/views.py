from django.shortcuts import render
from django.http import HttpResponse
from .models import Foods

posts = [
    {
        'food': 'Hot dog',
        'calories': '151'
    },
    {
        'food': 'Hamburger',
        'calories': '354'
    }
]

# def all_foods(request):
#     food_list = Foods.objects.all()
#     return render(request, 'counter/home.html', {'food_list': food_list})

def calorie_counter(request):
    # food_list = Foods.objects.all()
    context = {
        'author': 'Colton Kramer',
        'posts': posts,
        # 'food_list': food_list
    }
    return render(request, 'counter/home.html', context)

# , {'food_list': food_list}

def about(request):
        return render(request, 'counter/about.html', {'title': 'About'})

        # <!-- {% for food in foods %}
        # {{food}}
        # {% endfor %} -->
