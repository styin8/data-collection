from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QListWidget, QPushButton, QLabel, QGroupBox
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import Qt
import os


class FileListView():
    def __init__(self, ShowViewIns) -> None:
        # variable
        self.file_path = []
        self.folder_path = ""
        self.ShowViewIns = ShowViewIns

        # Component
        self.list_widget = QListWidget()
        self.clear_button = QPushButton("Clear List")

        # Layout
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.file_groupbox = QGroupBox("File List")
        self.file_groupbox.setAlignment(Qt.AlignCenter)

        self.file_layout = QVBoxLayout()
        self.file_layout.addWidget(self.list_widget)
        self.file_layout.addWidget(self.clear_button)
        self.file_groupbox.setLayout(self.file_layout)

        self.layout.addWidget(self.file_groupbox)

        # Connect Function
        self.list_widget.itemClicked.connect(self.displayImage)
        self.clear_button.clicked.connect(self.clearList)

    def displayImage(self, item):

        file_path = os.path.join(self.folder_path, item.text())

        # 加载图片并显示在 QLabel 控件中
        pixmap = QPixmap(file_path)
        self.ShowViewIns.origin_image.setPixmap(pixmap)

    def clearList(self):
        self.list_widget.clear()
        # self.ShowViewIns.origin_image.setText("")
