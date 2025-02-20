def compactar_string(s: str):
    if not s:
        return ""
    
    resultado = ""
    contador = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            contador += 1
        else:
            resultado += s[i - 1] + (str(contador) if contador > 1 else "")
            contador = 1
            
    resultado += s[-1] + (str(contador) if contador > 1 else "")
    
    return resultado

def main():
    entrada = input("Digite uma string para compactar: ")
    
    if not entrada.isalpha():
        print("Erro: A entrada deve conter apenas letras.")
        return

    saida = compactar_string(entrada)
    print(f"Resultado da compactação: {saida}")

if __name__ == "__main__":
    main()
