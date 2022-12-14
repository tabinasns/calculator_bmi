
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from timeit import default_timer as timer

start = timer()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 1000)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 650))
        MainWindow.setMaximumSize(QtCore.QSize(600, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/fb-icon-9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(128, -20, 560, 150)) 
        font = QtGui.QFont()
        font.setPointSize(13)
        self.judul.setFont(font)
        self.judul.setObjectName('judul')


        self.tinggi = QtWidgets.QLabel(self.centralwidget)
        self.tinggi.setGeometry(QtCore.QRect(50, 100, 91, 31)) 
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tinggi.setFont(font)
        self.tinggi.setObjectName("tinggi")
        MainWindow.setCentralWidget(self.centralwidget)


        self.massa = QtWidgets.QLabel(self.centralwidget)
        self.massa.setGeometry(QtCore.QRect(50, 170, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.massa.setFont(font)
        self.massa.setObjectName("massa")


        self.kolomTinggi = QtWidgets.QLineEdit(self.centralwidget)
        self.kolomTinggi.setGeometry(QtCore.QRect(495, 94, 65, 45))
        self.kolomTinggi.setObjectName("kolom_tinggi")
        self.kolomTinggi.textChanged.connect(self.value3)


        self.kolomMassa = QtWidgets.QLineEdit(self.centralwidget)
        self.kolomMassa.setGeometry(QtCore.QRect(495, 173, 65, 45)) 
        self.kolomMassa.setObjectName("kolom_massa")
        self.kolomMassa.textChanged.connect(self.value4)


        self.indikatorTinggi = QtWidgets.QSlider(self.centralwidget)
        self.indikatorTinggi.setGeometry(QtCore.QRect(143, 106, 330, 20)) 
        self.indikatorTinggi.setOrientation(QtCore.Qt.Horizontal)
        self.indikatorTinggi.setFocusPolicy(Qt.NoFocus)
        self.indikatorTinggi.setRange(0, 200) 
        self.indikatorTinggi.valueChanged.connect(self.valu)
        self.indikatorTinggi.setObjectName("indikator_tinggi")


        self.indikatorMassa = QtWidgets.QSlider(self.centralwidget)
        self.indikatorMassa.setGeometry(QtCore.QRect(143, 186, 330, 20))
        self.indikatorMassa.setOrientation(QtCore.Qt.Horizontal)
        self.indikatorMassa.setFocusPolicy(Qt.NoFocus)
        self.indikatorMassa.setRange(0, 200) 
        self.indikatorMassa.valueChanged.connect(self.valu2)
        self.indikatorMassa.setObjectName("indikator_massa")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 250, 100, 60)) 
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton.setObjectName("pushButton")


        self.outputBMI = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputBMI.setGeometry(QtCore.QRect(90, 390, 150, 30)) 
        self.outputBMI.setObjectName("output_BMI")


        self.outputAir = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputAir.setGeometry(QtCore.QRect(370, 390, 150, 30)) 
        self.outputAir.setObjectName("output_air")


        self.kategori = QtWidgets.QLabel(self.centralwidget)
        self.kategori.setGeometry(QtCore.QRect(157, 465, 560, 150)) 
        font = QtGui.QFont()
        font.setPointSize(11)
        self.kategori.setFont(font)
        self.kategori.setObjectName('kategori')


        self.hasilBMI = QtWidgets.QLabel(self.centralwidget)
        self.hasilBMI.setGeometry(QtCore.QRect(125, 290, 560, 150)) 
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hasilBMI.setFont(font)
        self.hasilBMI.setObjectName('hasilBMI')


        self.air = QtWidgets.QLabel(self.centralwidget)
        self.air.setGeometry(QtCore.QRect(385, 290, 560, 150)) 
        font = QtGui.QFont()
        font.setPointSize(11)
        self.air.setFont(font)
        self.air.setObjectName('air')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def valu(self):
        self.a = str(self.indikatorTinggi.value())
        self.kolomTinggi.setText(self.a)

    def valu2(self):
        self.k = str(self.indikatorMassa.value())
        self.kolomMassa.setText(self.k)


    def value3(self):
        self.j=str(self.kolomTinggi.text())
        self.indikatorTinggi.setSliderPosition(int(self.j))
        if int(self.j)==0:
            self.indikatorTinggi.setSliderPosition(int(1))


    def value4(self):
        self.j=str(self.kolomMassa.text())
        self.indikatorMassa.setSliderPosition(int(self.j))
        if int(self.j)==0:
            self.indikatorTinggi.setSliderPosition(int(1))


    def calculate(self):
        self.j = int(self.kolomMassa.text()) 
        self.k = int(self.kolomTinggi.text())
        self.bmi = self.j/((self.k/100)**2) 
        self.w = self.j*30 
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hitungBMI = '' + str(self.bmi)
        self.hitungAir = str(self.w) + ' ml/hari'
        print (self.hitungBMI)
        print (self.hitungAir)
        self.outputBMI.setPlainText(self.hitungBMI)
        self.outputAir.setPlainText(self.hitungAir)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KALKULATOR BMI DAN KEBUTUHAN AIR"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.judul.setText(_translate("MainWindow", "Kalkulator BMI dan Kebutuhan Air"))
        self.tinggi.setText(_translate("MainWindow", "Tinggi"))        
        self.kategori.setText(_translate("MainWindow", '           KATEGORI ANGKA BMI : \n\n    < 17.0 \t=  Sangat kurus \n  17.0 - 18.5 \t=  Kurus \n  18.5 - 25.0 \t=  Normal \n  25.0 - 27.0 \t=  Kelebihan berat badan \n    > 27.0 \t=  Obesitas'))
        self.massa.setText(_translate("MainWindow", "Massa"))
        self.hasilBMI.setText(_translate("MainWindow", "Hasil BMI :"))
        self.air.setText(_translate("MainWindow", "Kebutuhan Air :"))
        
end = timer()
print('waktu : ',end - start)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
