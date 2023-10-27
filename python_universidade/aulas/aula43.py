import PySide6.QtCore

# Imprimindo versão do PySide6.
# print(PySide6.__version__)

# Imprimindo a versão do Qt usada para compilar o PySide6.
# print(PySide6.QtCore.qVersion)

import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red')
botao.show()

app.exec()