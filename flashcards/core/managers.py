from django.db import models
from django.template.defaultfilters import first


# pylint: disable=too-few-public-methods
class CardManager(models.Manager):
    def next_card(self, current_date, deck):
        card_to_view = self.get_queryset().filter(
            deck_id=deck
        ).order_by(
            'next_review_date'
        ).first()

        return card_to_view
