import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "livraria"
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
            inserir = f'INSERT INTO livros (Nome_Livro, Gênero, Ano_Publicação) VALUES ("{Nome_Livro}","{Genero}","{Ano_Publicacao}")'
            meucursor.execute(inserir)
            banco.commit()
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            Nome_Autor = input("Informe o nome do escritor(a): ")
            Nacionalidade_Autor = input("Informe a nacionalidade do escritor(a): ")
            Nascimento_Autor = input("Informe o ano de nascimento do escritor(a): ")
            Falecimento_Autor = input("Informe o ano de falecimento do escritor(a) (se houver): ")
            inserir = f'INSERT INTO Autores (Nome_Autor, Nacionalidade_Autor, Nascimento_Autor, Falecimento_Autor) VALUES ("{Nome_Autor}","{Nacionalidade_Autor}","{Nascimento_Autor}","{Falecimento_Autor}")'
            meucursor.execute(inserir)
            banco.commit()
        elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
            Nome_Editora = input("Informe o nome da editora: ")
            Fundacao_Editora = input("Informe o ano de fundação da editora: ")
            Num_Selos = input("Informe o número de selos da editora: ")
            inserir = f'INSERT INTO Editoras (Nome_Editora, Fundação_Editora, Num_Selos) VALUES ("{Nome_Editora}","{Fundacao_Editora}","{Num_Selos}")'
            meucursor.execute(inserir)
            banco.commit()
        elif tabela == "vendas" or tabela == "vendas".upper() or tabela == "vendas".capitalize():
            fk_Livro = input("Informe o id do Livro: ")
            fk_Autor = input("Informe o nome do autor(a): ")
            fk_Editora = input("Informe o nome da editora: ")
            Valor_Livro = input("Informe o valor do livro: ")
            inserir = f'INSERT INTO Vendas (fk_Livro, fk_Autor, fk_Editora, Valor_Livro)  VALUES ("{fk_Livro}","{fk_Autor}","{fk_Editora}","{Valor_Livro}")'
            meucursor.execute(inserir)
            banco.commit()
        else:
            print("Opção inválida")
    elif menu == "2":
        tabela = input("\nQual tabela você deseja visualizar? ")
        if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
            leitura = f'SELECT * FROM {tabela}'
            meucursor.execute(leitura)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            leitura = f'SELECT * FROM {tabela}'
            meucursor.execute(leitura)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
            leitura = f'SELECT * FROM {tabela}'
            meucursor.execute(leitura)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        elif tabela == "vendas" or tabela == "vendas".upper() or tabela == "vendas".capitalize():
            leitura = f'SELECT * FROM {tabela}'
            meucursor.execute(leitura)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        else:
            print("Opção inválida")
    elif menu == "3":
        tabela = input("\nQual tabela você deseja alterar? ")
        if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "nomeNOME":
                idLivro = input("Informe o id do livro: ")
                novo_nome = input("Informe o novo nome: ")
                atualizar = f'UPDATE {tabela} SET Nome_Livro = "{novo_nome}" WHERE idLivro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "generoGENERO":
                idLivro = input("Informe o id do livro: ")
                novo_genero = input("Informe o novo gênero: ")
                atualizar = f'UPDATE {tabela} SET Gênero = "{novo_genero}" WHERE idLivro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "anoANO":
                idLivro = input("Informe o id do livro: ")
                novo_ano = input("Informe o novo ano: ")
                atualizar = f'UPDATE {tabela} SET Ano_Publicação = "{novo_ano}" WHERE idLivro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            else:
                print("Opção inválida")
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "nomeNOME":
                Nome_Autor = input("Informe o nome do escritor(a): ")
                novo_nome = input("Informe o novo nome: ")
                atualizar = f'UPDATE {tabela} SET Nome_Autor = "{novo_nome}" WHERE Nome_Autor = "{Nome_Autor}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "nacionalidadeNACIONALIDADE":
                Nome_Autor = input("Informe o nome do escritor(a): ")
                novo_nacional = input("Informe a nova nacionalidade: ")
                atualizar = f'UPDATE {tabela} SET Nacionalidade_Autor = "{novo_nacional}" WHERE Nome_Autor = "{Nome_Autor}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "anoANO":
                opcao = input("Informe qual ano será alterado\n(N- Nascimento |F- Falecimento)")
                if opcao == "f" or opcao == "F":
                    Nome_Autor = input("Informe o nome do escritor(a): ")
                    novo_ano = input("Informe o novo ano de falecimento: ")
                    atualizar = f'UPDATE {tabela} SET Falecimento_Autor = "{novo_ano}" WHERE Nome_Autor = "{Nome_Autor}"'
                    meucursor.execute(atualizar)
                    banco.commit()
                elif opcao == "n" or opcao == "n":
                    Nome_Autor = input("Informe o nome do escritor(a): ")
                    novo_ano = input("Informe o novo ano de Nascimento: ")
                    atualizar = f'UPDATE {tabela} SET Nascimento_Autor = "{novo_ano}" WHERE Nome_Autor = "{Nome_Autor}"'
                    meucursor.execute(atualizar)
                    banco.commit()
                else:
                    print("Opção inválida")
            else:
                print("Opção inválida")
        elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "nomeNOME":
                Nome_Editora = input("Informe a editora: ")
                novo_nome = input("Informe o novo nome: ")
                atualizar = f'UPDATE {tabela} SET Nome_Editora = "{novo_nome}" WHERE Nome_Editora = "{Nome_Editora}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "anoANO":
                Nome_Editora = input("Informe a editora: ")
                novo_ano = input("Informe o novo ano: ")
                atualizar = f'UPDATE {tabela} SET Fundação_Editora = "{novo_ano}" WHERE Nome_Editora = "{Nome_Editora}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "selosSELOS":
                Nome_Editora = input("Informe a editora: ")
                novo_selo = input("Informe o novo número de selos: ")
                atualizar = f'UPDATE {tabela} SET Num_Selos = "{novo_selo}" WHERE Nome_Editora = "{Nome_Editora}"'
                meucursor.execute(atualizar)
                banco.commit()
            else:
                print("Opção inválida")
        elif tabela == "vendas" or tabela == "vendas".upper() or tabela == "vendas".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "valorVALOR":
                novo_valor = input("Informe o novo valor: ")
                idLivro = input("Informe o id do livro que terá seu valor alterado: ")
                atualizar = f'UPDATE {tabela} SET Valor_Livro = "{novo_valor}" WHERE fk_Livro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "livroLIVRO":
                novo_id = input("Informe o novo id: ")
                idLivro = input("Informe o id do livro que terá seu valor alterado: ")
                atualizar = f'UPDATE {tabela} SET fk_Livro = "{novo_id}" WHERE fk_Livro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "autorAUTOR":
                novo_nome = input("Informe o novo nome: ")
                idLivro = input("Informe o id do livro que terá seu valor alterado: ")
                atualizar = f'UPDATE {tabela} SET fk_Autor = "{novo_nome}" WHERE fk_Livro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            elif coluna in "editoraEDITORA":
                novo_nome = input("Informe o novo nome: ")
                idLivro = input("Informe o id do livro que terá seu valor alterado: ")
                atualizar = f'UPDATE {tabela} SET fk_Editora = "{novo_nome}" WHERE fk_Livro = "{idLivro}"'
                meucursor.execute(atualizar)
                banco.commit()
            else:
                print("Opção inválida")
        else:
            print("Opção inválida")
    elif menu == "4":
        print("\nEssa operação irá excluir dados de forma permanente.\n"
              "-------Pense bem antes de realizar essa operação------\n"
              "--------Obs: Nessa operação apenas é permitado--------\n"
              "-------------o uso do nome como referência------------")
        continuar = input("\nDeseja continuar? (S/N)\n-> ")
        if continuar in "sS":
            tabela = input("\nQual tabela você deseja alterar? ")
            if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
                coluna = input("O que você deseja alterar? ")
                if coluna in "nomeNOME":
                    Item_del = input("Informe o que vai ser deletado: ")
                    deletar = f'DELETE FROM {tabela} WHERE Nome_Livro = "{Item_del}"'
                    meucursor.execute(deletar)
                    banco.commit()
                else:
                    print("Opção inválida")
            elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
                coluna = input("O que você deseja alterar? ")
                if coluna in "nomeNOME":
                    Item_del = input("Informe o que vai ser deletado: ")
                    deletar = f'DELETE FROM {tabela} WHERE Nome_Autor = "{Item_del}"'
                    meucursor.execute(deletar)
                    banco.commit()
                else:
                    print("Opção inválida")
            elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
                coluna = input("O que você deseja alterar? ")
                if coluna in "nomeNOME":
                    Item_del = input("Informe o que vai ser deletado: ")
                    deletar = f'DELETE FROM {tabela} WHERE Nome_Editora = "{Item_del}"'
                    meucursor.execute(deletar)
                    banco.commit()
                else:
                    print("Opção inválida")
            else:
                print("Opção inválida")
    else:
        print("Opção inválida")
    decisao = input("Deseja realizar alguma outra operação? (S/N)\n-> ")
    while decisao not in "sSnN" or decisao == "":
        decisao = input("Opção inválida. Digite novamente (S/N)\n-> ")
    if decisao in "sS":
        continue
    else:
        print("Operação encerrada")
        break

meucursor.close()
banco.close()
