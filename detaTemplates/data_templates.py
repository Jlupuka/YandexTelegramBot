from enum import Enum


class DataTimer(Enum):
    five_minute: int = 60 * 5
    one_minute: int = 60
    seconds_30: int = 30


class FacetsDice(Enum):
    hexagonal: int = 6
    double_hexagonal: int = 6
    twenty_sided: int = 20
