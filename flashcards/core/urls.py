from django.urls import path

from . import views


urlpatterns = [
    path('', views.deck_list, name='deck_list'),
    path('deck/<int:deck_id>/flashcard', views.flash_card, name='flash_card'),
]
