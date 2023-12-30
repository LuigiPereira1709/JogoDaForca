import tkinter as tk
from tkinter import messagebox, simpledialog
from game import Jogo
from player import Jogador
from word_generator import Word

class JogoInterface:
    def __init__(self, root):
        # Inicializa a interface do jogo
        self.root = root
        self.root.title("Jogo da Forca")
        self.cor_fundo = "#EAF3FA"  # Azul claro para o fundo
        self.cor_titulo = "#004876"  # Azul escuro para o título
        self.cor_texto = "#333333"  # Cor escura para o texto
        self.cor_botao = "#008CBA"  # Azul um pouco mais claro para os botões
        self.palavra_label = None
        self.tentativas_label = tk.Label(self.root, text="", bg=self.cor_fundo, fg=self.cor_texto)  # Inicializa como Label vazia
        self.vidas_label = None
        self.voltar_ao_menu_botao = None
        self.criar_interface()

    def criar_interface(self):
        self.root.configure(bg=self.cor_fundo)

        self.label_nivel = tk.Label(self.root, text="Escolha a dificuldade:", bg=self.cor_fundo, fg=self.cor_titulo)
        self.label_nivel.pack()

        self.nivel_var = tk.StringVar()
        self.nivel_var.set("1")

        self.niveis_radio = [
            ("Fácil", "1"),
            ("Médio", "2"),
            ("Difícil", "3"),
        ]

        self.dificuldade_frame = tk.Frame(self.root, bg=self.cor_fundo)
        self.dificuldade_frame.pack()

        for texto, nivel in self.niveis_radio:
            radio = tk.Radiobutton(self.dificuldade_frame, text=texto, variable=self.nivel_var, value=nivel, bg=self.cor_fundo, fg=self.cor_texto)
            radio.pack()

        self.botao_iniciar = tk.Button(self.root, text="Iniciar Jogo", command=self.iniciar_jogo, bg=self.cor_titulo, fg=self.cor_fundo)
        self.botao_iniciar.pack()
    
    def iniciar_jogo(self):
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

        self.label_nivel.pack_forget()
        self.nivel_var.set("")
        self.dificuldade_frame.pack_forget()
        self.botao_iniciar.pack_forget()

        self.exibir_interface()

    def exibir_interface(self):
        while not self.jogo.finalizado and self.jogo.lives > 0:
            tentativa = simpledialog.askstring("Jogo da Forca", "Digite uma letra:")
            if tentativa is None:
                self.voltar_ao_menu()
                return

            resultado = self.jogo.fazer_tentativa(tentativa)
            self.atualizar_interface()

            if resultado:
                break

        if self.jogo.lives <= 0:
            messagebox.showinfo("Fim do Jogo", f"Você perdeu! A palavra era: {self.jogo.word}")
        else:
            messagebox.showinfo("Fim do Jogo", f"Parabéns! Você acertou a palavra. Sua pontuação final: {self.jogo.score}")

        # Adiciona o botão "Voltar ao Menu"
        self.voltar_ao_menu_botao = tk.Button(self.root, text="Voltar ao Menu", command=self.voltar_ao_menu, bg=self.cor_titulo, fg=self.cor_fundo)
        self.voltar_ao_menu_botao.pack()

    def voltar_ao_menu(self):
        # Limpa os elementos antigos da interface
        self.limpar_interface()

        # Retorna ao menu principal
        self.criar_interface()

    def limpar_interface(self):
        # Limpa os elementos antigos da interface
        if self.tentativas_label is not None:
            self.tentativas_label.destroy()

        if hasattr(self, 'vidas_label') and self.vidas_label is not None:
            self.vidas_label.destroy()

        if hasattr(self, 'voltar_ao_menu_botao') and self.voltar_ao_menu_botao is not None:
            self.voltar_ao_menu_botao.destroy()

        if hasattr(self, 'palavra_label') and self.palavra_label is not None:
            self.palavra_label.destroy()

    def atualizar_interface(self):
        # Limpa os elementos antigos da interface
        self.limpar_interface()

        # Atualiza a interface com as tentativas, vidas restantes e palavra
        self.tentativas_label = tk.Label(self.root, text=f"Tentativas: {', '.join(self.jogo.guessed)}", bg=self.cor_fundo, fg=self.cor_texto)
        self.tentativas_label.pack()

        self.vidas_label = tk.Label(self.root, text=f"Vidas: {self.jogo.lives}", bg=self.cor_fundo, fg=self.cor_texto)
        self.vidas_label.pack()

        # Adiciona a exibição da palavra oculta e revelada
        palavra_oculta = " ".join("_" if letra not in self.jogo.guessed_letters else letra for letra in self.jogo.word)
        self.palavra_label = tk.Label(self.root, text=f"Palavra: {palavra_oculta}", bg=self.cor_fundo, fg=self.cor_texto)
        self.palavra_label.pack()

# Criar instâncias dos objetos necessários
root = tk.Tk()
interface = JogoInterface(root)

# Executar a interface
interface.root.mainloop()
