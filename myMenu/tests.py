from django.test import TestCase
from .models import Menu
from django.contrib.auth import get_user_model


# Create your tests here.
class MenuTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        test_thing = Menu.objects.create(restaurant=testuser1, title="Cheeseburger", price=4, description="Meat patty, tomato, ketchup, pickles")
        test_thing.save()

    def test_things_model(self):
        menu_1 = Menu.objects.get(id=1)
        actual_restaurant = str(menu_1.restaurant)
        actual_title = str(menu_1.title)
        actual_description = str(menu_1.description)
        self.assertEqual(actual_restaurant, "testuser1")
        self.assertEqual(actual_title, "Cheeseburger")
        self.assertEqual(actual_description, "Meat patty, tomato, ketchup, pickles")