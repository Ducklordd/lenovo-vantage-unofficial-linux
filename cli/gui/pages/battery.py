"""Battery page — conservation mode + statistics."""

from PyQt6.QtWidgets import (
    QComboBox, QLabel, QFrame, QGridLayout, QVBoxLayout,
)

from i18n import tr
from gui.widgets import create_row, create_scroll_page


def create_battery_page(gui):
    page, layout = create_scroll_page(tr("Battery Details"))

    lbl_mode = QLabel(tr("Battery Mode"))
    lbl_mode.setObjectName("SectionTitle")
    layout.addWidget(lbl_mode)

    bat = QComboBox()
    bat.addItems(["Normal", "Conservation"])
    gui.bat_combos.append(bat)
    bat.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['battery'] = create_row(
        tr("Conservation Mode"), tr("Conservation Mode subtitle"), bat
    )
    layout.addWidget(gui.rows['battery'])

    lbl_stats = QLabel(tr("Statistics"))
    lbl_stats.setObjectName("SectionTitle")
    layout.addWidget(lbl_stats)

    grid = QGridLayout()
    grid.setVerticalSpacing(20)
    grid.setHorizontalSpacing(50)

    gui.bat_labels = {}
    fields = [
        (tr("Battery %"), "percent"),
        (tr("Charging state"), "status"),
        (tr("Current capacity"), "current"),
        (tr("Full capacity"), "full"),
        (tr("Design capacity"), "design"),
        (tr("Health %"), "health"),
        (tr("Cycle count"), "cycles"),
    ]

    for i, (label, key) in enumerate(fields):
        r, c = divmod(i, 2)
        lbl_title = QLabel(label)
        lbl_title.setObjectName("BatStatTitle")
        lbl_val = QLabel("N/A")
        lbl_val.setObjectName("BatStatValue")
        lbl_val.setProperty("statKey", key)

        v = QVBoxLayout()
        v.addWidget(lbl_title)
        v.addWidget(lbl_val)
        gui.bat_labels[key] = lbl_val
        grid.addLayout(v, r, c)

    frame = QFrame()
    frame.setObjectName("SettingsRow")
    blayout = QVBoxLayout(frame)
    blayout.setContentsMargins(40, 40, 40, 40)
    blayout.addLayout(grid)

    layout.addWidget(frame)
    layout.addStretch()
    return page
