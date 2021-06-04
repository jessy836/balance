"""Testing the module wich manage units"""

# should support:
# masse: g, kg, pound
# volume: ml, l, m**3,

from balance.units import Mass, Volume


def test_mass():
    mass1000g = Mass(1000)
    assert mass1000g.gram == 1000
    assert mass1000g.kilogram == 1
    mass1pound = Mass()
    mass1pound.imperial_pound = 1
    assert mass1pound.imperial_pound == 1.0
    assert mass1pound.kilogram == 0.45359237


def test_volume():
    volume1ml = Volume()
    assert volume1ml.milliliter == 0.0
    volume1m3 = Volume()
    volume1m3.liter = 1000
    assert volume1m3.cubic_meter == 1.0
    volume1l = Volume()
    volume1l.milliliter = 1000
    assert volume1l.liter == 1.0
