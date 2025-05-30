
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Deck, Card


class FlashCardViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.deck1 = Deck.objects.create(name="Test Deck 1")
        cls.card1 = Card.objects.create(deck_id=cls.deck1, front="Test Front 1", back="Test Back 1")

    def setUp(self):
        self.client = Client()
        self.flash_card_url = reverse('flash_card', args=[self.deck1.pk])

    def test_flash_card_view_when_accessed_should_return_200(self):
        response = self.client.get(self.flash_card_url)

        self.assertEqual(response.status_code, 200)

    def test_flash_card_view_should_get_404_when_deck_does_not_exist(self):
        invalid_deck_id = 99999
        response = self.client.get(reverse('flash_card', args=[invalid_deck_id]))

        self.assertEqual(response.status_code, 404)

    def test_flash_card_view_when_accessed_should_have_deck_name(self):
        response = self.client.get(self.flash_card_url)

        self.assertTrue('deck_name' in response.context)
        self.assertEqual(response.context['deck_name'], "Test Deck 1")

    def test_flash_card_view_when_accessed_should_have_card(self):
        response = self.client.get(self.flash_card_url)

        self.assertTrue('card' in response.context)
        self.assertEqual(response.context['card'].id, self.card1.id)

    def test_flash_card_view_when_no_card_available(self):
        self.card1.delete()
        response = self.client.get(self.flash_card_url)

        self.assertTrue('card' in response.context)
        self.assertIsNone(response.context['card'])

    def test_flash_card_view_when_post_request_should_return_200(self):
        response = self.client.post(self.flash_card_url,
                                    {
                                        'card_id': self.card1.id,
                                        'feedback': 'again'
                                    })

        self.assertEqual(response.status_code, 200)

    def test_flash_card_view_when_post_request_should_update_card(self):
        self.client.post(self.flash_card_url, {'card_id': self.card1.id, 'feedback': 'again'})

        self.card1.refresh_from_db()
        self.assertNotEqual(self.card1.next_review_date, None)
        self.assertNotEqual(self.card1.last_review_date, None)

    def test_flash_card_view_when_post_request_should_update_deck(self):
        self.client.post(self.flash_card_url, {'card_id': self.card1.id, 'feedback': 'again'})

        self.deck1.refresh_from_db()
        self.assertNotEqual(self.deck1.last_studied, None)
