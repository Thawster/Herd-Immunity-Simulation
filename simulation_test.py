from simulation import Simulation
from virus import Virus
import unittest

class xfunction(unittest.TestCase):

     def xtype_of_cases(self):
         sim = Simulation(1000, .85, 15, virus)
         virus = Virus("Canada", .3, .8)
         assert Simulation.create_population('') is []


if __name__ == '__main__':
    unittest.main() 