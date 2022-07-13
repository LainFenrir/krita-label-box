"""
    label-box adds a color label box on the layer docker like CSP
    Copyright (C) 2022  LunarKreatures

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *
from PyQt5.QtWidgets import QHBoxLayout,QComboBox
from PyQt5.QtGui import QIcon,QPixmap
from .kritaUtils import getCurrentLayer,getSelectedLayers

# Colors for the color labels, copied from krita code in KisNodeViewColorScheme.cpp
transparentColor = QColor(Qt.transparent) #0
blueColor = QColor(91,173,220) #1
greenColor = QColor(151,202,63) #2
yellowColor = QColor(247,229,61) #3
orangeColor = QColor(255,170,63) #4
brownColor = QColor(177,102,63) #5
redColor = QColor(238,50,51) #6
purpleColor = QColor(191,106,209) #7
greyColor = QColor(118,119,114) #8

class LabelBox(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self.comboBox = self.buildComboBox()
        application = Krita.instance()
        appNotifier  = application.notifier()
        appNotifier.windowCreated.connect(self.addElement)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        pass

    # called after setup(self)
    def createActions(self, window):
        pass

    def addElement(self):
        layerDocker = next((w for w in Krita.instance().dockers() if w.objectName() == 'KisLayerBox'), None)
        # The layout where the layer name is located
        layout = layerDocker.findChild(QHBoxLayout,'hbox2')

        layout.insertWidget(0,self.comboBox)
        self.comboBox.activated.connect(lambda index: self.updateLayerColorLabel(index))

    def updateLayerColorLabel(self, index):
        selectedLayers = getSelectedLayers()
        if len(selectedLayers) == 0:
            currentLayer = getCurrentLayer()
            currentLayer.setColorLabel(index)
        else:
            for layer in selectedLayers:
                layer.setColorLabel(index)
    

    def buildComboBox(self)->QComboBox:
        comboBox = QComboBox()
        comboBox.setAccessibleName('colorLabelBox')
        comboBox.setObjectName('colorLabelBox')
        comboBox.setFixedSize(43,32)
        #todo make the combobox smaller

        # generates an array to automatize the process of creating icons 
        colors = [blueColor,greenColor,yellowColor,orangeColor,brownColor,redColor,purpleColor,greyColor]

        # I dont feel like figuring out how to make a transparent button like in the color labels
        # so i am going the csp route of just making an empty square
        transparentFill = QPixmap(20,20)
        transparentFill.fill(transparentColor)
        # draws a rectangle around the transparent area
        painter = QPainter(transparentFill)
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(0,0,20,20)
        painter.end()
        transparentIcon = QIcon(transparentFill)
        comboBox.addItem(transparentIcon,'')

        # generates all icons 
        for color in colors:
            colorFill = QPixmap(20,20)
            colorFill.fill(color)
            colorIcon = QIcon(colorFill)
            comboBox.addItem(colorIcon,'')
        return comboBox    

