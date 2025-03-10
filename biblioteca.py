
email_registro = []
senha_registro = []

def verifica_arrroba(email_registro):
    tem_arroba = False
    for a in email_registro:
        for i in a:
            if i == "@":
                tem_arroba = True

    return tem_arroba

def registro(email_registro, senha_registro):
    newemail = input("digite seu email: ")

    while verifica_arrroba(newemail) == False:
        newemail = input("digite um email valido: ")

    email_registro.append(newemail)
    senha_registro.append(input("digite a senha: "))
registro(email_registro, senha_registro)





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
