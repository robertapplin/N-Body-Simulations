# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import os

from xml.dom import minidom

from PyQt5.QtCore import QFile, QResource, QTextStream


def print_data():

    file = QFile(":/user-interface-properties.xml")
    if file.open(QFile.ReadOnly):
        mydoc = minidom.parseString(QTextStream(file).readAll())

        items = mydoc.getElementsByTagName('item')

        for elem in items:
            if elem.attributes['name'].value == "item2":
                print(elem.firstChild.data)
