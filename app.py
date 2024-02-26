from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
      self.nome = nome
      self.categoria = categoria
      self.console = console  

@app.route("/hello")
def hello_world():
  jogos1 = Jogo('Tetris', 'Puzzle', 'Atari')
  jogo2 = Jogo('God of war', 'Ação', 'PS4')
  jogos = [jogos1, jogo2]
  return render_template('lista.html', jogos=jogos)

app.run()