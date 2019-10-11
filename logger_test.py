#This code tests the Logger file
import os
from virus import Virus
from person import Person
from logger import Logger
from simulation import *

def test_logger_metadata():
    logger = Logger('test_log.txt')
    logger.write_metadata(100, 0.9, 'Ebola', 0.7, 0.25)

    with open('test_log.txt', 'r') as f:
        val = f.read()

        assert val == "Population size: 100  Vaccination percentage: 0.9  Virus name: Ebola  Mortality rate: 0.7  Basic reproduction num: 0.25\n"

    os.remove('test_log.txt')
