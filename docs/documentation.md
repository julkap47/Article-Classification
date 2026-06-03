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

1. **Proces treningowy** – przygotowanie danych, trenowanie modelu oraz zapis wytrenowanych artefaktów.
2. **Proces inferencyjny** – klasyfikacja nowych artykułów przy użyciu wcześniej wytrenowanego modelu.

### Komponenty

#### `src/download.py`

Odpowiada za pobieranie surowej zawartości strony internetowej (HTML) przy użyciu biblioteki `requests` oraz jej ekstrakcję za pomocą biblioteki `trafilatura`.

#### `text_extraction.py`

Moduł przetwarzający surowy kod HTML w celu wyodrębnienia czystej treści tekstowej artykułu.

#### `model_training.py`

Moduł odpowiedzialny za proces uczenia modelu. Realizuje:

* wektoryzację tekstu metodą TF-IDF,
* trenowanie klasyfikatora `LinearSVC`,
* serializację modelu i wektoryzatora.

#### `prediction.py`

Moduł produkcyjny odpowiedzialny za:

* wczytywanie wytrenowanego modelu,
* przetwarzanie nowych danych wejściowych,
* wykonywanie klasyfikacji.


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

Parametry:

* **ngram_range=(1, 2)** – analiza pojedynczych słów oraz fraz dwuwyrazowych.
* **max_features=3000** – ograniczenie liczby cech do 3000 najistotniejszych tokenów.

Takie podejście pozwala uchwycić zarówno pojedyncze słowa kluczowe, jak i istotny kontekst wynikający z występowania określonych fraz.

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

Model poprawnie sklasyfikował wszystkie artykuły oznaczone jako Niewiarygodne, a w przypadku klasy Wiarygodne wystąpił jeden błąd typu False Negative.
Precyzja dla klasy „Wiarygodne” wyniosła 100%, co oznacza, że każdy artykuł oznaczony przez model jako wiarygodny rzeczywiście należał do tej kategorii.



---

**Autor:** Julia Polek
**Projekt:** Article-Classification
