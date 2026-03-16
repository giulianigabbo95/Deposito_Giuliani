import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

# 1. Caricamento dati
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# 2. Split Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Addestramento Random Forest
# Usiamo 100 alberi (n_estimators)
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)

# 4. Predizione
y_pred = rf_clf.predict(X_test)

# --- GRAFICO 1: MATRICE DI CONFUSIONE ---
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', 
            xticklabels=data.target_names, yticklabels=data.target_names)
plt.title('Matrice di Confusione: Breast Cancer')
plt.xlabel('Previsione')
plt.ylabel('Reale')

# --- GRAFICO 2: FEATURE IMPORTANCE ---
plt.subplot(1, 2, 2)
importances = rf_clf.feature_importances_
indices = np.argsort(importances)[-10:] # Prendiamo le 10 più importanti

plt.barh(range(len(indices)), importances[indices], color='skyblue', align='center')
plt.yticks(range(len(indices)), [data.feature_names[i] for i in indices])
plt.title('Top 10 Caratteristiche più Importanti')
plt.xlabel('Importanza Relativa (Gini Importance)')

plt.tight_layout()
plt.show()

print(classification_report(y_test, y_pred, target_names=data.target_names))