# Importa a classe Word do módulo word_generator
from scripts.word_generator import Word

# Arquivo game.py
class Jogo:
    def __init__(self, dificuldade, jogador, palavra):
        # Atributos iniciais do jogo
        self.score = 0
        self.lives = 0
        self.level = dificuldade
        self.word_generator = palavra
        self.word = self.word_generator.palavradificuldade(self.level)  # Obtém uma palavra com base no nível
        self.guess = ""
        self.guessed = []
        self.guessed_letters = []
        self.wrong_guesses = []
        self.wrong_guessed = []
        self.wrong_guessed_letters = []
        self.finalizado = False  # Indica se o jogo foi finalizado
        self.player = jogador
        self.lives = self.player.life  # Atribui o número de vidas do jogador

    def iniciar_jogo(self):
        # Reinicializa as variáveis quando o jogo é iniciado
        self.guess = ""
        self.guessed = []
        self.guessed_letters = []
        self.wrong_guesses = []
        self.wrong_guessed = []
        self.wrong_guessed_letters = []

    def fazer_tentativa(self, tentativa):
        # Processa a tentativa do jogador
        self.guess = tentativa.lower()

        # Verifica se a tentativa já foi feita
        if self.guess in self.guessed or self.guess in self.wrong_guesses:
            print("Você já tentou isso. Tente novamente.")
            return

        # Verifica se a tentativa está correta
        if self.guess in self.word:
            if len(self.guess) == 1:
                self.guessed_letters.append(self.guess)
            else:
                self.guessed.append(self.guess)

            self.guessed.append(self.guess)
            # Atualiza a pontuação com base no nível de dificuldade
            self.score += 1 * 2 if self.level == '2' else (4 if self.level == '3' else 1)

            # Verifica se o jogador acertou toda a palavra
            if self.palavra_oculta() == self.word:
                print("Parabéns! Você acertou a palavra.")
                self.finalizado = True  # Define como True quando a palavra é adivinhada
                self.final_score = self.score * self.lives
                print(f"Sua pontuação final: {self.final_score}")
                return True

        else:
            # Processa uma tentativa incorreta
            if self.guess.isalpha():
                print("Letra incorreta. Você perdeu uma vida.")
                self.wrong_guesses.append(self.guess)
                self.wrong_guessed.append(self.guess)
                self.wrong_guessed_letters.append(self.guess)
                self.lives -= 1
            else:
                print("Entrada inválida. Por favor, digite apenas letras.")

        return False


    def palavra_oculta(self):
        # Retorna a palavra oculta com base nas letras adivinhadas
        return "".join(letter if letter in self.guessed_letters else "_" for letter in self.word)
