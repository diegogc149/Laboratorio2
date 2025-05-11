from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QCheckBox,
                             QPushButton, QMessageBox)
from PyQt6.QtGui import (QFont,QPixmap)
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()
    
    def iniciarUI(self):
        self.setGeometry(600,150,500,500)
        self.setWindowTitle("Bienvenido")
        self.generar_contenido()
    
    def generar_contenido(self):
        primera_l = QLabel(self)
        primera_l.setText("Bienvenido a la peor interfaz de usuario que verás hoy.\n" \
        "Como sabes, yo tengo acceso a la IP de todos los de la Lema\nque tienen internet, por lo tanto" \
        ", si no quieres ser doxeado \ny que tus datos estén publicos para el tren de Aragua\n" \
        "tendrás que depositar 1 000 000 000 de soles a mi yape, \navisado estás.")
        primera_l.setFont(QFont("Times",11))
        primera_l.move(20,20)

        try:
            dir = os.path.dirname(os.path.abspath(__file__))
            ruta_archivo = os.path.join(dir,"Imagen1.png")
            with open(ruta_archivo):
                imagen = QLabel(self)
                imagen.setPixmap(QPixmap(ruta_archivo))
                imagen.move(150,150)

        except FileNotFoundError:
            QMessageBox.warning(self,"Error",f"Error en copiar los archivos, no se encontró {ruta_archivo}",
                                QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self,"Error",f"Error identificado como: {e}",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            


