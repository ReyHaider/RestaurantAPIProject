from django.test import TestCase
from restaurant import views
from restaurant.models import Menu
from django.urls import reverse
import json
import decimal


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Biryani", price=8, inventory=20)
        Menu.objects.create(title="Pizza", price=10, inventory=20)

    def test_getall(self):
        # Retrieve all the Menu objects
        # Replace 'menu-list' with the actual URL name
        response = self.client.get(
            reverse('menu-items'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the response content
        serialized_data = json.loads(response.content)
        serialized_data[0]['price'] = decimal.Decimal(
            serialized_data[0]['price'])
        serialized_data[1]['price'] = decimal.Decimal(
            serialized_data[1]['price'])

        # Retrieve all Menu objects created in the setUp method
        menus = Menu.objects.all()

        # Serialize the Menu objects
        serialized_menus = []
        for menu in menus:

            serialized_menu = {
                'id': menu.id,
                'title': menu.title,
                'price': menu.price,
                'inventory': menu.inventory
            }
            serialized_menus.append(serialized_menu)

        # Check if the serialized data equals the response content
        self.assertEqual(serialized_data, serialized_menus)
