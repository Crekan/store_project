from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    def test_view(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'products.json']

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        url = reverse('products:products')
        response = self.client.get(url)

        self._common_tess(response)
        self.assertEqual(list(response.context_data['products']), list(self.products[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        url = reverse('products:category', kwargs={
            'category_id': category.id,
        })
        response = self.client.get(url)

        self._common_tess(response)
        self.assertEqual(
            list(response.context_data['products']), list(self.products.filter(category_id=category.id))
        )

    def _common_tess(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
