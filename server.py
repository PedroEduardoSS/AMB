from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sintomas = ['Calafrios', 'Diarreia', 'Dor de cabeça', 'Dor Geral', 'Dor de garganta', 'Dor no tórax/peito', 'Dor nos Olhos',
     'Emagrecimento', 'Febre', 'Mal-estar', 'Má Respiração', 'Man Vermelhas', 'Nausea', 'Olhos Vermelhos',
     'Perda Paladar', 'Perda Olfato', 'Sangue Nasal', 'Tosse', 'Tosse seca', 'Tontura', 'Vomitos']

@app.route('/')
def index():
    return render_template('base.html', sintomas=sintomas)

if __name__ == "__main__":
    app.run(debug=True)