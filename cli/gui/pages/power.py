"""Power & System page — power mode, GPU, fan, TDP, Fn lock."""

from PyQt6.QtWidgets import (
    QWidget, QComboBox, QLabel, QFrame, QCheckBox, QSpinBox, QPushButton,
    QVBoxLayout, QHBoxLayout,
)
from PyQt6.QtCore import Qt

from i18n import tr
from gui.widgets import create_row, create_scroll_page, set_row_state


def create_power_page(gui):
    page, layout = create_scroll_page(tr("Power & System"))

    _build_power_section(gui, layout)
    _build_gpu_section(gui, layout)
    _build_fan_section(gui, layout)
    _build_tdp_section(gui, layout)
    _build_fn_lock_section(gui, layout)

    layout.addStretch()
    return page


def _build_power_section(gui, layout):
    lbl = QLabel(tr("Power"))
    lbl.setObjectName("SectionTitle")
    layout.addWidget(lbl)

    pm = QComboBox()
    pm.addItems(["Quiet", "Balance", "Performance"])
    gui.pm_combos.append(pm)
    pm.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['power_main'] = create_row(
        tr("Power Mode"), tr("Power Mode power subtitle"), pm
    )
    layout.addWidget(gui.rows['power_main'])

    usb = QComboBox()
    usb.addItems(["Off", "On"])
    gui.usb_combos.append(usb)
    usb.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['usb'] = create_row(
        tr("Always on USB"), tr("Always on USB subtitle"), usb
    )
    layout.addWidget(gui.rows['usb'])

    ib = QComboBox()
    ib.addItems(["Off", "On"])
    gui.ib_combos.append(ib)
    ib.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['ib'] = create_row(
        tr("Instant Boot"), tr("Instant Boot subtitle"), ib
    )
    layout.addWidget(gui.rows['ib'])

    fs = QComboBox()
    fs.addItems(["Off", "On"])
    gui.fs_combos.append(fs)
    fs.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['fs'] = create_row(
        tr("Flip To Start"), tr("Flip To Start subtitle"), fs
    )
    layout.addWidget(gui.rows['fs'])


def _build_gpu_section(gui, layout):
    lbl = QLabel(tr("GPU"))
    lbl.setObjectName("SectionTitle")
    layout.addWidget(lbl)

    gm = QComboBox()
    gm.addItems(["Hybrid", "Integrated", "Dedicated"])
    gui.gpu_combos.append(gm)
    gm.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['gpu_main'] = create_row(
        tr("GPU Working Mode"), tr("GPU Working Mode subtitle"), gm
    )
    layout.addWidget(gui.rows['gpu_main'])

    dt = QComboBox()
    dt.addItems(["Disabled"])
    dt_row = create_row(
        tr("Discrete GPU Toggle"), tr("Discrete GPU Toggle subtitle"), dt
    )
    set_row_state(dt_row, False)
    layout.addWidget(dt_row)

    oc = QComboBox()
    oc.addItems(["Disabled"])
    oc_row = create_row(
        tr("GPU Overclock"), tr("GPU Overclock subtitle"), oc
    )
    set_row_state(oc_row, False)
    layout.addWidget(oc_row)


def _build_fan_section(gui, layout):
    lbl = QLabel(tr("Thermal / Fan Control"))
    lbl.setObjectName("SectionTitle")
    layout.addWidget(lbl)

    fm = QComboBox()
    fm.addItems(["Standard", "Super Silent", "Dust Cleaning", "Performance"])
    gui.fan_combos.append(fm)
    fm.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['fan_main'] = create_row(
        tr("Active Cooling Policy"), tr("Active Cooling Policy subtitle"), fm
    )
    layout.addWidget(gui.rows['fan_main'])


def _build_tdp_section(gui, layout):
    tdp_row = QFrame()
    tdp_row.setObjectName("SettingsRow")
    gui.rows['tdp'] = tdp_row
    tdp_outer = QVBoxLayout(tdp_row)
    tdp_outer.setContentsMargins(20, 15, 20, 15)
    tdp_outer.setSpacing(10)

    tdp_header = QHBoxLayout()
    tdp_title_v = QVBoxLayout()
    tdp_title_v.setSpacing(2)
    lbl_tdp_title = QLabel(tr("Custom TDP (RyzenAdj)"))
    lbl_tdp_title.setObjectName("RowTitle")
    tdp_title_v.addWidget(lbl_tdp_title)
    lbl_tdp_sub = QLabel(tr("Custom TDP subtitle"))
    lbl_tdp_sub.setObjectName("RowSubtitle")
    tdp_title_v.addWidget(lbl_tdp_sub)
    tdp_header.addLayout(tdp_title_v)
    tdp_header.addStretch()

    gui.tdp_check = QCheckBox(tr("Enable Override"))
    gui.tdp_check.setChecked(False)
    gui.tdp_check.toggled.connect(gui._on_tdp_toggle)
    tdp_header.addWidget(gui.tdp_check)
    tdp_outer.addLayout(tdp_header)

    tdp_grid_w = QWidget()
    tdp_grid_w.setObjectName("TdpGrid")
    gui.tdp_grid_w = tdp_grid_w
    tdp_grid = QHBoxLayout(tdp_grid_w)
    tdp_grid.setContentsMargins(0, 0, 0, 0)
    tdp_grid.setSpacing(18)

    for label_text in ("STAPM", "Fast Limit", "Slow Limit"):
        tdp_grid.addLayout(_make_tdp_spin(gui, label_text))
    tdp_grid.addStretch()

    gui.btn_apply_tdp = QPushButton(tr("Apply TDP"))
    gui.btn_apply_tdp.setObjectName("ApplyBtn")
    gui.btn_apply_tdp.setEnabled(False)
    gui.btn_apply_tdp.clicked.connect(gui.apply_tdp)
    tdp_grid.addWidget(
        gui.btn_apply_tdp, alignment=Qt.AlignmentFlag.AlignBottom
    )

    tdp_outer.addWidget(tdp_grid_w)
    layout.addWidget(tdp_row)


def _make_tdp_spin(gui, label_text):
    col = QVBoxLayout()
    col.setSpacing(4)
    lbl = QLabel(label_text)
    lbl.setObjectName("TdpFieldLabel")
    spin = QSpinBox()
    spin.setRange(10000, 100000)
    spin.setSingleStep(1000)
    spin.setSuffix(" mW")
    spin.setFixedWidth(160)
    spin.setEnabled(False)
    spin.valueChanged.connect(gui._on_tdp_spin_change)
    gui.tdp_spins.append(spin)
    col.addWidget(lbl)
    col.addWidget(spin)
    return col


def _build_fn_lock_section(gui, layout):
    fn = QComboBox()
    fn.addItems(["Off", "On"])
    gui.fn_combos.append(fn)
    fn.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['fn'] = create_row(tr("Fn Lock"), tr("Fn Lock subtitle"), fn)
    layout.addWidget(gui.rows['fn'])
