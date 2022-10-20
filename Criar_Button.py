from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QSize
import sys

# Criando a Classe para instanciar button;
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My first app Qt Design")

        self.button = QPushButton("CLIQUE AQUI!")

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clicked_button)

    
    # Métodos do button: 1 click + troca de Titulo ao clicar;
    @staticmethod
    def clicked_button(self):
        print("Botão Clicado!")

        self.button.SetEnabled(False)
        self.setWindowTitle("first click")



app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()
