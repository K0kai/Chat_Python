# 28/05/2024
# chat simples em python
# @Kokai
import os

mensagens = []
nome = input("Nome: ")

while True:
    # limpar terminal
    os.system('cls')

    #codigo
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])

    print("___________________")

    #obter texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adicionar mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })



