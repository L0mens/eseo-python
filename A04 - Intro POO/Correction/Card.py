from __future__ import annotations  # Permet de typer Card dans Card
import sys
from termcolor import colored, cprint
from colorama import Back, Style
from random import shuffle


class CardValue:
    def __init__(self, pts, txt) -> None:
        self.value_pts = pts
        self.value_txt = txt


class CardColor:
    def __init__(self, shade: str, shade_name: str, for_color: str, back_color) -> None:
        self.shade = shade
        self.shade_name = shade_name
        self.forground_color = for_color
        self.background_color = back_color


class Card:
    def __init__(
        self, pts, txt, shade, shade_name, for_color, back_color=Back.WHITE
    ) -> None:
        self.card_color = CardColor(shade, shade_name, for_color, back_color)
        self.card_value = CardValue(pts, txt)

    def is_equal_value(self, otherCard: Card) -> bool:
        return self.card_value.value_pts == otherCard.card_value.value_pts

    def __str__(self) -> str:
        return colored(
            f"{self.card_value.value_txt}{self.card_color.shade}",
            self.card_color.forground_color,
        )

    def __repr__(self) -> str:
        return colored(
            f"{self.card_value.value_txt}{self.card_color.shade}",
            self.card_color.forground_color,
        )

    def __eq__(self, __value: object) -> bool:
        return (self.card_color.shade, self.card_value.value_pts) == (
            __value.card_color.shade,
            __value.card_value.value_pts,
        )

    def __lt__(self, otherCard: Card) -> bool:
        return self.card_value.value_pts < otherCard.card_value.value_pts

    def __gt__(self, otherCard: Card) -> bool:
        return self.card_value.value_pts > otherCard.card_value.value_pts


class Deck:
    def __init__(self) -> None:
        self.main_deck = []
        self.defausse = []

    def init52_cards(self):
        card_data = {10: "J", 11: "Q", 12: "K", 13: "A"}
        shades = {
            "♠": {"name": "spade", "color": "black"},
            "♦": {"name": "diamond", "color": "light_red"},
            "♣": {"name": "clover", "color": "light_grey"},
            "♥": {"name": "heart", "color": "red"},
        }

        for shade, s_data in shades.items():
            for value in range(1, 14):
                txt = card_data.get(value, value)
                self.main_deck.append(
                    Card(value, txt, shade, s_data["name"], s_data["color"])
                )

    def shuffle(self):
        shuffle(self.main_deck)

    def draw(self) -> Card:
        return self.main_deck.pop(0)

    def discard(self, card: Card):
        self.defausse.append(card)
