import numpy as np
from keras.src.legacy.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import pandas as pd
from src.text_extraction import download_text

max_article_len = 500
num_words = 20000

'''

def tokenize_pad(X):
    seq = Tokenizer.texts_to_sequences(X)
    return pad_sequences(seq, maxlen=max_article_len, padding='post')


pipeline = Pipeline([
            ('tokenize_pad', FunctionTransformer(tokenize_pad, validate=False)),
            ('model', model)
        ])
'''

model = Sequential([
            Embedding(input_dim=num_words, output_dim=8, input_length=max_article_len),
            Flatten(),
            Dense(1, activation='sigmoid')
        ])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])



csv_path = 'data/data.csv' 
df = pd.read_csv(csv_path, encoding='utf-8')
teksty_treningowe = df['text'].tolist()
labels = df['label'].tolist()
labels = np.array(labels)
print(labels)
tokenizer = Tokenizer(num_words=num_words) 
tokenizer.fit_on_texts(teksty_treningowe)

sequences1 = tokenizer.texts_to_sequences(teksty_treningowe) 

X_train = pad_sequences(sequences1, maxlen=max_article_len, padding='post')
print(X_train)

model.fit(X_train, labels, epochs=5, batch_size=32, verbose=1)

predictions = model.predict(X_train)
pred_labels = (predictions > 0.5).astype(int)
print(pred_labels.T)
print(labels)

nowy = input("Podaj adres Url artykuły: ")
text = download_text(nowy)

seq_textu = tokenizer.texts_to_sequences([text])
y = pad_sequences(seq_textu, maxlen= max_article_len ,padding='post')
pred = model.predict(y)
print(pred)