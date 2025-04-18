from unittest import TestCase

from django.test import Client
from django.urls import reverse

from .models import Deck, Card


class DeckListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Deck.objects.create(id=1, name="Test Deck 1")
        Card.objects.create(deck_id=1, front="Test Front 1", back="Test Back 1")
        Deck.objects.create(id=2, name="Test Deck 2")
        Card.objects.create(deck_id=2, front="Test Front 2", back="Test Back 2")
        Card.objects.create(deck_id=2, front="Test Front 3", back="Test Back 3")

    def setUp(self):
        self.client = Client()
        self.deck_list_url = reverse('deck_list')

    def test_decklist_when_accessed_should_return_200(self):
        response = self.client.get(self.deck_list_url)
        self.assertEqual(response.status_code, 200)
