class Size:
    """ Representation of a binary size in octets (an octet is a byte 
    with 8 bits).

    Provides decimal and binary prefixes for multiples, from kilo-octets to
    yotta-octets and from kibi-octets to yobi-octets.

    Supports comparisons, string representations and arithmetic operations."""

    def __init__(self, octets: int):

        if not isinstance(octets, int):
            raise TypeError("'octets' argument must be an integer")

        if octets < 0:
            raise ValueError("'octets' argument must be positive")

        self.octets = octets

    """ Properties """

    @property
    def o(self) -> int:
        """ Just another way to access octets """
        return self.octets

    @property
    def Kio(self, decimals=None) -> float:
        """ Size in kibioctets """
        return float(self.octets / 2**10)

    @property
    def Mio(self) -> float:
        """ Size in mebioctets """
        return float(self.octets / 2**20)

    @property
    def Gio(self) -> float:
        """ Size in gibioctets """
        return float(self.octets / 2**30)

    @property
    def Tio(self) -> float:
        """ Size in tebioctets """
        return float(self.octets / 2**40)

    @property
    def Pio(self) -> float:
        """ Size in pebioctets """
        return float(self.octets / 2**50)

    @property
    def Eio(self) -> float:
        """ Size in exbioctets """
        return float(self.octets / 2**60)

    @property
    def Zio(self) -> float:
        """ Size in zebioctets """
        return float(self.octets / 2**70)

    @property
    def Yio(self) -> float:
        """ Size in yobioctets """
        return float(self.octets / 2**80)

    @property
    def ko(self) -> float:
        """ Size in kilooctets """
        return float(self.octets / 1e3)

    @property
    def Mo(self) -> float:
        """ Size in megaoctets """
        return float(self.octets / 1e6)

    @property
    def Go(self) -> float:
        """ Size in gigaoctets """
        return float(self.octets / 1e9)

    @property
    def To(self) -> float:
        """ Size in teraoctets """
        return float(self.octets / 1e12)

    @property
    def Po(self) -> float:
        """ Size in petaoctets """
        return float(self.octets / 1e15)

    @property
    def Eo(self) -> float:
        """ Size in exaoctets """
        return float(self.octets / 1e18)

    @property
    def Zo(self) -> float:
        """ Size in zettaoctets """
        return float(self.octets / 1e21)

    @property
    def Yo(self) -> float:
        """ Size in yottaoctets """
        return float(self.octets / 1e24)

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
