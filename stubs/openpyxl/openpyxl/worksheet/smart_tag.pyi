from _typeshed import Incomplete
from typing import overload
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, Integer, String, _ConvertibleToBool, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable

class CellSmartTagPr(Serialisable):
    tagname: str
    key: String[Literal[False]]
    val: String[Literal[False]]
    def __init__(self, key: str, val: str) -> None: ...

class CellSmartTag(Serialisable):
    tagname: str
    cellSmartTagPr: Incomplete
    type: Integer[Literal[False]]
    deleted: Bool[Literal[True]]
    xmlBased: Bool[Literal[True]]
    __elements__: Incomplete
    @overload
    def __init__(
        self,
        cellSmartTagPr=(),
        *,
        type: _ConvertibleToInt,
        deleted: _ConvertibleToBool | None = False,
        xmlBased: _ConvertibleToBool | None = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cellSmartTagPr,
        type: _ConvertibleToInt,
        deleted: _ConvertibleToBool | None = False,
        xmlBased: _ConvertibleToBool | None = False,
    ) -> None: ...

class CellSmartTags(Serialisable):
    tagname: str
    cellSmartTag: Incomplete
    r: String[Literal[False]]
    __elements__: Incomplete
    def __init__(self, cellSmartTag, r: str) -> None: ...

class SmartTags(Serialisable):
    tagname: str
    cellSmartTags: Incomplete
    __elements__: Incomplete
    def __init__(self, cellSmartTags=()) -> None: ...
