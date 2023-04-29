'''Ascii art for hand signs'''
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

HAND_ART = {
    'Paper': [
        '    _______        ',
        '___/   ____)____   ',
        '          ______)_ ',
        '          ________)',
        '___       ______)  ',
        '   \__________)    ',
        '                   '
    ],

    'Scissors': [
        '    _______        ',
        '___/   ____)____   ',
        '          ______)_ ',
        '          ________)',
        '___     (___)      ',
        '   \___(___)       ',
        '                   '
    ],

    'Rock': [
        '    _______        ',
        '___/   ____)_      ',
        '        (____)     ',
        '        (____)     ',
        '___     (___)      ',
        '   \___(___)       ',
        '                   '
    ],

    'Metal': [
        '    _______        ',
        '___/   ____)______ ',
        '          ________)',
        '        (__)       ',
        '___     (__)___    ',
        '   \___________)   ',
        '                   '
    ],

    'Pinky': [
        '    _______        ',
        '___/   ____)       ',
        '        (___)      ',
        '        (___)      ',
        '___     (__)___    ',
        '   \___________)   ',
        '                   ',
   ],

    'Yes': [
        '     __            ',
        '    │  │           ',
        '___/   │_____      ',
        '        (____)     ',
        '        (____)     ',
        '___     (___)      ',
        '   \___(___)       '
    ],

    'Shaka': [
        '     __            ',
        '    │  │           ',
        '___/   │____       ',
        '        (___)      ',
        '        (___)      ',
        '___     (__)___    ',
        '   \___________)   '
   ],

   'Point': [
        '    _______        ',
        '___/   ____)______ ',
        '          ________)',
        '        (___)      ',
        '___     (___)      ',
        '   \___(___)       ',
        '                   '
   ],

   'Gun': [
        '     __            ',
        '    │  │           ',
        '___/   │__________ ',
        '          ________)',
        '        (___)      ',
        '___     (___)      ',
        '   \___(___)       '
   ],

   'One': [
        '     __            ',
        '    │  │           ',
        '___/   │_____      ',
        '        (____)     ',
        '        (____)     ',
        '___     (___)      ',
        '   \___(___)       '
    ],

    'Two': [
        '     __            ',
        '    │  │           ',
        '___/   │__________ ',
        '          ________)',
        '        (___)      ',
        '___     (___)      ',
        '   \___(___)       '
   ],

   'Three': [
        '     __            ',
        '    │  │           ',
        '___/   │________   ',
        '          ______)_ ',
        '          ________)',
        '___     (___)      ',
        '   \___(___)       '
    ],

    'Four': [
        '     __            ',
        '    │  │           ',
        '___/   │________   ',
        '          ______)_ ',
        '          ________)',
        '___       ______)  ',
        '   \___(___)       '
    ],

    'Five': [
        '     __            ',
        '    │  │           ',
        '___/   │________   ',
        '          ______)_ ',
        '          ________)',
        '___       ______)  ',
        '   \__________)    '
    ],

}

HAND_HEIGHT = len(HAND_ART['Rock'])
HAND_WIDTH = len(HAND_ART['Rock'][0])

def reverse_art_line(art):
    '''Reverse one line of an ascii art'''
    art=art[::-1]
    art = art.replace(')', '#')
    art = art.replace('(', ')')
    art = art.replace('#', '(')
    art = art.replace('/', '#')
    art = art.replace('\\', '/')
    art = art.replace('#', '\\')

    return art
