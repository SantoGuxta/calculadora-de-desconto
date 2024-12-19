"""Exercício 1 da Atividade Prática - Lógica de programação e Algorítimos"""

print("Bem-vindo ao Market's Luiz Gustavodos Santos")


value = float(
    input("Digite o valor do produto aqui:\n$ ")
)  # Solicita ao usuário que insira o valor 
quantidade = float(
    input("Digite a quantidade do mesmo produto aqui:\nR: ")
)  # Solicita ao usuário que insira a quantidade 

total_value = (
    value * quantidade
)  # Calcula o valor total multiplicando o valor do produto pela quantidade
print(
    f"O valor total é de ${total_value:.2f} (sem desconto)"
)  # Exibe o valor total sem desconto

if quantidade >= 10:
    if 10 <= quantidade <= 99:
        DISCOUNTO = 0.05  # Desconto de 5% para valores entre 10 e 99
    elif 100 <= quantidade <= 999:
        DISCOUNTO = 0.1  # Desconto de 10% para valores entre 100 e 999
    elif quantidade >= 1000:
        DISCOUNTO= 0.15  # Desconto de 15% para valores maiores ou iguais a 1000
    else:
        DISCOUNTO = 0  # Nenhum desconto para valores abaixo de 10

    discounted_value = total_value - (
        DISCOUNTO * total_value
    )  # Calcula o valor com desconto
    print(
        f"O valor total é de ${discounted_value:.2f} ({DISCOUNTO * 100}% de desconto)"
    )  # Exibe o valor total com desconto e a porcentagem de desconto aplicada
else:
    print(
        "Não há desconto para a quantidade informada."
    )  # Exibe mensagem de que não há desconto para a quantidade informada
  