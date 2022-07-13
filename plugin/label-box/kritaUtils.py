"""
    Collection of utilities to make plugins in krita
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
    

def getCurrentLayer():
    app = Krita.instance()
    doc = app.activeDocument()
    currentLayer = doc.activeNode()
    return currentLayer


def getCurrentDoc():
    app = Krita.instance()
    doc = app.activeDocument()
    return doc


def getSelectedLayers():
    w = Krita.instance().activeWindow()
    v = w.activeView()
    selectedNodes = v.selectedNodes()
    return selectedNodes