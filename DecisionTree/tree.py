from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
data = pd.read_csv('examples.csv')

# Ajustar o nome da coluna conforme o CSV real
print(data.columns)  # Ajuda a verificar o nome exato
y = data['Supervisão (ChutarParaGol)']  # Use o nome exato aqui
X = data[['DistânciaAoGol', 'ÂnguloParaGol', 'NumeroDeOponentesNaFrente', 
          'DistanciaOponenteMaisProximo', 'VelocidadeDaBola', 'GoleiroVisivel', 
          'DistanciaGoleiro', 'AberturaNoGol']]

# Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do modelo
model = DecisionTreeClassifier(criterion='entropy', max_depth=5)
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')

# Plotando a árvore de decisão
plt.figure(figsize=(20,10))
plot_tree(model, 
          feature_names=X.columns, 
          class_names=['False', 'True'], 
          filled=True, 
          rounded=True, 
          fontsize=10)
plt.savefig('arvore_decisao.png')
plt.show()
