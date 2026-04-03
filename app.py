from flask import Flask, request
import joblib
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)

# Liberando acesso externo
CORS(app)

modelo = joblib.load('modelo.pkl')

@app.route('/')
def pagina():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():

    dados = request.get_json()
    print(dados)

    idade = dados['idade']
    salario = dados['salario']

    entrada = [[idade, salario]]

    previsao = modelo.predict(entrada)

    resultado = previsao[0]

    return {"previsao": int(resultado)}

if __name__ == '__main__':
    app.run()