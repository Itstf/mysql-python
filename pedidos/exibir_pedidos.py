import mysql.connector
import os
import time

def exibir_pedidos():
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='10.109.71.19',
        port=3306,
        database='thaiza_favarelli'
    )
    cursor = cnx.cursor()
    
    os.system('cls')
    time.sleep(1)
    
    print('Tabela Pedidos \n')
    cursor.execute("SELECT * FROM pedidos")
    print(cursor.fetchall())