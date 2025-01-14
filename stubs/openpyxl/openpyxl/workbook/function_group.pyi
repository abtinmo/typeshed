from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Integer, String, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable

class FunctionGroup(Serialisable):
    tagname: str
    name: String[Literal[False]]
    def __init__(self, name: str) -> None: ...

class FunctionGroupList(Serialisable):
    tagname: str
    builtInGroupCount: Integer[Literal[True]]
    functionGroup: Incomplete
    __elements__: Incomplete
    def __init__(self, builtInGroupCount: _ConvertibleToInt | None = 16, functionGroup=()) -> None: ...
