from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.chart.data_source import StrRef
from openpyxl.descriptors.base import Alias, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.text import ListStyle, RichTextProperties

class RichText(Serialisable):
    tagname: str
    bodyPr: Typed[RichTextProperties, Literal[False]]
    properties: Alias
    lstStyle: Typed[ListStyle, Literal[True]]
    p: Incomplete
    paragraphs: Alias
    __elements__: Incomplete
    def __init__(
        self, bodyPr: RichTextProperties | None = None, lstStyle: ListStyle | None = None, p: Incomplete | None = None
    ) -> None: ...

class Text(Serialisable):
    tagname: str
    strRef: Typed[StrRef, Literal[True]]
    rich: Typed[RichText, Literal[True]]
    __elements__: Incomplete
    def __init__(self, strRef: StrRef | None = None, rich: RichText | None = None) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
