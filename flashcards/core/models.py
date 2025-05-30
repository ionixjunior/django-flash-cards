from django.db import models

from .managers import CardManager


class Deck(models.Model):
    name = models.CharField(max_length=50)
    last_studied = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Card(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)
    last_review_date = models.DateTimeField(null=True, blank=True)
    next_review_date = models.DateTimeField(null=True, blank=True)

    objects = CardManager()

    def __str__(self):
        return f"{self.front} - {self.back}"
