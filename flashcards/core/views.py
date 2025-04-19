from django.shortcuts import render
from django.utils import timezone

from .models import Deck, Card


def deck_list(request):
    decks = Deck.objects.all()
    return render(request, "core/decks.html", {"decks": decks})


def flash_card(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    current_date = timezone.now()
    card = Card.objects.next_card(current_date=current_date, deck=deck)
    return render(request,
                  "core/flash_card.html",
                  {
                      "deck_name": deck.name,
                      "card_id": card.id,
                      "card_front": card.front,
                      "card_back": card.back
                  })
