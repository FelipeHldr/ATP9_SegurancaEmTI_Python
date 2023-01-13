"""Equipe 13
Felipe Alberto de Lima da Silva"""

import os
import stat
import pyrebase
from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyCk-egvupVb5ZQ7QWJhUCZlV9hZ5YmAtvo",
    "authDomain": "fir-pucpr-1838e.firebaseapp.com",
    "projectId": "fir-pucpr-1838e",
    "databaseURL": "https://" + "fir-pucpr-1838e" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-1838e.appspot.com",
    "messagingSenderId": "1062759128557",
    "appId": "1:1062759128557:web:3456c12cf1255d7559dbe4",
    "measurementId": "G-L4LHS03C3K"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
data = datetime.now()
datastr = data.strftime('%d/%m/%Y %H:%M')


status = auth.sign_in_with_email_and_password(user, password)
idToken = status["idToken"]

if os.path.isfile('acesso.txt'):
    os.chmod('acesso.txt', stat.S_IRWXU)

arquivo = open('acesso.txt', 'w')
arquivo.write('Usuário: ' + user + '\nData e hora do acesso: ' + datastr)
arquivo.close()

os.chmod('acesso.txt', stat.S_IRUSR)
