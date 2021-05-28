"""Testing the module wich manage units"""

#should support:
#masse: g, kg, pound
#volume: ml, l, m**3,

from balance.units import Mass, Volume

def test_mass():
	mass1000g = Mass(1000)
	assert mass1000g.g == 1000
	assert mass1000g.kg == 1
	mass1pound = Mass()
	mass1pound.imperial_pound=1
	assert mass1pound.imperial_pound == 1.0
	assert mass1pound.kg == 0.45359237
