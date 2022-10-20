from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QSize
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My first app Qt Design")

        button = QPushButton("CLIQUE AQUI!")

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)

        button.clicked.connect(self.clicked_button)

    @staticmethod
    def clicked_button():
        print("Botão Clicado!")


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()
