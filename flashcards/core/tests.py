from unittest import TestCase

from flashcards.core.models import Deck, Card


class DeckListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Deck.objects.create(id=1, name="Test Deck 1")
        Card.objects.create(deck_id=1, front="Test Front 1", back="Test Back 1")
        Deck.objects.create(id=2, name="Test Deck 2")
        Card.objects.create(deck_id=2, front="Test Front 2", back="Test Back 2")
        Card.objects.create(deck_id=2, front="Test Front 3", back="Test Back 3")
