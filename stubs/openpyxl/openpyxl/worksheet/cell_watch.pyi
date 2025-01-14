from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import String
from openpyxl.descriptors.serialisable import Serialisable

class CellWatch(Serialisable):
    tagname: str
    r: String[Literal[True]]
    def __init__(self, r: str) -> None: ...

class CellWatches(Serialisable):
    tagname: str
    cellWatch: Incomplete
    __elements__: Incomplete
    def __init__(self, cellWatch=()) -> None: ...
