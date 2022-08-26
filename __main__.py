"""
Módulo principal
Requisitos: importar módulos de entrada, processamento e saída.
Autor: Francisco Gomes
Data: 26/08/2022
Versão: 0.0.1
"""

# Importação dos módulos

import entrada
import processa
import saida

# Definição das funções

def main ():
    lista = entrada.entra_dados () # Entrada

    resultado = processa.opera(total) # Processamento

    saida.impressora(total, numero_1, numero_2)

# Chamada main

if __name__++"__main__":
    main()
    
