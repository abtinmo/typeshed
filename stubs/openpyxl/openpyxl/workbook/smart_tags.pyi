from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, NoneSet, String, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

_SmartTagPropertiesShow: TypeAlias = Literal["all", "noIndicator"]

class SmartTag(Serialisable):
    tagname: str
    namespaceUri: String[Literal[True]]
    name: String[Literal[True]]
    url: String[Literal[True]]
    def __init__(self, namespaceUri: str | None = None, name: str | None = None, url: str | None = None) -> None: ...

class SmartTagList(Serialisable):
    tagname: str
    smartTagType: Incomplete
    __elements__: Incomplete
    def __init__(self, smartTagType=()) -> None: ...

class SmartTagProperties(Serialisable):
    tagname: str
    embed: Bool[Literal[True]]
    show: NoneSet[_SmartTagPropertiesShow]
    def __init__(
        self, embed: _ConvertibleToBool | None = None, show: _SmartTagPropertiesShow | Literal["none"] | None = None
    ) -> None: ...
