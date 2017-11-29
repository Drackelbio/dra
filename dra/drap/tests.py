from django.test import TestCase


from drap.models import Compra


class CompraTestCase(TestCase):

    def setUp(self):
        Compra.objects.create(name="lion", cantidad="tres")
        Compra.objects.create(name="cat", cantidad="tres")

    def test_compras_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Compra.objects.get(name="lion")
        cat = Compra.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "tres"')
        self.assertEqual(cat.speak(), 'The cat says "tres"')
