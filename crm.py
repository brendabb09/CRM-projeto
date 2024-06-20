import mysql.connector# Importa a função mysql.connector para conectar ao banco de dados MySQL

class Usuario:#criando a classe usuario
    def __init__(self, nome, telefone,email,senha):#inicializa os atributos da classe usuario usando os parametros nome,telefone,email,senha
        self.nome = nome # o atributo nome da instancia atribui o valor do parametro nome
        self.telefone = telefone# o atributo telefone da instancia atribui o valor do parametro telefone
        self.email =  email # o atributo email da instancia atribui o valor do parametro email
        self.senha = senha # o atributo senha da instancia atribui o valor do parametro senha
class Cliente:# criando classe cliente
    def __init__(self, nome, telefone,email):#inicializa os atributos da classe usuario usando os parametros nome,telefone,email)
        self.nome = nome# o atributo nome da instancia atribui o valor do parametro nome
        self.telefone = telefone# o atributo telefone da instancia atribui o valor do parametro telefone
        self.email = email# o atributo email da instancia atribui o valor do parametro email
class SistemaDeCRM:#criando a classe SistemaDeCRM
    def __init__(self):# O método __init__ inicializa a conexão com o banco de dados
        self.conexao = mysql.connector.connect(# conecta ao banco de dados mysql
            host="localhost",#endereco do servidor do banco de dados
            user="root",# Nome do usuário do banco de dados
            password="he182555@",# senha do usuário do banco de dados
            database="crm_db"# meu banco de dados
        )
        self.cursor = self.conexao.cursor()#executa o comando sql no banco de dados conectado

    def adicionar_usuario(self):#definir o metodo adicionar usuario
        nome = input("Digite o nome do usuário: ")#solicita o nome do usuario 
        telefone = input("Digite o telefone do usuário: ")#solicita o telefone do usuario 
        email = input('digite o email do usuario :')#solicita o email do usuario 
        senha = input('digite a senha do usuario :')#solicita o senha do usuario 
        usuario = Usuario(nome, telefone,email,senha)#cria uma estancia da classe usuario
        sql = "INSERT INTO usuario (nome, telefone,email, senha) VALUES (%s, %s, %s, %s )"#inserir na tabela usuarios nome,telefone,email,senha
        valores = (usuario.nome, usuario.telefone ,usuario.email,usuario.senha)#atribuir os espaços vazio
        self.cursor.execute(sql, valores)# executar os valores das variaveis (sql e valores)
        self.conexao.commit() #atualizar 
        print('Usuário adicionado com sucesso.')# mostrar na tela

    def adicionar_cliente(self):#definir o metodo adicionar cliente
        nome = input("Digite o nome do cliente: ")#solicita o nome do usuario 
        telefone = input("Digite o telefone do cliente: ")#solicita o telefone do usuario 
        email = input('digite o email do cliente: ') #solicita o email do usuario 
        cliente = Cliente(nome, telefone,email)#cria uma estancia da classe usuario
        sql = "INSERT INTO cliente (nome, telefone, email) VALUES (%s, %s ,%s)"#inserir na tabela usuarios nome,telefone,email,
        valores = (cliente.nome, cliente.telefone, cliente.email)#atribuir os espaços vazio
        self.cursor.execute(sql, valores)# executar os valores das variaveis (sql e valores)
        self.conexao.commit()#atualizar
        print('Cliente adicionado com sucesso.')#mostrar na tela

    def listar_usuarios(self):#definir o metodo listar usuario
        self.cursor.execute("SELECT nome, telefone,email, senha FROM usuario")#Executa o comando SQL para selecionar dados nome e telefone email senha da tabela usuario
        usuarios = self.cursor.fetchall()#recupera os registro 
        for usuario in usuarios:# para cada usuario em usuario imprimir o resultado da f string abaixo
            print(f"Nome: {usuario[0]}, Telefone: {usuario[1]}, email:{usuario[2]},senha:{usuario[3]}")

    def listar_clientes(self):#definir o metodo listar cliente
        self.cursor.execute("SELECT nome, telefone,email FROM cliente")#Executa o comando SQL para selecionar dados nome e telefone email da tabela cliente
        clientes = self.cursor.fetchall()#recuperar os registro 
        for cliente in clientes:## para cada cliente em cliente imprimir o resultado da f string abaixo
            print(f"Nome: {cliente[0]}, Telefone: {cliente[1]} email{cliente[2]}")#imprima na tela

    def fechar_conexao(self):#fecha
        self.cursor.close()#fecha cursor
        self.conexao.close()#fecha conexao

    def menu(self):#define o metodo menu 
        while True:# enquanto for verdadeiro o loop vai rodar 
            print("Menu:")
            print("1. Adicionar usuário")
            print("2. Adicionar cliente")
            print("3. Listar usuários")
            print("4. Listar clientes")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.adicionar_usuario()
            elif escolha == '2':
                self.adicionar_cliente()
            elif escolha == '3':
                self.listar_usuarios()
            elif escolha == '4':
                self.listar_clientes()
            elif escolha == '5':
                self.fechar_conexao()
                print("Conexão fechada. Saindo...")
                break# finaliza o loop
            else:# se opcao for falsa ele mostra na tela 
                print("Opção inválida. Tente novamente.")

# Instancia o sistema de CRM e exibe o menu
sistema = SistemaDeCRM()#cria uma intancia da classe sistemadecrm
sistema.menu()# Chama o método menu para exibir o menu e permitir a interação do usuário.
