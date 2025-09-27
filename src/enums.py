"""
enum.py
----------------------
Defines categorical feature enums and Pydantic models 
for mushroom dataset classification API.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel

# -----------------------------
# Enums for each categorical feature
# -----------------------------

class CapShape(str, Enum):
    bell = "b"
    conical = "c"
    convex = "x"
    flat = "f"
    knobbed = "k"
    sunken = "s"


class CapSurface(str, Enum):
    fibrous = "f"
    grooves = "g"
    scaly = "y"
    smooth = "s"


class CapColor(str, Enum):
    brown = "n"
    buff = "b"
    cinnamon = "c"
    gray = "g"
    green = "r"
    pink = "p"
    purple = "u"
    red = "e"
    white = "w"
    yellow = "y"


class Bruises(str, Enum):
    yes = "t"
    no = "f"


class Odor(str, Enum):
    almond = "a"
    anise = "l"
    creosote = "c"
    fishy = "y"
    foul = "f"
    musty = "m"
    none = "n"
    pungent = "p"
    spicy = "s"


class GillAttachment(str, Enum):
    attached = "a"
    descending = "d"
    free = "f"
    notched = "n"


class GillSpacing(str, Enum):
    close = "c"
    crowded = "w"
    distant = "d"


class GillSize(str, Enum):
    broad = "b"
    narrow = "n"


class GillColor(str, Enum):
    black = "k"
    brown = "n"
    buff = "b"
    chocolate = "h"
    gray = "g"
    green = "r"
    orange = "o"
    pink = "p"
    purple = "u"
    red = "e"
    white = "w"
    yellow = "y"


class StalkShape(str, Enum):
    enlarging = "e"
    tapering = "t"


class StalkRoot(str, Enum):
    bulbous = "b"
    club = "c"
    cup = "u"
    equal = "e"
    rhizomorphs = "z"
    rooted = "r"
    missing = "?"


class StalkSurfaceAboveRing(str, Enum):
    fibrous = "f"
    scaly = "y"
    silky = "k"
    smooth = "s"


class StalkSurfaceBelowRing(str, Enum):
    fibrous = "f"
    scaly = "y"
    silky = "k"
    smooth = "s"


class StalkColorAboveRing(str, Enum):
    brown = "n"
    buff = "b"
    cinnamon = "c"
    gray = "g"
    orange = "o"
    pink = "p"
    red = "e"
    white = "w"
    yellow = "y"


class StalkColorBelowRing(str, Enum):
    brown = "n"
    buff = "b"
    cinnamon = "c"
    gray = "g"
    orange = "o"
    pink = "p"
    red = "e"
    white = "w"
    yellow = "y"


class VeilType(str, Enum):
    partial = "p"


class VeilColor(str, Enum):
    brown = "n"
    orange = "o"
    white = "w"
    yellow = "y"


class RingNumber(str, Enum):
    none = "n"
    one = "o"
    two = "t"


class RingType(str, Enum):
    cobwebby = "c"
    evanescent = "e"
    flaring = "f"
    large = "l"
    none = "n"
    pendant = "p"
    sheathing = "s"
    zone = "z"


class SporePrintColor(str, Enum):
    black = "k"
    brown = "n"
    buff = "b"
    chocolate = "h"
    green = "r"
    orange = "o"
    purple = "u"
    white = "w"
    yellow = "y"


class Population(str, Enum):
    abundant = "a"
    clustered = "c"
    numerous = "n"
    scattered = "s"
    several = "v"
    solitary = "y"


class Habitat(str, Enum):
    grasses = "g"
    leaves = "l"
    meadows = "m"
    paths = "p"
    urban = "u"
    waste = "w"
    woods = "d"


# -----------------------------
# Target Enum
# -----------------------------
class MushroomClass(str, Enum):
    edible = "e"
    poisonous = "p"


# -----------------------------
# Pydantic model for API input
# -----------------------------
class MushroomInput(BaseModel):
    cap_shape: CapShape
    cap_surface: CapSurface
    cap_color: CapColor
    bruises: Bruises
    odor: Odor
    gill_attachment: GillAttachment
    gill_spacing: GillSpacing
    gill_size: GillSize
    gill_color: GillColor
    stalk_shape: StalkShape
    stalk_root: Optional[StalkRoot]
    stalk_surface_above_ring: StalkSurfaceAboveRing
    stalk_surface_below_ring: StalkSurfaceBelowRing
    stalk_color_above_ring: StalkColorAboveRing
    stalk_color_below_ring: StalkColorBelowRing
    veil_type: VeilType
    veil_color: VeilColor
    ring_number: RingNumber
    ring_type: RingType
    spore_print_color: SporePrintColor
    population: Population
    habitat: Habitat

    class Config:
        json_schema_extra = {
            "example": {
                "cap_shape": "x",
                "cap_surface": "s",
                "cap_color": "n",
                "bruises": "t",
                "odor": "p",
                "gill_attachment": "f",
                "gill_spacing": "c",
                "gill_size": "b",
                "gill_color": "k",
                "stalk_shape": "e",
                "stalk_root": "b",
                "stalk_surface_above_ring": "s",
                "stalk_surface_below_ring": "s",
                "stalk_color_above_ring": "w",
                "stalk_color_below_ring": "w",
                "veil_type": "p",
                "veil_color": "w",
                "ring_number": "o",
                "ring_type": "p",
                "spore_print_color": "k",
                "population": "s",
                "habitat": "u"
            }
        }
