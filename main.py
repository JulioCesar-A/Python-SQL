import mysql.connector

banco = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '302302',
    database= 'academia'
)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()

for x in resultado:
    print(x)

meucursor.close()
banco.close()