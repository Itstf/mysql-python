import mysql.connector

def connect_bd():
    # conectar bd
    cnx = mysql.connector.connect(
                    user='root', 
                    password='root',
                    host='10.109.71.19',
                    port=3306,
                    database='thaiza_favarelli'
                    )
    cursor = cnx.cursor()