def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")

    if texto == texto[::-1]:
        return True
    return False

def main():
    print("Verificador de palíndromo")
    texto = input("Digite uma palavra ou frase: ")

    if verificar_palindromo(texto):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")

if __name__ == "__main__":
    main()