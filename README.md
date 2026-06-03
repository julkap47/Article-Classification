# Article-Classification

Aplikacja służąca do automatycznej klasyfikacji wiarygodności artykułów internetowych przy użyciu algorytmów uczenia maszynowego (SVM). Projekt pobiera treść artykułu z podanego adresu URL, a następnie ocenia, czy treść jest wiarygodna.

---

## Instalacja

```bash
git clone https://github.com/julkap47/Article-Classification.git
cd Article-Classification
```

---


#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

```bash
pip install -r requirements.txt
```


---

## Struktura projektu

```text
Article-Classification/
├── data/                   # Zbiory danych w formacie CSV
├── docs/                   # Dokumentacja techniczna i użytkownika
├── models/                 # Zapisane modele ML (pkl)
├── src/                    # Kod źródłowy aplikacji
│   ├── download.py         # Moduł pobierania i ekstrakcji treści
│   ├── prediction.py       # Moduł uzycia modelu
│   ├── text_extraction.py  # Wyodrębnienie tekstów z artykułów, baza artykułów
│   └── model_training.py   # Tworzenie modelu i jego trening
|    
├── main.py             
├── requirements.txt    
└── README.md           
```



## Autor

Julia Polek 
