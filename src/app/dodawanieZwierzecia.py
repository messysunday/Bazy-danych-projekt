from PyQt5 import QtWidgets, QtCore, QtGui
from management import Ui_MainWindow


class klasaDodawanieZwierzecia(object):
    def messagebox(self):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec()

    def initDodawanieZwierzecia(self, oknoDodawanieZwierzecia):

        oknoDodawanieZwierzecia.setWindowTitle("Dodawanie nowych zwierzątek")
        oknoDodawanieZwierzecia.setObjectName("oknoDodawanieZwierzecia")
        oknoDodawanieZwierzecia.setFixedSize(500, 500)
        oknoDodawanieZwierzecia.setWindowIcon(QtGui.QIcon("img/icon.png"))

        self.centralwidget = QtWidgets.QWidget(oknoDodawanieZwierzecia)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.photo.setPixmap(QtGui.QPixmap("img/dodawanieZwierzecia.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.zatwierdz = QtWidgets.QPushButton(self.centralwidget)
        self.zatwierdz.setGeometry(190, 50, 151, 51)
        self.zatwierdz.setObjectName("dodajZwierze")
        self.zatwierdz.setText("Zatwierdź")
        self.zatwierdz.clicked.connect(self.show_zatwierdz)

        oknoDodawanieZwierzecia.setCentralWidget(self.centralwidget)

        self.wpiszImie = QtWidgets.QLineEdit(oknoDodawanieZwierzecia)
        self.wpiszImie.move(100, 150)
        self.wpiszImie.resize(130, 40)
        self.wpiszImie.setPlaceholderText("Wprowadź imię")

        self.wybierzSektor = QtWidgets.QComboBox(oknoDodawanieZwierzecia)
        self.wybierzSektor.move(300, 150)
        self.wybierzSektor.resize(130, 40)
        self.wybierzSektor.setPlaceholderText("Wybierz sektor")
        self.wybierzSektor.addItem("Afryka")
        self.wybierzSektor.addItem("Ameryka Polnocna")
        self.wybierzSektor.addItem("Ameryka Poludniowa")
        self.wybierzSektor.addItem("Europa")
        self.wybierzSektor.addItem("Australia")
        self.wybierzSektor.addItem("Antarktyda")
        self.wybierzSektor.addItem("Azja")

        self.wpiszZagrode = QtWidgets.QLineEdit(oknoDodawanieZwierzecia)
        self.wpiszZagrode.move(100, 200)
        self.wpiszZagrode.resize(130, 40)
        self.wpiszZagrode.setPlaceholderText("Wprowadź zagrodę")

        self.wpiszGatunek = QtWidgets.QLineEdit(oknoDodawanieZwierzecia)
        self.wpiszGatunek.move(300, 200)
        self.wpiszGatunek.resize(130, 40)
        self.wpiszGatunek.setPlaceholderText("Wprowadź gatunek")

    def show_zatwierdz(self):
        imie = self.wpiszImie.text()
        zagroda = self.wpiszZagrode.text()
        gatunek = self.wpiszGatunek.text()
        if self.wybierzSektor.currentText() == 'Afryka':
            sektor = "1"
        elif self.wybierzSektor.currentText() == 'Ameryka Polnocna':
            sektor = "2"
        elif self.wybierzSektor.currentText() == 'Ameryka Poludniowa':
            sektor = "3"
        elif self.wybierzSektor.currentText() == 'Antarktyda':
            sektor = "4"
        elif self.wybierzSektor.currentText() == 'Azja':
            sektor = "5"
        elif self.wybierzSektor.currentText() == 'Europa':
            sektor = "6"
        else:
            sektor = "7"
        Ui_MainWindow.dodaj_zwierze(self, imie, gatunek, sektor, zagroda)  # jeszcze nie działa


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    oknoDodawanieZwierzecia = QtWidgets.QMainWindow()
    ui = klasaDodawanieZwierzecia()
    ui.initDodawanieZwierzecia(oknoDodawanieZwierzecia)
    oknoDodawanieZwierzecia.show()
    sys.exit(app.exec_())
