import mysql.connector
# from conectar_bd import connect_bd

def editar_produtos():
    # conectar bd
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='10.109.71.19',
        port=3306,
        database='thaiza_favarelli'
    )
    cursor = cnx.cursor()

    
editar_produtos()
  