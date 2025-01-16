import string

def limpar_texto(texto):
    """Remove pontuação, espaços e converte para minúsculas"""
    # Remove pontuação
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    # Remove espaços e converte para minúsculas
    return texto.lower().replace(" ", "")

def verificar_palindromo(texto):
    """Verifica se o texto é um palíndromo e retorna detalhes"""
    texto_original = texto
    texto_limpo = limpar_texto(texto)
    texto_invertido = texto_limpo[::-1]
    
    is_palindromo = texto_limpo == texto_invertido
    
    return {
        "original": texto_original,
        "processado": texto_limpo,
        "invertido": texto_invertido,
        "eh_palindromo": is_palindromo,
        "tamanho": len(texto_limpo)
    }

def exibir_resultado(resultado):
    """Exibe o resultado da análise de forma formatada"""
    print("\n=== Resultado da Análise ===")
    print(f"Texto original: {resultado['original']}")
    print(f"Texto processado: {resultado['processado']}")
    print(f"Texto invertido: {resultado['invertido']}")
    print(f"Tamanho: {resultado['tamanho']} caracteres")
    print(f"\nResultado: ", end="")
    
    if resultado['eh_palindromo']:
        print("✅ É um palíndromo!")
    else:
        print("❌ Não é um palíndromo!")

def main():
    while True:
        print("\n=== Verificador de Palíndromo ===")
        print("1. Verificar palavra/frase")
        print("2. Ver exemplos")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao == "1":
            texto = input("\nDigite uma palavra ou frase: ")
            if texto.strip():  # Verifica se não está vazio
                resultado = verificar_palindromo(texto)
                exibir_resultado(resultado)
            else:
                print("Texto vazio! Tente novamente.")
                
        elif opcao == "2":
            exemplos = [
                "ovo",
                "Socorram me subi no onibus em Marrocos",
                "A man, a plan, a canal - Panama!",
                "Python"
            ]
            print("\n=== Exemplos ===")
            for exemplo in exemplos:
                resultado = verificar_palindromo(exemplo)
                exibir_resultado(resultado)
                print()  # Linha em branco entre exemplos
                
        elif opcao == "3":
            print("\nObrigado por usar o verificador de palíndromos!")
            break
            
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
