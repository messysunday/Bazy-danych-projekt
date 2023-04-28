from PyQt5 import QtWidgets, QtCore, QtGui
from kupowanieBiletow import klasaKupno
from management import Ui_MainWindow


class klasaBilety(object):

    def openKupno(self):
        self.kupno = QtWidgets.QMainWindow()
        self.ui = klasaKupno()
        self.ui.initKupno(self.kupno)
        self.kupno.show()

    def initBilety(self, oknoBilety):
        oknoBilety.setWindowTitle("Bileciki")
        oknoBilety.setObjectName("oknoBilety")
        oknoBilety.setFixedSize(500, 500)
        oknoBilety.setWindowIcon(QtGui.QIcon("img/icon.png"))

        self.centralwidget = QtWidgets.QWidget(oknoBilety)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.photo.setPixmap(QtGui.QPixmap("img/bilety.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.tableWidget = QtWidgets.QTableWidget(oknoBilety)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 350, 350))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Nazwisko", "Typ", "Data i godzina"])
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.hide()

        self.kup = QtWidgets.QPushButton(self.centralwidget)
        self.kup.setGeometry(190, 450, 120, 40)
        self.kup.setObjectName("kup")
        self.kup.setText("Kup bilety")
        self.kup.clicked.connect(self.show_kup)

        # Sprawdzenie biletu dla danego nazwiska
        self.sprawdz = QtWidgets.QPushButton(self.centralwidget)
        self.sprawdz.setGeometry(10, 450, 120, 40)
        self.sprawdz.setObjectName("sprawdz")
        self.sprawdz.setText("Sprawdź bilety")
        self.sprawdz.clicked.connect(self.show_sprawdz)

        oknoBilety.setCentralWidget(self.centralwidget)

        self.wpiszNazwisko = QtWidgets.QLineEdit(oknoBilety)
        self.wpiszNazwisko.move(10, 400)
        self.wpiszNazwisko.resize(120, 40)
        self.wpiszNazwisko.setPlaceholderText("Wprowadź nazwisko")

    def show_kup(self):
        self.openKupno()

    def show_sprawdz(self):
        nazwisko = self.wpiszNazwisko.text()
        self.tableWidget.show()
        Ui_MainWindow.loadBilety(self, nazwisko)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    oknoBilety = QtWidgets.QMainWindow()
    ui = klasaBilety()
    ui.initBilety(oknoBilety)
    oknoBilety.show()
    sys.exit(app.exec_())
