from django.shortcuts import render


def decks(request):
    return render(request, "core/decks.html")