# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from os.path import dirname, abspath, join
import sys

THIS_DIRECTORY = dirname(__file__)

directory = abspath(join(THIS_DIRECTORY, '..', '..', '..', '..', 'interface', 'qt'))
sys.path.append(directory)
