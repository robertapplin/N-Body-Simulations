# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import sys
from os.path import dirname, abspath, join
import pytest
from PyQt5.QtCore import QCoreApplication

THIS_DIRECTORY = dirname(__file__)
STARTUP_SCRIPT = abspath(join(THIS_DIRECTORY, '..', '..', '..', 'python', 'startup.py'))

llll = abspath(join(THIS_DIRECTORY, '..', '..', '..', 'python'))
sys.path.append(llll)
from startup import qapp, MainGUI


def test_that_the_interface_opens_without_an_error():
    #QCoreApplication.setApplicationName("testing")
    exec(open(STARTUP_SCRIPT).read())
