import requests
import trafilatura
import pandas as pd

def download_text(url):
    headers = { 'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    downloaded = response.text

    text = trafilatura.extract(downloaded)
    return text

url_base = [
    {"https://www.gov.pl/web/premier/odprawa-w-rzadowym-centrum-bezpieczenstwa-po-serii-prowokacji-i-falszywych-alarmow": 1},
    {"https://www.gov.pl/web/obrona-narodowa/wspolpraca-polski-i-kanady-oparta-na-bezpieczenstwie-inwestycjach-i-nowoczesnych-technologiach" : 1},
    {"https://www.gov.pl/web/mswia/ruszaja-zapisy-na-szkolenia-z-ochrony-ludnosci-i-obrony-cywilnej-partnerzy-mswia-przeszkola-ponad-100-tysiecy-polek-i-polakow" : 1},
    {"https://www.gov.pl/web/rodzina/wazne-wiesci-dla-rodzicow-nawet-60-dni-dodatkowego-zasilku-opiekunczego-na-chore-dziecko": 1},
    {"https://www.plotek.pl/styl-i-uroda/7,198217,32818062,tlum-gwiazd-na-konferencji-przed-opolem-wyszkoni-w-dziwacznych.html" : 0},
    {"https://www.plotek.pl/plotek/7,111485,32817336,cyrwus-wygadal-sie-ile-dostawal-za-granie-ryska-w-klanie.html" : 0},
    {"https://www.plotek.pl/plotek/7,111485,32813208,bedoes-nie-szczedzil-gorzkich-slow-po-fryderykach-jest-mi.html" : 0},
    {"https://www.polsatnews.pl/wiadomosc/2026-05-27/papiez-leon-xiv-zwrocil-sie-do-polakow-podziekowal-kobietom/" : 1},
    {"https://lovekrakow.pl/tramwaj-do-mistrzejowic-z-nowa-data-miasto-podalo-termin-uruchomienia-linii" : 1},
    {"https://lovekrakow.pl/tragedia-w-uniszowej-90-letni-kierowca-smiertelnie-potracil-80-letnia-rowerzystke" : 1},
    {"https://lovekrakow.pl/tragiczna-smierc-posla-aleksander-miszalski-zegna-lukasza-litewke" :1},
    {"https://www.pudelek.pl/66-letnia-majka-jezowska-w-falbaniastej-mini-melduje-sie-na-konferencji-w-opolu-petarda-zdjecia-7290475585870048g" : 0},
    {"https://www.pomponik.pl/relacje-i-zwiazki/news-wisniewski-ledwo-wyszedl-z-sadu-a-za-chwile-tam-wroci-termin,nId,23488582" : 0},
    {"https://www.pomponik.pl/plotki/news-potwierdzily-sie-doniesienia-ws-kuszewskiego-decyzje-podjeto,nId,23488519" : 0},
    {"https://www.kozaczek.pl/pozar-na-grobie-lukasza-litewki-bliscy-sa-zrozpaczeni-nagrania-blyskawicznie-obiegly-siec/" : 0},
    {"https://www.kozaczek.pl/galeria/plejada-gwiazd-lsni-na-konferencji-kfpp-opole-2026-doda-kukulska-wyszkoni/" : 0},
    {"https://zero.pl/news/koncert-taco-hemingwaya-na-narodowym-kontrowersje-wokol-ceny-wody" : 1},
    {"https://zero.pl/news/papiez-o-sztucznej-inteligencji-zagrozenia-etyka-i-przyszlosc-czlowieka" : 1},
    {"https://zero.pl/news/emerytury-artystow-z-budzetu-jak-rzad-sprawdzi-kto-nim-jest" : 1},
    {"https://www.kozaczek.pl/co-sie-wydarzylo-na-premierach-w-opolu-widzowie-nie-zostawili-suchej-nitki/" : 0},
    {"https://www.kozaczek.pl/tego-polskiego-miliardera-prawie-nikt-nie-zna-jest-kumplem-muska-i-moze-trafic-do-swiatowej-elity/" :0}
]

dane_treningowe = []

for pozycja in url_base:
    url = list(pozycja.keys())[0]
    label = list(pozycja.values())[0]
    
    artykul_tekst = download_text(url)
    
    if artykul_tekst:
        czysty_tekst = artykul_tekst.replace("\n", " ").replace("\r", " ")
        dane_treningowe.append({"text": czysty_tekst, "label": label})
        
df = pd.DataFrame(dane_treningowe)
df.to_csv('data/data.csv', index=False, encoding='utf-8')
    