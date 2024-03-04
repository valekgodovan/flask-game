from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template(
        'index.html'
    )

@app.route('/live')
def live():
    live = GameOfLife()
    if live.counter > 0:
        live.form_new_generation()
    live.counter += 1
    return render_template(
        'live.html',
        live=live,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
