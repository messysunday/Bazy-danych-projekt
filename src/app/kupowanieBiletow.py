from PyQt5 import QtWidgets, QtCore, QtGui
from management import Ui_MainWindow


class klasaKupno(object):

    def initKupno(self, oknoKupno):
        oknoKupno.setWindowTitle("Proszę przygotować bilety do kontroli")
        oknoKupno.setObjectName("oknoKupno")
        oknoKupno.setFixedSize(450, 300)
        oknoKupno.setWindowIcon(QtGui.QIcon("img/icon.png"))

        self.centralwidget = QtWidgets.QWidget(oknoKupno)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 450, 300))
        self.photo.setPixmap(QtGui.QPixmap("img/bilety.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.zatwierdz = QtWidgets.QPushButton(self.centralwidget)
        self.zatwierdz.setGeometry(200, 80, 151, 51)
        self.zatwierdz.setObjectName("kup")
        self.zatwierdz.setText("Kup bilet")
        self.zatwierdz.clicked.connect(self.show_zatwierdz)

        oknoKupno.setCentralWidget(self.centralwidget)

        self.wpiszNazwisko = QtWidgets.QLineEdit(oknoKupno)
        self.wpiszNazwisko.move(10, 180)
        self.wpiszNazwisko.resize(130, 40)
        self.wpiszNazwisko.setPlaceholderText("Wprowadź nazwisko")

        self.wybierzTyp = QtWidgets.QComboBox(oknoKupno)
        self.wybierzTyp.move(150, 180)
        self.wybierzTyp.resize(130, 40)
        self.wybierzTyp.setPlaceholderText("Wybierz typ biletu")
        self.wybierzTyp.addItem("ulgowy")
        self.wybierzTyp.addItem("normalny")
        self.wybierzTyp.addItem("premium")

        self.wpiszDate = QtWidgets.QLineEdit(oknoKupno)
        self.wpiszDate.move(300, 180)
        self.wpiszDate.resize(130, 40)
        self.wpiszDate.setPlaceholderText('YYYY-MM-DD HH:MM:SS')

    def show_zatwierdz(self):
        nazwisko = self.wpiszNazwisko.text()
        data = self.wpiszDate.text()
        typ = self.wybierzTyp.currentText()
        Ui_MainWindow.kup_bilet(self, nazwisko, data, typ)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    oknoKupno = QtWidgets.QMainWindow()
    ui = klasaKupno()
    ui.initKupno(oknoKupno)
    oknoKupno.show()
    sys.exit(app.exec_())
