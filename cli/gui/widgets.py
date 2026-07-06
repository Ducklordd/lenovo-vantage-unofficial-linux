"""Reusable widget helpers for Vantage GUI pages."""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QScrollArea, QSizePolicy, QComboBox, QSpinBox, QCheckBox,
    QPushButton,
)
from PyQt6.QtGui import QCursor, QFontMetrics
from PyQt6.QtCore import Qt


def make_info_icon(tooltip_text):
    lbl = QLabel("ⓘ")
    lbl.setStyleSheet("color: #888888; font-size: 16px; font-weight: bold;")
    lbl.setToolTip(tooltip_text)
    lbl.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
    return lbl


def create_row(title, subtitle, widget, tooltip="", obj_name="SettingsRow"):
    row = QFrame()
    row.setObjectName(obj_name)
    h = QHBoxLayout(row)
    h.setContentsMargins(20, 15, 20, 15)

    text_v = QVBoxLayout()
    text_v.setSpacing(3)
    lbl_title = QLabel(title)
    lbl_title.setObjectName("RowTitle")
    text_v.addWidget(lbl_title)

    if subtitle:
        lbl_sub = QLabel(subtitle)
        lbl_sub.setObjectName("RowSubtitle")
        lbl_sub.setWordWrap(False)
        lbl_sub.setTextFormat(Qt.TextFormat.PlainText)
        lbl_sub.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        lbl_sub.setMinimumWidth(0)
        text_v.addWidget(lbl_sub)

    h.addLayout(text_v)
    h.addStretch()

    if tooltip:
        h.addWidget(make_info_icon(tooltip))
        h.addSpacing(10)
    if widget:
        h.addWidget(widget)

    return row


def set_row_state(row, enabled):
    """Disable only interactive widgets, not labels.

    Cascading Qt's disabled state to QLabel children overrides QSS color
    rules and makes enabled cards look dimmed. Instead we set a custom
    property and disable only the input widgets.
    """
    row.setProperty("rowDisabled", not enabled)
    for child in row.findChildren(QWidget):
        if isinstance(child, (QComboBox, QSpinBox, QCheckBox, QPushButton)):
            child.setEnabled(enabled)
    row.style().unpolish(row)
    row.style().polish(row)


def create_scroll_page(title):
    page = QWidget()
    layout = QVBoxLayout(page)
    layout.setContentsMargins(0, 0, 0, 0)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setFrameShape(QFrame.Shape.NoFrame)
    layout.addWidget(scroll)

    content = QWidget()
    content.setObjectName("ScrollContent")
    scroll.setWidget(content)

    clayout = QVBoxLayout(content)
    clayout.setContentsMargins(40, 30, 40, 40)
    clayout.setSpacing(15)

    lbl = QLabel(title)
    lbl.setObjectName("PageTitle")
    clayout.addWidget(lbl)

    return page, clayout
