from PyQt6.QtWidgets import (QLabel, 
QLineEdit, QCheckBox, QPushButton, QDialog, QWidget, QApplication, QMessageBox)
from PyQt6.QtGui import QFont
import os

class PantallaRegistro(QDialog):
    def __init__(self):
        super().__init__()
        self.generar_registro()
    
    def generar_registro(self):
        self.setGeometry(600,150,300,400)
        self.setWindowTitle("Registro")

        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont("Times",11))
        user_label.move(20,20)

        self.user_input = QLineEdit(self)
        self.user_input.resize(150,20)
        self.user_input.move(120,20)

        passw_label = QLabel(self)
        passw_label.setText("Contraseña:")
        passw_label.setFont(QFont("Times",11))
        passw_label.move(20,50)

        self.passw_input = QLineEdit(self)
        self.passw_input.resize(150,20)
        self.passw_input.move(120,50)
        self.passw_input.setEchoMode(QLineEdit.EchoMode.Password)

        conf_passw_label = QLabel(self)
        conf_passw_label.setText("Confirmar \ncontraseña: ")
        conf_passw_label.setFont(QFont("Times",11))
        conf_passw_label.move(20,80)

        self.conf_passw = QLineEdit(self)
        self.conf_passw.resize(150,20)
        self.conf_passw.move(120,90)
        self.conf_passw.setEchoMode(QLineEdit.EchoMode.Password)

        boton_crear_cuenta = QPushButton(self)
        boton_crear_cuenta.setText("Confirmar")
        boton_crear_cuenta.setFont(QFont("Times",12))
        boton_crear_cuenta.resize(125,30)
        boton_crear_cuenta.move(20,130)
        boton_crear_cuenta.clicked.connect(self.crear_cuenta)

        boton_cancelar = QPushButton(self)
        boton_cancelar.setText("Cancelar")
        boton_cancelar.setFont(QFont("Times",12))
        boton_cancelar.resize(125,30)
        boton_cancelar.move(155,130)
        boton_cancelar.clicked.connect(self.cancelar)    

    def crear_cuenta(self):
        try:
            dir = os.path.dirname(os.path.abspath(__file__))
            ruta_arch = os.path.join(dir,"Usuarios.txt")
            with open(ruta_arch,"a+") as archivo:
                usuario = self.user_input.text()
                contra1 = self.passw_input.text()
                contra2 = self.conf_passw.text()
                
                if  contra1 == "" or usuario == "" or contra2 =="":
                    QMessageBox.warning(self,"Error","Ingrese un usuario o contraseña válidos",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)
                elif contra1 != contra2:
                    QMessageBox.warning(self,"Error","Las contraseñas no coinciden",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)
                else:
                    archivo.write(f"{usuario},{contra1}\n")
                    QMessageBox.information(self,"Acción confirmada",
                                            "El usuario ha sido registrado correctamente",
                                            QMessageBox.StandardButton.Ok,
                                            QMessageBox.StandardButton.Ok)
                    self.close()
        except FileNotFoundError:
            QMessageBox.warning(self,"Error","No se encontró el archivo o el directorio",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)     
    
    def cancelar(self):
        self.close()