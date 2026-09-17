from django.test import TestCase
from .models import Product, Box


class BoxRecommendationTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=35,
            width=25,
            height=5,
            weight=3
        )

        self.medium = Box.objects.create(
            name="Medium",
            length=40,
            width=30,
            height=20,
            max_weight=10,
            cost=40
        )

        self.large = Box.objects.create(
            name="Large",
            length=60,
            width=40,
            height=40,
            max_weight=20,
            cost=70
        )

    def test_product_fits_in_medium_box(self):
        self.assertTrue(
            self.product.weight <= self.medium.max_weight
        )

    def test_product_does_not_fit_in_small_weight_limit(self):
        heavy_product = Product.objects.create(
            name="Heavy Item",
            length=30,
            width=20,
            height=15,
            weight=25
        )

        self.assertFalse(
            heavy_product.weight <= self.medium.max_weight
        )

    def test_large_box_can_fit_large_product(self):
        large_product = Product.objects.create(
            name="Large Item",
            length=55,
            width=35,
            height=35,
            weight=15
        )

        self.assertTrue(
            large_product.weight <= self.large.max_weight
        )