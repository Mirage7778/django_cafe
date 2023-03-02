from django.shortcuts import render
from .models import DishCategory, Dish
from django.http import HttpResponse
# Create your views here.

def main_page(request):
    categories = DishCategory.objects.filter(is_visibl=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)

    return render(request, 'index.html')
