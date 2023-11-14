import mysql.connector

banco = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '302302',
    database= 'academia'
)
meucursor = banco.cursor()

inicio = input("Deseja iniciar alguma ação? (s/n) -> ")
while inicio == "s" or inicio == "S":
    menu = input("Qual ação deseja realizar?\n(1- Inserir | 2- Ler | 3- Atualizar | 4- Deletar) -> ")
    while menu == "1" or menu == "2" or menu == "3" or menu == "4":
        #Create
        if menu == "1":
            nome_aluno = input("Informe o nome do aluno: ")
            cpf_aluno = input("Informe o CPF do aluno: ")
            telefone_aluno = input("Informe o telefone do aluno: ")
            endereço_aluno = input("Informe o endereço do aluno: ")
            comando = f'INSERT INTO alunos VALUES ("{nome_aluno}","{cpf_aluno}","{telefone_aluno}","{endereço_aluno}")'
            meucursor.execute(comando)
            banco.commit()
            menu = input("Qual ação deseja realizar?\n(1- Inserir | 2- Ler | 3- Atualizar | 4- Deletar | 5- Encerrar) -> ")
        #Read
        if menu == "2":
            comando = f'SELECT * FROM alunos'
            meucursor.execute(comando)
            resultado= meucursor.fetchall()
            print(resultado)
            menu = input("Qual ação deseja realizar?\n(1- Inserir | 2- Ler | 3- Atualizar | 4- Deletar | 5- Encerrar) -> ")
        #Update
        if menu == "3":
            colunaVN = input("Informe a coluna a ser alterada e o novo valor dela: ")
            condicao = input("Informe a condição para essa alteração: ")
            comando = f'UPDATE FROM alunos SET {colunaVN} WHERE {condicao}'
            meucursor.execute(comando)
            banco.commit()
        #Delete
        if menu == "4":
meucursor.close()
banco.close()
