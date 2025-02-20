import time
import os
#registro

print("==== Registro ====")
temarroba = False
email_registro = input("digite seu email: ")

for a in email_registro:
    if a == "@":
        temarroba=True

if temarroba == False:
    print("email invalido")

senha_registro = input("digite sua senha: ")
print("aguarde... ")
time.sleep(1)

#login

print("==== Login ====")
email_certo = False
senha_certa = False

email_login = input("digite seu email: ")
for e in email_login:
    if email_login == email_registro:
        email_certo = True
if email_certo == False:
    print("email incorreto")

senha_login = input("digite sua senha: ")
for i in senha_login:
    if senha_login == senha_registro:
        senha_certa = True
if senha_certa == False:
    print("senha incorreta")
