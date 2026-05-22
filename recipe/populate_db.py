import os
import django
import random

# Налаштовуємо середовище Django для цього скрипта
# Зверніть увагу: 'project_recipe.settings' має відповідати назві вашої головної папки з налаштуваннями
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_recipe.settings')
django.setup()

# Імпортуємо моделі тільки ПІСЛЯ налаштування django
from recipe.models import Category, Recipe


def populate():
    # 1. Створюємо кілька тестових категорій
    category_names = ['Breakfast', 'Lunch', 'Dinner', 'Desserts', 'Vegan', 'Drinks']
    categories = []

    print("Creating categories...")
    for name in category_names:
        # get_or_create запобігає дублюванню, якщо скрипт запустити двічі
        category, created = Category.objects.get_or_create(name=name)
        categories.append(category)
        if created:
            print(f" - Added category: {name}")

    # 2. Генеруємо випадкові дані для рецептів
    adjectives = ['Spicy', 'Sweet', 'Savory', 'Quick', 'Easy', 'Healthy', 'Classic', 'Baked']
    nouns = ['Chicken', 'Beef', 'Pasta', 'Salad', 'Cake', 'Soup', 'Tacos', 'Pancakes']

    print("\nCreating random recipes...")
    for i in range(15):  # Змініть число, щоб створити більше або менше рецептів
        title = f"{random.choice(adjectives)} {random.choice(nouns)} {random.randint(1, 99)}"
        category = random.choice(categories)

        recipe = Recipe.objects.create(
            title=title,
            description=f"This is a wonderfully {random.choice(adjectives).lower()} dish perfect for any occasion.",
            instructions="Step 1: Prepare ingredients.\nStep 2: Cook for 20 minutes.\nStep 3: Serve and enjoy!",
            ingredients="Salt, Pepper, Water, Love, " + random.choice(nouns),
            category=category
        )
        print(f" - Added recipe: {recipe.title} (Category: {category.name})")


if __name__ == '__main__':
    print("Starting database population script...")
    populate()
    print("\nDatabase populated successfully!")