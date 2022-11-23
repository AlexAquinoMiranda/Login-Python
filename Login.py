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

        #creamos layouts que son verticales
        layout_vertical = QVBoxLayout()
        

        #creamos botones y textos
        botonEnviar = QPushButton("send")
        botonEnviar.setStyleSheet("background-color: rgb(10,128 , 255); color:white;")
      
        #textos de entrada
        self.contra = QLineEdit("")
        self.usertext= QLineEdit("")
        #color de fondo de los textos[blanco]
        self.usertext.setStyleSheet("background-color: rgb(255,255,255);")
        self.contra.setStyleSheet("background-color: rgb(255,255,255);")

        #creacion de titulo 
        titulo = QLabel('<div align = "center"> <font size="8"> <b>Login session</b> </font> </div>')
        titulo.setStyleSheet(" border-radius:30px; color:white;")
        #creacion de subtitulo usuario
        User = QLabel('<div align = "center"> <font size="8"> <b>User </b></font> </div>')
        User.setStyleSheet("background-color: rgb(0,128 , 255); border-radius:20px; color:white;")
        
        #creación de subtitulo password
        password =  QLabel('<div align = "center"> <font size="8"><b> Password </b></font> </div>')
        password.setStyleSheet("background-color: rgb(10,128 , 255); border-radius:20px; color:white;")


        #creacion de icono en un qlabel
        title = QLabel() 
        title.setPixmap(QPixmap("login.png").scaled(250, 250))
        title.move(30,30)
        title.setAlignment(PySide6.QtCore.Qt.AlignVCenter)

    
        #agg aqui el icono
        layout_vertical.addWidget(titulo)#login 
        layout_vertical.addWidget(title)#logo
        layout_vertical.setAlignment(title,PySide6.QtCore.Qt.AlignVCenter )
        layout_vertical.addWidget(User)#titulo de user
        layout_vertical.addWidget(self.usertext)#entrada de texto
        layout_vertical.addWidget(password)#titulon de pass
        layout_vertical.addWidget(self.contra)#entrada de texto de pass
        layout_vertical.addWidget(botonEnviar)#boton enviar
        
        #evento del boton enviar
        botonEnviar.clicked.connect(self.seHaClickado)

        #creacion de widget 
        componentePrincipal  = QWidget()
        
        componentePrincipal.setLayout(layout_vertical)
        componentePrincipal.setStyleSheet("background-color: rgb(102, 178, 255);")
        self.setCentralWidget(componentePrincipal)

        #boton.clicked.connect(self.mostrar_dialogo)
       

    
    def checkEmail(self, email):  
        regex = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)) or email == 'admin':  
            dato="Mail entered is <b>Correct</b>" 
            self.informar(dato)   
        else:  
            dato="Mail entered is <b>Incorrect</b>" 
            self.informar(dato)
           
    def seHaClickado(self):
        self.textoUser = self.contra.text()
        email =  self.usertext.text()
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

def cargar_traductor(app):
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)


app = QApplication([])
ventana_principal = VentanaPrincipal()
ventana_principal.show()
app.exec()
