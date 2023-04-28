# Temat projektu
####Ogród Zoologiczny - Temat nr 20

| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :---------------------- | :-----: | :------: | :-----: | :---: | :------------: |
|Radosław Jurczak         | WIMiIP  | IS       |   4     | ĆP02     | 2019/2020      |
| Emil Kobyłecki         | WIMiIP  | IS       |   4     | ĆP02     | 2019/2020      |

## Projekt bazy danych
* Opis projektu:
Projekt przedstawia bazę SQL stworzoną dla zoo podzielonego na sektory (po jednym dla każdego z kontynentów), które z kolei są podzielone na zagrody.
W każdej zagrodzie umieszczeni są mieszkańcy tego samego gatunku. W bazie znajdują się też pracownicy zoo oraz przydzielone im dyżury.
Dodatkowo jest możliwość zapisywania biletów. Baza obsługiwana jest za pomocą aplikacji okienkowej, która dla poszczególnych kategorii aktywności
(obsługa pracowników, zwierząt lub biletów) posiada osobne okna. Dodatkowo aplikacja posiada stronę informacyjną.

Schemat bazy danych: 
![alt text](https://github.com/phajder-databases/db2020-project-ogrod-zoologiczny-20/blob/master/resources/Schemat%20v.2.png?raw=true)
* Dodatkowo, kilka przykładowych zapytań z grupy DDL (CREATE, DROP, ALTER, TRUNCATE, RENAME)

## Implementacja zapytań SQL
* Funkcjonalności SQL:
1. Wyświetlanie wszystkich zwierząt w zoo:
	SELECT * from zwierze order by gatunek
2. Wyszukiwanie zwierząt po gatunku:
	select id, sektor, zagroda, imie, gatunek from zwierze where gatunek = %s order by gatunek;
3. Dodawanie zwierząt do bazy danych:
	insert into zwierze (sektor, zagroda, imie, gatunek) values ({}, {}, {}, {});
4. Usuwanie zwierząt z bazy danych po ID:
	delete from zwierze where id = %s;
5. Wyświetlanie wszystkich pracowników:
	SELECT * from pracownicy order by nazwisko
6. Wyszukiwanie pracowników po nazwisku:
	select id, imie, nazwisko, email, nr_tel from pracownicy where nazwisko = %s;
7. Sprawdzanie dyżurów pracownika:
	select dyzury.id, dyzury.sektor, dyzury.czynnosc, dyzury.godzina_rozpoczecia," \
        " dyzury.godzina_zakonczenia from dyzury inner join pracownicy on pracownicy.id = dyzury.pracownik" \
        " where pracownicy.nazwisko = %s order by czynnosc;
8. Wyświetlanie biletów kupionych na konkretne nazwisko:
	SELECT nazwisko, typ, godzina from bilety WHERE nazwisko = %s order by godzina
9. Dodawanie nowego biletu do bazy danych:
	insert into bilety (cena, typ, godzina, nazwisko) values ({}, {}, {}, {});

## Aplikacja
Aplikacja wykorzystuje bibliotekę pymysql w celu komunikacji z bazą danych oraz bibliotekę PyQt5 w celu utworzenia okienkowego interfejsu.
Wszystkie zapytania SQL skupione są w pliku management.py, który obsługuje połączenie z bazą oraz przesyłanie poleceń.
Natomiast poszczególne okienka skoncetrowane wokół konkretnej tematyki (na przykład zwierząt) znajdują się w odpowiednich osobnych plikach .py.
Głównym założeniem aplikacji jest dostarczenie użytkownikowi możliwości przeprowadzania podstawowych operacji na bazie danych bez znajomości zapytań
oraz bez konieczności przedzierania się przez niekoniecznie przejrzysty interfejs konsolowy.

## Dodatkowe uwagi
* nk