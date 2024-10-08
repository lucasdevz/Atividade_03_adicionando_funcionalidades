
import os

# Entrada

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    return peso / (altura** 2)

def exibir (imc):
    if imc > 18.5:
        print("Você está abaixo do peso.")
    elif imc >= 18.5 and imc <=24.9:
        print("Peso ideal")
    elif imc >= 25 and imc <=29.9:
        print("Você está com sobre peso")
    elif imc >= 30 and imc <=34.9:
        print("Você está com obesidade grau 1")
    elif imc >= 35 and imc <=39.9:
        print("Você está com obesidade grau 2")
    else:
        print("GRAVE!!! Obesidade grau 3")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))

    # Dando valor as funções
    imc = calcular_imc (peso, altura)
    exibindo = exibir(imc)
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"Seu indice de massa corporal é: {imc:.2f}")
    exibir(imc)
