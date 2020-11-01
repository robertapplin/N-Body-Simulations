# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from xml.dom import minidom

from PyQt5.QtCore import QFile, QTextStream

INTERFACE_PROPERTY_FILE = ":/interface-properties.xml"
USER_INTERFACE_PROPERTY_FILE = ":/user-interface-properties.xml"


def get_interface_property(property_name: str) -> str:
    """Returns the specified property from the interface-properties.xml file."""
    return get_xml_file_property(INTERFACE_PROPERTY_FILE, property_name)


def get_user_interface_property(property_name: str) -> str:
    """Returns the specified property from the user-interface-properties.xml file."""
    return get_xml_file_property(USER_INTERFACE_PROPERTY_FILE, property_name)


def get_xml_file_property(filename: str, item_name: str) -> str:
    """Get an item with the specified name from an xml file."""
    file = QFile(filename)
    if file.open(QFile.ReadOnly):
        document_string = minidom.parseString(QTextStream(file).readAll())
        return get_xml_property(document_string, filename, item_name)

    raise RuntimeError(f"Could not open the file '{filename}'.")


def get_xml_property(document_string: str, filename: str, item_name: str) -> str:
    """Get an item with the specified name from an xml document string."""
    for element in document_string.getElementsByTagName('item'):
        if element.attributes['name'].value == item_name:
            return element.firstChild.data

    raise ValueError(f"The item '{item_name}' does not exist in the file '{filename}'.")
