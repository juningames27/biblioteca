class usuario:
    def __init__(self,nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def falar(self):
        print(f"olá, eu sou o {self.nome}")

email = input("")
nome = input("")
senha = input("")

user = usuario(nome, email, senha)

print(user.nome,user.email,user.senha)

user.falar()
