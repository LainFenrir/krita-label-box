# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *

from .labelBox import LabelBox

Krita.instance().addExtension(LabelBox(Krita.instance()))

