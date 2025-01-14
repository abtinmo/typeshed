from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Alias, Bool, Integer, NoneSet, String, Typed, _ConvertibleToBool, _ConvertibleToInt
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.workbook.defined_name import DefinedNameList
from openpyxl.workbook.function_group import FunctionGroupList
from openpyxl.workbook.properties import CalcProperties, FileVersion, WorkbookProperties
from openpyxl.workbook.protection import FileSharing, WorkbookProtection
from openpyxl.workbook.smart_tags import SmartTagList, SmartTagProperties
from openpyxl.workbook.web import WebPublishing, WebPublishObjectList

_ChildSheetState: TypeAlias = Literal["visible", "hidden", "veryHidden"]
_WorkbookPackageConformance: TypeAlias = Literal["strict", "transitional"]

class FileRecoveryProperties(Serialisable):
    tagname: str
    autoRecover: Bool[Literal[True]]
    crashSave: Bool[Literal[True]]
    dataExtractLoad: Bool[Literal[True]]
    repairLoad: Bool[Literal[True]]
    def __init__(
        self,
        autoRecover: _ConvertibleToBool | None = None,
        crashSave: _ConvertibleToBool | None = None,
        dataExtractLoad: _ConvertibleToBool | None = None,
        repairLoad: _ConvertibleToBool | None = None,
    ) -> None: ...

class ChildSheet(Serialisable):
    tagname: str
    name: String[Literal[False]]
    sheetId: Integer[Literal[False]]
    state: NoneSet[_ChildSheetState]
    id: Incomplete
    def __init__(
        self,
        name: str,
        sheetId: _ConvertibleToInt,
        state: _ChildSheetState | Literal["none"] | None = "visible",
        id: Incomplete | None = None,
    ) -> None: ...

class PivotCache(Serialisable):
    tagname: str
    cacheId: Integer[Literal[False]]
    id: Incomplete
    def __init__(self, cacheId: _ConvertibleToInt, id: Incomplete | None = None) -> None: ...

class WorkbookPackage(Serialisable):
    tagname: str
    conformance: NoneSet[_WorkbookPackageConformance]
    fileVersion: Typed[FileVersion, Literal[True]]
    fileSharing: Typed[FileSharing, Literal[True]]
    workbookPr: Typed[WorkbookProperties, Literal[True]]
    properties: Alias
    workbookProtection: Typed[WorkbookProtection, Literal[True]]
    bookViews: Incomplete
    sheets: Incomplete
    functionGroups: Typed[FunctionGroupList, Literal[True]]
    externalReferences: Incomplete
    definedNames: Typed[DefinedNameList, Literal[True]]
    calcPr: Typed[CalcProperties, Literal[True]]
    oleSize: Incomplete
    customWorkbookViews: Incomplete
    pivotCaches: Incomplete
    smartTagPr: Typed[SmartTagProperties, Literal[True]]
    smartTagTypes: Typed[SmartTagList, Literal[True]]
    webPublishing: Typed[WebPublishing, Literal[True]]
    fileRecoveryPr: Typed[FileRecoveryProperties, Literal[True]]
    webPublishObjects: Typed[WebPublishObjectList, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    Ignorable: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        conformance: _WorkbookPackageConformance | Literal["none"] | None = None,
        fileVersion: FileVersion | None = None,
        fileSharing: FileSharing | None = None,
        workbookPr: WorkbookProperties | None = None,
        workbookProtection: WorkbookProtection | None = None,
        bookViews=(),
        sheets=(),
        functionGroups: FunctionGroupList | None = None,
        externalReferences=(),
        definedNames: DefinedNameList | None = None,
        calcPr: CalcProperties | None = None,
        oleSize: Incomplete | None = None,
        customWorkbookViews=(),
        pivotCaches=(),
        smartTagPr: SmartTagProperties | None = None,
        smartTagTypes: SmartTagList | None = None,
        webPublishing: WebPublishing | None = None,
        fileRecoveryPr: FileRecoveryProperties | None = None,
        webPublishObjects: WebPublishObjectList | None = None,
        extLst: Unused = None,
        Ignorable: Unused = None,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def active(self): ...
