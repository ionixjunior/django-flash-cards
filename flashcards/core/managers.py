from django.db import models


# pylint: disable=too-few-public-methods
class CardManager(models.Manager):
    def next_card(self, deck):
        pass
