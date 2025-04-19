from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from ...srs.simple_srs import SimpleSRS


class SimpleSRSTest(TestCase):
    def setUp(self):
        self.simple_srs = SimpleSRS()
        self.today = timezone.now()

    def test_calculate_next_review_date_should_return_correct_date_when_feedback_is_again(self):
        feedback = 'again'
        next_review_date = self.today + timedelta(days=0)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_calculate_next_review_date_should_return_correct_date_when_feedback_is_hard(self):
        feedback = 'hard'
        next_review_date = self.today + timedelta(days=1)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_calculate_next_review_date_should_return_correct_date_when_feedback_is_good(self):
        feedback = 'good'
        next_review_date = self.today + timedelta(days=3)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_calculate_next_review_date_should_return_correct_date_when_feedback_is_easy(self):
        feedback = 'easy'
        next_review_date = self.today + timedelta(days=7)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)

    def test_calculate_next_review_date_should_return_correct_date_when_feedback_is_invalid(self):
        feedback = 'invalid'
        next_review_date = self.today + timedelta(days=0)

        result = self.simple_srs.calculate_next_review_date(self.today, feedback)

        self.assertEqual(result, next_review_date)
