"""A module for implemeting units mesures"""


class Mass:
    """Object representing a Mass in different units"""

    def __init__(self, g=0):
        """initialize a Mass object default to 0 g"""
        self._g = float(g)

    @property
    def g(self):
        """return mass in g"""
        return self._g

    @g.setter
    def g(self, g):
        """set the value of mass by g"""
        self._g = float(g)

    @property
    def kg(self):
        """return mass in kg"""
        return self._g / 1000

    @kg.setter
    def kg(self, kg):
        """set the mass with  kg"""
        self._g = kg * 1000

    @property
    def imperial_pound(self):
        """return mass in imperial pound"""
        return self.kg / 0.45359237

    @imperial_pound.setter
    def imperial_pound(self, pound):
        """set the mass with imperial_pound"""
        self.kg = pound * 0.45359237


class Volume:
    """object representing a volume in several units"""

    def __init__(self, ml=0.0):
        """initialized a Volume object default to 0.0 ml"""
        self._ml = float(ml)

    @property
    def ml(self):
        """return the value of volume in ml """
        return self._ml

    @ml.setter
    def ml(self, ml):
        """set the volume in ml """
        self._ml = float(ml)

    @property
    def l(self):
        """Return the value of volume in l"""
        return self.ml / 1000

    @l.setter
    def l(self, l):
        """set the value of volume with  l"""
        self.ml = l * 1000

    @property
    def m3(self):
        """return the value of volume in m3"""
        return self.l / 1000

    @m3.setter
    def m3(self, m3):
        """set the value of volume with m3"""
        self.l = float(m3) * 1000
