"""
Módulo aritmético - processa as operações definidas pelo usuário com
os números informados.
Autor: Francisco Gomes
Data: 26/08/2022
Versão: 0.0.1
"""

# Informa a operação desejada

operacao = input("\Informe a operação desejada: +; -; * ou / . ")

                 

# Definição da função

def opera ():
    if operacao == "+":
        total = (lista_numeros[0] + lista_numeros[1])
    elif operação == "-":
        total = (lista_numeros[0] - lista_numeros[1])
    elif operação == "*":
        total = (lista_numeros[0] * lista_numeros[1])
    else:
        total = (lista_numeros[0] / lista_numeros[1])
return total        
        
