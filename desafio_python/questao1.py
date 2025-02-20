def gerar_numeros(n: int) -> list[int]:
    return [i ** 2 for i in range(n, 0, -1)]


def imprimir_estrutura(numeros: list[int]):
    for i in range(len(numeros)):
        print(" ".join(map(str, numeros[i:])))


def main():
    try:
        valor = int(input("Digite um valor inteiro: "))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
            return
        
        numeros = gerar_numeros(valor)
        imprimir_estrutura(numeros)
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()