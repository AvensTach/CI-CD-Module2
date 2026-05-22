import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_recipe.settings')
django.setup()

from recipe.models import Category, Recipe


def populate_real_data():
    # 1. Define specific categories
    categories = ['Breakfast', 'Main Course', 'Desserts', 'Salads']
    category_objs = {}

    print("Creating categories...")
    for name in categories:
        cat, created = Category.objects.get_or_create(name=name)
        category_objs[name] = cat
        if created:
            print(f" - Created: {name}")

    # 2. Define realistic recipe data
    recipes_data = [
        {
            "title": "Classic Fluffy Pancakes",
            "category": "Breakfast",
            "description": "Soft, fluffy, and delicious pancakes perfect for a weekend morning.",
            "ingredients": "1 cup flour, 2 tbsp sugar, 1 cup milk, 1 egg, 2 tbsp butter, 1 tsp baking powder.",
            "instructions": "1. Mix dry ingredients.\n2. Add wet ingredients and whisk.\n3. Pour batter onto a hot pan.\n4. Flip when bubbles form. Serve with syrup."
        },
        {
            "title": "Spaghetti Bolognese",
            "category": "Main Course",
            "description": "A traditional Italian meat sauce poured over al dente spaghetti.",
            "ingredients": "200g spaghetti, 300g ground beef, 1 onion, 2 cloves garlic, 400g crushed tomatoes, olive oil.",
            "instructions": "1. Boil pasta in salted water.\n2. Sauté onion and garlic in oil.\n3. Brown the beef.\n4. Add crushed tomatoes and simmer for 20 mins.\n5. Mix with pasta."
        },
        {
            "title": "Chocolate Fudge Cake",
            "category": "Desserts",
            "description": "Rich, moist chocolate cake with a creamy fudge icing.",
            "ingredients": "2 cups sugar, 1.5 cups flour, 3/4 cup cocoa powder, 2 eggs, 1 cup milk, 1/2 cup oil.",
            "instructions": "1. Preheat oven to 350F (175C).\n2. Mix dry ingredients together.\n3. Add wet ingredients and beat well.\n4. Bake for 30-35 mins. Let cool before frosting."
        },
        {
            "title": "Fresh Caesar Salad",
            "category": "Salads",
            "description": "Crisp romaine lettuce, crunchy croutons, and parmesan cheese tossed in Caesar dressing.",
            "ingredients": "Romaine lettuce, croutons, parmesan cheese, Caesar dressing, black pepper.",
            "instructions": "1. Chop lettuce into bite-sized pieces.\n2. Toss generously with dressing.\n3. Top with croutons and freshly grated parmesan."
        },
        {
            "title": "Avocado Toast with Egg",
            "category": "Breakfast",
            "description": "A quick, healthy, and protein-packed breakfast to start your day right.",
            "ingredients": "2 slices sourdough bread, 1 avocado, 2 eggs, salt, pepper, red pepper flakes.",
            "instructions": "1. Toast the bread to your liking.\n2. Mash the avocado and spread it on the toast.\n3. Fry or poach the eggs and place on top.\n4. Season with salt, pepper, and chili flakes."
        }
    ]

    print("\nCreating recipes...")
    for data in recipes_data:
        # get_or_create checks if a recipe with this title already exists.
        # The 'defaults' dictionary is only used if the recipe needs to be created.
        recipe, created = Recipe.objects.get_or_create(
            title=data['title'],
            defaults={
                'description': data['description'],
                'ingredients': data['ingredients'],
                'instructions': data['instructions'],
                'category': category_objs[data['category']]
            }
        )
        if created:
            print(f" - Added recipe: {recipe.title}")
        else:
            print(f" - Skipped (already exists): {recipe.title}")


if __name__ == '__main__':
    print("Starting database population script...")
    populate_real_data()
    print("\nDatabase populated successfully!")