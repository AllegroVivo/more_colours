"""A module containing additional Discord Embed accent colors.

    Typical usage:
    --------------
    foo = CustomColour.amethyst()
    bar = discord.Embed(colour=foo)

Module By Stephanie Phillips
"""

import random

from discord import Colour
from typing import Type, TypeVar
######################################################################
CT = TypeVar("CT", bound="Colour")
######################################################################
class CustomColour(Colour):

    def __init__(self, value: int):
        super().__init__(value)

######################################################################
    @classmethod
    def alice_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF0F8FF``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xF0F8FF)

    @classmethod
    def amaranth(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE52B50``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xE52B50)

    @classmethod
    def amber(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFBF00``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFFBF00)

    @classmethod
    def amethyst(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x9966CC``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x9966CC)

    @classmethod
    def antique_white(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFAE8D7``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFAE8D7)

    @classmethod
    def apricot(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFBCEB1``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFBCEB1)

    @classmethod
    def aquamarine(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7FFFD4``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x7FFFD4)

    @classmethod
    def azure(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x007FFF``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x007FFF)

    @classmethod
    def baby_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x89CFF0``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x89CFF0)

    @classmethod
    def beige(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF5F5DC``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xF5F5DC)

    @classmethod
    def black(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x000000``.

        Does not belong to any Colour group."""
        return cls(0x000000)

    @classmethod
    def blanched_almond(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFE8CD``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xFFE8CD)

    @classmethod
    def blue_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x0095B6``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x0095B6)

    @classmethod
    def blue_violet(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x8A2BE2``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x8A2BE2)

    @classmethod
    def blush(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDE5D83``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xDE5D83)

    @classmethod
    def brick_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCB4154``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xCB4154)

    @classmethod
    def bright_gold(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFD700``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xFFD700)

    @classmethod
    def bright_lime(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00FF00``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x00FF00)

    @classmethod
    def bright_orange(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFA500``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFFA500)

    @classmethod
    def bright_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF0000``.

        Ahh! That's bright! X_X

        Belongs to group RED_COLOURS.
        """
        return cls(0xFF0000)

    @classmethod
    def bright_violet(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xEE82EE``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xEE82EE)

    @classmethod
    def bright_yellow(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFFF00``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xFFFF00)

    @classmethod
    def bronze(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCD7F32``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xCD7F32)

    @classmethod
    def brown(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x993300``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0x993300)

    @classmethod
    def burgundy(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x800020``.

        Belongs to group RED_COLOURS.
        """
        return cls(0x800020)

    @classmethod
    def burlywood(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDE8887``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xDE8887)

    @classmethod
    def byzantium(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x702963``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x702963)

    @classmethod
    def cadet_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x5F9EA0``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x5F9EA0)

    @classmethod
    def carmine(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x960018``.

        Belongs to group RED_COLOURS.
        """
        return cls(0x960018)

    @classmethod
    def cherise(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDE3163``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xDE3163)

    @classmethod
    def cerulean(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x007BA7``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x007BA7)

    @classmethod
    def champagne(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF7E7CE``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xF7E7CE)

    @classmethod
    def chartreuse(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7FFF00``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x7FFF00)

    @classmethod
    def chocolate(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7B3F00``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0x7B3F00)

    @classmethod
    def cobalt_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x0047AB``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x0047AB)

    @classmethod
    def coffee(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x6F4E37``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0x6F4E37)

    @classmethod
    def copper(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xB87333``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xB87333)

    @classmethod
    def coral(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF7F50``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFF7F50)

    @classmethod
    def cornflower_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x6495ED``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x6495ED)

    @classmethod
    def cornsilk(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFF8DC``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xFFF8DC)

    @classmethod
    def crimson(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDC143C``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xDC143C)

    @classmethod
    def cyan(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00FFFF``.

        Belongs to group CYAN_COLOURS. (Obviously)
        """
        return cls(0x00FFFF)

    @classmethod
    def dark_cyan(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x008B8B``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x008B8B)

    @classmethod
    def dark_goldenrod(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xB8860B``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xB8860B)

    @classmethod
    def dark_khaki(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xBDB76B``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xBDB76B)

    @classmethod
    def dark_olive(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x556B2F``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x556B2F)

    @classmethod
    def dark_orange_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF4500``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFF4500)

    @classmethod
    def dark_orchid(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x9932CC``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x9932CC)

    @classmethod
    def dark_salmon(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE9967A``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xE9967A)

    @classmethod
    def dark_sea_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x8FBC8F``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x8FBC8F)

    @classmethod
    def dark_slate_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x483D8B``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x6A5ACD)

    @classmethod
    def dark_slate_grey(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x2F4F4F``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0x2F4F4F)

    dark_slate_gray = dark_slate_grey

    @classmethod
    def dark_turquoise(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00CED1``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x00CED1)

    @classmethod
    def dark_violet(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x9400D3``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x9400D3)

    @classmethod
    def darker_magenta(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x8B008B``.

        Belongs to group RED_COLOURS.
        """
        return cls(0x8B008B)

    @classmethod
    def darkish_orange(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF8C00``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFF8C00)

    @classmethod
    def deep_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x0000FF``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x0000FF)

    @classmethod
    def deep_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x006400``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x006400)

    @classmethod
    def deep_indigo(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x4B0082``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x4B0082)

    @classmethod
    def deep_pink(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF1493``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFF1493)

    @classmethod
    def deep_purple(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x800080``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x800080)

    @classmethod
    def deep_sky_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00BFFF``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x00BFFF)

    @classmethod
    def deep_teal(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x008080``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x008080)

    @classmethod
    def desert_sand(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xEDC9AF``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xEDC9AF)

    @classmethod
    def dim_grey(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x696969``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0x696969)

    dim_gray = dim_grey

    @classmethod
    def dodger_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x1E90FF``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x1E90FF)

    @classmethod
    def electric_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7DF9FF``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x7DF9FF)

    @classmethod
    def emerald(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x50C878``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x50C878)

    @classmethod
    def erin_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00FF3F``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x00FF3F)

    @classmethod
    def fire_brick(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xB22222``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xB22222)

    @classmethod
    def floral_white(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFFAF0``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFFFAF0)

    @classmethod
    def forest_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x228B22``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x228B22)

    @classmethod
    def gainsboro(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDCDCDC``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0xDCDCDC)

    @classmethod
    def ghost_white(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF8F8FF``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xF8F8FF)

    @classmethod
    def goldenrod(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDAA520``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xDAA520)

    @classmethod
    def grape(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x9370DB``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x9370DB)

    @classmethod
    def greenish_yellow(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xADFF2F``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0xADFF2F)

    @classmethod
    def harlequin(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x3FFF00``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x3FFF00)

    @classmethod
    def honeydew(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF0FFF0``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xF0FFF0)

    @classmethod
    def hot_pink(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF69B4``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFF69B4)

    @classmethod
    def indian_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCD5C5C``.

        It's not racist, that's just the name of the color! >.<

        Belongs to group RED_COLOURS.
        """
        return cls(0xCD5C5C)

    @classmethod
    def indigo(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x4B0082``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xDC143C)

    @classmethod
    def ivory(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFFFF0``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFFFFF0)

    @classmethod
    def jade(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00A86B``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x00A86B)

    @classmethod
    def jungle_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x29AB87``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x29AB87)

    @classmethod
    def khaki(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF0E68C``.

        Popularized by Jake, from State Farm™ ...

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xF0E68C)

    @classmethod
    def lavender(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xB57EDC``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xB57EDC)

    @classmethod
    def lavender_blush(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFF0F5``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFFF0F5)

    @classmethod
    def lawn_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7CFC00``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x7CFC00)

    @classmethod
    def lemon(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFF700``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xFFF700)

    @classmethod
    def lemon_chiffon(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFFACD``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xFFFACD)

    @classmethod
    def light_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xADD8E6``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0xADD8E6)

    @classmethod
    def light_coral(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF08080``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xF08080)

    @classmethod
    def light_cyan(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE0FFFF``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0xE0FFFF)

    @classmethod
    def light_goldenrod(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFAFAD2``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xFAFAD2)

    @classmethod
    def light_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x90EE90``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x90EE90)

    @classmethod
    def light_lavender(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE6E6FA``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xE6E6FA)

    @classmethod
    def light_lime(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xBFFF00``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0xBFFF00)

    @classmethod
    def light_pink(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF86C1``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFF86C1)

    @classmethod
    def light_plum(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDDA0DD``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xDDA0DD)

    @classmethod
    def light_salmon(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFA07A``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFFA07A)

    @classmethod
    def light_sea_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x20B2AA``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x20B2AA)

    @classmethod
    def light_sky_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x87CEFA``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x87CEFA)

    @classmethod
    def light_slate(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x778899``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0x778899)

    @classmethod
    def light_steel_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xB0C4DE``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0xB0C4DE)

    @classmethod
    def light_yellow(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFFFE0``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xFFFFE0)

    @classmethod
    def lilac(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xC8A2C8``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xC8A2C8)

    @classmethod
    def lime_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x32CD32``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x32CD32)

    @classmethod
    def linen(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFAF0E6``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFAF0E6)

    @classmethod
    def magenta_rose(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF00AF``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFF00AF)

    @classmethod
    def maroon(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x800000``.

        Belongs to group RED_COLOURS.
        """
        return cls(0x800000)

    @classmethod
    def mauve(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE0B0FF``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xE0B0FF)

    @classmethod
    def medium_aquamarine(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x66CDAA``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x66CDAA)

    @classmethod
    def medium_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x008001``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x008000)

    @classmethod
    def medium_magenta(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF00FF``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xFF00FF)

    @classmethod
    def medium_orange(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF6600``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFF6600)

    @classmethod
    def medium_orchid(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xBA55D3``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xBA55D3)

    @classmethod
    def medium_purple(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x6A0DAD``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x6A0DAD)

    @classmethod
    def medium_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x8B0000``.

        Belongs to group RED_COLOURS.
        """
        return cls(0x8B0000)

    @classmethod
    def medium_sea_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x3CB371``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x3CB371)

    @classmethod
    def medium_slate_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7B68EE``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x7B68EE)

    @classmethod
    def medium_spring_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00FA9A``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x00FA9A)

    @classmethod
    def medium_turquoise(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x48D1CC``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x48D1CC)

    @classmethod
    def medium_violet_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xC71585``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xC71585)

    @classmethod
    def midnight_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x191970``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x191970)

    @classmethod
    def mint_cream(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF5FFFA``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xF5FFFA)

    @classmethod
    def misty_rose(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFE4E1``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFFE4E1)

    @classmethod
    def moccasin(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFE4B5``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFFE4B5)

    @classmethod
    def navajo_white(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFDEAD``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xFFDEAD)

    @classmethod
    def navy_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x000080``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x000080)

    @classmethod
    def ochre(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCC7722``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xDC143C)

    @classmethod
    def old_lace(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFDF5E6``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFDF5E6)

    @classmethod
    def olive(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x808000``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0x808000)

    @classmethod
    def olive_drab(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x6B8E23``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x6B8E23)

    @classmethod
    def orange_chocolate(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xD2691E``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xD2691E)

    @classmethod
    def orange_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF4500``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFF4500)

    @classmethod
    def orchid(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDA70D6``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xDA70D6)

    @classmethod
    def pale_goldenrod(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xEEE8AA``.

        Belongs to group YELLOW_COLOURS.
        """
        return cls(0xEEE8AA)

    @classmethod
    def pale_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x98FB98``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x98FB98)

    @classmethod
    def pale_turquoise(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xAFEEEE``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0xAFEEEE)

    @classmethod
    def pale_violet_red(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xDB7093``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xDB7093)

    @classmethod
    def papaya_whip(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFEFD5``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFFEFD5)

    @classmethod
    def peach(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFE5B4``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFFE5B4)

    @classmethod
    def peach_puff(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFDAB9``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFFDAB9)

    @classmethod
    def pear(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xD1E231``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0xD1E231)

    @classmethod
    def periwinkle(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCCCCFF``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xCCCCFF)

    @classmethod
    def persian_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x1C39BB``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x1C39BB)

    @classmethod
    def peru(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCD853F``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xCD853F)

    @classmethod
    def pink(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFC0CB``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFFC0CB)

    @classmethod
    def plum(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x8E4585``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x8E4585)

    @classmethod
    def powder_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xB0E0E6``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0xB0E0E6)

    @classmethod
    def prussian_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x003153``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x003153)

    @classmethod
    def puce(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xCC8899``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xCC8899)

    @classmethod
    def raspberry(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE30B5C``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xE30B5C)

    @classmethod
    def red_brown(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xA52A2A``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xA52A2A)

    @classmethod
    def red_violet(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xC71585``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0xC71585)

    @classmethod
    def rose(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF007F``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xFF007F)

    @classmethod
    def rosy_brown(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xBC8F8F``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xBC8F8F)

    @classmethod
    def royal_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x4169E1``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x4169E1)

    @classmethod
    def ruby(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xE0115F``.

        Belongs to group PINK_COLOURS.
        """
        return cls(0xE0115F)

    @classmethod
    def saddle_brown(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x8B4513``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0x8B4513)

    @classmethod
    def salmon(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFA8072``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xFA8072)

    @classmethod
    def sandy_brown(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF4A460``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xF4A460)

    @classmethod
    def sangria(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x92000A``.

        Belongs to group RED_COLOURS.
        """
        return cls(0x92000A)

    @classmethod
    def sapphire(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x0F52BA``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x0F52BA)

    @classmethod
    def scarlet(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF2400``.

        Belongs to group RED_COLOURS.
        """
        return cls(0xFF2400)

    @classmethod
    def sea_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x2E8B57``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x2E8B57)

    @classmethod
    def sienna(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xA0522D``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xA0522D)

    @classmethod
    def silver(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xC0C0C0``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0xC0C0C0)

    @classmethod
    def sky_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x87CEEB``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x87CEEB)

    @classmethod
    def slate_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x6A5ACD``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x6A5ACD)

    @classmethod
    def slate_grey(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x708090``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0x708090)

    slate_gray = slate_grey

    @classmethod
    def spring_bud(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xA7FC00``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0xA7FC00)

    @classmethod
    def spring_green(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x00FF7F``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x00FF7F)

    @classmethod
    def steel_blue(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x4682B4``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x4682B4)

    @classmethod
    def tan(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xD2B48C``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xD2B48C)

    @classmethod
    def taupe(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x483C32``.

        Belongs to group GREY_COLOURS.
        """
        return cls(0x483C32)

    @classmethod
    def thistle(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xD8BFD8``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0xD8BFD8)

    @classmethod
    def tomato(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFF6347``.

        Belongs to group ORANGE_COLOURS.
        """
        return cls(0xFF6347)

    @classmethod
    def turquoise(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x40E0D0``.

        Belongs to group CYAN_COLOURS.
        """
        return cls(0x40E0D0)

    @classmethod
    def ultramarine(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x3F00FF``.

        Belongs to group BLUE_COLOURS.
        """
        return cls(0x3F00FF)

    @classmethod
    def violet(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x7F00FF``.

        Belongs to group PURPLE_COLOURS.
        """
        return cls(0x7F00FF)

    @classmethod
    def viridian(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0x40826D``.

        Belongs to group GREEN_COLOURS.
        """
        return cls(0x40826D)

    @classmethod
    def wheat(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF5DEB3``.

        Belongs to group BROWN_COLOURS.
        """
        return cls(0xF5DEB3)

    @classmethod
    def white(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xFFFFFF``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xFFFFFF)

    @classmethod
    def white_smoke(cls: Type[CT]) -> CT:
        """A custom method that returns a :class: `Colour` with a value of ``0xF5F5F5``.

        Belongs to group WHITE_COLOURS.
        """
        return cls(0xF5F5F5)


CustomColor = CustomColour
######################################################################
# Return random colours based on family

def random_red() -> CT:
    """A custom method that returns a random :class: `Colour` from the RED family."""
    return random.choice(RED_COLOURS)

def random_pink() -> CT:
    """A custom method that returns a random :class: `Colour` from the PINK family."""
    return random.choice(PINK_COLOURS)

def random_orange() -> CT:
    """A custom method that returns a random :class: `Colour` from the ORANGE family."""
    return random.choice(ORANGE_COLOURS)

def random_yellow() -> CT:
    """A custom method that returns a random :class: `Colour` from the YELLOW family."""
    return random.choice(YELLOW_COLOURS)

def random_purple() -> CT:
    """A custom method that returns a random :class: `Colour` from the PURPLE family."""
    return random.choice(PURPLE_COLOURS)

def random_green() -> CT:
    """A custom method that returns a random :class: `Colour` from the GREEN family."""
    return random.choice(GREEN_COLOURS)

def random_cyan() -> CT:
    """A custom method that returns a random :class: `Colour` from the CYAN family."""
    return random.choice(CYAN_COLOURS)

def random_blue() -> CT:
    """A custom method that returns a random :class: `Colour` from the BLUE family."""
    return random.choice(BLUE_COLOURS)

def random_brown() -> CT:
    """A custom method that returns a random :class: `Colour` from the BROWN family."""
    return random.choice(BROWN_COLOURS)

def random_white() -> CT:
    """A custom method that returns a random :class: `Colour` from the WHITE family."""
    return random.choice(WHITE_COLOURS)

def random_grey() -> CT:
    """A custom method that returns a random :class: `Colour` from the GREY family."""
    return random.choice(GREY_COLOURS)

def random_all() -> CT:
    """A custom method that returns a random :class: `Colour` from all families."""

    # ALL_COLOURS is a list of colour lists.
    # Randomly choose one of those first, then choose a colour.

    return random.choice(random.choice(ALL_COLOURS))


######################################################################
# Colour Lists - Including original Colours

RED_COLOURS = [
    CustomColour.amaranth(), CustomColour.brick_red(), CustomColour.bright_red(),
    CustomColour.burgundy(), CustomColour.carmine(), CustomColour.crimson(),
    CustomColour.fire_brick(), CustomColour.indian_red(),
    CustomColour.light_coral(), CustomColour.maroon(), CustomColour.medium_red(),
    CustomColour.red_brown(), CustomColour.salmon(), CustomColour.sangria(),
    CustomColour.scarlet(), Colour.brand_red(), Colour.red(),
    Colour.dark_red()
]

PINK_COLOURS = [
    CustomColour.apricot(), CustomColour.blush(), CustomColour.cherise(), CustomColour.deep_pink(),
    CustomColour.hot_pink(), CustomColour.light_pink(), CustomColour.magenta_rose(),
    CustomColour.pale_violet_red(), CustomColour.pink(), CustomColour.puce(),
    CustomColour.raspberry(), CustomColour.rose(), CustomColour.ruby(), Colour.magenta(),
    Colour.dark_magenta(), Colour.fuchsia(), Colour.nitro_pink()
]

ORANGE_COLOURS = [
    CustomColour.amber(), CustomColour.bright_orange(), CustomColour.bronze(),
    CustomColour.coral(), CustomColour.dark_orange_red(), CustomColour.dark_salmon(),
    CustomColour.darkish_orange(), CustomColour.light_salmon(), CustomColour.medium_orange(), CustomColour.ochre(), CustomColour.orange_chocolate(),
    CustomColour.orange_red(), CustomColour.papaya_whip(), CustomColour.peach_puff(),
    CustomColour.tomato(), Colour.orange(), Colour.dark_orange()
]

YELLOW_COLOURS = [
    CustomColour.bright_gold(), CustomColour.bright_yellow(), CustomColour.dark_goldenrod(),
    CustomColour.dark_khaki(), CustomColour.goldenrod(), CustomColour.lemon(),
    CustomColour.lemon_chiffon(), CustomColour.light_goldenrod(), CustomColour.light_yellow(), CustomColour.moccasin(),
    CustomColour.olive(), CustomColour.pale_goldenrod(), Colour.gold(), Colour.dark_gold(), Colour.yellow()
]

PURPLE_COLOURS = [
    CustomColour.amethyst(), CustomColour.blue_violet(), CustomColour.bright_violet(),
    CustomColour.byzantium(), CustomColour.dark_orchid(), CustomColour.dark_violet(), CustomColour.darker_magenta(),
    CustomColour.deep_indigo(), CustomColour.deep_purple(), CustomColour.grape(),
    CustomColour.indigo(), CustomColour.lavender(), CustomColour.light_lavender(),
    CustomColour.light_plum(), CustomColour.lilac(), CustomColour.mauve(),
    CustomColour.medium_magenta(), CustomColour.medium_orchid(), CustomColour.medium_purple(),
    CustomColour.medium_violet_red(), CustomColour.orchid(), CustomColour.periwinkle(),
    CustomColour.plum(), CustomColour.red_violet(), CustomColour.violet(), Colour.purple(),
    Colour.dark_purple(), CustomColour.thistle()
]

GREEN_COLOURS = [
    CustomColour.bright_lime(), CustomColour.chartreuse(), CustomColour.dark_olive(),
    CustomColour.dark_sea_green(), CustomColour.deep_green(), CustomColour.emerald(),
    CustomColour.erin_green(), CustomColour.forest_green(), CustomColour.greenish_yellow(),
    CustomColour.harlequin(), CustomColour.jade(), CustomColour.jungle_green(),
    CustomColour.lawn_green(), CustomColour.light_green(), CustomColour.light_lime(),
    CustomColour.lime_green(), CustomColour.medium_green(), CustomColour.medium_sea_green(),
    CustomColour.medium_spring_green(), CustomColour.olive_drab(), CustomColour.pale_green(),
    CustomColour.pear(), CustomColour.sea_green(), CustomColour.spring_bud(),
    CustomColour.spring_green(), CustomColour.viridian(),
    Colour.brand_green(), Colour.green(), Colour.dark_green()
]

CYAN_COLOURS = [
    CustomColour.aquamarine(), CustomColour.cadet_blue(), CustomColour.cerulean(),
    CustomColour.cyan(), CustomColour.dark_cyan(), CustomColour.dark_turquoise(),
    CustomColour.deep_teal(), CustomColour.light_cyan(), CustomColour.light_sea_green(),
    CustomColour.medium_aquamarine(), CustomColour.medium_turquoise(),
    CustomColour.pale_turquoise(), CustomColour.powder_blue(), CustomColour.turquoise(), Colour.teal(), Colour.dark_teal()
]

BLUE_COLOURS = [
    CustomColour.baby_blue(), CustomColour.blue_green(), CustomColour.cobalt_blue(),
    CustomColour.cornflower_blue(), CustomColour.dark_slate_blue(), CustomColour.deep_blue(),
    CustomColour.deep_sky_blue(), CustomColour.dodger_blue(), CustomColour.electric_blue(),
    CustomColour.light_blue(), CustomColour.light_sky_blue(), CustomColour.light_steel_blue(),
    CustomColour.medium_slate_blue(), CustomColour.midnight_blue(), CustomColour.navy_blue(),
    CustomColour.persian_blue(), CustomColour.prussian_blue(), CustomColour.royal_blue(),
    CustomColour.sapphire(), CustomColour.sky_blue(), CustomColour.slate_blue(),
    CustomColour.steel_blue(), CustomColour.ultramarine(), Colour.blue(), Colour.dark_blue(),
    Colour.blurple(), Colour.og_blurple()
]

BROWN_COLOURS = [
    CustomColour.blanched_almond(), CustomColour.brown(), CustomColour.burlywood(),
    CustomColour.chocolate(), CustomColour.coffee(), CustomColour.copper(),
    CustomColour.cornsilk(), CustomColour.desert_sand(),
    CustomColour.khaki(),  CustomColour.navajo_white(),
    CustomColour.peru(), CustomColour.rosy_brown(), CustomColour.saddle_brown(),
    CustomColour.sandy_brown(), CustomColour.sienna(), CustomColour.tan(), CustomColour.wheat()
]

WHITE_COLOURS = [
    CustomColour.alice_blue(), CustomColour.antique_white(), CustomColour.beige(),
    CustomColour.champagne(), CustomColour.floral_white(), CustomColour.ghost_white(),
    CustomColour.ivory(), CustomColour.lavender_blush(), CustomColour.linen(),
    CustomColour.misty_rose(), CustomColour.old_lace(), CustomColour.peach(),
    CustomColour.white(), CustomColour.white_smoke(), CustomColour.honeydew(), CustomColour.mint_cream()
]

GREY_COLOURS = [
    CustomColour.dark_slate_grey(), CustomColour.dim_grey(), CustomColour.gainsboro(),
    CustomColour.light_slate(), CustomColour.silver(), CustomColour.slate_grey(),
    CustomColour.taupe(), Colour.lighter_grey(), Colour.dark_grey(), Colour.light_grey(),
    Colour.darker_grey(), Colour.greyple(), Colour.dark_theme()
]

ALL_COLOURS = [
    RED_COLOURS, PINK_COLOURS, ORANGE_COLOURS, YELLOW_COLOURS, PURPLE_COLOURS, GREEN_COLOURS,
    CYAN_COLOURS, BLUE_COLOURS, BROWN_COLOURS, WHITE_COLOURS, GREY_COLOURS
]
######################################################################
