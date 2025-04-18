from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=100)
    last_studied = models.DateTimeField()

    def __str__(self):
        return self.name