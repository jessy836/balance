"""Testing the module wich manage units"""

# should support:
# masse: g, kg, pound
# volume: ml, l, m**3,

from balance.units import Mass, Volume


def test_mass():
    mass1000g = Mass(1000)
    assert mass1000g.g == 1000
    assert mass1000g.kg == 1
    mass1pound = Mass()
    mass1pound.imperial_pound = 1
    assert mass1pound.imperial_pound == 1.0
    assert mass1pound.kg == 0.45359237


def test_volume():
    volume1ml = Volume()
    assert volume1ml.ml == 0.0
    volume1m3 = Volume()
    volume1m3.l = 1000
    assert volume1m3.m3 == 1.0
    volume1l = Volume()
    volume1l.ml = 1000
    assert volume1l.l == 1.0
