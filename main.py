
from src.download import download_text 
from src.prediction import predict_new_article

def main():
    
    newy = input("Podaj adres Url artykuły: ")
    text = download_text(newy)
    text_poj = [text]  # Przekształcenie pojedynczego tekstu do formatu listy
    predykcja = predict_new_article(text_poj)
    print(predykcja)

if __name__ == "__main__":
    main()
       