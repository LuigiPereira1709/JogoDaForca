import tkinter as tk
from tkinter import messagebox, simpledialog
from game import Jogo
from player import Jogador
from scripts.word_generator import Word

class JogoInterface:
    def __init__(self, root):
        # Inicializa a interface do jogo
        self.root = root
        self.root.title("Jogo da Forca")

        self.jogo = None
        self.palavra_label = None
        self.dificuldade_frame = None
        self.criar_interface()

    def criar_interface(self):
        # Cria a interface inicial para escolher a dificuldade do jogo
        self.label_nivel = tk.Label(self.root, text="Escolha a dificuldade:")
        self.label_nivel.pack()

        self.nivel_var = tk.StringVar()
        self.nivel_var.set("1")

        self.niveis_radio = [
            ("Fácil", "1"),
            ("Médio", "2"),
            ("Difícil", "3"),
        ]

        self.dificuldade_frame = tk.Frame(self.root)
        self.dificuldade_frame.pack()

        for texto, nivel in self.niveis_radio:
            radio = tk.Radiobutton(self.dificuldade_frame, text=texto, variable=self.nivel_var, value=nivel)
            radio.pack()

        self.botao_iniciar = tk.Button(self.root, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.botao_iniciar.pack()

    def iniciar_jogo(self):
        # Inicia o jogo com base na dificuldade escolhida
        nivel_escolhido = self.nivel_var.get()

        if not nivel_escolhido:
            messagebox.showwarning("Alerta", "Por favor, escolha a dificuldade.")
            return

        player = Jogador()
        nome = simpledialog.askstring("Jogo da Forca", "Digite seu nome:")
        idade = simpledialog.askinteger("Jogo da Forca", "Digite sua idade:")

        if not nome or idade is None or idade <= 0:
            messagebox.showwarning("Alerta", "Por favor, preencha seu nome e idade válida.")
            return

        player.playername = nome
        player.playerage = idade
        player.playeratribute(nivel_escolhido)

        self.jogo = Jogo(nivel_escolhido, player, Word("frutas"))
        self.jogo.iniciar_jogo()

        # Oculta os elementos de entrada
        self.label_nivel.pack_forget()
        self.nivel_var.set("")  # Limpa a seleção
        self.dificuldade_frame.pack_forget()
        self.botao_iniciar.pack_forget()

        # Exibe a interface do jogo
        self.exibir_interface()

    def exibir_interface(self):
        while not self.jogo.finalizado and self.jogo.lives > 0:
            tentativa = simpledialog.askstring("Jogo da Forca", "Digite uma letra ou palavra:")
            if tentativa is None:
                # Usuário pressionou Cancelar, volta ao menu principal
                self.voltar_ao_menu()
                return

            resultado = self.jogo.fazer_tentativa(tentativa)

            # Atualiza a interface com as tentativas, vidas restantes e palavra
            self.atualizar_interface()

            if resultado:
                break

        if self.jogo.lives <= 0:
            messagebox.showinfo("Fim do Jogo", f"Você perdeu! A palavra era: {self.jogo.word}")
        else:
            messagebox.showinfo("Fim do Jogo", f"Parabéns! Você acertou a palavra. Sua pontuação final: {self.jogo.score}")

        # Adiciona o botão "Voltar ao Menu"
        self.voltar_ao_menu_botao = tk.Button(self.root, text="Voltar ao Menu", command=self.voltar_ao_menu)
        self.voltar_ao_menu_botao.pack()

    def voltar_ao_menu(self):
        # Limpa os elementos antigos da interface
        self.limpar_interface()

        # Retorna ao menu principal
        self.criar_interface()

    def limpar_interface(self):
        # Limpa os elementos antigos da interface
        if hasattr(self, 'tentativas_label'):
            self.tentativas_label.destroy()

        if hasattr(self, 'vidas_label'):
            self.vidas_label.destroy()

        if hasattr(self, 'voltar_ao_menu_botao'):
            self.voltar_ao_menu_botao.destroy()

        if self.palavra_label is not None:
            self.palavra_label.destroy()

    def atualizar_interface(self):
        # Limpa os elementos antigos da interface
        self.limpar_interface()

        # Atualiza a interface com as tentativas, vidas restantes e palavra
        self.tentativas_label = tk.Label(self.root, text=f"Tentativas: {', '.join(self.jogo.guessed)}")
        self.tentativas_label.pack()

        self.vidas_label = tk.Label(self.root, text=f"Vidas: {self.jogo.lives}")
        self.vidas_label.pack()

        # Adiciona a exibição da palavra oculta e revelada
        palavra_oculta = " ".join("_" if letra not in self.jogo.guessed_letters else letra for letra in self.jogo.word)
        self.palavra_label = tk.Label(self.root, text=f"Palavra: {palavra_oculta}")
        self.palavra_label.pack()

# Criar instâncias dos objetos necessários
root = tk.Tk()
interface = JogoInterface(root)

# Executar a interface
interface.root.mainloop()
