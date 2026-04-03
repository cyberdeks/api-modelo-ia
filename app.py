from flask import Flask, request
import joblib
from flask_cors import CORS

app = Flask(__name__)

# Liberando acesso externo
CORS(app)

modelo = joblib.load('modelo.pkl')

@app.route('/')
def home():
    return "API está funcionando!"

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