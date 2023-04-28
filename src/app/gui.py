from PyQt5 import QtCore, QtGui, QtWidgets
from Zwierzeta import klasaZwierzeta
from Bilety import klasaBilety
from Pracownicy import klasaPracownicy
from About import klasaAbout


class Ui_MainWindow(object):

    # ----dołączenie okienek----#
    def openZwierzeta(self):
        self.zwierzeta = QtWidgets.QMainWindow()
        self.ui = klasaZwierzeta()
        self.ui.initZwierzeta(self.zwierzeta)
        self.zwierzeta.show()

    def openBilety(self):
        self.bilety = QtWidgets.QMainWindow()
        self.ui = klasaBilety()
        self.ui.initBilety(self.bilety)
        self.bilety.show()

    def openPracownicy(self):
        self.pracownicy = QtWidgets.QMainWindow()
        self.ui = klasaPracownicy()
        self.ui.initPracownicy(self.pracownicy)
        self.pracownicy.show()

    def openAbout(self):
        self.about = QtWidgets.QMainWindow()
        self.ui = klasaAbout()
        self.ui.initAbout(self.about)
        self.about.show()

    # -------------------------------------------------#

    def setupUi(self, MainWindow):
        # Nazwa okna
        MainWindow.setObjectName("MainWindow")
        # Tytuł okna
        MainWindow.setWindowTitle("Nasze Wspólne Zoo")
        # Ikona programu
        MainWindow.setWindowIcon(QtGui.QIcon("img/icon.png"))
        # Rozmiar bez możliwości rozciągania
        MainWindow.setFixedSize(500, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label jako zdjęcie w tle
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("img/background.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        # Guzik1 "zwierzetaWindow.py"
        self.zwierzeta = QtWidgets.QPushButton(self.centralwidget)
        self.zwierzeta.setGeometry(QtCore.QRect(30, 30, 121, 51))
        self.zwierzeta.setObjectName("Zwierzęta")
        self.zwierzeta.clicked.connect(self.show_zwierzeta)

        # Guzik2 "biletyWindow.py"
        self.bilety = QtWidgets.QPushButton(self.centralwidget)
        self.bilety.setGeometry(QtCore.QRect(30, 100, 121, 51))
        self.bilety.setObjectName("Bilety")
        self.bilety.clicked.connect(self.show_bilety)

        # Guzik3 "pracownicyWindow.py"
        self.pracownicy = QtWidgets.QPushButton(self.centralwidget)
        self.pracownicy.setGeometry(QtCore.QRect(30, 170, 121, 51))
        self.pracownicy.setObjectName("Pracownicy")
        self.pracownicy.clicked.connect(self.show_pracownicy)

        # Guzik4 "oProgramie.py"
        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(30, 400, 121, 51))
        self.about.setObjectName("O Programie")
        self.about.clicked.connect(self.show_oprogramie)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.zwierzeta.setText(_translate("MainWindow", "Zwierzęta"))
        self.bilety.setText(_translate("MainWindow", "Bilety"))
        self.pracownicy.setText(_translate("MainWindow", "Pracownicy"))
        self.about.setText(_translate("MainWindow", "O Programie"))

    def show_zwierzeta(self):
        self.openZwierzeta()

    def show_bilety(self):
        self.openBilety()

    def show_pracownicy(self):
        self.openPracownicy()

    def show_oprogramie(self):
        self.openAbout()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
