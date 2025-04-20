from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product, Order

class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Products
        self.product_jo = Product.objects.create(
            title='Game JO',
            description='Jordanian Game',
            price=10.00,
            location='JO'
        )
        self.product_sa = Product.objects.create(
            title='Game SA',
            description='Saudi Game',
            price=20.00,
            location='SA'
        )

    def test_get_all_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_filter_products_by_location(self):
        url = reverse('product-list') + '?location=JO'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['location'], 'JO')

    def test_get_product_detail(self):
        url = reverse('product-detail', args=[self.product_jo.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.product_jo.title)

    def test_purchase_product(self):
        url = reverse('product-buy', args=[self.product_sa.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['product']['id'], self.product_sa.id)
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.user, self.user)
