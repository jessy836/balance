"""Testing the module wich manage units"""

from balance.units import Mass, Volume
#wich should support:
#for each units, it should support subd
#masse: g, kg, pound
#volume: l, m**3,

def test_mass():
	mass1000g = Mass(1000)
	assert masse1000g.g == 1000
	assert mass1000g.kg == 1
	mass1pound = Mass()
	mass1pound.pound=1
	assert mass1pound.kg == 0.45359237
