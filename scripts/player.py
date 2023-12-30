# player.py
class Jogador:
    def __init__(self):
        # Atributos do jogador
        self.playername = ""
        self.playerage = 0
        self.life = 0

    def playerinfo(self):
        # Retorna um dicionário contendo informações do jogador
        dataplayer = {}
        dataplayer['nome'] = self.playername.capitalize()
        dataplayer['idade'] = str(self.playerage)
        return dataplayer

    def playeratribute(self, level):
        # Define o número de vidas com base no nível de dificuldade
        playerlife = 8 if level == '1' else (5 if level == '2' else 3)
        self.life = playerlife
