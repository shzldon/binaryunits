from typing import Union


class Multiple:
    """
    Binary multiples
    """

    KIBI = 2**10
    MEBI = 2**20
    GIBI = 2**30
    TEBI = 2**40
    PEBI = 2**50
    EXBI = 2**60
    ZEBI = 2**70
    YOBI = 2**80

    KILO = 1e3
    MEGA = 1e6
    GIGA = 1e9
    TERA = 1e12
    PETA = 1e15
    EXA = 1e18
    ZETTA = 1e21
    YOTTA = 1e24


class Size:
    """
    Representation of a binary size in octets (an octet is a byte 
    with 8 bits).

    Provides decimal and binary prefixes for multiples, from kilo-octets to
    yotta-octets and from kibi-octets to yobi-octets.

    Supports comparisons, string representations and arithmetic operations.

    For more information: https://en.wikipedia.org/wiki/Octet_(computing)
    """

    """ Constructors """

    def __init__(self, octets: int):

        if not isinstance(octets, int):
            raise TypeError("'octets' argument must be an integer")

        if octets < 0:
            raise ValueError("'octets' argument must be positive")

        self.octets = octets

    @classmethod
    def from_Kio(cls, kibioctets: Union[int, float]):
        return cls(int(kibioctets * Multiple.KIBI))

    @classmethod
    def from_Mio(cls, mebioctets: Union[int, float]):
        return cls(int(mebioctets * Multiple.MEBI))

    @classmethod
    def from_Gio(cls, gibioctets: Union[int, float]):
        return cls(int(gibioctets * Multiple.GIBI))

    @classmethod
    def from_Tio(cls, tebioctets: Union[int, float]):
        return cls(int(tebioctets * Multiple.TEBI))

    @classmethod
    def from_Pio(cls, pebioctets: Union[int, float]):
        return cls(int(pebioctets * Multiple.PEBI))

    @classmethod
    def from_Eio(cls, exbioctets: Union[int, float]):
        return cls(int(exbioctets * Multiple.EXBI))

    @classmethod
    def from_Zio(cls, zebioctets: Union[int, float]):
        return cls(int(zebioctets * Multiple.ZEBI))

    @classmethod
    def from_Yio(cls, yobioctets: Union[int, float]):
        return cls(int(yobioctets * Multiple.YOBI))

    """ Properties """

    @property
    def o(self) -> int:
        """ Just another way to access octets """
        return self.octets

    @property
    def Kio(self, decimals=None) -> float:
        """ Size in kibioctets """
        return float(self.octets / Multiple.KIBI)

    @property
    def Mio(self) -> float:
        """ Size in mebioctets """
        return float(self.octets / Multiple.MEBI)

    @property
    def Gio(self) -> float:
        """ Size in gibioctets """
        return float(self.octets / Multiple.GIGA)

    @property
    def Tio(self) -> float:
        """ Size in tebioctets """
        return float(self.octets / Multiple.TEBI)

    @property
    def Pio(self) -> float:
        """ Size in pebioctets """
        return float(self.octets / Multiple.PEBI)

    @property
    def Eio(self) -> float:
        """ Size in exbioctets """
        return float(self.octets / Multiple.EXBI)

    @property
    def Zio(self) -> float:
        """ Size in zebioctets """
        return float(self.octets / Multiple.ZEBI)

    @property
    def Yio(self) -> float:
        """ Size in yobioctets """
        return float(self.octets / Multiple.YOBI)

    @property
    def ko(self) -> float:
        """ Size in kilooctets """
        return float(self.octets / Multiple.KILO)

    @property
    def Mo(self) -> float:
        """ Size in megaoctets """
        return float(self.octets / Multiple.MEGA)

    @property
    def Go(self) -> float:
        """ Size in gigaoctets """
        return float(self.octets / Multiple.GIGA)

    @property
    def To(self) -> float:
        """ Size in teraoctets """
        return float(self.octets / Multiple.TERA)

    @property
    def Po(self) -> float:
        """ Size in petaoctets """
        return float(self.octets / Multiple.PETA)

    @property
    def Eo(self) -> float:
        """ Size in exaoctets """
        return float(self.octets / Multiple.EXA)

    @property
    def Zo(self) -> float:
        """ Size in zettaoctets """
        return float(self.octets / Multiple.ZETTA)

    @property
    def Yo(self) -> float:
        """ Size in yottaoctets """
        return float(self.octets / Multiple.YOTTA)

    """ Comparison magic methods """

    def __eq__(self, other):
        return self.octets == other.octets

    def __ne__(self, other):
        return self.octets != other.octets

    def __lt__(self, other):
        return self.octets < other.octets

    def __gt__(self, other):
        return self.octets > other.octets

    def __le__(self, other):
        return self.octets <= other.octets

    def __ge__(self, other):
        return self.octets >= other.octets

    """ Representations """

    def __str__(self):
        return f"{self.octets} octets"

    def __repr__(self):
        return f"{__name__} {self.octets}"

    def __hash__(self):
        return hash(self.octets)

    def __nonzero__(self):
        return self.octets == 0

    """ Normal arithmetic operators """

    def __add__(self, other):
        return Size(self.octets + other.octets)

    def __sub__(self, other):
        difference = self.octets - other.octets
        if difference < 0:
            raise ValueError(
                "Difference between Size objects cannot be negative")
        else:
            return Size(difference)

    def __div__(self, other):
        return self.octets / other.octets

    def __floordiv__(self, other):
        return self.octets // other.octets

    def __mod__(self, other):
        return Size(self.octets % other.octets)

    def __divmod__(self, other):
        return (self.octets // other.octets, Size(self.octets % other.octets))

    def __pow__(self, power):
        return Size(self.octets ** power)

    # rshift

    # lshift
