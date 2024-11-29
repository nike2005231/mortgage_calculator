from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowOutput(object):
    def setupUi(self, WindowOutput):
        WindowOutput.setObjectName("WindowOutput")
        WindowOutput.resize(545, 356)
        WindowOutput.setStyleSheet("QWidget {\n"
"    background-color: #f0f0f0; /* Светлый фон */\n"
"    font-family: Arial, sans-serif; /* Шрифт */\n"
"    font-size: 14px; /* Размер шрифта */\n"
"    color: #333; /* Цвет текста */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(WindowOutput)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    background-color: #fff; /* Белый фон */\n"
"    border: 1px solid #ccc; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 5px; /* Отступы внутри поля */\n"
"    color: #000; /* Цвет текста */\n"
"    font-family: Arial; /* Шрифт текста */\n"
"    font-size: 12pt; /* Размер шрифта */\n"
"}\n"
"\n"
"QTextBrowser::text {\n"
"    color: #333; /* Цвет текста внутри */\n"
"    font-weight: normal; /* Нормальный вес шрифта */\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        WindowOutput.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowOutput)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 22))
        self.menubar.setObjectName("menubar")
        WindowOutput.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowOutput)
        self.statusbar.setObjectName("statusbar")
        WindowOutput.setStatusBar(self.statusbar)

        self.retranslateUi(WindowOutput)
        QtCore.QMetaObject.connectSlotsByName(WindowOutput)

    def retranslateUi(self, WindowOutput):
        _translate = QtCore.QCoreApplication.translate
        WindowOutput.setWindowTitle(_translate("WindowOutput", "Вывод"))
        self.textBrowser.setHtml(_translate("WindowOutput", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">asddasdasas sd</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">lkjhgfds</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">hgfdsdfghjkl</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:16pt;\"><br /></p></body></html>"))
