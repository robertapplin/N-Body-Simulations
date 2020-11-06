# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from xml.dom import minidom

from n_body_simulations.interface_resources_rc import qInitResources

from PyQt5.QtCore import QCoreApplication, QFile, QTextStream

SIMULATION_SETTINGS_FILE = ":/simulation-settings.xml"
USER_INTERFACE_PROPERTY_FILE = ":/user-interface-properties.xml"


def get_simulation_setting(property_name: str) -> str:
    """Returns the specified simulation setting from the simulation-settings.xml file."""
    return _get_xml_file_property(SIMULATION_SETTINGS_FILE, property_name)


def get_user_interface_property(property_name: str) -> str:
    """Returns the specified property from the user-interface-properties.xml file."""
    return _get_xml_file_property(USER_INTERFACE_PROPERTY_FILE, property_name)


def _get_xml_file_property(filename: str, item_name: str) -> str:
    """Get an item with the specified name from an xml file."""
    if QCoreApplication.applicationName() == "test":
        qInitResources()

    file = QFile(filename)
    if file.open(QFile.ReadOnly):
        document_string = minidom.parseString(QTextStream(file).readAll())
        return _get_xml_property(document_string, filename, item_name)

    raise RuntimeError(f"Could not open the file '{filename}'.")


def _get_xml_property(document_string: str, filename: str, item_name: str) -> str:
    """Get an item with the specified name from an xml document string."""
    for element in document_string.getElementsByTagName('item'):
        if element.attributes['name'].value == item_name:
            return element.firstChild.data

    raise ValueError(f"The item '{item_name}' does not exist in the file '{filename}'.")
