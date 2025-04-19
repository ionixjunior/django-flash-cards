from datetime import datetime, timedelta

from django.test import TestCase

from ..models import Deck, Card

class CardManagerTest(TestCase):
    def test_next_card_should_be_none_when_no_cards_in_deck(self):
        deck = Deck.objects.create(name="Test Deck")

        next_card = Card.objects.next_card(deck)

        self.assertIsNone(next_card)

    def test_next_card_should_be_none_when_cards_in_deck_has_future_next_review_date(self):
        next_review_date = datetime.today() + timedelta(days=1)
        deck = Deck.objects.create(name="Test Deck")
        Card.objects.create(deck_id=deck, front="Test Front", back="Test Back", next_review_date=next_review_date)
        next_card = Card.objects.next_card(deck)
        self.assertIsNone(next_card)