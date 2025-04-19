from datetime import datetime, timedelta

from django.test import TestCase

from ..models import Deck, Card

class CardManagerTest(TestCase):
    def test_next_card_should_be_none_when_no_cards_in_deck(self):
        today = datetime.today()
        deck = Deck.objects.create(name="Test Deck")

        next_card = Card.objects.next_card(today, deck)

        self.assertIsNone(next_card)

    def test_next_card_should_be_none_when_cards_in_deck_has_future_next_review_date(self):
        today = datetime.today()
        next_review_date = datetime.today() + timedelta(days=1)
        deck = Deck.objects.create(name="Test Deck")
        Card.objects.create(deck_id=deck,
                            front="Test Front",
                            back="Test Back",
                            next_review_date=next_review_date)

        next_card = Card.objects.next_card(today, deck)

        self.assertIsNone(next_card)

    def test_next_card_should_return_card_with_today_next_review_date(self):
        today = datetime.today()
        deck = Deck.objects.create(name="Test Deck")
        expected_card = Card.objects.create(deck_id=deck,
                                            front="Test Front",
                                            back="Test Back",
                                            next_review_date=today)

        next_card = Card.objects.next_card(today, deck)

        self.assertEqual(next_card.id, expected_card.id)

    def test_next_card_should_return_card_with_yesterday_next_review_date(self):
        today = datetime.today()
        yesterday = datetime.today() - timedelta(days=1)
        deck = Deck.objects.create(name="Test Deck")
        expected_card = Card.objects.create(deck_id=deck,
                                            front="Test Front",
                                            back="Test Back",
                                            next_review_date=yesterday)

        next_card = Card.objects.next_card(today, deck)

        self.assertEqual(next_card.id, expected_card.id)

    def test_next_card_should_return_the_older_card(self):
        two_days_before = datetime.today() - timedelta(days=2)
        one_day_before = datetime.today() - timedelta(days=1)
        today = datetime.today()
        deck = Deck.objects.create(name="Test Deck")
        expected_card = Card.objects.create(deck_id=deck,
                                            front="Test Front",
                                            back="Test Back",
                                            next_review_date=two_days_before)
        Card.objects.create(deck_id=deck,
                            front="Test Front 2",
                            back="Test Back 2",
                            next_review_date=one_day_before)
        Card.objects.create(deck_id=deck,
                            front="Test Front 3",
                            back="Test Back 3",
                            next_review_date=today)
        Card.objects.create(deck_id=deck,
                            front="Test Front 4",
                            back="Test Back 4")

        next_card = Card.objects.next_card(today, deck)

        self.assertEqual(next_card.id, expected_card.id)

    def test_next_card_should_return_unreviewed_card(self):
        today = datetime.today()
        one_day_later = datetime.today() + timedelta(days=1)
        deck = Deck.objects.create(name="Test Deck")
        Card.objects.create(deck_id=deck,
                            front="Test Front 1",
                            back="Test Back 2",
                            next_review_date=one_day_later)
        expected_card = Card.objects.create(deck_id=deck,
                                            front="Test Front 2",
                                            back="Test Back 2")

        next_card = Card.objects.next_card(today, deck)

        self.assertEqual(next_card.id, expected_card.id)
