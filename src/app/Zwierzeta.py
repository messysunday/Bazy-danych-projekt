from PyQt5 import QtWidgets, QtCore, QtGui
from management import Ui_MainWindow
from dodawanieZwierzecia import klasaDodawanieZwierzecia


class klasaZwierzeta(object):

    def initZwierzeta(self, oknoZwierzeta):
        oknoZwierzeta.setWindowTitle("Nasze Zwierzątka")
        oknoZwierzeta.setObjectName("oknoZwierzeta")
        oknoZwierzeta.setFixedSize(500, 500)
        oknoZwierzeta.setWindowIcon(QtGui.QIcon("img/icon.png"))

        self.centralwidget = QtWidgets.QWidget(oknoZwierzeta)
        self.centralwidget.setObjectName("centralwidget")

        # Zdjecie w tle
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.photo.setPixmap(QtGui.QPixmap("img/fatcat.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        # Tabela do wyświetlania zwierząt
        self.tableWidget = QtWidgets.QTableWidget(oknoZwierzeta)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 480, 380))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Sektor", "Zagroda", "Imię", "Gatunek"])
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.hide()

        # Guzik1 - wyświetl wszystkie zwierzęta
        self.wszystkie = QtWidgets.QPushButton(self.centralwidget)
        self.wszystkie.setGeometry(330, 390, 150, 50)
        self.wszystkie.setObjectName("wszystkie")
        self.wszystkie.setText("Pokaż wszystkie zwierzęta")
        self.wszystkie.clicked.connect(self.show_wszystkie)

        # Guzik2 - wyszukiwanie
        self.wyszukajZwierze = QtWidgets.QPushButton(self.centralwidget)
        self.wyszukajZwierze.setGeometry(170, 390, 150, 50)
        self.wyszukajZwierze.setObjectName("wyszukajZwierze")
        self.wyszukajZwierze.setText("Znajdź zwierzaka")
        self.wyszukajZwierze.clicked.connect(self.show_wyszukajZwierze)

        # Guzik3 - dodawanie
        self.dodajZwierze = QtWidgets.QPushButton(self.centralwidget)
        self.dodajZwierze.setGeometry(330, 440, 150, 50)
        self.dodajZwierze.setObjectName("wyszukajZwierze")
        self.dodajZwierze.setText("Dodaj zwierzaka")
        self.dodajZwierze.clicked.connect(self.show_dodajZwierze)

        # Guzik4 - usuwanie
        self.usunZwierze = QtWidgets.QPushButton(self.centralwidget)
        self.usunZwierze.setGeometry(170, 440, 150, 50)
        self.usunZwierze.setObjectName("usunZwierze")
        self.usunZwierze.setText("Usuń zwierzaka")
        self.usunZwierze.clicked.connect(self.usuwanieZwierzecia)

        oknoZwierzeta.setCentralWidget(self.centralwidget)

        # Textbox do wyszukiwania
        self.wpiszGatunek = QtWidgets.QLineEdit(oknoZwierzeta)
        self.wpiszGatunek.move(20, 393)
        self.wpiszGatunek.resize(145, 45)
        self.wpiszGatunek.setPlaceholderText("Wprowadź gatunek")

        # Textbox do usuwania
        self.wpiszID = QtWidgets.QLineEdit(oknoZwierzeta)
        self.wpiszID.move(20, 443)
        self.wpiszID.resize(145, 45)
        self.wpiszID.setPlaceholderText("Wprowadź ID")

        # Tabela do wyświetlania zwierząt
        self.tableWidgetZwierzeta = QtWidgets.QTableWidget(oknoZwierzeta)
        self.tableWidgetZwierzeta.setGeometry(QtCore.QRect(10, 0, 480, 380))
        self.tableWidgetZwierzeta.setObjectName("tableWidget")
        self.tableWidgetZwierzeta.setRowCount(20)
        self.tableWidgetZwierzeta.setColumnCount(5)
        self.tableWidgetZwierzeta.setHorizontalHeaderLabels(
            ["ID", "Sektor", "Zagroda", "Imie", "Gatunek"])  # nowa tabela bo są inne kolumny, da sie to jakoś obejść?
        self.tableWidgetZwierzeta.verticalHeader().hide()
        self.tableWidgetZwierzeta.hide()

    def dodawanieZwierzecia(self):
        self.oknoDodawanieZwierzecia = QtWidgets.QMainWindow()
        self.ui = klasaDodawanieZwierzecia()
        self.ui.initDodawanieZwierzecia(self.oknoDodawanieZwierzecia)
        self.oknoDodawanieZwierzecia.show()

    def usuwanieZwierzecia(self):
        id = self.wpiszID.text()
        Ui_MainWindow.usun_zwierze(self, id)

    def show_wszystkie(self):
        self.tableWidgetZwierzeta.hide()
        self.tableWidget.show()
        Ui_MainWindow.loadZwierzeta(self)

    def show_wyszukajZwierze(self):
        gatunek = self.wpiszGatunek.text()
        self.tableWidget.hide()
        self.tableWidgetZwierzeta.show()
        Ui_MainWindow.wyszukaj_zwierze(self, gatunek)

    def show_dodajZwierze(self):
        self.dodawanieZwierzecia()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    oknoZwierzeta = QtWidgets.QMainWindow()
    ui = klasaZwierzeta()
    ui.initZwierzeta(oknoZwierzeta)
    oknoZwierzeta.show()
    sys.exit(app.exec_())
