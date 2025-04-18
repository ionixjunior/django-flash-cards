from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=50)
    last_studied = models.DateTimeField()

    def __str__(self):
        return self.name


class Card(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.CharField(max_length=100)
    back = models.TextField(max_length=100)
    last_review_date = models.DateTimeField()
    next_review_date = models.DateTimeField()

    def __str__(self):
        return f"{self.front} - {self.back}"