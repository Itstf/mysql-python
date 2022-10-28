import os
import bcrypt
import mysql.connector
from conectar_bd import connect_bd

def cadastro_usuario():
    connect_bd()
    
    # limpar terminal
    os.system('cls')
    
    id_usuario = str(input('id: '))
    print(id_usuario)
    
    nome_usuario = str(input('Usuario: '))
    print(nome_usuario)
    
    senha_usuario = str(input('Senha: '))
    print(senha_usuario)
    
    #criptografar senha
    bytes = senha_usuario.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    print(hash)

    inserir = (
        "INSERT INTO usuario(idusuario, usuario, senha)"
        "VALUES(%s, %s, %s)"
    )
    dados = (f'{id_usuario}', f'{nome_usuario}', f'{hash}')
    cursor.execute(inserir, dados)
    
    cnx.commit() # salvar 
    
    # limpar terminal
    os.system('cls')
    
    cursor.execute("SELECT * FROM usuario")
    print(cursor.fetchall())
    
cadastro_usuario()