import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_excel('dados_modelo.xlsx')

print("Dados carregados:")
print(df)

X = df[['idade', 'salario']]

y = df['comprou']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

joblib.dump(modelo, 'modelo.pkl')
print("Modelo treinado e salvo com sucesso!")