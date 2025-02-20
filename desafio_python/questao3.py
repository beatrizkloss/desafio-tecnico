def ler_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Digite um número positivo (0 para parar): "))
            if num == 0:
                break
            elif num > 0:
                numeros.append(num)
            else:
                print("Digite apenas números positivos.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro válido.")
    return numeros

def gerar_relatorio(numeros):
    if not numeros:
        print("Nenhum número foi digitado.")
        return

    total = len(numeros)
    maior = max(numeros)
    media = sum(numeros) / total
    impares = [n for n in numeros if n % 2 != 0]
    menor_impar = min(impares) if impares else "Nenhum ímpar"
    contagem = {n: numeros.count(n) for n in set(numeros)}

    print(f"\nRelatório:")
    print(f"a) Quantos números foram lidos: {total}")
    print(f"b) O maior número lido: {maior}")
    print(f"c) A média dos números lidos: {media:.2f}")
    print(f"d) O menor número ímpar lido: {menor_impar}")
    print(f"e) A quantidade de vezes que cada número ocorreu:")
    for num, qtd in contagem.items():
        print(f"O número {num} ocorreu {qtd} vezes.")

def main():
    numeros = ler_numeros()
    gerar_relatorio(numeros)

if __name__ == "__main__":
    main()

