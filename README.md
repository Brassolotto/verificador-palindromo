# Verificador de Palíndromos em Python

## 📝 Descrição
Um programa que verifica se uma palavra ou frase é um palíndromo (pode ser lida igual de trás para frente). Disponível em duas versões: básica e avançada.

## 🚀 Funcionalidades

### Versão Básica
- Verificação simples de palíndromos
- Remove espaços
- Converte para minúsculas
- Interface via linha de comando

### Versão Avançada
- Remove pontuação e caracteres especiais
- Exibe texto original e processado
- Mostra texto invertido
- Menu interativo
- Exemplos prontos
- Análise detalhada

## 📋 Pré-requisitos
- Python 3.6 ou superior instalado
- Módulos utilizados:
  - string (biblioteca padrão)

## 🔧 Como executar

1. Clone este repositório:
```bash
git clone https://github.com/Brassolotto/verificador-palindromo.git
```

2. Navegue até o diretório do projeto:
```bash
cd verificador-palindromo
```

3. Execute a versão desejada:
```bash
python verificador_palindromo_basico.py
# ou
python verificador_palindromo_avancado.py
```

## 📖 Como usar

### Versão Básica
1. Digite uma palavra ou frase
2. O programa informará se é um palíndromo

### Versão Avançada
1. Escolha uma opção do menu:
   - Verificar palavra/frase
   - Ver exemplos
   - Sair
2. Siga as instruções na tela

## 🎯 Exemplos de uso
```
=== Verificador de Palíndromo ===

Digite uma palavra ou frase: Socorram me subi no onibus em Marrocos

Resultado: É um palíndromo!
```

## ⚠️ Tratamento de Erros
- Validação de entrada vazia
- Tratamento de caracteres especiais
- Validação de opções do menu (versão avançada)

## 🔍 Estrutura do Código

### Versão Básica
```
verificador_palindromo_basico.py
├── Função verificar_palindromo()
└── Função main()
```

### Versão Avançada
```
verificador_palindromo_avancado.py
├── Função limpar_texto()
├── Função verificar_palindromo()
├── Função exibir_resultado()
└── Função main()
```

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Melhorias Futuras
- [ ] Interface gráfica
- [ ] Verificação de palíndromos numéricos
- [ ] Suporte a outros idiomas
- [ ] Histórico de verificações
- [ ] Estatísticas de uso

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por [Rick Brassolotto] 😊