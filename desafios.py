```python
"""
Desafio Sprint 1 - Exercícios Práticos da Semana 01
Fundamentos de Python: Variáveis, Tipos, Operadores e Manipulação de Strings.
"""

def desafio_1_calculadora_troco():
    print("\n--- Desafio 1: Calculadora de Troco ---")
    valor_compra = float(input("Digite o valor total da compra (R$): "))
    valor_pago = float(input("Digite o valor pago pelo cliente (R$): "))
    
    troco = valor_pago - valor_compra
    
    if troco < 0:
        print(f"Valor insuficiente! Faltam R$ {abs(troco):.2f}.")
    else:
        print(f"Troco a devolver: R$ {troco:.2f}")


def desafio_2_media_notas():
    print("\n--- Desafio 2: Média de Notas ---")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média final do aluno é: {media:.2f}")


def desafio_3_conversor_tempo():
    print("\n--- Desafio 3: Conversor de Tempo ---")
    total_segundos = int(input("Digite o tempo total em segundos: "))
    
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    
    print(f"Resultado: {horas}h {minutos}m {segundos}s")


def desafio_4_calculadora_desconto():
    print("\n--- Desafio 4: Calculadora de Desconto ---")
    preco_original = float(input("Digite o preço do produto (R$): "))
    percentual_desconto = float(input("Digite a percentagem de desconto (%): "))
    
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")


def desafio_5_par_ou_impar():
    print("\n--- Desafio 5: Par ou Ímpar ---")
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")


def desafio_6_inversor_nome():
    print("\n--- Desafio 6: Inversor de Nome ---")
    nome = input("Digite o seu nome: ").strip()
    nome_invertido = nome[::-1]
    
    print(f"Nome original: {nome}")
    print(f"Nome invertido: {nome_invertido}")


def main():
    print("========================================")
    print("      ENTREGÁVEL - SPRINT 1 PYTHON      ")
    print("========================================")
    
    desafio_1_calculadora_troco()
    desafio_2_media_notas()
    desafio_3_conversor_tempo()
    desafio_4_calculadora_desconto()
    desafio_5_par_ou_impar()
    desafio_6_inversor_nome()
    
    print("\n========================================")
    print("   TODOS OS DESAFIOS FORAM CONCLUÍDOS   ")
    print("========================================")


if __name__ == "__main__":
    main()
