#import mysql.connector

#banco = mysql.connector.connect(
   # host = "localhost",
  #  user = "root",
 #   password = "302302"
#    database = "livraria"
#)
while True:
    menu = input("Qual ação deseja realizar?\n(1- Inserir | 2- Ler | 3- Atualizar | 4- Deletar)\nAção escolhida: ")
    if menu == "1":
        tabela = input("\nEm qual tabela você deseja inserir dados? ")
        if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
            Nome_Livro = input("Informe o nome do livro: ")
            Genero = input("Informe o gênero do livro: ")
            Ano_Publicacao = input("Informe o ano de publicação do livro: ")
            Valor_Livro = input("Informe o valor do livro: ")
        #    inserir = f'INSERT INTO Livros VALUES ("{Nome_Livro}","{Genero}","{Ano_Publicacao}","{Valor_Livro}")'
       #     meucursor.execute(inserir)
      #      banco.commit()
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            Nome_Autor = input("Informe o nome do escritor(a): ")
            Nacionalidade_Autor = input("Informe a nacionalidade do escritor(a): ")
            Nascimento_Autor = input("Informe o ano de nascimento do escritor(a): ")
            Falecimento_Autor = input("Informe o ano de falecimento do escritor(a) (se houver): ")
     #       inserir = f'INSERT INTO Autores VALUES ("{Nome_Autor}","{Nacionalidade_Autor}","{Nascimento_Autor}","{Falecimento_Autor}")'
    #        meucursor.execute(inserir)
   #         banco.commit()
        elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
            Nome_Editora = input("Informe o nome da editora: ")
            Fundacao_Editora = input("Informe o ano de fundação da editora: ")
            Num_Selos = input("Informe o número de selos da editora: ")
  #          inserir = f'INSERT INTO Editoras VALUES ("{Nome_Editora}","{Fundacao_Editora}","{Num_Selos}")'
 #           meucursor.execute(inserir)
#            banco.commit()
        else:
            print("Opção inválida")        
    elif menu == "2":
        tabela = input("\nQual tabela você deseja visualizar? ")
        if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
            leitura = f'SELECT * FROM {tabela}'
        #    meucursor.execute(leitura)
       #     resultado = meucursor.fetchall()
      #      for x in resultado:
     #           print(x)
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            leitura = f'SELECT * FROM {tabela}'
  #          meucursor.execute(leitura)
 #           resultado = meucursor.fetchall()
#            for x in resultado:
    #            print(x)
        elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
            leitura = f'SELECT * FROM {tabela}'
    #        meucursor.execute(leitura)
   #         resultado = meucursor.fetchall()
   #         for x in resultado:
   #             print(x)
        elif tabela == "publicados" or tabela == "publicados".upper() or tabela == "publicados".capitalize():
            leitura = f'SELECT * FROM {tabela}'
 #           meucursor.execute(leitura)
#            resultado = meucursor.fetchall()
  #           for x in resultado:
  #             print(x)
        else:
            print("Opção inválida")
    elif menu == "3":
        tabela = input("\nQual tabela você deseja alterar? ")    
        if tabela == "livros" or tabela == "livros".upper() or tabela == "livros".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "nomeNOME":
                antigo_nome = input("Informe o antigo nome: ")
                novo_nome = input("Informe o novo nome: ")
              #  atualizar = f'UPDATE {tabela} SET Nome_Livro = "{novo_nome}" WHERE Nome_Livro = "{antigo_nome}"'
             #   meucursor.execute(atualizar)
            #    banco.commit()
            elif coluna in "generoGENERO":
                antigo_genero = input("Informe o antigo genero: ")
                novo_genero = input("Informe o novo genero: ")
           #     atualizar = f'UPDATE {tabela} SET Gênero = "{novo_genero}" WHERE Gênero = "{antigo_genero}"'
          #      meucursor.execute(atualizar)
         #       banco.commit()
            elif coluna in "anoANO":
                antigo_ano = input("Informe o antigo ano: ")
                novo_ano = input("Informe o novo ano: ")
        #        atualizar = f'UPDATE {tabela} SET Ano_Publicação = "{novo_ano}" WHERE Ano_Publicação = "{antigo_ano}"'
       #         meucursor.execute(atualizar)
      #          banco.commit()
            elif coluna in "valorVALOR":
                antigo_valor = input("Informe o antigo valor: ")
                novo_valor = input("Informe o novo valor: ")
     #           atualizar = f'UPDATE {tabela} SET Valor_Livro = "{novo_valor}" WHERE Valor_Livro = "{antigo_valor}"'
    #            meucursor.execute(atualizar)
   #             banco.commit()
            else:
                print("Opção inválida")
        elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "nomeNOME":
                antigo_nome = input("Informe o antigo nome: ")
                novo_nome = input("Informe o novo nome: ")
  #              atualizar = f'UPDATE {tabela} SET Nome_Autor = "{novo_nome}" WHERE Nome_Autor = "{antigo_nome}"'
 #               meucursor.execute(atualizar)
#                banco.commit()
            elif coluna in "nacionalidadeNACIONALIDADE":
                antigo_nacional = input("Informe a antiga nacionalidade: ")
                novo_nacional = input("Informe a nova nacionalidade: ")
              #  atualizar = f'UPDATE {tabela} SET Nacionalidade_Autor = "{novo_nacional}" WHERE Nacionalidade_Autor = "{antigo_nacional}"'
             #   meucursor.execute(atualizar)
            #    banco.commit()
            elif coluna in "anoANO":
                opcao = input("Informe qual ano será alterado\n(N- Nascimento |F- Falecimento)")
                if opcao == "f" or opcao == "F":
                    antigo_ano = input("Informe o antigo ano de falecimento: ")
                    novo_ano = input("Informe o novo ano de falecimento: ")
           #         atualizar = f'UPDATE {tabela} SET Falecimento_Autor = "{novo_ano}" WHERE Falecimento_Autor = "{antigo_ano}"'
          #          meucursor.execute(atualizar)
         #           banco.commit()
                elif opcao == "n" or opcao == "n":
                    antigo_ano = input("Informe o antigo ano de nascimento: ")
                    novo_ano = input("Informe o novo ano de Nascimento: ")
        #            atualizar = f'UPDATE {tabela} SET Nascimento_Autor = "{novo_ano}" WHERE Nascimento_Autor = "{antigo_ano}"'
       #             meucursor.execute(atualizar)
      #              banco.commit()
                else:
                    print("Opção inválida")
            else:
                print("Opção inválida")
        elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
            coluna = input("O que você deseja alterar? ")
            if coluna in "nomeNOME":
                antigo_nome = input("Informe o antigo nome: ")
                novo_nome = input("Informe o novo nome: ")
     #           atualizar = f'UPDATE {tabela} SET Nome_Editora = "{novo_nome}" WHERE Nome_Editora = "{antigo_nome}"'
    #            meucursor.execute(atualizar)
   #             banco.commit()
            elif coluna in "anoANO":
                antigo_ano = input("Informe o antigo ano: ")
                novo_ano = input("Informe o novo ano: ")
         #       atualizar = f'UPDATE {tabela} SET Fundação_Editora = "{novo_ano}" WHERE Fundação_Editora = "{antigo_ano}"'
        #        meucursor.execute(atualizar)
       #         banco.commit()
            elif coluna in "selosSELOS":
                antigo_selo = input("Informe o antigo número de selos: ")
                novo_selo = input("Informe o novo número de selos: ")
         #       atualizar = f'UPDATE {tabela} SET Num_Selos = "{novo_selo}" WHERE Num_Selos = "{antigo_selo}"'
        #        meucursor.execute(atualizar)
       #         banco.commit()
        #UPDATE da tabela publicados        
        #elif tabela == "publicados" or tabela == "publicados".upper() or tabela == "publicados".capitalize():
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
        #            deletar = f'DELETE FROM {tabela} WHERE Nome_Livro = "{Item_del}"'
       #             meucursor.execute(deletar)
      #              banco.commit()
                else:
                    print("Opção inválida")
            elif tabela == "autores" or tabela == "autores".upper() or tabela == "autores".capitalize():
                coluna = input("O que você deseja alterar? ")
                if coluna in "nomeNOME":
                    Item_del = input("Informe o que vai ser deletado: ")
     #               deletar = f'DELETE FROM {tabela} WHERE Nome_Autor = "{Item_del}"'
   #                 meucursor.execute(deletar)
  #                  banco.commit()
                else:
                    print("Opção inválida")
            elif tabela == "editoras" or tabela == "editoras".upper() or tabela == "editoras".capitalize():
                coluna = input("O que você deseja alterar? ")
                if coluna in "nomeNOME":
                    Item_del = input("Informe o que vai ser deletado: ")
    #                deletar = f'DELETE FROM {tabela} WHERE Nome_Editora = "{Item_del}"'
#                    meucursor.execute(deletar)
 #                   banco.commit()
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
