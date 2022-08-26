# Módulo de entrada de dados - parte da Calculadora
# Esta função orienta a entrada de dados pelo usuário
# Autor: Francisco Gomes
# Data: 26/08/2022
# Versão: 0.0.1

# Definição da função

def entra_dados():
    i = 0  # Contador zerado
    lista_numeros = [] # Cria uma lista vazia
    while i < 2: # Foi solicitado apenas 2 números
        numero = float(input("\nDigite um número: ."))
        lista_numeros.append(numero) # adiciona o número digitado à lista
        i+=1 # incrementa o contator
    return lista_numeros # Armazena a lista obtida para utilização posterior    
