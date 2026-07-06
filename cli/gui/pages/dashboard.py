"""Dashboard page — real-time telemetry + quick controls."""

from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QLabel, QComboBox, QProgressBar, QFrame,
    QVBoxLayout, QHBoxLayout,
)
from PyQt6.QtCore import Qt

from i18n import tr
from gui.widgets import create_row, create_scroll_page


def create_dashboard_page(gui):
    page, layout = create_scroll_page(tr("Dashboard"))

    lbl_model = QLabel(get_laptop_model())
    lbl_model.setObjectName("DeviceSubtitle")
    layout.addWidget(lbl_model)

    layout.addWidget(_build_monitor_card(gui))
    layout.addWidget(_build_quick_controls(gui))

    layout.addStretch()
    return page


def _build_monitor_card(gui):
    dash_group = QFrame()
    dash_group.setObjectName("DashboardCard")
    dash_layout = QHBoxLayout(dash_group)
    dash_layout.setContentsMargins(25, 25, 25, 25)
    dash_layout.setSpacing(40)

    dash_layout.addWidget(_build_cpu_monitor(gui))
    dash_layout.addWidget(_build_gpu_monitor(gui))
    return dash_group


def _build_cpu_monitor(gui):
    cpu_w = QWidget()
    cpu_l = QGridLayout(cpu_w)
    cpu_l.setContentsMargins(0, 0, 0, 0)
    cpu_l.setVerticalSpacing(18)

    cpu_title = QLabel(tr("CPU"))
    cpu_title.setObjectName("MonitorTitle")
    cpu_l.addWidget(cpu_title, 0, 0, 1, 3)

    _add_monitor_row(gui, cpu_l, 1, "pb_cpu", "lbl_cpu_util", tr("Utilization"), "0.0%", 100)
    _add_monitor_row(gui, cpu_l, 2, "pb_cput", "lbl_cpu_temp", tr("Temperature"), "0.0 °C", 100)
    _add_monitor_row(gui, cpu_l, 3, "pb_cpuf", "lbl_cpu_fan", tr("Fan"), "— RPM", 5000)

    return cpu_w


def _build_gpu_monitor(gui):
    gpu_w = QWidget()
    gpu_l = QGridLayout(gpu_w)
    gpu_l.setContentsMargins(0, 0, 0, 0)
    gpu_l.setVerticalSpacing(18)

    gpu_title = QLabel(tr("GPU"))
    gpu_title.setObjectName("MonitorTitle")
    gpu_l.addWidget(gpu_title, 0, 0, 1, 3)

    _add_monitor_row(gui, gpu_l, 1, "pb_gpu", "lbl_gpu_util", tr("Utilization"), "0.0%", 100)
    _add_monitor_row(gui, gpu_l, 2, "pb_gput", "lbl_gpu_temp", tr("Temperature"), "0.0 °C", 100)
    _add_monitor_row(gui, gpu_l, 3, "pb_gpuf", "lbl_gpu_fan", tr("Fan"), "— RPM", 5000)

    return gpu_w


def _add_monitor_row(gui, grid, row, pb_attr, lbl_attr, label_text, initial, max_val):
    lbl = QLabel(label_text)
    lbl.setObjectName("MonitorLabel")
    grid.addWidget(lbl, row, 0)

    pb = QProgressBar()
    pb.setFixedHeight(10)
    pb.setRange(0, max_val)
    setattr(gui, pb_attr, pb)
    grid.addWidget(pb, row, 1)

    val_lbl = QLabel(initial)
    val_lbl.setAlignment(
        Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
    )
    setattr(gui, lbl_attr, val_lbl)
    grid.addWidget(val_lbl, row, 2)


def _build_quick_controls(gui):
    container = QWidget()
    cl = QVBoxLayout(container)
    cl.setContentsMargins(0, 0, 0, 0)

    lbl_qc = QLabel(tr("Quick Controls"))
    lbl_qc.setObjectName("SectionTitle")
    cl.addWidget(lbl_qc)

    pm = QComboBox()
    pm.addItems(["Quiet", "Balance", "Performance"])
    gui.pm_combos.append(pm)
    pm.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['power_dash'] = create_row(
        tr("Power Mode"), tr("Power Mode subtitle"), pm
    )
    cl.addWidget(gui.rows['power_dash'])

    gm = QComboBox()
    gm.addItems(["Hybrid", "Integrated", "Dedicated"])
    gui.gpu_combos.append(gm)
    gm.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['gpu_dash'] = create_row(
        tr("GPU Working Mode"), tr("GPU Working Mode subtitle"), gm
    )
    cl.addWidget(gui.rows['gpu_dash'])

    fm = QComboBox()
    fm.addItems(["Standard", "Super Silent", "Dust Cleaning", "Performance"])
    gui.fan_combos.append(fm)
    fm.currentIndexChanged.connect(gui.auto_apply_change)
    gui.rows['fan_dash'] = create_row(
        tr("Active Cooling Policy"), tr("Active Cooling Policy subtitle"), fm
    )
    cl.addWidget(gui.rows['fan_dash'])

    return container


def get_laptop_model():
    import os
    try:
        with open("/sys/class/dmi/id/product_version") as f:
            val = f.read().strip()
            if val and val.lower() != "lenovo" and val != "None":
                return val
    except Exception:
        pass
    try:
        with open("/sys/class/dmi/id/product_name") as f:
            name = f.read().strip()
        try:
            with open("/sys/class/dmi/id/product_family") as f:
                family = f.read().strip()
            if family and family.lower() != "lenovo":
                return f"{family} ({name})"
        except Exception:
            pass
        return name
    except Exception:
        return tr("Device subtitle fallback")
