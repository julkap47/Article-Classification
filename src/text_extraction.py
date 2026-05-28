
from src.dwon import download_text
import pandas as pd


url_base = [
    # --- ETYKIETA 0 niewiarygodne ---
    {"https://www.plotek.pl/styl-i-uroda/7,198217,32818062,tlum-gwiazd-na-konferencji-przed-opolem-wyszkoni-w-dziwacznych.html" : 0},
    {"https://www.plotek.pl/plotek/7,111485,32817336,cyrwus-wygadal-sie-ile-dostawal-za-granie-ryska-w-klanie.html" : 0},
    {"https://www.plotek.pl/plotek/7,111485,32813208,bedoes-nie-szczedzil-gorzkich-slow-po-fryderykach-jest-mi.html" : 0},
    {"https://www.pudelek.pl/66-letnia-majka-jezowska-w-falbaniastej-mini-melduje-sie-na-konferencji-w-opolu-petarda-zdjecia-7290475585870048g" : 0},
    {"https://www.pomponik.pl/relacje-i-zwiazki/news-wisniewski-ledwo-wyszedl-z-sadu-a-za-chwile-tam-wroci-termin,nId,23488582" : 0},
    {"https://www.pomponik.pl/plotki/news-potwierdzily-sie-doniesienia-ws-kuszewskiego-decyzje-podjeto,nId,23488519" : 0},
    {"https://www.kozaczek.pl/pozar-na-grobie-lukasza-litewki-bliscy-sa-zrozpaczeni-nagrania-blyskawicznie-obiegly-siec/" : 0},
    {"https://www.kozaczek.pl/galeria/plejada-gwiazd-lsni-na-konferencji-kfpp-opole-2026-doda-kukulska-wyszkoni/" : 0},
    {"https://www.kozaczek.pl/co-sie-wydarzylo-na-premierach-w-opolu-widzowie-nie-zostawili-suchej-nitki/" : 0},
    {"https://www.kozaczek.pl/tego-polskiego-miliardera-prawie-nikt-nie-zna-jest-kumplem-muska-i-moze-trafic-do-swiatowej-elity/" : 0},
    {"https://www.plotek.pl/styl-i-uroda/7,198204,32818603,w-19-miesiecy-zrzucila-50-kg-tak-dzis-wyglada-mama-na-obrotach.html": 0},
    {"https://www.plotek.pl/najnowsze-plotki/7,194210,32818670,doda-odsuwa-sie-od-sprawy-smierci-lukasza-litewki-zostalam.html" :0},
    {"https://www.gazeta.pl/0,0.html?foryou=enc02qhrmp2x6jeqbmut3egucoetwugqjlmdzagsriudrqmcz6udraocblescrjdksifjficroec2jembmst4ugzjmudrqmcblqd34gxjmqdzmg2ri&utm_campaign=amtp_pnHP_related&mp=promo&do_w=49&do_v=1859&do_st=RS&do_sid=2822&do_a=2822&e=ForYouHP3" : 0},
    {"https://www.domiporta.pl/informacje/a/miliardy-dla-samorzadow-na-nowe-mieszkania-i-remonty-7574#s=BoxOpImg8" : 0},
    {"https://www.pudelek.pl/asystent-matthew-perryego-uslyszal-wyrok-stal-sie-jego-pomocnikiem-i-dostawca-narkotykow-7290697002203424a" : 0},
    {"https://www.pudelek.pl/marta-wierzbicka-swietuje-pierwsza-rocznice-slubu-w-najlepszym-hotelu-w-warszawie-z-tej-okazji-pokazala-meza-zdjecia-7290770212596000g" : 0},
    {"https://www.plotek.pl/plotek/7,111483,32818964,splonal-grob-litewki-opiekun-cmentarza-ujawnia-nam-mowilem.html" : 0},
    {"https://www.plotek.pl/plotek/7,195992,32817383,kim-jest-corka-andrzeja-mleczki-w-swojej-dziedzinie-odnosi.html" : 0},
    {"https://www.gazeta.pl/0,0.html?foryou=enc02qhrmp2x6jeqbmut3egucoetwugqjlmdzagsriudrqmcz6udraocblescrjdksifjficroec2jemzmqd2egrjmudrqmcblmd3ahyjmqdzmg2ri&utm_campaign=amtp_pnHP_related&mp=promo&do_w=49&do_v=1859&do_st=RS&do_sid=2821&do_a=2821&e=ForYouHP5" : 0},
    {"https://www.pomponik.pl/plotki/news-anna-wyszkoni-zaluje-dzis-ze-postawila-na-kariere-solowa-pad,nId,23489054" : 0},
    {"https://www.pomponik.pl/plotki/news-allan-krupa-dlugo-czekal-na-ten-moment-teraz-oficjalnie-oglo,nId,23488976" : 0},
    {"https://www.pomponik.pl/plotki/news-zrobili-pazurze-awanture-wystarczylo-jedno-zdanie-przestrasz,nId,23489022" : 0},
    {"https://www.pomponik.pl/plotki/news-krol-karol-iii-nie-popisal-sie-na-oficjalnym-spotkaniu-wyraz,nId,23488866" : 0},
    {"https://www.pomponik.pl/gwiazdy-telewizji/news-program-kocham-cie-polsko-ledwo-wrocil-na-antene-a-tu-takie,nId,23488927" : 0},
    {"https://www.pomponik.pl/plotki/news-koniec-romansu-z-gdynskim-biznesmenem-marcela-leszczak-potwi,nId,23488877" :0},
    {"https://www.pomponik.pl/plotki/news-julia-wieniawa-oceniona-przez-ekspertke-wokalna-mozna-jeszcz,nId,23488781" : 0},
    {"https://www.pomponik.pl/gwiazdy-telewizji/news-taka-jest-prawda-o-relacjach-gawlinskiego-z-doroslymi-synami,nId,23488490" :0},
    {"https://www.plotek.pl/plotek/7,195990,31488755,bartosz-obuchowicz-bal-sie-najgorszego-przestal-dzwonic.html":0},
    {"https://www.plotek.pl/plotek/7,111483,32819434,zawadzka-zmaga-sie-z-kolanem-gospodyni-lekarz-wyjasnil-nam.html#e=RelRecImg6": 0},
    {"https://www.plotek.pl/celebryci/7,198201,32820083,lewandowska-z-kolejnym-sukcesem-tak-pisza-o-niej-hiszpanskie.html#do_w=589&do_v=1864&do_st=RS&do_sid=2824&do_a=2824&e=RelRecImg1&do_upid=1864_ti&do_utid=32820083&do_uvid=1779979166685" : 0},
    {"https://www.plotek.pl/celebryci/7,198205,32818193,uslyszal-ze-ma-raka-kiedy-jego-zona-byla-w-ciazy-slowa-henryka.html#e=RelRecImg6" :0},
    {"https://www.pomponik.pl/plotki/news-zaskakujace-doniesienia-zza-zamknietych-drzwi-domu-cichopek,nId,23489123" :0},
    {"https://wolnemedia.net/nowa-metoda-pozwala-odzyskiwac-lit-z-odpadow-solnych/":0},
    {"https://wolnemedia.net/palestynczycy-zostana-usunieci-we-wlasciwym-czasie/":0},
    {"https://wolnemedia.net/nowy-teleskop-zobaczy-100-razy-wiecej-niz-hubble/":0},
    {"https://wolnemedia.net/upadek-brytyjskiego-premiera-keira-starmera/":0},
    {"https://wolnemedia.net/kali-miec-krowa/":0},
    {"http://wolnemedia.net/kometa-zwolnila-a-pozniej-zaczela-obracac-sie-w-druga-strone/":0},
    {"https://wolnemedia.net/jak-general-hitlera-zostal-mozgiem-nato/":0},
    {"https://wolnemedia.net/teraz-nawet-uslugi-psychologiczne-staly-sie-kopalnia-danych/":0},
    {"https://wolnemedia.net/swiadomosc-klasowa-robotow/":0},

    # --- ETYKIETA 1 wiarygodne ---
    {"https://www.gov.pl/web/premier/odprawa-w-rzadowym-centrum-bezpieczenstwa-po-serii-prowokacji-i-falszywych-alarmow": 1},
    {"https://www.gov.pl/web/obrona-narodowa/wspolpraca-polski-i-kanady-oparta-na-bezpieczenstwie-inwestycjach-i-nowoczesnych-technologiach" : 1},
    {"https://www.gov.pl/web/mswia/ruszaja-zapisy-na-szkolenia-z-ochrony-ludnosci-i-obrony-cywilnej-partnerzy-mswia-przeszkola-ponad-100-tysiecy-polek-i-polakow" : 1},
    {"https://www.gov.pl/web/rodzina/wazne-wiesci-dla-rodzicow-nawet-60-dni-dodatkowego-zasilku-opiekunczego-na-chore-dziecko": 1},
    {"https://www.polsatnews.pl/wiadomosc/2026-05-27/papiez-leon-xiv-zwrocil-sie-do-polakow-podziekowal-kobietom/" : 1},
    {"https://lovekrakow.pl/tramwaj-do-mistrzejowic-z-nowa-data-miasto-podalo-termin-uruchomienia-linii" : 1},
    {"https://lovekrakow.pl/tragedia-w-uniszowej-90-letni-kierowca-smiertelnie-potracil-80-letnia-rowerzystke" : 1},
    {"https://lovekrakow.pl/tragiczna-smierc-posla-aleksander-miszalski-zegna-lukasza-litewke" : 1},
    {"https://zero.pl/news/koncert-taco-hemingwaya-na-narodowym-kontrowersje-wokol-ceny-wody" : 1},
    {"https://zero.pl/news/papiez-o-sztucznej-inteligencji-zagrozenia-etyka-i-przyszlosc-czlowieka" : 1},
    {"https://zero.pl/news/emerytury-artystow-z-budzetu-jak-rzad-sprawdzi-kto-nim-jest" : 1},
    {"https://zero.pl/news/system-kaucyjny-w-polsce-a-norwegia-dlaczego-nie-mozna-wrzucic-calego-worka-do-automatu" :1},
    {"https://zero.pl/news/pogoda-na-spacer-co-zrobic-z-pusta-butelka":1},
    {"https://zero.pl/news/mlody-norweg-mial-zostac-porzucony-w-indiach-wrocil-do-europy-i-opowiedzial-o-przezyciach" :1},
    {"https://zero.pl/news/imgw-oglosil-alerty-pogodowe-przymrozki-w-dziewieciu-wojewodztwach" :1},
    {"https://zero.pl/news/ambasada-usa-dementuje-slowa-szefowej-dyplomacji-ue-falszywe-doniesienia" :1},
    {"https://lovekrakow.pl/kapielisko-na-zakrzowku-szykuja-sie-zmiany" :1},
    {"https://lovekrakow.pl/to-koniec-jego-dzialalnosci-w-sieci-przynajmniej-na-kilka-lat":1},
    {"https://lovekrakow.pl/cracovia-zagra-z-legenda-europejskich-pucharow-sevilla-fc-na-jubileuszu-pasow":1},
    {"https://lovekrakow.pl/wykonawca-przejal-teren-miesiac-temu-prace-jeszcze-nie-ruszyly":1},
    {"https://lovekrakow.pl/utrudnienia-na-czyzynach-trwa-akcja-sluzb-po-zdarzeniu-drogowym":1},
    {"https://lovekrakow.pl/tesco-technology-rosnie-w-krakowie-zatrudni-nawet-150-osob" :1},
    {"https://lovekrakow.pl/dwa-lata-temu-otworzyli-sklep-w-bonarce-teraz-zostali-sponsorem-wisly" :1},
    {"https://lovekrakow.pl/biedronka-patrzy-na-krowodrze-gorke-bedzie-nowy-sklep" :1},
    {"https://www.gov.pl/web/cyfryzacja/12-milionow-mobywateli-cyfrowe-uslugi-zmieniaja-polske":1},
    {"https://www.gov.pl/web/piorin/udzial-przedstawiciela-giorin-w-otwarciu-polskiego-stoiska-narodowego-na-targach-apas-show-w-so-paulo":1},
    {"https://www.gov.pl/web/piorin/narada-kierownictwa-piorin-w-chomiazy-szlacheckiej":1},
    {"https://www.gov.pl/web/piorin/wreczenie-odznaczen-panstwowych-pracownikom-wiorin-w-rzeszowie":1},
    {"https://www.gov.pl/web/gddkia-szczecin/mozemy-budowac-odcinek-wjazdowy-s10-do-szczecina":1},
    {"https://zero.pl/news/warszawa-zwabil-i-porwal-mezczyzne-schowal-sie-pod-dzieciecym-lozkiem":1},
    {"https://zero.pl/news/jas-kapela-broni-rzadowego-programu-wsparcia-artystow-polacy-ich-nie-szanuja" :1},
    {"https://sii.pl/blog/adobe-summit-2026-agentic-ai-aem-i-nowa-era-customer-experience-orchestration/" :1},
    {"https://sii.pl/blog/dlaczego-wdrozenia-sap-s-4hana-wciaz-kuleja-mimo-ze-wszystko-bylo-przetestowane/":1},
    {"https://sii.pl/blog/proces-selekcji-kandydatow-oczami-rekrutera-i-asesora-technicznego/":1},
    {"https://sii.pl/blog/nie-tylko-select-ai-jako-funkcja-w-sql/":1},
    {"https://sii.pl/blog/odkryj-budzetowanie-w-ax-2012/":1},
    {"https://sii.pl/blog/visual-studio-express-for-desktop-stworzenie-projektu/":1},
    {"https://sii.pl/blog/finanse-w-microsoft-dynamics-ax/":1},
    {"https://sii.pl/blog/tworzenie-zewnetrznej-klasy-do-testow-soapui/":1},
    {"https://sii.pl/blog/planowanie-budzetu-w-ax-2012/" :1},
    {"https://sii.pl/blog/seo-czyli-jak-trafic-do-top10/":1}


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
    