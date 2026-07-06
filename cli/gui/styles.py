"""QSS stylesheets and theme detection for Vantage GUI."""

import subprocess


DARK_STYLESHEET = """
QMainWindow, QWidget#MainWidget, QScrollArea, QStackedWidget, QWidget#ScrollContent {
    background-color: #121212;
    color: #ffffff;
    font-family: 'Inter', 'Noto Sans', 'Segoe UI', sans-serif;
    border: none;
}
QToolTip {
    background-color: #1e1e1e;
    color: #ffffff;
    border: 1px solid #333333;
    border-radius: 4px;
    padding: 6px;
    font-size: 12px;
}
QWidget#Sidebar {
    background-color: #181818;
    border-right: 1px solid #222222;
}
QPushButton.SidebarBtn {
    background-color: transparent;
    color: #9e9e9e;
    text-align: left;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: 600;
    border: none;
    border-radius: 6px;
    margin: 2px 10px;
}
QPushButton.SidebarBtn:hover:!checked {
    background-color: #242424;
    color: #ffffff;
}
QPushButton.SidebarBtn:checked {
    background-color: #0078d4;
    color: #ffffff;
    border-left: 3px solid #005a9e;
    border-top-left-radius: 0px;
    border-bottom-left-radius: 0px;
}
QFrame#SidebarDivider {
    background-color: #2a2a2a;
    max-height: 1px;
    margin: 6px 14px;
}
QFrame#DashboardCard {
    background-color: #1e1e1e;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
}
QFrame#SettingsRow {
    background-color: #1e1e1e;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    min-height: 64px;
}
QFrame#SettingsRow[rowDisabled="true"] {
    background-color: #181818;
    border: 1px solid #222222;
}
QFrame#SettingsRow QLabel#RowTitle {
    color: #ffffff;
    font-weight: 600;
    font-size: 14px;
    background: transparent;
}
QFrame#SettingsRow QLabel#RowSubtitle {
    color: #a0a0a0;
    font-size: 12px;
    background: transparent;
}
QFrame#SettingsRow[rowDisabled="true"] QLabel#RowTitle {
    color: #888888;
}
QFrame#SettingsRow[rowDisabled="true"] QLabel#RowSubtitle {
    color: #666666;
}
QLabel#TdpFieldLabel {
    color: #888888;
    font-size: 11px;
    font-weight: 600;
}
QFrame#SettingsRow[rowDisabled="true"] QLabel#TdpFieldLabel {
    color: #4a4a4a;
}
QLabel#BatStatTitle {
    font-size: 12px;
    color: #888888;
    font-weight: normal;
    background: transparent;
}
QLabel#BatStatValue {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    background: transparent;
}
QLabel#BatStatValue[statKey="health"] {
    color: #27ae60;
}
QLabel {
    color: #ffffff;
}
QLabel#MonitorTitle {
    font-weight: bold;
    font-size: 18px;
    color: #ffffff;
    margin-bottom: 6px;
}
QLabel#DeviceSubtitle {
    font-size: 14px;
    color: #888888;
    padding-bottom: 8px;
}
QLabel#MonitorLabel {
    color: #c0c0c0;
    font-size: 13px;
}
QLabel#SectionTitle {
    font-size: 16px;
    font-weight: bold;
    color: #ffffff;
    margin-top: 25px;
    margin-bottom: 8px;
}
QLabel#PageTitle {
    font-size: 26px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 10px;
}
QComboBox, QSpinBox {
    background-color: #0078d4;
    border: 1px solid #005a9e;
    border-radius: 6px;
    padding: 6px 12px;
    color: #ffffff;
    min-width: 130px;
    max-width: 200px;
    font-size: 13px;
    font-weight: 500;
    selection-background-color: #005a9e;
}
QSpinBox {
    max-width: 170px;
}
QComboBox:disabled, QSpinBox:disabled {
    background-color: #252525;
    color: #666666;
    border: 1px solid #333333;
}
QComboBox:hover:!disabled, QSpinBox:hover:!disabled {
    background-color: #106ebe;
    border: 1px solid #0078d4;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 28px;
    border-left: 1px solid rgba(255,255,255,0.15);
    border-radius: 0 6px 6px 0;
}
QComboBox::down-arrow {
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #ffffff;
    margin: 0 4px;
}
QComboBox::down-arrow:disabled {
    border-top: 6px solid #555555;
}
QPushButton#ApplyBtn {
    background-color: #0078d4;
    color: white;
    font-weight: 600;
    font-size: 13px;
    border-radius: 6px;
    padding: 8px 16px;
}
QPushButton#ApplyBtn:hover:!disabled {
    background-color: #106ebe;
}
QPushButton#ApplyBtn:disabled {
    background-color: #333333;
    color: #777777;
}
QProgressBar {
    background-color: #2a2a2a;
    border: none;
    border-radius: 4px;
    text-align: right;
    color: transparent;
}
QProgressBar::chunk {
    border-radius: 4px;
    background-color: #27ae60;
    min-width: 2px;
}
QProgressBar[zero="true"]::chunk {
    background-color: #2a2a2a;
}
QComboBox:disabled::drop-down {
    border-left: 1px solid #333333;
}
QComboBox QAbstractItemView {
    background-color: #1e1e1e;
    color: #ffffff;
    border: 1px solid #333333;
    border-radius: 4px;
    selection-background-color: #0078d4;
    selection-color: #ffffff;
    outline: none;
    padding: 2px;
}
QComboBox QAbstractItemView::item {
    min-height: 28px;
    padding: 4px 12px;
    background-color: transparent;
    color: #ffffff;
}
QComboBox QAbstractItemView::item:hover {
    background-color: #2a2a2a;
    color: #ffffff;
}
QComboBox QAbstractItemView::item:selected {
    background-color: #0078d4;
    color: #ffffff;
}
QScrollBar:vertical {
    border: none;
    background: #121212;
    width: 10px;
    margin: 0px 0px 0px 0px;
}
QScrollBar::handle:vertical {
    background: #333333;
    min-height: 20px;
    border-radius: 5px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QFrame#ChangesBar {
    background-color: #1a2a3a;
    border-bottom: 1px solid #0078d4;
}
QLabel#ChangesLabel {
    color: #64b5f6;
    font-size: 13px;
    font-weight: 600;
}
QPushButton#ApplyAllBtn {
    background-color: #0078d4;
    color: #ffffff;
    font-weight: 700;
    font-size: 13px;
    border-radius: 6px;
    padding: 7px 20px;
    border: none;
}
QPushButton#ApplyAllBtn:hover {
    background-color: #106ebe;
}
QPushButton#RevertBtn {
    background-color: transparent;
    color: #9e9e9e;
    font-size: 13px;
    border: 1px solid #333333;
    border-radius: 6px;
    padding: 7px 16px;
}
QPushButton#RevertBtn:hover {
    color: #ffffff;
    border-color: #555555;
    background-color: #242424;
}
QCheckBox {
    color: #c0c0c0;
    font-size: 13px;
    spacing: 8px;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 3px;
    border: 1px solid #555555;
    background-color: #1e1e1e;
}
QCheckBox::indicator:checked {
    background-color: #0078d4;
    border-color: #005a9e;
}
QCheckBox::indicator:unchecked:hover {
    border-color: #0078d4;
}
QPushButton#ThemeBtn {
    background-color: transparent;
    color: #9e9e9e;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #333333;
    border-radius: 6px;
    padding: 6px 14px;
}
QPushButton#ThemeBtn:hover {
    color: #ffffff;
    border-color: #0078d4;
    background-color: #242424;
}
"""

LIGHT_STYLESHEET = """
QMainWindow, QWidget#MainWidget, QScrollArea, QStackedWidget, QWidget#ScrollContent {
    background-color: #f5f5f5;
    color: #1a1a1a;
    font-family: 'Inter', 'Noto Sans', 'Segoe UI', sans-serif;
    border: none;
}
QToolTip {
    background-color: #ffffff;
    color: #1a1a1a;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 6px;
    font-size: 12px;
}
QWidget#Sidebar {
    background-color: #ececec;
    border-right: 1px solid #d0d0d0;
}
QPushButton.SidebarBtn {
    background-color: transparent;
    color: #555555;
    text-align: left;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: 600;
    border: none;
    border-radius: 6px;
    margin: 2px 10px;
}
QPushButton.SidebarBtn:hover:!checked {
    background-color: #dcdcdc;
    color: #1a1a1a;
}
QPushButton.SidebarBtn:checked {
    background-color: #0078d4;
    color: #ffffff;
    border-left: 3px solid #005a9e;
    border-top-left-radius: 0px;
    border-bottom-left-radius: 0px;
}
QFrame#SidebarDivider {
    background-color: #cccccc;
    max-height: 1px;
    margin: 6px 14px;
}
QFrame#DashboardCard {
    background-color: #ffffff;
    border: 1px solid #d0d0d0;
    border-radius: 8px;
}
QFrame#SettingsRow {
    background-color: #ffffff;
    border: 1px solid #d0d0d0;
    border-radius: 8px;
    min-height: 64px;
}
QFrame#SettingsRow[rowDisabled="true"] {
    background-color: #f0f0f0;
    border: 1px solid #d8d8d8;
}
QFrame#SettingsRow QLabel#RowTitle {
    color: #1a1a1a;
    font-weight: 600;
    font-size: 14px;
    background: transparent;
}
QFrame#SettingsRow QLabel#RowSubtitle {
    color: #666666;
    font-size: 12px;
    background: transparent;
}
QFrame#SettingsRow[rowDisabled="true"] QLabel#RowTitle {
    color: #777777;
}
QFrame#SettingsRow[rowDisabled="true"] QLabel#RowSubtitle {
    color: #999999;
}
QLabel#TdpFieldLabel {
    color: #666666;
    font-size: 11px;
    font-weight: 600;
}
QFrame#SettingsRow[rowDisabled="true"] QLabel#TdpFieldLabel {
    color: #bbbbbb;
}
QLabel#BatStatTitle {
    font-size: 12px;
    color: #666666;
    font-weight: normal;
    background: transparent;
}
QLabel#BatStatValue {
    font-size: 18px;
    font-weight: bold;
    color: #1a1a1a;
    background: transparent;
}
QLabel#BatStatValue[statKey="health"] {
    color: #27ae60;
}
QLabel {
    color: #1a1a1a;
}
QLabel#MonitorTitle {
    font-weight: bold;
    font-size: 18px;
    color: #1a1a1a;
    margin-bottom: 6px;
}
QLabel#DeviceSubtitle {
    font-size: 14px;
    color: #666666;
    padding-bottom: 8px;
}
QLabel#MonitorLabel {
    color: #444444;
    font-size: 13px;
}
QLabel#SectionTitle {
    font-size: 16px;
    font-weight: bold;
    color: #1a1a1a;
    margin-top: 25px;
    margin-bottom: 8px;
}
QLabel#PageTitle {
    font-size: 26px;
    font-weight: bold;
    color: #1a1a1a;
    margin-bottom: 10px;
}
QComboBox, QSpinBox {
    background-color: #0078d4;
    border: 1px solid #005a9e;
    border-radius: 6px;
    padding: 6px 12px;
    color: #ffffff;
    min-width: 130px;
    max-width: 200px;
    font-size: 13px;
    font-weight: 500;
    selection-background-color: #005a9e;
}
QSpinBox {
    max-width: 170px;
}
QComboBox:disabled, QSpinBox:disabled {
    background-color: #e0e0e0;
    color: #999999;
    border: 1px solid #cccccc;
}
QComboBox:hover:!disabled, QSpinBox:hover:!disabled {
    background-color: #106ebe;
    border: 1px solid #0078d4;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 28px;
    border-left: 1px solid rgba(255,255,255,0.15);
    border-radius: 0 6px 6px 0;
}
QComboBox::down-arrow {
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #ffffff;
    margin: 0 4px;
}
QComboBox::down-arrow:disabled {
    border-top: 6px solid #aaaaaa;
}
QPushButton#ApplyBtn {
    background-color: #0078d4;
    color: white;
    font-weight: 600;
    font-size: 13px;
    border-radius: 6px;
    padding: 8px 16px;
}
QPushButton#ApplyBtn:hover:!disabled {
    background-color: #106ebe;
}
QPushButton#ApplyBtn:disabled {
    background-color: #cccccc;
    color: #888888;
}
QProgressBar {
    background-color: #d0d0d0;
    border: none;
    border-radius: 4px;
    text-align: right;
    color: transparent;
}
QProgressBar::chunk {
    border-radius: 4px;
    background-color: #27ae60;
    min-width: 2px;
}
QProgressBar[zero="true"]::chunk {
    background-color: #d0d0d0;
}
QComboBox:disabled::drop-down {
    border-left: 1px solid #cccccc;
}
QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #1a1a1a;
    border: 1px solid #cccccc;
    border-radius: 4px;
    selection-background-color: #0078d4;
    selection-color: #ffffff;
    outline: none;
    padding: 2px;
}
QComboBox QAbstractItemView::item {
    min-height: 28px;
    padding: 4px 12px;
    background-color: transparent;
    color: #1a1a1a;
}
QComboBox QAbstractItemView::item:hover {
    background-color: #e8f0fa;
    color: #1a1a1a;
}
QComboBox QAbstractItemView::item:selected {
    background-color: #0078d4;
    color: #ffffff;
}
QScrollBar:vertical {
    border: none;
    background: #f5f5f5;
    width: 10px;
    margin: 0px 0px 0px 0px;
}
QScrollBar::handle:vertical {
    background: #cccccc;
    min-height: 20px;
    border-radius: 5px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QFrame#ChangesBar {
    background-color: #e0ecf5;
    border-bottom: 1px solid #0078d4;
}
QLabel#ChangesLabel {
    color: #005a9e;
    font-size: 13px;
    font-weight: 600;
}
QPushButton#ApplyAllBtn {
    background-color: #0078d4;
    color: #ffffff;
    font-weight: 700;
    font-size: 13px;
    border-radius: 6px;
    padding: 7px 20px;
    border: none;
}
QPushButton#ApplyAllBtn:hover {
    background-color: #106ebe;
}
QPushButton#RevertBtn {
    background-color: transparent;
    color: #555555;
    font-size: 13px;
    border: 1px solid #cccccc;
    border-radius: 6px;
    padding: 7px 16px;
}
QPushButton#RevertBtn:hover {
    color: #1a1a1a;
    border-color: #999999;
    background-color: #dcdcdc;
}
QCheckBox {
    color: #444444;
    font-size: 13px;
    spacing: 8px;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 3px;
    border: 1px solid #999999;
    background-color: #ffffff;
}
QCheckBox::indicator:checked {
    background-color: #0078d4;
    border-color: #005a9e;
}
QCheckBox::indicator:unchecked:hover {
    border-color: #0078d4;
}
QPushButton#ThemeBtn {
    background-color: transparent;
    color: #555555;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #cccccc;
    border-radius: 6px;
    padding: 6px 14px;
}
QPushButton#ThemeBtn:hover {
    color: #1a1a1a;
    border-color: #0078d4;
    background-color: #e8e8e8;
}
"""


def detect_system_theme() -> str:
    """Detect whether the desktop prefers a dark or light theme.

    Tries gsettings (GNOME/Zorin/Ubuntu) first, then falls back to Qt palette.
    Returns 'dark' or 'light'.
    """
    try:
        result = subprocess.run(
            ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
            capture_output=True, text=True, timeout=3
        )
        scheme = result.stdout.strip().lower()
        if "dark" in scheme:
            return "dark"
        if "light" in scheme or "default" in scheme:
            return "light"
    except Exception:
        pass

    try:
        from PyQt6.QtGui import QPalette
        from PyQt6.QtWidgets import QApplication
        app = QApplication.instance()
        if app:
            bg = app.palette().color(QPalette.ColorRole.Window)
            if bg.value() < 128:
                return "dark"
    except Exception:
        pass

    return "dark"
