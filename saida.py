"""
Módulo de saída
Reqisito: informar na tela o resultado da operação indicada pelo usuário
Autor: Francisco Gomes
Data: 26/08/2022
Versão: 0.0.1
"""

# Definição da função

def impressora(total, numero_1, numero_2):
    if operacao == "+":
        print(f"A soma de {numero_1} com {numero_2} é igual a {total}. ")
    elif operação == "-":
        print(f"A subtração de {numero_2} de {numero_1} é igual a {total}. ")
    elif operação == "*":
        print(f"O produto de {numero_1} com {numero_2} é igual a {total}. ")
    else:
        print(f"O quociente da divisão de {numero_1} por {numero_2} é igual a {total}. ")
