# Dokumentacja Techniczna Projektu: Article-Classification

## 1. Wstęp

Article-Classification służy do automatycznej klasyfikacji wiarygodności artykułów internetowych. Aplikacja wykorzystuje uczenie maszynowe (algorytm SVM) do analizy treści tekstowej i przypisywania jej do jednej z dwóch kategorii:

* **Wiarygodne**
* **Niewiarygodne**

---

## 2. Kryteria Klasyfikacji (Dataset Taxonomy)

Zbiór danych treningowych został przygotowany w oparciu o następujące definicje:

### Etykieta 0: Treści Niewiarygodne

Kategoria obejmuje źródła o niskiej wartości merytorycznej:

* **Portale plotkarskie i tabloidy** – źródła skoncentrowane na sensacji subiektywnych opiniach plotkach czy clickbaitach (np. Plotek, Pudelek, Pomponik).
* **Źródła z historią dezinformacji** – serwisy publikujące niesprawdzone doniesienia, teorie spiskowe lub pseudonaukowe tezy (np. wolnemedia.net).

### Etykieta 1: Treści Wiarygodne

Kategoria obejmuje źródła o wysokim standardzie informacyjnym:

* **Instytucje rządowe** – oficjalne serwisy administracji publicznej (np. gov.pl).
* **Zweryfikowane media** – portale informacyjne przestrzegające standardów etyki dziennikarskiej (np. Polsat News, zero.pl).
* **Serwisy eksperckie** – blogi technologiczne firm oraz rzetelne serwisy lokalne (np. sii.pl, lovekrakow.pl).

---

## 3. Architektura Systemu

System działa w oparciu o dwa główne procesy:

1. **Proces pobierania danych** 

`download.py`

Moduł odpowiedzialny za pobieranie zawartości stron internetowych przy użyciu biblioteki `requests` oraz ekstrakcję głównej treści artykułu z wykorzystaniem biblioteki `trafilatura`.

`text_extraction.py`

Moduł służący do budowy zbioru danych treningowych z wykorzystaniem modułu `download.py`.

2. **Proces tworzenia i trenowania modelu** 

`model_training.py`

Moduł odpowiedzialny za proces uczenia modelu. W pierwszej kolejności wykonuje wektoryzację tekstu metodą TF-IDF, następnie przeprowadza trenowanie klasyfikatora `LinearSVC`, a na końcu zapisuje wytrenowany model oraz wektoryzator do plików.

`prediction.py`

Moduł wykorzystywany do wczytywania wcześniej wytrenowanego modelu i wykonywania predykcji dla nowych artykułów.

---

## 4. Specyfikacja Modelu

### Wektoryzacja

Do reprezentacji tekstu wykorzystano klasę `TfidfVectorizer` z biblioteki scikit-learn:

```python
TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=3000
)
```

Zastosowano następujące parametry:

ngram_range=(1, 2) – umożliwia analizę zarówno pojedynczych słów, jak i fraz dwuwyrazowych.
max_features=3000 – ogranicza liczbę cech do 3000 najistotniejszych tokenów.

### Klasyfikator

Do klasyfikacji wykorzystano:

```python
LinearSVC
```

Klasyfikator `Linear Support Vector Classifier` został wybrany ze względu na wysoką skuteczność w zadaniach klasyfikacji tekstu , dobrą skalowalność oraz efektywność obliczeniową.

---

## 5. Ewaluacja i Wyniki

Model został oceniony na zbiorze testowym zawierającym 17 artykułów.

### Raport Klasyfikacji

| Metryka   | Niewiarygodne (0) | Wiarygodne (1) |
| --------- | ----------------- | -------------- |
| Precision | 0.90              | 1.00           |
| Recall    | 1.00              | 0.88           |
| F1-score  | 0.95              | 0.93           |

### Dokładność Całkowita

**Accuracy: 94%**

### Macierz Pomyłek

```text
[[9, 0],
 [1, 7]]
```

### Interpretacja Wyników

Model poprawnie sklasyfikował wszystkie artykuły oznaczone jako Niewiarygodne, a w przypadku klasy Wiarygodne wystąpił jeden błąd typu False Negative, czyli artykuł wiarygodny został błędnie zakwalifikowany jako niewiarygodny.
Precyzja dla klasy „Wiarygodne” wyniosła 100%, co oznacza, że każdy artykuł oznaczony przez model jako wiarygodny rzeczywiście należał do tej kategorii.



---

**Autor:** Julia Polek
**Projekt:** Article-Classification
