from PySide2.QtWidgets import QLabel, QMainWindow, QApplication
from PySide2.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    # Criando a label;

        self.setWindowTitle("First Label") #Title;

        widget = QLabel("Label")
        font = widget.font()
        font.setPointSize(35)
        widget.setFont(font)

        widget.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        self.setCentralWidget(widget)    

        self.setFixedSize(QSize(400, 300))

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()
