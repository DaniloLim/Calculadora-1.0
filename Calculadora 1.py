continuar= True 
def soma(a, b):
 return (a + b)
def subtração(a, b):
 return (a - b)
def multiplicação(a, b):
 return (a * b)
def divisão(a, b):
 return (a / b)
def exponenciação(a, b):
 return (a ** b)

while continuar:

 print("Selecione a operação que deseja realizar")
 print("Soma [1]")
 print("Subtração [2]")
 print("Multiplicação [3]")
 print("Divisão [4]")
 print("Exponenciação [5]")
 print("Sair [6]")

 escolha = float(input("Digite a sua operação:"))
 if escolha == 6:
    print("Saindo da calculadora...")
    continuar = False
    break
 num1 = float(input("Digite o primeiro número:"))
 num2 = float(input("Digite o segundo número:"))

 if escolha == 1:
    print(soma(num1, num2))
 elif escolha == 2:
    print(subtração(num1, num2))
 elif escolha == 3:
    print(multiplicação(num1, num2))
 elif escolha == 4: 
    print(divisão(num1, num2))
 elif escolha == 5:
    print(exponenciação(num1, num2))
 else:
    print("Você não escolheu um operação válida!")
 