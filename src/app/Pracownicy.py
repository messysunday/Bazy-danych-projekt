from PyQt5 import QtWidgets, QtCore, QtGui
from management import Ui_MainWindow


class klasaPracownicy(object):

    def initPracownicy(self, oknoPracownicy):
        oknoPracownicy.setWindowTitle("Pracownicy")
        oknoPracownicy.setObjectName("oknoPracownicy")
        oknoPracownicy.setFixedSize(500, 500)
        oknoPracownicy.setWindowIcon(QtGui.QIcon("img/icon.png"))

        self.centralwidget = QtWidgets.QWidget(oknoPracownicy)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.photo.setPixmap(QtGui.QPixmap("img/office2.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        # TABELA DO WYŚWIETLANIA DANYCH PRACOWNIKOW:
        self.tableWidget = QtWidgets.QTableWidget(oknoPracownicy)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 460, 390))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Imię", "Nazwisko", "E-mail",
                                                    "Numer telefonu"])  # import z BD = za dużo zabawy, i tak vertical ukryte
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.hide()  # bo otwiera się na kliknięciu guzika

        # TABELA DO WYŚWIETLANIA DYZUROW:
        self.tableWidgetDyzury = QtWidgets.QTableWidget(oknoPracownicy)
        self.tableWidgetDyzury.setGeometry(QtCore.QRect(10, 0, 460, 390))
        self.tableWidgetDyzury.setObjectName("tableWidget")
        self.tableWidgetDyzury.setRowCount(20)
        self.tableWidgetDyzury.setColumnCount(5)
        self.tableWidgetDyzury.setHorizontalHeaderLabels(
            ["ID", "Sektor", "Czynność", "Start", "Koniec"])  # nowa tabela bo są inne kolumny, da sie to jakoś obejść?
        self.tableWidgetDyzury.verticalHeader().hide()
        self.tableWidgetDyzury.hide()

        self.dyzury = QtWidgets.QPushButton(self.centralwidget)
        self.dyzury.setGeometry(10, 440, 150, 50)
        self.dyzury.setObjectName("dyzury")
        self.dyzury.setText("Sprawdź dyżury")
        self.dyzury.clicked.connect(self.show_dyzury)

        self.danePracownika = QtWidgets.QPushButton(self.centralwidget)
        self.danePracownika.setGeometry(170, 440, 150, 50)
        self.danePracownika.setObjectName("danePracownika")
        self.danePracownika.setText("Sprawdź dane")
        self.danePracownika.clicked.connect(self.show_danePracownika)

        self.wszyscyPracownicy = QtWidgets.QPushButton(self.centralwidget)
        self.wszyscyPracownicy.setGeometry(330, 440, 150, 50)
        self.wszyscyPracownicy.setObjectName("wszyscyPracownicy")
        self.wszyscyPracownicy.setText("Wyświetl wszystkich")
        self.wszyscyPracownicy.clicked.connect(self.show_wszyscyPracownicy)

        oknoPracownicy.setCentralWidget(self.centralwidget)

        self.wpiszNazwisko = QtWidgets.QLineEdit(oknoPracownicy)
        self.wpiszNazwisko.move(10, 400)
        self.wpiszNazwisko.resize(150, 40)
        self.wpiszNazwisko.setPlaceholderText("wprowadź nazwisko")

    def show_dyzury(self):
        nazwisko = self.wpiszNazwisko.text()
        self.tableWidget.hide()
        self.tableWidgetDyzury.show()
        Ui_MainWindow.sprawdz_dyzury(self, nazwisko)

    def show_danePracownika(self):
        nazwisko = self.wpiszNazwisko.text()
        self.tableWidgetDyzury.hide()
        self.tableWidget.show()
        Ui_MainWindow.wyszukaj_pracownika(self, nazwisko)

    def show_wszyscyPracownicy(self):
        self.tableWidgetDyzury.hide()
        self.tableWidget.show()
        Ui_MainWindow.loadPracownicy(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    oknoPracownicy = QtWidgets.QMainWindow()
    ui = klasaPracownicy()
    ui.initPracownicy(oknoPracownicy)
    oknoPracownicy.show()
    sys.exit(app.exec_())
