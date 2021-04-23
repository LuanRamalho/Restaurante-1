#-*- coding:utf-8 -*-

class Restaurante:
    def Refeição():       
        print("Digite o preço da comida a ser pago: ")
        comida = float (input())
        print("Digite o preço da sobremesa a ser pago: ")
        sobremesa = float(input())
        print("Digite o preço da bebida a ser pago: ")
        bebida = float (input())
        
        preçototal = comida + sobremesa + bebida
        gorjeta = preçototal *0.10
        
        print("")
        print("")
        
        print("Valor total a ser pago: R$%.2f" % preçototal)
        print("Gorjeta do Garçom: R$%.2f" % gorjeta)

R = Restaurante
R.Refeição()
input()