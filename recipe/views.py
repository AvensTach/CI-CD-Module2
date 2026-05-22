from django.shortcuts import render
from django.db.models import Count
from .models import Recipe, Category

def main(request):
    recent_recipes = Recipe.objects.all().order_by('-created_at')[:5]
    return render(request, 'main.html', {'recent_recipes': recent_recipes})

def category_list(request):
    categories = Category.objects.annotate(recipe_count=Count('categories'))
    return render(request, 'category_list.html', {'categories': categories})
