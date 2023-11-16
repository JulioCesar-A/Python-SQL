import mysql.connector

banco = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '302302',
    database= 'academia'
)
meucursor = banco.cursor()

while True:
    menu = input("Qual ação deseja realizar?\n(1- Inserir | 2- Ler | 3- Atualizar | 4- Deletar)\nAção escolhida: ")
    if menu == "1":
        tabela = input("\nEm qual tabela você deseja inserir dados? ")
        if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
            Nome_Livro = input("Informe o nome do livro: ")
            Genero = input("Informe o gênero do livro: ")
            Ano_Publicacao = input("Informe o ano de publicação do livro: ")
            Valor_Livro = input("Informe o valor do livro: ")
            inserir = f'INSERT INTO Livros VALUES ("{Nome_Livro}","{Genero}","{Ano_Publicacao}","{Valor_Livro}")'
            meucursor.execute(inserir)
            banco.commit()
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            Nome_Autor = input("Informe o nome do escritor(a): ")
            Nacionalidade_Autor = input("Informe a nacionalidade do escritor(a): ")
            Nascimento_Autor = input("Informe o ano de nascimento do escritor(a): ")
            Falecimento_Autor = input("Informe o ano de falecimento do escritor(a) (se houver): ")
            inserir = f'INSERT INTO Autores VALUES ("{Nome_Autor}","{Nacionalidade_Autor}","{Nascimento_Autor}","{Falecimento_Autor}")'
            meucursor.execute(inserir)
            banco.commit()
        elif tabela == "editora" or tabela == "editora".upper() or tabela == "editora".capitalize():
            Nome_Editora = input("Informe o nome da editora: ")
            Fundacao_Editora = input("Informe o ano de fundação da editora: ")
            Num_Selos = input("Informe o número de selos da editora: ")
            
            
            
    elif menu == "2":


    elif menu == "2":


    elif menu == "2":
meucursor.close()
banco.close()
