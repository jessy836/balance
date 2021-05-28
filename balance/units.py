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

    pass
