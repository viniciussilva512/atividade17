# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date 

ano_atual = date.today().year 

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento 

if idade < 18:
    anos_falta = 18 - idade
    print(f"Você ainda não atingiu a idade para se alistar. Faltam {anos_falta} anos para o alistamento.")
elif idade == 18:
    print("Está na hora de se alistar! Procure a Junta Militar mais próxima. ")
else:
    anos_passados = idade - 18
    print(f"Já passou do tempo de se alistar. Passaram {anos_passados} anos desde o prazo. ")

