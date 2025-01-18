#Configurando el entorno 
import firebase_admin
from firebase_admin import credentials, db

#Conectar a firebase
cred = firebase_admin.credentials.Certificate(r"C:\Users\julia\OneDrive\Documentos\Unal 1 semestre\Programación\Batalla naval\Apuntes-de-clase\Firebase.py")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL':"https://bookstoreproject-8b4f0-default-rtdb.firebaseio.com/"
})

#Referencia al nodo en la base de datos
ref = db.reference("hola1") #Cambia nodo principal por el nombre que se le asigna
ref_2=db.reference("Prueba con 2do nodo") ##Probando agregar nuevo nodo

#Escribir datos en tiempo real
ref.set ({
    "mensaje1": "los amo",
    "activo": True
})
ref_2.set ({
    "Mensaje2": "¿Prueba exitosa?",
    "activo": True
})

#Escucha cambios en tiempo real
def escuchar_eventos(event):
    print(f"Cambio detectado: {event.data}")

ref.listen(escuchar_eventos)