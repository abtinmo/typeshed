from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import (
    Alias,
    Bool,
    Integer,
    MinMax,
    NoneSet,
    Set,
    String,
    Typed,
    _ConvertibleToBool,
    _ConvertibleToFloat,
    _ConvertibleToInt,
)
from openpyxl.descriptors.excel import Coordinate, ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.effect import Color, EffectContainer, EffectList
from openpyxl.drawing.fill import BlipFillProperties, GradientFillProperties, PatternFillProperties
from openpyxl.drawing.geometry import Scene3D
from openpyxl.drawing.line import LineProperties

_CharacterPropertiesU: TypeAlias = Literal[
    "words",
    "sng",
    "dbl",
    "heavy",
    "dotted",
    "dottedHeavy",
    "dash",
    "dashHeavy",
    "dashLong",
    "dashLongHeavy",
    "dotDash",
    "dotDashHeavy",
    "dotDotDash",
    "dotDotDashHeavy",
    "wavy",
    "wavyHeavy",
    "wavyDbl",
]
_CharacterPropertiesStrike: TypeAlias = Literal["noStrike", "sngStrike", "dblStrike"]
_CharacterPropertiesCap: TypeAlias = Literal["small", "all"]
_ParagraphPropertiesAlgn: TypeAlias = Literal["l", "ctr", "r", "just", "justLow", "dist", "thaiDist"]
_ParagraphPropertiesFontAlgn: TypeAlias = Literal["auto", "t", "ctr", "base", "b"]
_RichTextPropertiesVertOverflow: TypeAlias = Literal["overflow", "ellipsis", "clip"]
_RichTextPropertiesHorzOverflow: TypeAlias = Literal["overflow", "clip"]
_RichTextPropertiesVert: TypeAlias = Literal[
    "horz", "vert", "vert270", "wordArtVert", "eaVert", "mongolianVert", "wordArtVertRtl"
]
_RichTextPropertiesWrap: TypeAlias = Literal["none", "square"]
_RichTextPropertiesAnchor: TypeAlias = Literal["t", "ctr", "b", "just", "dist"]
_AutonumberBulletType: TypeAlias = Literal[
    "alphaLcParenBoth",
    "alphaUcParenBoth",
    "alphaLcParenR",
    "alphaUcParenR",
    "alphaLcPeriod",
    "alphaUcPeriod",
    "arabicParenBoth",
    "arabicParenR",
    "arabicPeriod",
    "arabicPlain",
    "romanLcParenBoth",
    "romanUcParenBoth",
    "romanLcParenR",
    "romanUcParenR",
    "romanLcPeriod",
    "romanUcPeriod",
    "circleNumDbPlain",
    "circleNumWdBlackPlain",
    "circleNumWdWhitePlain",
    "arabicDbPeriod",
    "arabicDbPlain",
    "ea1ChsPeriod",
    "ea1ChsPlain",
    "ea1ChtPeriod",
    "ea1ChtPlain",
    "ea1JpnChsDbPeriod",
    "ea1JpnKorPlain",
    "ea1JpnKorPeriod",
    "arabic1Minus",
    "arabic2Minus",
    "hebrew2Minus",
    "thaiAlphaPeriod",
    "thaiAlphaParenR",
    "thaiAlphaParenBoth",
    "thaiNumPeriod",
    "thaiNumParenR",
    "thaiNumParenBoth",
    "hindiAlphaPeriod",
    "hindiNumPeriod",
    "hindiNumParenR",
    "hindiAlpha1Period",
]
_TabStopAlgn: TypeAlias = Literal["l", "ctr", "r", "dec"]
_PresetTextShapePrst: TypeAlias = Literal[
    "textNoShape",
    "textPlain",
    "textStop",
    "textTriangle",
    "textTriangleInverted",
    "textChevron",
    "textChevronInverted",
    "textRingInside",
    "textRingOutside",
    "textArchUp",
    "textArchDown",
    "textCircle",
    "textButton",
    "textArchUpPour",
    "textArchDownPour",
    "textCirclePour",
    "textButtonPour",
    "textCurveUp",
    "textCurveDown",
    "textCanUp",
    "textCanDown",
    "textWave1",
    "textWave2",
    "textDoubleWave1",
    "textWave4",
    "textInflate",
    "textDeflate",
    "textInflateBottom",
    "textDeflateBottom",
    "textInflateTop",
    "textDeflateTop",
    "textDeflateInflate",
    "textDeflateInflateDeflate",
    "textFadeRight",
    "textFadeLeft",
    "textFadeUp",
    "textFadeDown",
    "textSlantUp",
    "textSlantDown",
    "textCascadeUp",
    "textCascadeDown",
]

class EmbeddedWAVAudioFile(Serialisable):
    name: String[Literal[True]]
    def __init__(self, name: str | None = None) -> None: ...

class Hyperlink(Serialisable):
    tagname: str
    namespace: Incomplete
    invalidUrl: String[Literal[True]]
    action: String[Literal[True]]
    tgtFrame: String[Literal[True]]
    tooltip: String[Literal[True]]
    history: Bool[Literal[True]]
    highlightClick: Bool[Literal[True]]
    endSnd: Bool[Literal[True]]
    snd: Typed[EmbeddedWAVAudioFile, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        invalidUrl: str | None = None,
        action: str | None = None,
        tgtFrame: str | None = None,
        tooltip: str | None = None,
        history: _ConvertibleToBool | None = None,
        highlightClick: _ConvertibleToBool | None = None,
        endSnd: _ConvertibleToBool | None = None,
        snd: EmbeddedWAVAudioFile | None = None,
        extLst: ExtensionList | None = None,
        id: Incomplete | None = None,
    ) -> None: ...

class Font(Serialisable):
    tagname: str
    namespace: Incomplete
    typeface: String[Literal[False]]
    panose: Incomplete
    pitchFamily: MinMax[float, Literal[True]]
    charset: Integer[Literal[True]]
    def __init__(
        self,
        typeface: str,
        panose: Incomplete | None = None,
        pitchFamily: _ConvertibleToFloat | None = None,
        charset: _ConvertibleToInt | None = None,
    ) -> None: ...

class CharacterProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    kumimoji: Bool[Literal[True]]
    lang: String[Literal[True]]
    altLang: String[Literal[True]]
    sz: MinMax[float, Literal[True]]
    b: Bool[Literal[True]]
    i: Bool[Literal[True]]
    u: NoneSet[_CharacterPropertiesU]
    strike: NoneSet[_CharacterPropertiesStrike]
    kern: Integer[Literal[True]]
    cap: NoneSet[_CharacterPropertiesCap]
    spc: Integer[Literal[True]]
    normalizeH: Bool[Literal[True]]
    baseline: Integer[Literal[True]]
    noProof: Bool[Literal[True]]
    dirty: Bool[Literal[True]]
    err: Bool[Literal[True]]
    smtClean: Bool[Literal[True]]
    smtId: Integer[Literal[True]]
    bmk: String[Literal[True]]
    ln: Typed[LineProperties, Literal[True]]
    highlight: Typed[Color, Literal[True]]
    latin: Typed[Font, Literal[True]]
    ea: Typed[Font, Literal[True]]
    cs: Typed[Font, Literal[True]]
    sym: Typed[Font, Literal[True]]
    hlinkClick: Typed[Hyperlink, Literal[True]]
    hlinkMouseOver: Typed[Hyperlink, Literal[True]]
    rtl: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Typed[GradientFillProperties, Literal[True]]
    blipFill: Typed[BlipFillProperties, Literal[True]]
    pattFill: Typed[PatternFillProperties, Literal[True]]
    grpFill: Incomplete
    effectLst: Typed[EffectList, Literal[True]]
    effectDag: Typed[EffectContainer, Literal[True]]
    uLnTx: Incomplete
    uLn: Typed[LineProperties, Literal[True]]
    uFillTx: Incomplete
    uFill: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        kumimoji: _ConvertibleToBool | None = None,
        lang: str | None = None,
        altLang: str | None = None,
        sz: _ConvertibleToFloat | None = None,
        b: _ConvertibleToBool | None = None,
        i: _ConvertibleToBool | None = None,
        u: _CharacterPropertiesU | Literal["none"] | None = None,
        strike: _CharacterPropertiesStrike | Literal["none"] | None = None,
        kern: _ConvertibleToInt | None = None,
        cap: _CharacterPropertiesCap | Literal["none"] | None = None,
        spc: _ConvertibleToInt | None = None,
        normalizeH: _ConvertibleToBool | None = None,
        baseline: _ConvertibleToInt | None = None,
        noProof: _ConvertibleToBool | None = None,
        dirty: _ConvertibleToBool | None = None,
        err: _ConvertibleToBool | None = None,
        smtClean: _ConvertibleToBool | None = None,
        smtId: _ConvertibleToInt | None = None,
        bmk: str | None = None,
        ln: LineProperties | None = None,
        highlight: Color | None = None,
        latin: Font | None = None,
        ea: Font | None = None,
        cs: Font | None = None,
        sym: Font | None = None,
        hlinkClick: Hyperlink | None = None,
        hlinkMouseOver: Hyperlink | None = None,
        rtl: Incomplete | None = None,
        extLst: ExtensionList | None = None,
        noFill: Incomplete | None = None,
        solidFill: Incomplete | None = None,
        gradFill: GradientFillProperties | None = None,
        blipFill: BlipFillProperties | None = None,
        pattFill: PatternFillProperties | None = None,
        grpFill: Incomplete | None = None,
        effectLst: EffectList | None = None,
        effectDag: EffectContainer | None = None,
        uLnTx: Incomplete | None = None,
        uLn: LineProperties | None = None,
        uFillTx: Incomplete | None = None,
        uFill: Incomplete | None = None,
    ) -> None: ...

class TabStop(Serialisable):
    pos: Typed[Coordinate[bool], Literal[True]]
    algn: Typed[Set[_TabStopAlgn], Literal[False]]
    def __init__(self, pos: Coordinate[bool] | None = None, algn: Set[_TabStopAlgn] | None = None) -> None: ...

class TabStopList(Serialisable):
    tab: Typed[TabStop, Literal[True]]
    def __init__(self, tab: Incomplete | None = None) -> None: ...

class Spacing(Serialisable):
    spcPct: Incomplete
    spcPts: Incomplete
    __elements__: Incomplete
    def __init__(self, spcPct: Incomplete | None = None, spcPts: Incomplete | None = None) -> None: ...

class AutonumberBullet(Serialisable):
    type: Set[_AutonumberBulletType]
    startAt: Integer[Literal[False]]
    def __init__(self, type: _AutonumberBulletType, startAt: _ConvertibleToInt) -> None: ...

class ParagraphProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    marL: Integer[Literal[True]]
    marR: Integer[Literal[True]]
    lvl: Integer[Literal[True]]
    indent: Integer[Literal[True]]
    algn: NoneSet[_ParagraphPropertiesAlgn]
    defTabSz: Integer[Literal[True]]
    rtl: Bool[Literal[True]]
    eaLnBrk: Bool[Literal[True]]
    fontAlgn: NoneSet[_ParagraphPropertiesFontAlgn]
    latinLnBrk: Bool[Literal[True]]
    hangingPunct: Bool[Literal[True]]
    lnSpc: Typed[Spacing, Literal[True]]
    spcBef: Typed[Spacing, Literal[True]]
    spcAft: Typed[Spacing, Literal[True]]
    tabLst: Typed[TabStopList, Literal[True]]
    defRPr: Typed[CharacterProperties, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    buClrTx: Incomplete
    buClr: Typed[Color, Literal[True]]
    buSzTx: Incomplete
    buSzPct: Incomplete
    buSzPts: Incomplete
    buFontTx: Incomplete
    buFont: Typed[Font, Literal[True]]
    buNone: Incomplete
    buAutoNum: Incomplete
    buChar: Incomplete
    buBlip: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        marL: _ConvertibleToInt | None = None,
        marR: _ConvertibleToInt | None = None,
        lvl: _ConvertibleToInt | None = None,
        indent: _ConvertibleToInt | None = None,
        algn: _ParagraphPropertiesAlgn | Literal["none"] | None = None,
        defTabSz: _ConvertibleToInt | None = None,
        rtl: _ConvertibleToBool | None = None,
        eaLnBrk: _ConvertibleToBool | None = None,
        fontAlgn: _ParagraphPropertiesFontAlgn | Literal["none"] | None = None,
        latinLnBrk: _ConvertibleToBool | None = None,
        hangingPunct: _ConvertibleToBool | None = None,
        lnSpc: Spacing | None = None,
        spcBef: Spacing | None = None,
        spcAft: Spacing | None = None,
        tabLst: TabStopList | None = None,
        defRPr: CharacterProperties | None = None,
        extLst: ExtensionList | None = None,
        buClrTx: Incomplete | None = None,
        buClr: Color | None = None,
        buSzTx: Incomplete | None = None,
        buSzPct: Incomplete | None = None,
        buSzPts: Incomplete | None = None,
        buFontTx: Incomplete | None = None,
        buFont: Font | None = None,
        buNone: Incomplete | None = None,
        buAutoNum: Incomplete | None = None,
        buChar: Incomplete | None = None,
        buBlip: Incomplete | None = None,
    ) -> None: ...

class ListStyle(Serialisable):
    tagname: str
    namespace: Incomplete
    defPPr: Typed[ParagraphProperties, Literal[True]]
    lvl1pPr: Typed[ParagraphProperties, Literal[True]]
    lvl2pPr: Typed[ParagraphProperties, Literal[True]]
    lvl3pPr: Typed[ParagraphProperties, Literal[True]]
    lvl4pPr: Typed[ParagraphProperties, Literal[True]]
    lvl5pPr: Typed[ParagraphProperties, Literal[True]]
    lvl6pPr: Typed[ParagraphProperties, Literal[True]]
    lvl7pPr: Typed[ParagraphProperties, Literal[True]]
    lvl8pPr: Typed[ParagraphProperties, Literal[True]]
    lvl9pPr: Typed[ParagraphProperties, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        defPPr: ParagraphProperties | None = None,
        lvl1pPr: ParagraphProperties | None = None,
        lvl2pPr: ParagraphProperties | None = None,
        lvl3pPr: ParagraphProperties | None = None,
        lvl4pPr: ParagraphProperties | None = None,
        lvl5pPr: ParagraphProperties | None = None,
        lvl6pPr: ParagraphProperties | None = None,
        lvl7pPr: ParagraphProperties | None = None,
        lvl8pPr: ParagraphProperties | None = None,
        lvl9pPr: ParagraphProperties | None = None,
        extLst: ParagraphProperties | None = None,
    ) -> None: ...

class RegularTextRun(Serialisable):
    tagname: str
    namespace: Incomplete
    rPr: Typed[CharacterProperties, Literal[True]]
    properties: Alias
    t: Incomplete
    value: Alias
    __elements__: Incomplete
    def __init__(self, rPr: CharacterProperties | None = None, t: str = "") -> None: ...

class LineBreak(Serialisable):
    tagname: str
    namespace: Incomplete
    rPr: Typed[CharacterProperties, Literal[True]]
    __elements__: Incomplete
    def __init__(self, rPr: CharacterProperties | None = None) -> None: ...

class TextField(Serialisable):
    id: String[Literal[False]]
    type: String[Literal[True]]
    rPr: Typed[CharacterProperties, Literal[True]]
    pPr: Typed[CharacterProperties, Literal[True]]
    t: String[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        id: str,
        type: str | None = None,
        rPr: CharacterProperties | None = None,
        pPr: CharacterProperties | None = None,
        t: str | None = None,
    ) -> None: ...

class Paragraph(Serialisable):
    tagname: str
    namespace: Incomplete
    pPr: Typed[ParagraphProperties, Literal[True]]
    properties: Alias
    endParaRPr: Typed[CharacterProperties, Literal[True]]
    r: Incomplete
    text: Alias
    br: Typed[LineBreak, Literal[True]]
    fld: Typed[TextField, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        pPr: ParagraphProperties | None = None,
        endParaRPr: CharacterProperties | None = None,
        r: Incomplete | None = None,
        br: LineBreak | None = None,
        fld: TextField | None = None,
    ) -> None: ...

class GeomGuide(Serialisable):
    name: String[Literal[False]]
    fmla: String[Literal[False]]
    def __init__(self, name: str, fmla: str) -> None: ...

class GeomGuideList(Serialisable):
    gd: Incomplete
    def __init__(self, gd: Incomplete | None = None) -> None: ...

class PresetTextShape(Serialisable):
    prst: Typed[Set[_PresetTextShapePrst], Literal[False]]
    avLst: Typed[GeomGuideList, Literal[True]]
    def __init__(self, prst: Set[_PresetTextShapePrst], avLst: GeomGuideList | None = None) -> None: ...

class TextNormalAutofit(Serialisable):
    fontScale: Integer[Literal[False]]
    lnSpcReduction: Integer[Literal[False]]
    def __init__(self, fontScale: _ConvertibleToInt, lnSpcReduction: _ConvertibleToInt) -> None: ...

class RichTextProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Integer[Literal[True]]
    spcFirstLastPara: Bool[Literal[True]]
    vertOverflow: NoneSet[_RichTextPropertiesVertOverflow]
    horzOverflow: NoneSet[_RichTextPropertiesHorzOverflow]
    vert: NoneSet[_RichTextPropertiesVert]
    wrap: NoneSet[_RichTextPropertiesWrap]
    lIns: Integer[Literal[True]]
    tIns: Integer[Literal[True]]
    rIns: Integer[Literal[True]]
    bIns: Integer[Literal[True]]
    numCol: Integer[Literal[True]]
    spcCol: Integer[Literal[True]]
    rtlCol: Bool[Literal[True]]
    fromWordArt: Bool[Literal[True]]
    anchor: NoneSet[_RichTextPropertiesAnchor]
    anchorCtr: Bool[Literal[True]]
    forceAA: Bool[Literal[True]]
    upright: Bool[Literal[True]]
    compatLnSpc: Bool[Literal[True]]
    prstTxWarp: Typed[PresetTextShape, Literal[True]]
    scene3d: Typed[Scene3D, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    noAutofit: Incomplete
    normAutofit: Incomplete
    spAutoFit: Incomplete
    flatTx: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rot: _ConvertibleToInt | None = None,
        spcFirstLastPara: _ConvertibleToBool | None = None,
        vertOverflow: _RichTextPropertiesVertOverflow | Literal["none"] | None = None,
        horzOverflow: _RichTextPropertiesHorzOverflow | Literal["none"] | None = None,
        vert: _RichTextPropertiesVert | Literal["none"] | None = None,
        wrap: _RichTextPropertiesWrap | Literal["none"] | None = None,
        lIns: _ConvertibleToInt | None = None,
        tIns: _ConvertibleToInt | None = None,
        rIns: _ConvertibleToInt | None = None,
        bIns: _ConvertibleToInt | None = None,
        numCol: _ConvertibleToInt | None = None,
        spcCol: _ConvertibleToInt | None = None,
        rtlCol: _ConvertibleToBool | None = None,
        fromWordArt: _ConvertibleToBool | None = None,
        anchor: _RichTextPropertiesAnchor | Literal["none"] | None = None,
        anchorCtr: _ConvertibleToBool | None = None,
        forceAA: _ConvertibleToBool | None = None,
        upright: _ConvertibleToBool | None = None,
        compatLnSpc: _ConvertibleToBool | None = None,
        prstTxWarp: Incomplete | None = None,
        scene3d: Incomplete | None = None,
        extLst: Incomplete | None = None,
        noAutofit: Incomplete | None = None,
        normAutofit: Incomplete | None = None,
        spAutoFit: Incomplete | None = None,
        flatTx: Incomplete | None = None,
    ) -> None: ...
