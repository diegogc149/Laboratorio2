import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QLabel, QStackedWidget, QHBoxLayout,QLineEdit,QCheckBox,QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from Registro import PantallaRegistro
from Main import MainWindow
import os

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(570,150,300,400)
        self.setWindowTitle("Login")
        self.generar_form()

    def generar_form(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont("Times",12))
        user_label.move(20,54)

        password_label = QLabel(self)
        password_label.setText("Contraseña: ")
        password_label.setFont(QFont("Times",12))
        password_label.move(20,84)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(150,20)
        self.user_input.move(110,54)

        self.password_input = QLineEdit(self)
        self.password_input.resize(150,20)
        self.password_input.move(110,84)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.view_passw = QCheckBox(self)
        self.view_passw.setText("Ver contraseña")
        self.view_passw.setFont(QFont("Times",11))
        self.view_passw.move(20,109)
        self.view_passw.toggled.connect(self.mostrar_contra)

        loggin_button = QPushButton(self)
        loggin_button.setText("Login")
        loggin_button.setFont(QFont("Times",12))
        loggin_button.resize(125,30)
        loggin_button.move(20,150)
        loggin_button.clicked.connect(self.iniciar_sesion)

        register_button = QPushButton(self)
        register_button.setText("Register")
        register_button.setFont(QFont("Times",12))
        register_button.resize(125,30)
        register_button.move(155,150)
        register_button.clicked.connect(self.registrarse)

        boton_salir = QPushButton(self)
        boton_salir.setText("Salir")
        boton_salir.setFont(QFont("Times",12))
        boton_salir.resize(260,30)
        boton_salir.move(20,190)
        boton_salir.clicked.connect(self.salir)
         
    def mostrar_contra(self,clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def iniciar_sesion(self):
        usuarios = []
        try:
            dir = os.path.dirname(os.path.abspath(__file__))
            ruta_arch = os.path.join(dir,"Usuarios.txt")
            with open(ruta_arch,"r") as f:
                for linea in f:
                    usuarios.append(linea.strip())

            login_info = f"{self.user_input.text()},{self.password_input.text()}"  

            if login_info in usuarios:
                self.is_logged = True
                self.main = MainWindow()
                self.main.show()
                self.close()
  
            else:
                QMessageBox.warning(self,"Error al iniciar sesión","El usuario o la contraseña son incorrectas",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except FileNotFoundError:
            QMessageBox.warning(self,"Error","El archivo o ruta no se encontró",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        

    def registrarse(self):
        self.pantalla_registro = PantallaRegistro()
        self.pantalla_registro.show()
    
    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())
