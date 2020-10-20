class Size:

    """ Constructor """

    def __init__(self, size_in_bytes: int):

        if not isinstance(size_in_bytes, int):
            raise TypeError("Size must be an integer")

        if size_in_bytes < 0:
            raise ValueError("Size must be positive")

        self._size_in_bytes = size_in_bytes

    """ Properties """

    @property
    def B(self) -> int:
        return self._size_in_bytes

    @property
    def KiB(self, decimals=None) -> float:
        """ Size in kibibytes """
        return float(self._size_in_bytes / 2**10)

    @property
    def MiB(self) -> float:
        """ Size in mebibytes """
        return float(self._size_in_bytes / 2**20)

    @property
    def GiB(self) -> float:
        """ Size in gibibytes """
        return float(self._size_in_bytes / 2**30)

    @property
    def TiB(self) -> float:
        """ Size in tebibytes """
        return float(self._size_in_bytes / 2**40)

    @property
    def PiB(self) -> float:
        """ Size in pebibytes """
        return float(self._size_in_bytes / 2**50)

    @property
    def EiB(self) -> float:
        """ Size in exbibytes """
        return float(self._size_in_bytes / 2**60)

    @property
    def ZiB(self) -> float:
        """ Size in zebibytes """
        return float(self._size_in_bytes / 2**70)

    @property
    def YiB(self) -> float:
        """ Size in yobibytes """
        return float(self._size_in_bytes / 2**80)

    @property
    def kB(self) -> float:
        """ Size in kilobytes """
        return float(self._size_in_bytes / 1e3)

    @property
    def MB(self) -> float:
        """ Size in megabytes """
        return float(self._size_in_bytes / 1e6)

    @property
    def GB(self) -> float:
        """ Size in gigabytes """
        return float(self._size_in_bytes / 1e9)

    @property
    def TB(self) -> float:
        """ Size in terabytes """
        return float(self._size_in_bytes / 1e12)

    @property
    def PB(self) -> float:
        """ Size in petabytes """
        return float(self._size_in_bytes / 1e15)

    @property
    def EB(self) -> float:
        """ Size in exabytes """
        return float(self._size_in_bytes / 1e18)

    @property
    def ZB(self) -> float:
        """ Size in zettabytes """
        return float(self._size_in_bytes / 1e21)

    @property
    def YB(self) -> float:
        """ Size in yottabytes """
        return float(self._size_in_bytes / 1e24)

    """ Comparison magic methods """

    def __eq__(self, other):
        return self.B == other.B

    def __ne__(self, other):
        return self.B != other.B

    def __lt__(self, other):
        return self.B < other.B

    def __gt__(self, other):
        return self.B > other.B

    def __le__(self, other):
        return self.B <= other.B

    def __ge__(self, other):
        return self.B >= other.B

    """ Representations """

    def __str__(self):
        return "%i bytes" % self.B

    def __repr__(self):
        return "%s %i" % (__name__, self.B)

    def __hash__(self):
        return hash(self.B)

    # def __nonzero__(self):
    #     return bool(self.B)

    """ Normal arithmetic operators """

    def __add__(self, other):
        return Size(self.B + other.B)

    def __sub__(self, other):
        return Size(self.B - other.B)

    def __div__(self, other):
        return self.B / other.B

    def __floordiv__(self, other):
        return self.B // other.B

    def __mod__(self, other):
        return Size(self.B % other.B)

    def __divmod__(self, other):
        return (self.B // other.B, Size(self.B % other.B))

    def __pow__(self, power):
        return Size(self.B ** power)

    """ Augmented assigment """

    # TODO : complete this section

    """ Type conversion magic methods """

    # TODO : complete this section
    
    # TODO : descriptors