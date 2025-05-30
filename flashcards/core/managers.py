from django.db import models
from django.db.models import Q, F


# pylint: disable=too-few-public-methods
class CardManager(models.Manager):
    def next_card(self, current_date, deck):
        card = self.get_queryset().filter(
            deck_id=deck
        ).filter(
            Q(next_review_date__lte=current_date) | Q(next_review_date__isnull=True)
        ).order_by(
            F('next_review_date').asc(nulls_last=True)
        ).first()

        return card
