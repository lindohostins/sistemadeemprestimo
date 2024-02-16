import hashlib
import random

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = hashlib.sha256(senha.encode()).hexdigest()

class Jogo:
    def __init__(self, titulo, descricao, categoria):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.jogos = []

    def cadastrar_usuario(self, nome, email, senha):
        novo_usuario = Usuario(nome, email, senha)
        self.usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")

    def fazer_login(self, email, senha):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == hashlib.sha256(senha.encode()).hexdigest():
                return usuario
        return None

    def adicionar_jogo(self, titulo, descricao, categoria):
        novo_jogo = Jogo(titulo, descricao, categoria)
        self.jogos.append(novo_jogo)
        print("Jogo adicionado com sucesso!")

    def buscar_jogos_por_categoria(self, categoria):
        resultados = []
        for jogo in self.jogos:
            if jogo.categoria.lower() == categoria.lower():
                resultados.append(jogo)
        return resultados

# Função para exibir tela de registro de usuário
def tela_registro():
    print("----- Registro de Usuário -----")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    return nome, email, senha

# Função para exibir tela de login
def tela_login():
    print("----- Login -----")
    email = input("E-mail: ")
    senha = input("Senha: ")
    return email, senha

# Função para exibir tela de busca de jogos
def tela_busca_jogos():
    print("----- Busca de Jogos -----")
    categoria = input("Digite a categoria desejada (Corrida, Ação, Luta, RPG, Esportes): ")
    return categoria

# Inicialização do sistema
sistema = Sistema()

# Lista de jogos aleatórios
jogos_aleatorios = [
    {"titulo": "Need for Speed: Heat", "descricao": "Jogo de corrida de rua", "categoria": "Corrida"},
    {"titulo": "Grand Theft Auto V", "descricao": "Ação e aventura em mundo aberto", "categoria": "Ação"},
    {"titulo": "Street Fighter V", "descricao": "Jogo de luta", "categoria": "Luta"},
    {"titulo": "The Witcher 3: Wild Hunt", "descricao": "RPG de mundo aberto com história rica", "categoria": "RPG"},
    {"titulo": "FIFA 22", "descricao": "Simulador de futebol", "categoria": "Esportes"}
]

# Adicionando jogos aleatórios ao sistema
for jogo in jogos_aleatorios:
    sistema.adicionar_jogo(jogo["titulo"], jogo["descricao"], jogo["categoria"])

# Loop principal
while True:
    print("\n1. Registrar Usuário")
    print("2. Login")
    print("3. Buscar Jogos por Categoria")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome, email, senha = tela_registro()
        sistema.cadastrar_usuario(nome, email, senha)
    elif opcao == "2":
        email, senha = tela_login()
        usuario_logado = sistema.fazer_login(email, senha)
        if usuario_logado:
            print(f"Bem-vindo, {usuario_logado.nome}!")
        else:
            print("E-mail ou senha incorretos.")
    elif opcao == "3":
        if not sistema.usuarios:
            print("Você precisa fazer login primeiro.")
        else:
            categoria = tela_busca_jogos()
            resultados = sistema.buscar_jogos_por_categoria(categoria)
            if resultados:
                print("\nResultados da busca:")
                for jogo in resultados:
                    print(f"Título: {jogo.titulo}, Descrição: {jogo.descricao}")
            else:
                print("Nenhum jogo encontrado para esta categoria.")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
