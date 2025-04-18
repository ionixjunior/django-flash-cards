from django.shortcuts import render

from flashcards.core.models import Deck


def decks(request):
    decks = Deck.objects.all()
    return render(request, "core/decks.html", {"decks": decks})