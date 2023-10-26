from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QListWidget, QPushButton, QLabel, QGroupBox
from PyQt5.QtCore import Qt


class ActionView():
    def __init__(self) -> None:

        # Component
        button1 = QPushButton("按钮1")
        button2 = QPushButton("按钮2")
        button3 = QPushButton("按钮3")
        button4 = QPushButton("按钮4")
        button5 = QPushButton("按钮5")
        button6 = QPushButton("按钮6")
        button7 = QPushButton("按钮7")
        output = QListWidget()

        # Layout
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        # self.widget.setFixedSize(200,600)

        # Action
        self.action_groupbox = QGroupBox("Action")
        self.action_groupbox.setAlignment(Qt.AlignCenter)
        # self.action_groupbox.setFixedSize(200, 300)

        self.action_layout = QVBoxLayout()
        self.action_layout.addWidget(button1)
        self.action_layout.addWidget(button2)
        self.action_layout.addWidget(button3)
        self.action_layout.addWidget(button4)
        self.action_layout.addWidget(button5)
        self.action_layout.addWidget(button6)
        self.action_layout.addWidget(button7)
        self.action_groupbox.setLayout(self.action_layout)

        # Output
        self.output_groupbox = QGroupBox("Output")
        self.output_groupbox.setAlignment(Qt.AlignCenter)

        self.output_layout = QVBoxLayout()
        self.output_layout.addWidget(output)
        self.output_groupbox.setLayout(self.output_layout)

        # Add to Layout
        self.layout.addWidget(self.action_groupbox)
        self.layout.addWidget(self.output_groupbox)

