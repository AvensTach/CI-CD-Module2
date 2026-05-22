from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category


class RecipeViewsTest(TestCase):
    def setUp(self):
        # Створюємо тестову категорію
        self.category = Category.objects.create(name="Test Category")

        # Створюємо 6 тестових рецептів, щоб перевірити ліміт у 5 на головній сторінці.
        # Обов'язково заповнюємо всі текстові поля моделі.
        for i in range(6):
            Recipe.objects.create(
                title=f"Test Recipe {i}",
                description="Test description",
                instructions="Test instructions",
                ingredients="Test ingredients",
                category=self.category
            )

    def test_main_view(self):
        # Робимо GET-запит на головну сторінку
        response = self.client.get(reverse('main'))

        # Перевіряємо статус код та використаний шаблон
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

        # Перевіряємо наявність потрібного ключа в контексті
        self.assertIn('recipes', response.context)

        # Перевіряємо, що повернулося рівно 5 рецептів із 6 існуючих
        self.assertEqual(len(response.context['recipes']), 5)

    def test_category_list_view(self):
        # Робимо GET-запит на сторінку категорій
        response = self.client.get(reverse('category_list'))

        # Перевіряємо статус код та використаний шаблон
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')

        # Перевіряємо наявність потрібного ключа в контексті
        self.assertIn('categories', response.context)

        # Отримуємо QuerySet категорій з контексту
        categories = response.context['categories']
        self.assertEqual(categories.count(), 1)

        # Перевіряємо, що анотація Count працює правильно і бачить 6 рецептів
        first_category = categories.first()
        self.assertTrue(hasattr(first_category, 'recipe_count'))
        self.assertEqual(first_category.recipe_count, 6)