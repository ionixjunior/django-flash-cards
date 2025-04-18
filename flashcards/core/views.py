from django.shortcuts import render

from .models import Deck


def deck_list(request):
    decks = Deck.objects.all()
    return render(request, "core/decks.html", {"decks": decks})