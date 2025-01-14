from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.cell_style import CellStyleList
from openpyxl.styles.colors import ColorList
from openpyxl.styles.named_styles import _NamedCellStyleList
from openpyxl.styles.numbers import NumberFormatList
from openpyxl.styles.table import TableStyleList

class Stylesheet(Serialisable):
    tagname: str
    numFmts: Typed[NumberFormatList, Literal[False]]
    fonts: Incomplete
    fills: Incomplete
    borders: Incomplete
    cellStyleXfs: Typed[CellStyleList, Literal[False]]
    cellXfs: Typed[CellStyleList, Literal[False]]
    cellStyles: Typed[_NamedCellStyleList, Literal[False]]
    dxfs: Incomplete
    tableStyles: Typed[TableStyleList, Literal[True]]
    colors: Typed[ColorList, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    number_formats: Incomplete
    cell_styles: Incomplete
    alignments: Incomplete
    protections: Incomplete
    named_styles: Incomplete
    def __init__(
        self,
        numFmts: NumberFormatList | None = None,
        fonts=(),
        fills=(),
        borders=(),
        cellStyleXfs: CellStyleList | None = None,
        cellXfs: CellStyleList | None = None,
        cellStyles: _NamedCellStyleList | None = None,
        dxfs=(),
        tableStyles: TableStyleList | None = None,
        colors: ColorList | None = None,
        extLst: Unused = None,
    ) -> None: ...
    @classmethod
    def from_tree(cls, node): ...
    @property
    def custom_formats(self): ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...

def apply_stylesheet(archive, wb): ...
def write_stylesheet(wb): ...
