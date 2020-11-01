# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Sun Nov 1 15:46:30 2020
#      by: The Resource Compiler for PySide2 (Qt v5.12.9)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
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
\x00\x00\x06\x07\
<\
?xml version = \x22\
1.0\x22 encoding = \
\x22UTF-8\x22 ?>\x0d\x0a<!--\
Interface proper\
ties changeable \
by the user are \
stored here.-->\x0d\
\x0a<data>\x0d\x0a    <it\
ems>\x0d\x0a        <!\
--Default values\
.-->\x0d\x0a        <i\
tem name=\x22time-s\
tep-default\x22>1.0\
</item>\x0d\x0a       \
 <item name=\x22dur\
ation-default\x22>5\
00.0</item>\x0d\x0a\x0d\x0a \
       <!--Step \
between values w\
hen using a QDou\
bleSpinBox.-->\x0d\x0a\
        <item na\
me=\x22time-step-st\
ep\x22>1.0</item>\x0d\x0a\
        <item na\
me=\x22duration-ste\
p\x22>10.0</item>\x0d\x0a\
        <item na\
me=\x22mass-step\x22>0\
.1</item>\x0d\x0a     \
   <item name=\x22p\
osition-step\x22>0.\
1</item>\x0d\x0a      \
  <item name=\x22ve\
locity-step\x22>0.1\
</item>\x0d\x0a\x0d\x0a     \
   <!--Minimum a\
llowed values.--\
>\x0d\x0a        <item\
 name=\x22time-step\
-min\x22>0.0</item>\
\x0d\x0a        <item \
name=\x22duration-m\
in\x22>0.0</item>\x0d\x0a\
        <item na\
me=\x22mass-min\x22>0.\
000001</item>\x0d\x0a \
       <item nam\
e=\x22position-min\x22\
>-1000.0</item>\x0d\
\x0a        <item n\
ame=\x22velocity-mi\
n\x22>-1000.0</item\
>\x0d\x0a\x0d\x0a        <!-\
-Maximum allowed\
 values.-->\x0d\x0a   \
     <item name=\
\x22time-step-max\x22>\
500.0</item>\x0d\x0a  \
      <item name\
=\x22duration-max\x22>\
10000.0</item>\x0d\x0a\
        <item na\
me=\x22mass-max\x22>10\
0.0</item>\x0d\x0a    \
    <item name=\x22\
position-max\x22>10\
00.0</item>\x0d\x0a   \
     <item name=\
\x22velocity-max\x22>1\
000.0</item>\x0d\x0a\x0d\x0a\
        <!--Unit\
s for different \
parameters.-->\x0d\x0a\
        <item na\
me=\x22time-unit\x22>d\
</item>\x0d\x0a       \
 <item name=\x22mas\
s-unit\x22>M*</item\
>\x0d\x0a        <item\
 name=\x22position-\
unit\x22>au</item>\x0d\
\x0a\x0d\x0a        <!--N\
umber of decimal\
 places.-->\x0d\x0a   \
     <item name=\
\x22time-dp\x22>2</ite\
m>\x0d\x0a        <ite\
m name=\x22mass-dp\x22\
>6</item>\x0d\x0a     \
   <item name=\x22p\
osition-dp\x22>6</i\
tem>\x0d\x0a        <i\
tem name=\x22veloci\
ty-dp\x22>6</item>\x0d\
\x0a    </items>\x0d\x0a<\
/data>\
"

qt_resource_name = b"\
\x00\x18\
\x04\xc2\xb9\x9c\
\x00i\
\x00n\x00t\x00e\x00r\x00f\x00a\x00c\x00e\x00-\x00p\x00r\x00o\x00p\x00e\x00r\x00t\
\x00i\x00e\x00s\x00.\x00x\x00m\x00l\
\x00\x1d\
\x05\x0a|\xdc\
\x00u\
\x00s\x00e\x00r\x00-\x00i\x00n\x00t\x00e\x00r\x00f\x00a\x00c\x00e\x00-\x00p\x00r\
\x00o\x00p\x00e\x00r\x00t\x00i\x00e\x00s\x00.\x00x\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x00\x82\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
