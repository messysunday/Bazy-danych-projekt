from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_MainWindow(object):

    # Zapełnianie tabeli
    def fillTable(self, wynik):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(wynik):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidget.resizeColumnsToContents()

    # Połączenie z BD
    def connectDB(self):
        conn = pymysql.connect(host='sql7.freemysqlhosting.net',
                               user='sql7343753',
                               password='JGWVXubSX1',
                               db='sql7343753',
                               charset='latin1')
        print("Połączono z bazą danych.")
        return conn

    # Wczytanie wszystkich zwierząt
    def loadZwierzeta(self):
        # połączenie z BD:
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        # polecenie i wykonanie
        query = "SELECT id, sektor, zagroda, imie, gatunek from zwierze order by gatunek"
        cur.execute(query)
        result = cur.fetchall()

        # Wyświetlanie
        Ui_MainWindow.fillTable(self, result)

        # Rozłączenie z BD
        conn.close()

    # Wczytanie wszystkich pracowników
    def loadPracownicy(self):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        query = "SELECT * from pracownicy"
        cur.execute(query)
        result = cur.fetchall()

        Ui_MainWindow.fillTable(self, result)

        conn.close()

    # Wczytanie bieltów po nazwisku
    def loadBilety(self, nazwisko):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        query = "SELECT nazwisko, typ, godzina from bilety WHERE nazwisko = %s order by godzina"
        cur.execute(query, nazwisko)
        result = cur.fetchall()

        Ui_MainWindow.fillTable(self, result)

        conn.close()

    # Wyświetlenie danych pracownika
    def wyszukaj_pracownika(self, nazwisko):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        query = "select id, imie, nazwisko, email, nr_tel from pracownicy where nazwisko = %s;"
        cur.execute(query, nazwisko)
        result = cur.fetchall()

        Ui_MainWindow.fillTable(self, result)

        conn.close()

    # Sprawdzenie dyżurów pracownika
    def sprawdz_dyzury(self, nazwisko):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        query = "select dyzury.id, dyzury.sektor, dyzury.czynnosc, dyzury.godzina_rozpoczecia," \
                " dyzury.godzina_zakonczenia from dyzury inner join pracownicy on pracownicy.id = dyzury.pracownik" \
                " where pracownicy.nazwisko = %s order by dyzury.czynnosc;"

        cur.execute(query, nazwisko)
        result = cur.fetchall()

        # Wyświetlanie (inny widget)
        self.tableWidgetDyzury.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetDyzury.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetDyzury.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidgetDyzury.resizeColumnsToContents()

        conn.close()

    # Kupowanie biletów
    def kup_bilet(self, nazwisko, data, typ):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        if typ == 'ulgowy':
            cena = 10
        elif typ == 'normalny':
            cena = 20
        else:
            cena = 50

        query = "insert into bilety (cena, typ, godzina, nazwisko) values (%s, %s, %s, %s);"
        cur.execute(query, (cena, typ, data, nazwisko))
        conn.commit()
        conn.close()

    # Wyszukiwanie zwierząt po gatunku
    def wyszukaj_zwierze(self, gatunek):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        # polecenie i wykonanie
        query = "select id, sektor, zagroda, imie, gatunek from zwierze where gatunek = %s order by imie;"
        cur.execute(query, gatunek)
        result = cur.fetchall()

        # Wczytanie do tabeli (wyświetlanie)
        self.tableWidgetZwierzeta.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetZwierzeta.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetZwierzeta.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidgetZwierzeta.resizeColumnsToContents()

        conn.close()

    # Dodawanie zwierząt
    def dodaj_zwierze(self, imie, gatunek, sektor, zagroda):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        query = "insert into zwierze (sektor, zagroda, imie, gatunek) values (%s, %s, %s, %s);"
        cur.execute(query, (sektor, zagroda, imie, gatunek))
        conn.commit()
        print("Dodano zwierzę: Imię: %s Gatunek: %s Sektor: %s Zagroda: %s", imie, gatunek, sektor, zagroda)
        conn.close()

    # Usuwanie zwierząt po ID
    def usun_zwierze(self, id):
        conn = Ui_MainWindow.connectDB(self)
        cur = conn.cursor()

        query = "delete from zwierze where id = %s"
        cur.execute(query, id)
        print("Usunięto zwierze: ", id)

        conn.commit()
        conn.close()
