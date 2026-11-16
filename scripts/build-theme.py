# -*- coding: utf-8 -*-
"""Build the Cedar & Sand Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "cedar-sand-theme"
SLUG = "cedar-sand"
DISPLAY = "Cedar & Sand Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/cedar-sand-theme"

UI = {
    "foreground": ("#2A3B31", "#E8E3D4"),
    "editor.foreground": ("#2A3B31", "#E8E3D4"),
    "terminal.foreground": ("#2A3B31", "#E8E3D4"),
    "input.foreground": ("#24342B", "#F0EBDD"),
    "dropdown.foreground": ("#24342B", "#F0EBDD"),
    "quickInput.foreground": ("#24342B", "#F0EBDD"),
    "editorWidget.foreground": ("#24342B", "#F0EBDD"),
    "editorHoverWidget.foreground": ("#24342B", "#F0EBDD"),
    "editorSuggestWidget.foreground": ("#24342B", "#F0EBDD"),
    "notifications.foreground": ("#24342B", "#F0EBDD"),
    "descriptionForeground": ("#7B8478", "#9AA695"),
    "input.placeholderForeground": ("#7B8478", "#9AA695"),
    "focusBorder": ("#1E3B2F", "#C0AC84"),
    "inputOption.activeBorder": ("#16291F", "#D9CBAE"),
    "input.border": ("#E2DAC8", "#34513F"),
    "dropdown.border": ("#E2DAC8", "#34513F"),
    "editor.background": ("#F1EFE2", "#1E3B2F"),
    "tab.activeBackground": ("#F1EFE2", "#1E3B2F"),
    "titleBar.activeBackground": ("#DDD8C1", "#16291F"),
    "titleBar.activeForeground": ("#2A3B31", "#E8E3D4"),
    "titleBar.inactiveBackground": ("#D9D4BC", "#14241B"),
    "titleBar.inactiveForeground": ("#8C9585", "#7E8C7A"),
    "activityBar.background": ("#DFDAC9", "#14241B"),
    "activityBar.foreground": ("#1E3B2F", "#B29D6B"),
    "activityBar.activeBorder": ("#B29D6B", "#B29D6B"),
    "activityBar.inactiveForeground": ("#8C9585", "#6E7D6A"),
    "sideBar.background": ("#E4DFCA", "#2A4C40"),
    "sideBar.foreground": ("#2A3B31", "#DCD7C6"),
    "sideBarSectionHeader.background": ("#DAD5BF", "#2E5146"),
    "sideBarSectionHeader.foreground": ("#3E5044", "#E4DFCE"),
    "panel.background": ("#E9E6D5", "#1A3329"),
    "terminal.background": ("#E9E6D5", "#1A3329"),
    "panel.border": ("#D9D4BF", "#2F4B3D"),
    "editorGroup.border": ("#D9D4BF", "#2F4B3D"),
    "tab.border": ("#D9D4BF", "#2F4B3D"),
    "sideBar.border": ("#D9D4BF", "#2F4B3D"),
    "titleBar.border": ("#D9D4BF", "#2F4B3D"),
    "statusBar.background": ("#1E3B2F", "#B29D6B"),
    "statusBar.noFolderBackground": ("#1E3B2F", "#B29D6B"),
    "statusBar.foreground": ("#F1EFE2", "#1E3B2F"),
    "statusBar.noFolderForeground": ("#F1EFE2", "#1E3B2F"),
    "statusBarItem.hoverBackground": ("#2C4B3D", "#C3B083"),
    "statusBar.debuggingBackground": ("#96702A", "#D9C08A"),
    "statusBar.debuggingForeground": ("#F1EFE2", "#1E3B2F"),
    "editorGroupHeader.tabsBackground": ("#DCD7C2", "#172C22"),
    "tab.inactiveBackground": ("#DCD7C2", "#172C22"),
    "tab.activeForeground": ("#2A3B31", "#F0EBDD"),
    "tab.activeBorderTop": ("#B29D6B", "#B29D6B"),
    "tab.inactiveForeground": ("#7B8478", "#84927F"),
    "tab.hoverBackground": ("#D8D3BD", "#2E5146"),
    "tab.activeModifiedBorder": ("#96702A", "#E0C070"),
    "tab.inactiveModifiedBorder": ("#96702A", "#E0C070"),
    "list.hoverBackground": ("#DFDBC8", "#2E5146"),
    "list.activeSelectionBackground": ("#D3CBB5", "#35594A"),
    "editorSuggestWidget.selectedBackground": ("#D3CBB5", "#35594A"),
    "list.activeSelectionForeground": ("#24342B", "#F2EDE0"),
    "list.inactiveSelectionForeground": ("#24342B", "#F2EDE0"),
    "editorSuggestWidget.selectedForeground": ("#24342B", "#F2EDE0"),
    "list.inactiveSelectionBackground": ("#DAD4BF", "#2F5244"),
    "list.highlightForeground": ("#1E3B2F", "#D9CBAE"),
    "list.focusHighlightForeground": ("#1E3B2F", "#D9CBAE"),
    "tree.indentGuidesStroke": ("#D5D0BA", "#2F4B3D"),
    "editorLineNumber.foreground": ("#A6AB9C", "#6E7D6A"),
    "editorLineNumber.activeForeground": ("#1E3B2F", "#B29D6B"),
    "editor.lineHighlightBackground": ("#E5E2D1", "#234437"),
    "editor.lineHighlightBorder": ("#D9D4BF", "#2B4C3E"),
    "editorCursor.foreground": ("#1E3B2F", "#B29D6B"),
    "selection.background": ("#D3CBB5", "#35594A"),
    "editor.selectionBackground": ("#D3CBB5", "#35594A"),
    "terminal.selectionBackground": ("#D3CBB5", "#35594A"),
    "editor.inactiveSelectionBackground": ("#DAD4BF", "#2F5244"),
    "editor.wordHighlightBackground": ("#D3CBB580", "#3D635399"),
    "editor.wordHighlightStrongBackground": ("#D3CBB580", "#3D635399"),
    "editor.selectionHighlightBackground": ("#D3CBB566", "#3D635388"),
    "editor.findMatchHighlightBackground": ("#DCD3B4", "#46604A"),
    "editor.findMatchBackground": ("#D0BE86", "#6B7A50"),
    "editor.findMatchBorder": ("#1E3B2F", "#D9C08A"),
    "editorBracketMatch.background": ("#E3E0CE", "#2E5146"),
    "editorBracketMatch.border": ("#1E3B2F", "#B29D6B"),
    "editorIndentGuide.background1": ("#D9D4BF", "#294437"),
    "editorIndentGuide.activeBackground1": ("#A6AB9C", "#4C6B58"),
    "editorWhitespace.foreground": ("#D9D4BF", "#294437"),
    "editorRuler.foreground": ("#E5E1CF", "#243F32"),
    "textLink.foreground": ("#1E3B2F", "#D9CBAE"),
    "textLink.activeForeground": ("#3E5A48", "#E8DCC0"),
    "editorLink.activeForeground": ("#3E5A48", "#E8DCC0"),
    "quickInput.background": ("#F6F5EB", "#233F33"),
    "editorHoverWidget.background": ("#F6F5EB", "#233F33"),
    "notifications.background": ("#F6F5EB", "#233F33"),
    "input.background": ("#F6F5EB", "#1E3B2F"),
    "dropdown.background": ("#F6F5EB", "#1E3B2F"),
    "editorWidget.background": ("#F6F5EB", "#233F33"),
    "editorSuggestWidget.background": ("#F6F5EB", "#233F33"),
    "editorWidget.border": ("#DFDCC9", "#385443"),
    "editorHoverWidget.border": ("#DFDCC9", "#385443"),
    "editorSuggestWidget.border": ("#DFDCC9", "#385443"),
    "notifications.border": ("#DFDCC9", "#385443"),
    "button.background": ("#B29D6B", "#B29D6B"),
    "button.foreground": ("#1E3B2F", "#16291F"),
    "button.hoverBackground": ("#A48F60", "#C3B083"),
    "button.secondaryBackground": ("#DAD5BF", "#2E5146"),
    "button.secondaryForeground": ("#2A3B31", "#E4DFCE"),
    "button.secondaryHoverBackground": ("#D3CBB5", "#35594A"),
    "badge.background": ("#1E3B2F", "#B29D6B"),
    "activityBarBadge.background": ("#1E3B2F", "#B29D6B"),
    "badge.foreground": ("#F1EFE2", "#1E3B2F"),
    "activityBarBadge.foreground": ("#F1EFE2", "#1E3B2F"),
    "scrollbarSlider.background": ("#A6AB9C66", "#5C7A6888"),
    "scrollbarSlider.hoverBackground": ("#8C958588", "#75968499"),
    "scrollbarSlider.activeBackground": ("#1E3B2F99", "#B29D6B99"),
    "errorForeground": ("#A8433F", "#F0928A"),
    "editorError.foreground": ("#A8433F", "#F0928A"),
    "problemsErrorIcon.foreground": ("#A8433F", "#F0928A"),
    "gitDecoration.deletedResourceForeground": ("#A8433F", "#F0928A"),
    "editorGutter.deletedBackground": ("#A8433F", "#F0928A"),
    "editorWarning.foreground": ("#96702A", "#E0C070"),
    "problemsWarningIcon.foreground": ("#96702A", "#E0C070"),
    "editorInfo.foreground": ("#3F6B84", "#9CC3DC"),
    "problemsInfoIcon.foreground": ("#3F6B84", "#9CC3DC"),
    "gitDecoration.addedResourceForeground": ("#4A7A52", "#8FC9A0"),
    "gitDecoration.untrackedResourceForeground": ("#4A7A52", "#8FC9A0"),
    "editorGutter.addedBackground": ("#4A7A52", "#8FC9A0"),
    "gitDecoration.modifiedResourceForeground": ("#96702A", "#E0C070"),
    "editorGutter.modifiedBackground": ("#96702A", "#E0C070"),
    "diffEditor.insertedTextBackground": ("#CFE4D5AA", "#2E4A3A66"),
    "diffEditor.removedTextBackground": ("#F0D6D4AA", "#5A2A2A66"),
    "diffEditor.insertedLineBackground": ("#CFE4D566", "#2E4A3A44"),
    "diffEditor.removedLineBackground": ("#F0D6D466", "#5A2A2A44"),
    "terminal.ansiBlack": ("#2A3B31", "#172C22"),
    "terminal.ansiRed": ("#A8433F", "#F0928A"),
    "terminal.ansiGreen": ("#4A7A52", "#8FC9A0"),
    "terminal.ansiYellow": ("#96702A", "#E0C070"),
    "terminal.ansiBlue": ("#3F6B84", "#9CC3DC"),
    "terminal.ansiMagenta": ("#7A5A6E", "#D4AEC4"),
    "terminal.ansiCyan": ("#3E6E64", "#8FD0C4"),
    "terminal.ansiWhite": ("#7B8478", "#D8D2C2"),
    "terminal.ansiBrightBlack": ("#5C6A55", "#5C6A55"),
    "terminal.ansiBrightRed": ("#C25B54", "#F5AEA6"),
    "terminal.ansiBrightGreen": ("#5E9A6E", "#A9DDB8"),
    "terminal.ansiBrightYellow": ("#BC8C2E", "#F2D89A"),
    "terminal.ansiBrightBlue": ("#5A86A0", "#B0D2E6"),
    "terminal.ansiBrightMagenta": ("#9A6A98", "#E4C6E2"),
    "terminal.ansiBrightCyan": ("#3E8E88", "#A8E0DC"),
    "terminal.ansiBrightWhite": ("#24342B", "#F2EDE0"),
}

TOKENS = [
    ("comment", ("#8C9585", "#8FA08A"), "italic"),
    (("keyword", "storage"), ("#8C4A32", "#E0A085"), None),
    ("string", ("#6B7A3A", "#C6D48E"), None),
    (("entity.name.function", "support.function"), ("#3F6B65", "#8FC9C0"), None),
    (("entity.name.type", "support.type", "support.class"), ("#6A5A3E", "#D3BE9A"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#96702A", "#E0C070"), None),
    ("variable", ("#2A3B31", "#E8E3D4"), None),
    ("variable.parameter", ("#5C6A55", "#B9C4AE"), None),
    (("variable.other.property", "support.variable.property"), ("#7A5A48", "#D3B49E"), None),
    ("keyword.operator", ("#7A8676", "#A8B4A2"), None),
    ("punctuation", ("#8C9585", "#8E9A88"), None),
    ("entity.name.tag", ("#8C4A32", "#E0A085"), None),
    ("entity.other.attribute-name", ("#96702A", "#E0C070"), None),
    ("string.regexp", ("#A65A32", "#E8A87C"), None),
    ("constant.character.escape", ("#96702A", "#E0C070"), None),
    ("markup.heading", ("#1E3B2F", "#F6F2E8"), "bold"),
    ("markup.bold", ("#1E3B2F", "#F6F2E8"), "bold"),
    ("markup.italic", ("#1E3B2F", "#F6F2E8"), "italic"),
    ("invalid", ("#A8433F", "#F0928A"), None),
]

SEMANTIC = {
    "variable": "#2A3B31|#E8E3D4",
    "parameter": "#5C6A55|#B9C4AE",
    "property": "#7A5A48|#D3B49E",
    "function": "#3F6B65|#8FC9C0",
    "method": "#3F6B65|#8FC9C0",
    "type": "#6A5A3E|#D3BE9A",
    "class": "#6A5A3E|#D3BE9A",
    "interface": "#6A5A3E|#D3BE9A",
    "variable.readonly": "#96702A|#E0C070",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "A cedar forest and warm sand: deep cedar green and sand gold on bone paper in the light variant, midnight cedar with a sand status bar in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "cedar", "sand", "forest", "green", "sand gold", "earthy"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#1E3B2F", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
