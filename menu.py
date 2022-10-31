import time
import os

from pedidos.exibir_pedidos import exibir_pedidos

from produtos.editar_produtos import editar_produtos
from produtos.cadastrar_produtos import cadastrar_produtos
from produtos.excluir_produto import excluir_produto
from produtos.exibir_produtos import exibir_produtos

from conectar_bd import connect_bd


def menu():    
    os.system('cls') # limpar terminal
    
    connect_bd()
    
    home_menu = int(input(
        '\n[1] Menu Produtos'
        '\n[2] Menu Pedidos'
    ))
     
    if home_menu == 1:
        time.sleep(1)
        os.system('cls')
        escolha_produtos = int(input(
            '\n[1] Exibir Produtos Cadastrados'
            '\n[2] Cadastrar Produto'
            '\n[3] Editar Produto'
            '\n[4] Excluir Produto'
        ))
        if escolha_produtos == 1:
            time.sleep(1)
            os.system('cls')
            exibir_produtos()
            
        if escolha_produtos == 2:
            time.sleep(1)
            os.system('cls')
            cadastrar_produtos()
            
        if escolha_produtos == 3:
            time.sleep(1)
            os.system('cls')
            editar_produtos()
            
        if escolha_produtos == 4:
            time.sleep(1)
            os.system('cls')
            excluir_produto()
    
    if home_menu == 2:
        time.sleep(1)
        os.system('cls')
        escolha_pedidos = int(input(
            '\n[1] Pedidos Existentes'
            '\n[2] Criar pedido'
            '\n[3] Add produto ao pedido'
            '\n[4] Remover produto de um pedido'
        ))
        if escolha_pedidos == 1:
            exibir_pedidos()

menu()