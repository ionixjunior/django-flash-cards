from django.shortcuts import render
from django.utils import timezone

from .models import Deck, Card
from .srs.simple_srs import SimpleSRS


def deck_list(request):
    decks = Deck.objects.all()
    return render(request, "core/decks.html", {"decks": decks})


def flash_card(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    current_date = timezone.now()

    if request.method == "POST":
        deck.last_studied = current_date
        deck.save()

        card_id = request.POST.get("card_id")
        feedback = request.POST.get("feedback")
        srs = SimpleSRS()
        next_review_date = srs.calculate_next_review_date(today=current_date, feedback=feedback)
        card = Card.objects.get(pk=card_id)
        card.last_review_date = current_date
        card.next_review_date = next_review_date
        card.save()

    card = Card.objects.next_card(current_date=current_date, deck=deck)
    return render(request,
                  "core/flash_card.html",
                  {"deck_name": deck.name, "card": card})
