import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. Caricamento dati - Usiamo solo Petal Length e Petal Width per la visualizzazione
iris = datasets.load_iris()
X = iris.data[:, 2:4] # Feature 2 e 3 (Petali)
y = iris.target

# 2. Addestramento del modello
# max_depth=3 è perfetto per vedere bene i "tagli" senza complicare troppo
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_clf.fit(X, y)

# 3. Creazione del grafico con due sotto-grafici (Subplots)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# --- SOTTO-GRAFICO 1: Confini di Decisione ---
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                    np.arange(y_min, y_max, 0.02))

Z = tree_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

ax1.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
scatter = ax1.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=40, cmap='viridis')
ax1.set_title("Confini di Decisione (Rappresentazione Geometrica)")
ax1.set_xlabel(iris.feature_names[2])
ax1.set_ylabel(iris.feature_names[3])

# --- SOTTO-GRAFICO 2: Struttura dell'Albero ---
plot_tree(tree_clf, 
        feature_names=[iris.feature_names[2], iris.feature_names[3]],  
        class_names=iris.target_names, 
        filled=True, rounded=True, ax=ax2)
ax2.set_title("Logica Interna (Decision Tree)")

plt.tight_layout()
plt.show()