import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import joblib
import os
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


csv_path = 'data/data.csv' 
df = pd.read_csv(csv_path, encoding='utf-8')

X = df['text'].tolist()
Y = df['label'].tolist()

#podział danych
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

# Wektoryzacja
vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2))

# Dopasowanie i transformacja zbioru treningowego
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

#Trenowanie moddelu SVM
svm_model = LinearSVC(random_state=42)
svm_model.fit(X_train_tfidf, y_train)

# Sprawdzenie dokładności
train_preds = svm_model.predict(X_train_tfidf)
test_preds = svm_model.predict(X_test_tfidf)

print(f"Dokładność SVM na zbiorze TRENINGOWYM: {accuracy_score(y_train, train_preds):.2f}")
print(f"Dokładność SVM na zbiorze TESTOWYM: {accuracy_score(y_test, test_preds):.2f}")
print("Predykcje modelu: ", list(test_preds))
print("Prawdziwe etykiety:", y_test)
os.makedirs('models', exist_ok=True)

joblib.dump(svm_model, 'models/svm_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("\n--- RAPORT KLASYFIKACJI ---")
print(classification_report(y_test, test_preds, target_names=['Niewiarygodne', 'Wiarygodne']))

# Macierz pomyłek
conf_matrix = confusion_matrix(y_test, test_preds)
print("\n--- MACIERZ POMYŁEK ---")
print(conf_matrix)
