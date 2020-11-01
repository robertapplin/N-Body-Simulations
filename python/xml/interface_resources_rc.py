# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Sun Nov 1 14:22:13 2020
#      by: The Resource Compiler for PySide2 (Qt v5.12.9)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xf4\
<\
?xml version = \x22\
1.0\x22 encoding = \
\x22UTF-8\x22 ?>\x0d\x0a<!--\
Interface proper\
ties changeable \
by the user are \
stored here.-->\x0d\
\x0a<data>\x0d\x0a    <it\
ems>\x0d\x0a        <i\
tem name=\x22item1\x22\
>item1abc</item>\
\x0d\x0a        <item \
name=\x22item2\x22>ite\
m2abc</item>\x0d\x0a  \
  </items>\x0d\x0a</da\
ta>\
\x00\x00\x00~\
<\
?xml version = \x22\
1.0\x22 encoding = \
\x22UTF-8\x22 ?>\x0d\x0a<!--\
Interface proper\
ties which are n\
ot changeable by\
 the user are st\
ored here.-->\
"

qt_resource_name = b"\
\x00\x1d\
\x05\x0a|\xdc\
\x00u\
\x00s\x00e\x00r\x00-\x00i\x00n\x00t\x00e\x00r\x00f\x00a\x00c\x00e\x00-\x00p\x00r\
\x00o\x00p\x00e\x00r\x00t\x00i\x00e\x00s\x00.\x00x\x00m\x00l\
\x00\x18\
\x04\xc2\xb9\x9c\
\x00i\
\x00n\x00t\x00e\x00r\x00f\x00a\x00c\x00e\x00-\x00p\x00r\x00o\x00p\x00e\x00r\x00t\
\x00i\x00e\x00s\x00.\x00x\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00@\x00\x00\x00\x00\x00\x01\x00\x00\x00\xf8\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
