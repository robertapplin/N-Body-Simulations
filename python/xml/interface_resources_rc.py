# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Fri Nov 6 20:18:51 2020
#      by: The Resource Compiler for PySide2 (Qt v5.12.9)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xec\
<\
?xml version = \x22\
1.0\x22 encoding = \
\x22UTF-8\x22 ?>\x0d\x0a<!--\
Simulation setti\
ngs are stored h\
ere.-->\x0d\x0a<data>\x0d\
\x0a    <items>\x0d\x0a  \
      <!--Settin\
gs used for the \
simulation.-->\x0d\x0a\
        <item na\
me=\x22max-number-o\
f-bodies\x22>5</ite\
m>\x0d\x0a    </items>\
\x0d\x0a</data>\x0d\x0a\
\x00\x00\x06\x0d\
<\
?xml version = \x22\
1.0\x22 encoding = \
\x22UTF-8\x22 ?>\x0d\x0a<!--\
Interface proper\
ties are stored \
here to avoid ha\
rd-coded values.\
-->\x0d\x0a<data>\x0d\x0a   \
 <items>\x0d\x0a      \
  <!--Default va\
lues.-->\x0d\x0a      \
  <item name=\x22ti\
me-step-default\x22\
>1.0</item>\x0d\x0a   \
     <item name=\
\x22duration-defaul\
t\x22>500.0</item>\x0d\
\x0a\x0d\x0a        <!--S\
tep between valu\
es when using a \
QDoubleSpinBox.-\
->\x0d\x0a        <ite\
m name=\x22time-ste\
p-step\x22>1.0</ite\
m>\x0d\x0a        <ite\
m name=\x22duration\
-step\x22>10.0</ite\
m>\x0d\x0a        <ite\
m name=\x22mass-ste\
p\x22>0.1</item>\x0d\x0a \
       <item nam\
e=\x22position-step\
\x22>0.1</item>\x0d\x0a  \
      <item name\
=\x22velocity-step\x22\
>0.1</item>\x0d\x0a\x0d\x0a \
       <!--Minim\
um allowed value\
s.-->\x0d\x0a        <\
item name=\x22time-\
step-min\x22>0.0</i\
tem>\x0d\x0a        <i\
tem name=\x22durati\
on-min\x22>0.0</ite\
m>\x0d\x0a        <ite\
m name=\x22mass-min\
\x22>0.000001</item\
>\x0d\x0a        <item\
 name=\x22position-\
min\x22>-1000.0</it\
em>\x0d\x0a        <it\
em name=\x22velocit\
y-min\x22>-1000.0</\
item>\x0d\x0a\x0d\x0a       \
 <!--Maximum all\
owed values.-->\x0d\
\x0a        <item n\
ame=\x22time-step-m\
ax\x22>500.0</item>\
\x0d\x0a        <item \
name=\x22duration-m\
ax\x22>10000.0</ite\
m>\x0d\x0a        <ite\
m name=\x22mass-max\
\x22>100.0</item>\x0d\x0a\
        <item na\
me=\x22position-max\
\x22>1000.0</item>\x0d\
\x0a        <item n\
ame=\x22velocity-ma\
x\x22>1000.0</item>\
\x0d\x0a\x0d\x0a        <!--\
Units for differ\
ent parameters.-\
->\x0d\x0a        <ite\
m name=\x22time-uni\
t\x22>d</item>\x0d\x0a   \
     <item name=\
\x22mass-unit\x22>M*</\
item>\x0d\x0a        <\
item name=\x22posit\
ion-unit\x22>au</it\
em>\x0d\x0a\x0d\x0a        <\
!--Number of dec\
imal places.-->\x0d\
\x0a        <item n\
ame=\x22time-dp\x22>2<\
/item>\x0d\x0a        \
<item name=\x22mass\
-dp\x22>6</item>\x0d\x0a \
       <item nam\
e=\x22position-dp\x22>\
6</item>\x0d\x0a      \
  <item name=\x22ve\
locity-dp\x22>6</it\
em>\x0d\x0a    </items\
>\x0d\x0a</data>\x0d\x0a\
"

qt_resource_name = b"\
\x00\x17\
\x04#\x14\xfc\
\x00s\
\x00i\x00m\x00u\x00l\x00a\x00t\x00i\x00o\x00n\x00-\x00s\x00e\x00t\x00t\x00i\x00n\
\x00g\x00s\x00.\x00x\x00m\x00l\
\x00\x1d\
\x05\x0a|\xdc\
\x00u\
\x00s\x00e\x00r\x00-\x00i\x00n\x00t\x00e\x00r\x00f\x00a\x00c\x00e\x00-\x00p\x00r\
\x00o\x00p\x00e\x00r\x00t\x00i\x00e\x00s\x00.\x00x\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x004\x00\x00\x00\x00\x00\x01\x00\x00\x00\xf0\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
