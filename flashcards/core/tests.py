from datetime import datetime, UTC

from django.test import TestCase, Client
from django.urls import reverse

from .models import Deck, Card


class DeckListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        deck1 = Deck.objects.create(name="Test Deck 1")
        deck2 = Deck.objects.create(name="Test Deck 2", last_studied=datetime(2025, 4, 18, 12, 0, 0, tzinfo=UTC))
        Card.objects.create(deck_id=deck1, front="Test Front 1", back="Test Back 1")
        Card.objects.create(deck_id=deck2, front="Test Front 2", back="Test Back 2")
        Card.objects.create(deck_id=deck2, front="Test Front 3", back="Test Back 3")

    def setUp(self):
        self.client = Client()
        self.deck_list_url = reverse('deck_list')

    def test_decklist_when_accessed_should_return_200(self):
        response = self.client.get(self.deck_list_url)
        self.assertEqual(response.status_code, 200)

    def test_decklist_when_accessed_should_have_decks(self):
        response = self.client.get(self.deck_list_url)
        self.assertTrue('decks' in response.context)
        self.assertEqual(len(response.context['decks']), 2)

    def test_decklist_when_accessed_should_list_all_deck_names(self):
        response = self.client.get(self.deck_list_url)
        deck_names = [deck.name for deck in response.context['decks']]
        self.assertIn("Test Deck 1", deck_names)
        self.assertIn("Test Deck 2", deck_names)

    def test_decklist_when_accessed_should_list_number_of_cards_of_each_deck(self):
        response = self.client.get(self.deck_list_url)
        deck_cards_count = {deck.name: deck.card_set.count() for deck in response.context['decks']}
        self.assertEqual(deck_cards_count["Test Deck 1"], 1)
        self.assertEqual(deck_cards_count["Test Deck 2"], 2)

    def test_decklist_when_accessed_should_list_last_studied_date_of_each_deck(self):
        response = self.client.get(self.deck_list_url)
        deck_last_studied = {deck.name: deck.last_studied for deck in response.context['decks']}
        self.assertIsNone(deck_last_studied["Test Deck 1"])
        self.assertEqual(deck_last_studied["Test Deck 2"], datetime(2025, 4, 18, 12, 0, 0, tzinfo=UTC))