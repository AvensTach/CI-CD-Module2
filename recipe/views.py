from django.shortcuts import render
from django.db.models import Count
from .models import Recipe, Category # Переконайтеся, що імпортували моделі

def main(request):
    """Відображає останні 5 створених рецептів."""
    # Припускаємо, що модель Recipe має поле created_at
    recent_recipes = Recipe.objects.all().order_by('-created_at')[:5]
    return render(request, 'main.html', {'recent_recipes': recent_recipes})