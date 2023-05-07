'''Card object'''
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

import cardArt

class Card:
    def __init__(self, suit, rank) -> None:
        self.face_up=False
        self.suit = cardArt.CARD_SUITS[suit]
        self.rank = rank
        if rank in ('J', 'Q', 'K', 'A'):
            self.value = 10
        else:
            self.value = int(rank)

        self.back_design=cardArt.CARD_BACK
        for key, value in enumerate(self.back_design):
            colored_design=cardArt.CARD_BACK_COLOR
            colored_design+=value
            colored_design+=cardArt.CARD_TCOLOR_END
            self.back_design[key]=colored_design

        self.design = cardArt.CARD_TEMPLATE.copy()
        begin=''
        end=''
        if self.suit['en_tcolor'] != '':
            begin=self.suit['en_tcolor']
            end=cardArt.CARD_TCOLOR_END

        card_sign=begin+self.suit['sign']+end
        card_rank=begin+self.rank+end

        self.design[1]=self.design[1].replace('S', card_sign)
        template='R'
        if self.rank=='10':
            template=' R'
        self.design[1]=self.design[1].replace(template, card_rank)

        self.design[4]=self.design[4].replace('S', card_sign)
        if self.rank=='10':
            template='R '
        self.design[4]=self.design[4].replace(template, card_rank)

    def __str__(self) -> str:
        face=self.suit['sign']
        face+=self.rank
        face+=f'({self.value}) '
        return face

    def turn_card(self):
        self.face_up = not self.face_up

    def show_card(self):
        self.face_up = True

    def get_design(self):
        if self.face_up:
            return self.design
        else:
            return self.back_design