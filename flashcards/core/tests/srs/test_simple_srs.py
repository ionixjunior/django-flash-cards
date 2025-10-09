from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from ...srs.simple_srs import SimpleSRS


class SimpleSRSTest(TestCase):
    def setUp(self):
        self.simple_srs = SimpleSRS()
        self.today = timezone.now()

    def test_next_review_date_with_again_feedback(self):
        feedback = 'again'
        next_review_date = self.today + timedelta(minutes=1)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_next_review_date_with_hard_feedback(self):
        feedback = 'hard'
        next_review_date = self.today + timedelta(days=1)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_next_review_date_with_good_feedback(self):
        feedback = 'good'
        next_review_date = self.today + timedelta(days=3)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_next_review_date_with_easy_feedback(self):
        feedback = 'easy'
        next_review_date = self.today + timedelta(days=7)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_next_review_date_with_invalid_feedback(self):
        feedback = 'invalid'
        next_review_date = self.today + timedelta(days=0)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)
