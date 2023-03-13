# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:06:43 2023

@author: fernando.cruz7
"""

while True:
    try:
        identificação = input("Digite identificação: ")
        endereco = input("Digite o endereço: ")
        cpf = input("Digite o CPF: ")
        renda_anual = float(input("Digite a Renda Anual: "))
        imposto_pago = float(input("Digite o Imposto Pago: "))
    except Exception:
        print("\n\nUm dos valores é inválido!\n\n")
        continue
    is_correct = input("As informações estão corretas? Digite \"sim\" para continuar: ").lower()
    if not is_correct in ("yes", "y", "sim", "s"):
        continue
    else:
        break
            
print("\n\n")
print(f"Identificação: {identificação}")
print(f"Endereço: {endereco}")
print(f"CPF: {cpf}")
print("Renda Anual: R$ " + "{:.2f}".format( renda_anual ))
print("Imposto Pago: R$ " + "{:.2f}".format( imposto_pago ))
if renda_anual > 44000.00:
    imposto = renda_anual * 0.15 - imposto_pago
    if imposto >= 0:
        print("Imposto a pagar: R$ " + "{:.2f}".format( imposto ))
    else:
        print("Restituição: R$" + "{:.2f}".format( imposto*-1 ))
