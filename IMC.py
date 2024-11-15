#Autor: Tomás Henrique Nogueira de Souza
#Data: 15/11/2024
#Código: IMC, peso e altura = massa

def calcular_imc(peso, altura):
    # Calculando o IMC
    imc = peso / (altura ** 2)

    # Classificando o IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc >= 18.5 and imc < 24.9:
        classificacao = "Peso normal"
    elif imc >= 25 and imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    # Retornando o resultado com IMC arredondado para duas casas decimais
    return f"IMC: {imc:.2f} - {classificacao}"


# Solicitar peso e altura do usuário
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Exibir o resultado
resultado = calcular_imc(peso, altura)
print(resultado)
