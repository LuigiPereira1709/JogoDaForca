# Jogo da Forca - Projeto Data Science Academy

Bem-vindo ao Jogo da Forca, um projeto desenvolvido como parte do curso de Python para Análise de Dados da Data Science Academy.

## Descrição do Projeto

O Jogo da Forca é uma implementação simples de um jogo clássico de forca. O jogador escolhe a dificuldade, faz tentativas para adivinhar a palavra oculta e ganha ou perde com base no número de vidas disponíveis.

## Objetivo do Projeto

Este projeto teve como intuito colocar em prática conhecimentos sobre:

- Programação Orientada a Objetos (POO)
- Modularização
- Manipulação de arquivos
- Loops
- Condicionais
- Tratamento de erros

## Requisitos

- Python 3.x
- Bibliotecas Python: tkinter, json, unidecode

## Estrutura do Projeto

- `files`: Pasta com arquivos utilizados no jogo
  - `frutas.json`: Documento JSON com os nomes das frutas utilizadas no jogo  
- `scripts`: Pasta dos scripts Python do jogo
  - `game.py`: Implementação da classe Jogo.
  - `player.py`: Implementação da classe Jogador.
  - `word_generator.py`: Implementação da classe Word para gerar palavras com base no tema e dificuldade.
  - `main.py`: Script principal para executar o jogo usando a interface gráfica Tkinter.
- `JogoDaForca`: Arquivo .exe do jogo
- `requirements.txt`: Arquivo contendo as bibliotecas necessárias. Pode ser gerado usando o comando:
  ```bash
  pip freeze > requirements.txt
## Como Executar
Certifique-se de ter os requisitos instalados e execute o script main.py.
```bash
  python main.py
```
## Download do Executável
Você pode baixar o executável do jogo diretamente [aqui](Jogo%20da%20Forca.exe), aperte as teclas de atalho `ctrl + shift + s` para fazer o download.
## Autor
Luigi Pereira
## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
