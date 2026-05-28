
import joblib
svm_model = joblib.load('models/svm_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def predict_new_article(url):

    text_poj = vectorizer.transform(url)  # Przekształcenie pojedynczego tekstu do formatu TF-IDF
    pred = svm_model.predict(text_poj)  # Predykcja etykiety dla nowego tekstu
    if pred == 1:
        pred = "WIARYGODNY"
    else:
        pred = "NIEWIARYGODNY"
    return pred
