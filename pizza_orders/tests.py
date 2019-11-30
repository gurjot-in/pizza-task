from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pizza_orders.models import Customer, Order, OrderItems


class PizzaTests(APITestCase):

    def setUp(self):
        customer = Customer.objects.create(
            phone_number='123', name='Gurjot', address='44 Enclave Berlin')
        order = Order.objects.create(customer=customer, order_status='pending')
        order_item = OrderItems.objects.create(
            order=order, pizza_flavour='Salami', pizza_size='Large', quantity='10')
        self.customer_id = customer.id
        self.order_id = order.id
        self.order_item_id = order_item.id

    def test_create_order_with_multiple_item_entries(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('orders-list')
        data = {
                "order_items": [
                    {
                    "pizza_flavour": "Marinara",
                    "pizza_size": "Large",
                    "quantity": 123
                    },
                    {
                    "pizza_flavour": "Salami",
                    "pizza_size": "Large",
                    "quantity": 123
                    },
                    {
                    "pizza_flavour": "Margarita",
                    "pizza_size": "Large",
                    "quantity": 123
                    }
                ],
                "customer": self.customer_id
                }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update_order_with_order_status_delivered(self):
        Order.objects.update(id=self.order_id, order_status='Delivered')

        url = reverse('orders-detail',  kwargs={'pk': self.order_id})

        data = {
                "order_items": [
                {   "id": self.order_item_id,
                    "pizza_flavour": "Marinara",
                    "pizza_size": "Large",
                    "quantity": 223
                }
                ],
                "customer": self.customer_id
                }

        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_customer_with_no_order_details(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('customers-list')
        data = {
            'name': 'Maerlina'
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_order_with_invalid_pizza(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('orders-list')
        data = {
                "order_items": [
                    {
                    "pizza_flavour": "Invalid Pizza Flavour",
                    "pizza_size": "Large",
                    "quantity": 123
                    }
                ],
                "customer": self.customer_id
                }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_order_with_wrong_item_id(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('orders-detail',  kwargs={'pk': self.order_id})

        data = {
                "order_items": [
                    { "id": 888999,
                    "pizza_flavour": "Marinara",
                    "pizza_size": "Large",
                    "quantity": 123
                    }
                ],
                "customer": self.customer_id
                }

        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_quantity_flavour_of_existing_order(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('orders-detail',  kwargs={'pk': self.order_id})

        data = {
                "order_items": [
                    { "id": self.order_item_id,
                    "pizza_flavour": "Marinara",
                    "pizza_size": "Large",
                    "quantity": 123
                    }
                ],
                "customer": self.customer_id
                }

        prev_db_obj = OrderItems.objects.filter(pk=self.order_item_id).first()
        prev_pizza_flavour = prev_db_obj.pizza_flavour
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_db_obj = OrderItems.objects.filter(pk=self.order_item_id).first()
        new_pizza_flavour = updated_db_obj.pizza_flavour

        self.assertNotEqual(prev_pizza_flavour, new_pizza_flavour)
        self.assertEqual(new_pizza_flavour, 'Marinara')
    

    