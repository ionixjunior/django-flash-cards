from django.test import TestCase

from ..models import Deck, Card

class CardManagerTest(TestCase):
    def test_next_card_should_be_none_when_no_cards_in_deck(self):
        deck = Deck.objects.create(name="Test Deck")
        next_card = Card.objects.next_card(deck)
        self.assertIsNone(next_card)