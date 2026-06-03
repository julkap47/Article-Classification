import numpy as np
from keras.src.legacy.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import pandas as pd

class WeryfikatorModel:
    def __init__(self, num_words=20000, max_article_len=500):
        self.num_words = num_words
        self.max_article_len = max_article_len
        
        self.tokenizer = Tokenizer(num_words=self.num_words, lower=True)
        self.model = self._built_model()
        self.pipeline = self._pipeline()

    def _built_model(self):
        model = Sequential([
            Embedding(input_dim=self.num_words, output_dim=8, input_length=self.max_article_len),
            Flatten(),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def _tokenize_pad_wrapper(self, X):
        seq = self.tokenizer.texts_to_sequences(X)
        return pad_sequences(seq, maxlen=self.max_article_len, padding='post')

    def _pipeline(self):
        return Pipeline([
            ('tokenize_pad', FunctionTransformer(self._tokenize_pad_wrapper, validate=False)),
            ('model', self.model)
        ])

    def trenuj(self, teksty_treningowe, etykiety, epochs=5):
        self.tokenizer.fit_on_texts(teksty_treningowe)
        X_data = np.array(teksty_treningowe)
        y_data = np.array(etykiety)
        self.pipeline.fit(X_data, y_data, model__epochs=epochs)

    def przewiduj_wiarygodnosc(self, pojedynczy_tekst):

        dane_wejsciowe = np.array([pojedynczy_tekst])
        prediction = self.pipeline.predict(dane_wejsciowe)
        
        if prediction > 0.5:
            return f"WIARYGODNY ({prediction*100:.1f}%)"
        else:
            return f"NIEWIARYGODNY ({(1-prediction)*100:.1f}%)"
        

    
