from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.value = 0.0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 90, 391, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.number = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.number.setStyleSheet("font: 8pt \"MS Sans Serif\";")
        self.number.setSmallDecimalPoint(False)
        self.number.setDigitCount(3)
        self.number.setProperty("value", self.value)
        self.number.setObjectName("number")
        self.horizontalLayout.addWidget(self.number)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.increment = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.increment.setObjectName("increment")
        self.increment.clicked.connect(self.increment_value)  # Connect the 'clicked' signal to the 'increment_value' method
        self.verticalLayout.addWidget(self.increment)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def increment_value(self):  # Define the 'increment_value' method
        self.value += 1.0
        self.number.display(self.value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PyQt5 jug jug ah ah", "PyQt5 jug jug ah ah"))
        self.increment.setText(_translate("MainWindow", "Increment"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
