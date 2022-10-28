import os
import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='root',
                              host='10.109.71.19',
                              port=3306,
                              database='thaiza_favarelli'
                            )
cursor = cnx.cursor()

os.system('cls')

print('Tabela Usuario')
cursor.execute("SELECT * FROM usuario")
print(cursor.fetchall())

print('\n')

print('Tabela Produtos')
cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())
