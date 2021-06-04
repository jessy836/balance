"""A module for implemeting units mesures"""


class Mass:
    """Object representing a Mass in different units"""

    def __init__(self, gram=0):
        """initialize a Mass object default to 0 g"""
        self._gram = float(gram)

    @property
    def gram(self):
        """return mass in g"""
        return self._gram

    @gram.setter
    def gram(self, gram):
        """set the value of mass by g"""
        self._gram = float(gram)

    @property
    def kilogram(self):
        """return mass in kg"""
        return self._gram / 1000

    @kilogram.setter
    def kilogram(self, kilogram):
        """set the mass with  kg"""
        self._gram = kilogram * 1000

    @property
    def imperial_pound(self):
        """return mass in imperial pound"""
        return self.kilogram / 0.45359237

    @imperial_pound.setter
    def imperial_pound(self, pound):
        """set the mass with imperial_pound"""
        self.kilogram = pound * 0.45359237


class Volume:
    """object representing a volume in several units"""

    def __init__(self, milliliter=0.0):
        """initialized a Volume object default to 0.0 ml"""
        self._milliliter = float(milliliter)

    @property
    def milliliter(self):
        """return the value of volume in ml """
        return self._milliliter

    @milliliter.setter
    def milliliter(self, milliliter):
        """set the volume in ml """
        self._milliliter = float(milliliter)

    @property
    def liter(self):
        """Return the value of volume in l"""
        return self.milliliter / 1000

    @liter.setter
    def liter(self, liter):
        """set the value of volume with  l"""
        self.milliliter = liter * 1000

    @property
    def cubic_meter(self):
        """return the value of volume in m3"""
        return self.liter / 1000

    @cubic_meter.setter
    def cubic_meter(self, cubic_meter):
        """set the value of volume with m3"""
        self.liter = float(cubic_meter) * 1000
