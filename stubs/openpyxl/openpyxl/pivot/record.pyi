from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

class Record(Serialisable):
    tagname: str
    m: Incomplete
    n: Incomplete
    b: Incomplete
    e: Incomplete
    s: Incomplete
    d: Incomplete
    x: Incomplete
    def __init__(
        self,
        _fields=(),
        m: Incomplete | None = None,
        n: Incomplete | None = None,
        b: Incomplete | None = None,
        e: Incomplete | None = None,
        s: Incomplete | None = None,
        d: Incomplete | None = None,
        x: Incomplete | None = None,
    ) -> None: ...

class RecordList(Serialisable):
    mime_type: str
    rel_type: str
    tagname: str
    r: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Unused = None, r=(), extLst: ExtensionList | None = None) -> None: ...
    @property
    def count(self): ...
    def to_tree(self): ...
    @property
    def path(self): ...
