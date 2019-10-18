"""This module contains the 'Deck' class and related methods.
"""
import pandas as pd
import numpy as np
from card import Card


class Deck:
    """ A class defining the properties and methods of a deck object. *** Add method overview ***
    """
    def __init__(self):
        """ For now, creating a Deck object initialises that object with four arrays:
        '_deck_array', '_suit_array', '_rank_array' and '_value_array' (the leading underscore is a Python convention;
        it hints that the variable is for internal use within the object's methods, i.e. it shouldn't be called when
        interacting with a 'Deck' object elsewhere in the code). The '_deck_array' is the most important feature of the
        Deck class; it is empty on initialisation of a Deck object but the 'new_deck' method will populate this list
        with 'Card' objects when called. The final three (lets call them 'property') arrays contain details of a
        standard deck of cards. Individual elements of these arrays are passed to a Card object when it is initialised.
        The '_suit_array' holds the four suits found in a pack of cards. The '_rank_array' holds the 13 ranks in each
        suit and the '_value_array' holds their corresponding values in the game of blackjack.
        """
        self._deck_array = []
        self._suit_array = ['spades', 'hearts', 'clubs', 'diamonds']
        self._rank_array = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                            'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self._value_array = [(1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Maybe change the Ace tuple to a dict?

    def new_deck(self):
        """ The 'new_deck' method loops through a 'Deck' object's property arrays to populate the '_deck_array' with
        Card objects: together forming six full 52-card decks. On creation of each Card, its 'print_all_details' method
        is called; this prints the suit, rank and value of that card. Another 'Deck' method: 'shuffle' will then be
        called to randomly order the 312 'Card' objects within the list, giving a shuffled deck to start the game.
        """
        for i in range(6):
            for suit in self._suit_array:
                j = 0
                for rank in self._rank_array:
                    self._deck_array.append(Card(suit, rank, self._value_array[j], i))
                    self._deck_array[-1].print_all_details()
                    j += 1
