"""Equipe 13
Felipe Alberto de Lima da Silva"""

import pyrebase

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
status = auth.create_user_with_email_and_password(user, password)
print("Resultado: ", status)
