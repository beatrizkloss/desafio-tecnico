def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    return []

def contar_vc(linha):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    # v = vogais, c = consoantes
    v, c = 0, 0
    for char in linha:
        if char in vogais:
            v += 1
        elif char in consoantes:
            c += 1
    return v, c

def main():
    nome_arquivo = input("Digite o nome do arquivo de texto (com extensão .txt): ")
    linhas = ler_arquivo(nome_arquivo)

    if not linhas:
        return

    max_v, max_c = -1, -1
    linha_v, linha_c = -1, -1

    for i, linha in enumerate(linhas, 1):
        vogais, consoantes = contar_vc(linha)
        if vogais > max_v:
            max_v, linha_v = vogais, i
        if consoantes > max_c:
            max_c, linha_c = consoantes, i

    print(f"A linha com mais vogais é a linha {linha_v} com {max_v} vogais.")
    print(f"A linha com mais consoantes é a linha {linha_c} com {max_c} consoantes.")

if __name__ == "__main__":
    main()

