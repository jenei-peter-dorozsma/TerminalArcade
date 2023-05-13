'''Ascii art for cards'''
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

import terminalColors

CARD_SUITS={
    'clubs': {
        'sign': '♣',
        'name': 'Clubs',
        'color': 'black',
        'tcolor': '',
        'en_color': 'green',
        'en_tcolor': terminalColors.TColor.OKGREEN
    },
    'diamonds': {
        'sign': '♦',
        'name': 'Diamonds',
        'color': 'red',
        'tcolor': terminalColors.TColor.FAIL,
        'en_color': 'blue',
        'en_tcolor': terminalColors.TColor.OKBLUE
    },
    'hearts': {
        'sign': '♥',
        'name': 'Hearts',
        'color': 'red',
        'tcolor': terminalColors.TColor.FAIL,
        'en_color': 'red',
        'en_tcolor': terminalColors.TColor.FAIL
    },
    'spades': {
        'sign': '♠',
        'name': 'Spades',
        'color': 'black',
        'tcolor': '',
        'en_color': 'black',
        'en_tcolor': ''
    }
}

CARD_RANKS = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

CARD_DESIGNS = {
    0: [
        '╔══════╗',
        '║      ║',
        '║      ║',
        '║      ║',
        '║      ║',
        '╚══════╝'
    ],
    1: [
        '╔══════╗',
        '║ S  R ║',
        '║      ║',
        '║      ║',
        '║ R  S ║',
        '╚══════╝'
    ],
    2: [
        '╔══════╗',
        '║ █▓▒░ ║',
        '║ █▓▒░ ║',
        '║ █▓▒░ ║',
        '║ █▓▒░ ║',
        '╚══════╝'
    ],
    3: [
        '╔══════╗',
        '║ ▒░   ║',
        '║ ▓▒░  ║',
        '║ █▓▒░ ║',
        '║ ██▓▒░║',
        '╚══════╝'
    ],
    4: [
        '╔══════╗',
        '║▓▒░░▒▓║',
        '║▓▒░░▒▓║',
        '║▓▒░░▒▓║',
        '║▓▒░░▒▓║',
        '╚══════╝'
    ],
    5: [
        '╔══════╗',
        '║░▒▓▓▒░║',
        '║░▒▓▓▒░║',
        '║░▒▓▓▒░║',
        '║░▒▓▓▒░║',
        '╚══════╝'
    ],
    6: [
        '╔══════╗',
        '║░░░░░░║',
        '║▒▒▒▒▒▒║',
        '║▓▓▓▓▓▓║',
        '║██████║',
        '╚══════╝'
    ],
    7: [
        '╔══════╗',
        '║§§§§§§║',
        '║§§§§§§║',
        '║§§§§§§║',
        '║§§§§§§║',
        '╚══════╝'
    ],
    8: [
        '╔══════╗',
        '║ ╬╬╬╬ ║',
        '║ ╬╬╬╬ ║',
        '║ ╬╬╬╬ ║',
        '║ ╬╬╬╬ ║',
        '╚══════╝'
    ],
    9: [
        '╔╦╦╦╦╦╦╗',
        '╠╬╬╬╬╬╬╣',
        '╠╬╬╬╬╬╬╣',
        '╠╬╬╬╬╬╬╣',
        '╠╬╬╬╬╬╬╣',
        '╚╩╩╩╩╩╩╝'
    ],
    10: [
        '╔═╤╤╤╤═╗',
        '║╔╧╧╧╧╗║',
        '╟╢    ╟╢',
        '╟╢    ╟╢',
        '║╚╤╤╤╤╝║',
        '╚═╧╧╧╧═╝'
    ],
    11: [
        '╔╦══╦══╗',
        '║╚╗ ╚╗ ║',
        '║ ╚╗ ╚╗║',
        '╠╗ ╚╗ ╚╣',
        '║╚╗ ╚╗ ║',
        '╚═╩══╩═╝'
    ],
    12: [
        '╔══════╗',
        '║ ♦  ♠ ║',
        '║      ║',
        '║      ║',
        '║ ♣  ♥ ║',
        '╚══════╝'
    ],
    13: [
        '╔══════╗',
        '║╔════╗║',
        '║║╔══╗║║',
        '║║╚══╝║║',
        '║╚════╝║',
        '╚══════╝'
    ],
    14: [
        '╔╦════╦╗',
        '╠╝    ╚╣',
        '║  ╔╗  ║',
        '║  ╚╝  ║',
        '╠╗    ╔╣',
        '╚╩════╩╝'
    ],
    15: [
        '╔══════╗',
        '║  ╔═╗ ║',
        '║ ╔╬╗║ ║',
        '║ ║╚╬╝ ║',
        '║ ╚═╝  ║',
        '╚══════╝'
    ],
    16: [
        '╔╦════╦╗',
        '╠╝ ╔═╗╚╣',
        '║ ╔╬╗║ ║',
        '║ ║╚╬╝ ║',
        '╠╗╚═╝ ╔╣',
        '╚╩════╩╝'
    ],
    17: [
        '╔══════╗',
        '║* ___*║',
        '║ /o  \║',
        '║├-----║',
        '║*\___/║',
        '╚══════╝'
    ],
    18: [
        '╔══════╗',
        '║.  ├o┤║',
        '║├o┤ * ║',
        '║ * . .║',
        '║ .├o┤ ║',
        '╚══════╝'
    ],
    19: [
        '╔══════╗',
        '║      ║',
        '║\  o  ║',
        '║ \/|\ ║',
        '║  / \ ║',
        '╚══════╝'
    ],
    20: [
        '╔══════╗',
        '║   ├o┤║',
        '║   /  ║',
        '║  /   ║',
        '║ /    ║',
        '╚══════╝'
    ],
    21: [
        '╔══════╗',
        '║   ├o┤║',
        '║PEW/  ║',
        '║  /   ║',
        '║ / PEW║',
        '╚══════╝'
    ],
    22: [
        '╔══════╗',
        '║(•)(•)║',
        '║   U  ║',
        '║└┬┬┬┬┘║',
        '║ └┘└┘ ║',
        '╚══════╝',
    ],
    23: [
        '╔══════╗',
        '║  /\  ║',
        '║ /  \ ║',
        '║/    \║',
        '║(•)(•)║',
        '╚══════╝',
    ],
    24: [
        '╔══════╗',
        '║ ┼ ┼  ║',
        '║┌┴─┴┐ ║',
        '║│(•)│ ║',
        '║│ - │ ║',
        '╚══════╝',
    ],
    25: [
        '╔══════╗',
        '║ _--_ ║',
        '║(_  _)║',
        '║(•)(•)║',
        '║ ──U──║',
        '╚══════╝',
    ],
    26: [
        '╔══════╗',
        '║┌─┐┌─┐║',
        '║│ ││ │║',
        '║│$││$│║',
        '║│ ││ │║',
        '╚══════╝',
    ],
    27: [
        '╔═╤═══╤╗',
        '╟─┴─┬─┴╢',
        '╟─┬─┴─┬╢',
        '╟─┴─┬─┴╢',
        '╟─┬─┴─┬╢',
        '╚═╧═══╧╝',
    ],
}

CARD_BLANK = CARD_DESIGNS[0]
CARD_TEMPLATE = CARD_DESIGNS[1]
CARD_BACK = CARD_DESIGNS[16]
CARD_HEIGHT = len(CARD_TEMPLATE)
CARD_WIDTH = len(CARD_TEMPLATE[0])
CARD_BACK_COLOR = terminalColors.TColor.WARNING
CARD_TCOLOR_END = terminalColors.TColor.ENDC