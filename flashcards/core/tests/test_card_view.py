
from django.test import TestCase, Client
from django.urls import reverse


class CardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.flash_card_url = reverse('flash_card', args=[1])

    def test_card_view_when_accessed_should_return_200(self):
        response = self.client.get(self.flash_card_url)
        self.assertEqual(response.status_code, 200)
