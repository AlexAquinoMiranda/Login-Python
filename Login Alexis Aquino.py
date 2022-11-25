from PySide6.QtCore import *
#QLibraryInfo, QTranslator
from PySide6.QtWidgets import QApplication, QFormLayout,QTextEdit,QWidget,QVBoxLayout, QFileDialog, QMainWindow, QPushButton, QLabel, QLineEdit,QDialog
from PySide6.QtGui  import *
from PySide6.QtCore import *
import PySide6
import re 

class VentanaPrincipal(QMainWindow):
    textoUser = ""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica 2 ")
        self.setWindowIcon(QIcon("Login.png"))
        #ponemos tamaños fijos
        self.resize(270,400)
        self.setMaximumHeight(400)
        self.setMaximumWidth(270)

        self.elementos()
        self.miLayout()
        self.mostrarVentana()
    
        self.botonEnviar.clicked.connect(self.seHaClickado)

    def mostrarVentana(self):
         #creacion de widget 
        componentePrincipal  = QWidget()
        componentePrincipal.setLayout(self.layout_vertical)
        componentePrincipal.setStyleSheet("background-color: rgb(102, 178, 255);")
        self.setCentralWidget(componentePrincipal)
        
    def miLayout(self):
         #creamos layouts que son verticales
        self.layout_vertical = QVBoxLayout()
        #agg aqui el icono
        self.layout_vertical.addWidget(self.titulo)#login 
        self.layout_vertical.addWidget(self.title)#logo
        self.layout_vertical.setAlignment(self.title,PySide6.QtCore.Qt.AlignVCenter )
        self.layout_vertical.addWidget(self.User)#titulo de user
        self.layout_vertical.addWidget(self.textUser)#entrada de texto
        self.layout_vertical.addWidget(self.password)#titulon de pass
        self.layout_vertical.addWidget(self.textContra)#entrada de texto de pass
        self.layout_vertical.addWidget(self.botonEnviar)#boton enviar
       
    def elementos(self):
        #boton enviar
        self.botonEnviar = QPushButton("send")
        self.botonEnviar.setStyleSheet("background-color: rgb(10,128 , 255); color:white;")
        #textos del usuario y contraseña
        self.textContra = QLineEdit("")
        self.textUser= QLineEdit("")
        #color de fondo de los textos[blanco]
        self.textUser.setStyleSheet("background-color: rgb(255,255,255);")
        self.textContra.setStyleSheet("background-color: rgb(255,255,255);")
        #creacion de titulo 
        self.titulo = QLabel('<div align = "center"> <font size="8"> <b>Login session</b> </font> </div>')
        self.titulo.setStyleSheet(" border-radius:30px; color:white;")
        #creacion de subtitulo usuario
        self.User = QLabel('<div align = "center"> <font size="8"> <b>User </b></font> </div>')
        self.User.setStyleSheet("background-color: rgb(0,128 , 255); border-radius:20px; color:white;")
        #creación de subtitulo password
        self.password =  QLabel('<div align = "center"> <font size="8"><b> Password </b></font> </div>')
        self.password.setStyleSheet("background-color: rgb(10,128 , 255); border-radius:20px; color:white;")
        #creacion de icono en un qlabel
        self.title = QLabel() 
        self.title.setPixmap(QPixmap("login.png").scaled(250, 250))
        self.title.move(30,30)
        self.title.setAlignment(PySide6.QtCore.Qt.AlignVCenter)

    
    def checkEmail(self, email):  
        regex = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)) or email == 'admin':  
            dato="Mail entered is <b>Correct</b>" 
            self.informar(dato)   
        else:  
            dato="Mail entered is <b>Incorrect</b>" 
            self.informar(dato)
           
    def seHaClickado(self):
        self.textoUser = self.textContra.text()
        email =  self.textUser.text()
        if self.textoUser.__len__() > 0 and email.__len__() >0:
            self.checkEmail(email)
        else:
            dato="<b>¡Rellena todos los campos!</b>" 
            self.informar(dato)

    def informar(self, dato):
        self.d = QDialog()
        b1 = QLabel(str(dato),self.d)
        b1.move(70,30)
        self.d.setWindowTitle("Información")
        self.d.setStyleSheet("background-color: rgb(255, 255, 255);")
        self. d.setWindowModality(Qt.ApplicationModal)
        self.d.exec()

app = QApplication([])
ventana_principal = VentanaPrincipal()
ventana_principal.show()
app.exec()