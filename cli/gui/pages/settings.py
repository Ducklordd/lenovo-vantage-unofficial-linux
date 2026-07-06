"""Settings page — language, theme, tray, autorun, boot logo."""

from PyQt6.QtWidgets import QComboBox, QLabel, QMessageBox, QCheckBox
from PyQt6.QtCore import Qt

from i18n import (
    tr, save_locale, set_locale, get_locale, save_theme, load_tray,
)
from gui.widgets import create_row, create_scroll_page, set_row_state


def create_settings_page(gui):
    page, layout = create_scroll_page(tr("Settings"))

    lbl_gen = QLabel(tr("General"))
    lbl_gen.setObjectName("SectionTitle")
    layout.addWidget(lbl_gen)

    # ── Language selector ───────────────────────────────────────────
    lang = QComboBox()
    lang.addItems([tr("System Default"), tr("English"), tr("Russian")])
    current_lang = get_locale()
    if current_lang == "ru":
        lang.setCurrentIndex(2)
    elif current_lang == "en":
        lang.setCurrentIndex(1)
    else:
        lang.setCurrentIndex(0)
    lang.currentIndexChanged.connect(lambda idx: _on_language_changed(gui, idx))
    lang_row = create_row(tr("Language"), tr("Language subtitle"), lang)
    layout.addWidget(lang_row)

    # ── Theme selector ──────────────────────────────────────────────
    theme = QComboBox()
    theme.addItems([tr("Dark Theme"), tr("Light Theme"), tr("System Default")])
    if gui.current_theme == "light":
        theme.setCurrentIndex(1)
    else:
        theme.setCurrentIndex(0)
    theme.currentIndexChanged.connect(lambda idx: _on_theme_changed(gui, idx))
    theme_row = create_row(tr("Theme"), tr("Theme subtitle"), theme)
    layout.addWidget(theme_row)

    lbl_beh = QLabel(tr("Behavior"))
    lbl_beh.setObjectName("SectionTitle")
    layout.addWidget(lbl_beh)

    # ── System Tray toggle ─────────────────────────────────────────
    tray_check = QCheckBox()
    tray_check.setChecked(load_tray())
    if not gui.tray_available:
        tray_check.setEnabled(False)
        tray_check.setChecked(False)
    tray_check.toggled.connect(
        lambda checked: gui.set_tray_enabled(checked)
    )
    tray_row = create_row(
        tr("System Tray"), tr("System Tray subtitle"), tray_check
    )
    if not gui.tray_available:
        set_row_state(tray_row, False)
    layout.addWidget(tray_row)

    autorun = QComboBox()
    autorun.addItems(["Off"])
    autorun.setEnabled(False)
    autorun_row = create_row(tr("Autorun"), tr("Autorun subtitle"), autorun)
    set_row_state(autorun_row, False)
    layout.addWidget(autorun_row)

    bl = QComboBox()
    bl.addItems(["Disabled"])
    bl.setEnabled(False)
    bl_row = create_row(
        tr("Boot Logo"), tr("Boot Logo subtitle"), bl
    )
    set_row_state(bl_row, False)
    layout.addWidget(bl_row)

    layout.addStretch()
    return page


def _on_language_changed(gui, index):
    if index == 1:
        save_locale("en")
        set_locale("en")
    elif index == 2:
        save_locale("ru")
        set_locale("ru")
    else:
        save_locale("en")
        set_locale("en")
    QMessageBox.information(gui, tr("Language"), tr("Language subtitle"))
    import sys, subprocess
    subprocess.Popen([sys.executable] + sys.argv)
    gui.close()


def _on_theme_changed(gui, index):
    if index == 1:
        gui.current_theme = "light"
    else:
        gui.current_theme = "dark"
    gui._apply_theme(gui.current_theme)
    save_theme(gui.current_theme)
