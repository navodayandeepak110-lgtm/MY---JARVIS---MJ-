from __future__ import annotations

import json
import math
import os
import platform
import random
import subprocess
import sys
import threading
import time
from pathlib import Path

import psutil

if platform.system() == "Windows":
    _WIN_HIDE: dict = {"creationflags": subprocess.CREATE_NO_WINDOW}
else:
    _WIN_HIDE: dict = {}

from PyQt6.QtCore import (
    QEasingCurve, QLineF, QMimeData, QObject, QParallelAnimationGroup, QPointF,
    QPropertyAnimation, QRect, QRectF, QSize, Qt, QTimer, QUrl, pyqtSignal,
)
from PyQt6.QtGui import (
    QBrush, QColor, QConicalGradient, QDragEnterEvent, QDropEvent, QFont,
    QFontDatabase, QKeySequence, QLinearGradient, QPainter, QPainterPath,
    QPen, QPixmap, QRadialGradient, QShortcut,
)
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy, QSplitter,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget, QProgressBar,
)
