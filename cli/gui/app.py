"""Entry point for Vantage GUI."""

import sys
import os

_CLI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _CLI_DIR not in sys.path:
    sys.path.insert(0, _CLI_DIR)

from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QLockFile, QStandardPaths

from i18n import (
    tr, load_locale, save_locale, set_locale,
    load_theme, save_theme, is_first_run,
)
from gui.styles import detect_system_theme
from gui.service import VantageService
from gui.dialogs import LanguageDialog
from gui.main_window import VantageGUI


def main():
    os.environ.setdefault("QT_QPA_PLATFORM", "xcb")
    os.environ.setdefault("QT_AUTO_SCREEN_SCALE_FACTOR", "1")
    os.environ.setdefault("QT_ENABLE_HIGHDPI_SCALING", "1")

    app = QApplication(sys.argv)
    icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icon.png")
    if not os.path.exists(icon_path):
        icon_path = "/usr/lib/vantage/icon.png"
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    tmp_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.TempLocation)
    lock_path = os.path.join(tmp_dir, f"vantage-gui-{os.getuid()}.lock")
    lock = QLockFile(lock_path)
    lock.setStaleLockTime(0)
    if not lock.tryLock(100):
        sys.exit(0)

    if is_first_run():
        detected = detect_system_theme()
        save_theme(detected)
        dlg = LanguageDialog()
        if dlg.exec() == QDialog.DialogCode.Accepted and dlg.chosen():
            save_locale(dlg.chosen())
            set_locale(dlg.chosen())
        else:
            save_locale("en")
            set_locale("en")
    else:
        set_locale(load_locale())

    svc = VantageService()
    if svc.limited:
        QMessageBox.warning(None, tr("Service Error"), tr("Service Error"))

    gui = VantageGUI(svc)
    gui.show()
    sys.exit(app.exec())
