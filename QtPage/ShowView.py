from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QListWidget, QPushButton, QLabel, QGroupBox
from PyQt5.QtCore import Qt


class ShowView():
    def __init__(self) -> None:

        # Component
        self.origin_image = QLabel()

        # Layout
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        # Prigin Image
        self.origin_groupbox = QGroupBox("Origin Image")
        self.origin_groupbox.setAlignment(Qt.AlignCenter)
        self.origin_layout = QHBoxLayout()
        self.origin_layout.addWidget(self.origin_image)
        self.origin_groupbox.setLayout(self.origin_layout)

        # Preview
        self.preview_groupbox = QGroupBox("Preview Image")
        self.preview_groupbox.setAlignment(Qt.AlignCenter)
        self.preview_layout = QHBoxLayout()
        self.preview_layout.addWidget(self.origin_image)
        self.preview_layout.addWidget(self.origin_image)
        self.preview_layout.addWidget(self.origin_image)
        self.preview_groupbox.setLayout(self.preview_layout)

        self.layout.addWidget(self.origin_groupbox,3)
        self.layout.addWidget(self.preview_groupbox,2)

