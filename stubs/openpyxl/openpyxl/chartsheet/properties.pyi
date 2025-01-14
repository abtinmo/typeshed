from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.styles.colors import Color

class ChartsheetProperties(Serialisable):
    tagname: str
    published: Bool[Literal[True]]
    codeName: String[Literal[True]]
    tabColor: Typed[Color, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, published: _ConvertibleToBool | None = None, codeName: str | None = None, tabColor: Color | None = None
    ) -> None: ...
