import os

# Entrada
def logo_senai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def exibir(imc):
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc <= 24.9:
        print("Peso ideal.")
    elif 25 <= imc <= 29.9:
        print("Você está com sobrepeso.")
    elif 30 <= imc <= 34.9:
        print("Você está com obesidade grau 1.")
    elif 35 <= imc <= 39.9:
        print("Você está com obesidade grau 2.")
    else:
        print("GRAVE!!! Obesidade grau 3.")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Entrada

while True:
    logo_senai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))

    # Calculando o IMC
    imc = calcular_imc(peso, altura)
    exibir(imc)
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Saída
logo_senai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i + 1}:")
    print("Nome Completo:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    imc = calcular_imc(pesos[i], alturas[i])  # Calculando o IMC para cada usuário
    print(f"Seu índice de massa corporal é: {imc:.2f}")
    exibir(imc)
