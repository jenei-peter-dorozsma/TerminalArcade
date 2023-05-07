'''Functions to handle decks'''
# Copyright 2023 Peter Jenei

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import card
import cardArt

def generate_deck(number_of_decks=1):
    deck = []
    for i in range(number_of_decks):
        for suit in cardArt.CARD_SUITS:
            for rank in cardArt.CARD_RANKS:
                deck.append(card.Card(suit, rank))
    return deck

def turn_deck(deck):
    for card in deck:
        card.turn_card()

def show_deck(deck):
    for card in deck:
        card.show_card()

def print_deck(deck, row_limit=10):
    rows_of_cards = [deck[x:x+row_limit] for x in range(0, len(deck), row_limit)]

    for row_of_cards in rows_of_cards:
        for i in range(cardArt.CARD_HEIGHT):
            for card in row_of_cards:
                print(card.get_design()[i]+' ', end='')
            print('')
        print('')

if __name__ == '__main__':
    mydeck = generate_deck()
    print_deck(mydeck, 13)

    player_deck=[]
    for i in range(5):
        mycard = mydeck.pop(random.randrange(len(mydeck)))
        mycard.turn_card()
        player_deck.append(mycard)

    mydeck+=player_deck

    print('---------------')
    print_deck(mydeck, 13)
    print('---------------')
    show_deck(mydeck)
    print_deck(mydeck, 13)
