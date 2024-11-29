from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalculatorWindow(object):
    def setupUi(self, CalculatorWindow):
        CalculatorWindow.setObjectName("CalculatorWindow")
        CalculatorWindow.resize(650, 574)
        CalculatorWindow.setStyleSheet("QWidget {\n"
"    background-color: #f0f0f0; /* Светлый фон */\n"
"    font-family: Arial, sans-serif; /* Шрифт */\n"
"    font-size: 14px; /* Размер шрифта */\n"
"    color: #333; /* Цвет текста */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(CalculatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_label = QtWidgets.QWidget(self.widget_4)
        self.widget_label.setObjectName("widget_label")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_label)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_label)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_label)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_label)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.widget_label)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_label)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget_label)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addWidget(self.widget_label)
        self.widget_edit = QtWidgets.QWidget(self.widget_4)
        self.widget_edit.setObjectName("widget_edit")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_edit)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.price = QtWidgets.QLineEdit(self.widget_edit)
        self.price.setMaximumSize(QtCore.QSize(16777215, 25))
        self.price.setStyleSheet("QLineEdit {\n"
"    background-color: #fff; /* Белый фон */\n"
"    border: 1px solid #ccc; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 5px; /* Отступы внутри поля */\n"
"}")
        self.price.setObjectName("price")
        self.verticalLayout_2.addWidget(self.price)
        self.first_deposit = QtWidgets.QLineEdit(self.widget_edit)
        self.first_deposit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.first_deposit.setStyleSheet("QLineEdit {\n"
"    background-color: #fff; /* Белый фон */\n"
"    border: 1px solid #ccc; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 5px; /* Отступы внутри поля */\n"
"}")
        self.first_deposit.setObjectName("first_deposit")
        self.verticalLayout_2.addWidget(self.first_deposit)
        self.label_loan_amount = QtWidgets.QLabel(self.widget_edit)
        self.label_loan_amount.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_loan_amount.setStyleSheet("QLabel {\n"
"    color: #555; /* Цвет текста лейблов */\n"
"    font-weight: bold; /* Жирный текст */\n"
"    padding: 5px; /* Отступы */\n"
"}")
        self.label_loan_amount.setObjectName("label_loan_amount")
        self.verticalLayout_2.addWidget(self.label_loan_amount)
        self.term = QtWidgets.QLineEdit(self.widget_edit)
        self.term.setMaximumSize(QtCore.QSize(16777215, 25))
        self.term.setStyleSheet("QLineEdit {\n"
"    background-color: #fff; /* Белый фон */\n"
"    border: 1px solid #ccc; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 5px; /* Отступы внутри поля */\n"
"}")
        self.term.setObjectName("term")
        self.verticalLayout_2.addWidget(self.term)
        self.interest_rate = QtWidgets.QLineEdit(self.widget_edit)
        self.interest_rate.setMaximumSize(QtCore.QSize(16777215, 25))
        self.interest_rate.setStyleSheet("QLineEdit {\n"
"    background-color: #fff; /* Белый фон */\n"
"    border: 1px solid #ccc; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 5px; /* Отступы внутри поля */\n"
"}")
        self.interest_rate.setObjectName("interest_rate")
        self.verticalLayout_2.addWidget(self.interest_rate)

        # Заменяем QListView на QListWidget
        self.list_type = QtWidgets.QListWidget(self.widget_edit)
        self.list_type.setMaximumSize(QtCore.QSize(16777215, 25))
        self.list_type.setStyleSheet("QListWidget {\n"
"    background-color: #fff; /* Белый фон */\n"
"    border: 1px solid #ccc; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"}")
        self.list_type.setObjectName("list_type")

        font = QtGui.QFont()
        font.setPointSize(22) 
        self.list_type.setFont(font)

        self.verticalLayout_2.addWidget(self.list_type)
        self.add_items_to_list_widget()

        self.horizontalLayout.addWidget(self.widget_edit)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_button = QtWidgets.QWidget(self.centralwidget)
        self.widget_button.setObjectName("widget_button")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_button)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CalculateButton = QtWidgets.QPushButton(self.widget_button)
        self.CalculateButton.setMinimumSize(QtCore.QSize(0, 0))
        self.CalculateButton.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(1)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Зеленый фон */\n"
"    color: white; /* Цвет текста */\n"
"    border: none; /* Без рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 10px; /* Отступы */\n"
"    font-size: 16px; /* Размер шрифта */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Цвет при наведении */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #66CC66; /* Цвет при нажатии */\n"
"}")
        self.CalculateButton.setObjectName("CalculateButton")
        self.horizontalLayout_4.addWidget(self.CalculateButton)
        self.verticalLayout_4.addWidget(self.widget_button)
        CalculatorWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(CalculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CalculatorWindow)
        self.first_deposit.setMaxLength(11)
        self.price.setMaxLength(12)
        self.term.setMaxLength(2)
        self.interest_rate.setMaxLength(2)

    def add_items_to_list_widget(self):
        font = QtGui.QFont()
        font.setPointSize(11)  # Увеличиваем размер шрифта

        # Добавляем элементы в QListWidget с установленным шрифтом
        item1 = QtWidgets.QListWidgetItem("Аннуитетные")
        item1.setFont(font)
        self.list_type.addItem(item1)

        item2 = QtWidgets.QListWidgetItem("Дифференцированные")
        item2.setFont(font)
        self.list_type.addItem(item2)

    def retranslateUi(self, CalculatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CalculatorWindow.setWindowTitle(_translate("CalculatorWindow", "Калькулятор ипотеки"))
        self.label.setText(_translate("CalculatorWindow", "Стоимость недвижимости"))
        self.label_2.setText(_translate("CalculatorWindow", "Первоначальный взнос"))
        self.label_3.setText(_translate("CalculatorWindow", "Сумма кредита"))
        self.label_5.setText(_translate("CalculatorWindow", "Срок кредита / лет"))
        self.label_6.setText(_translate("CalculatorWindow", "Годовая процентная ставка / %"))
        self.label_7.setText(_translate("CalculatorWindow", "Тип ежемесячных платежей"))
        self.label_loan_amount.setText(_translate("CalculatorWindow", "0"))
        self.CalculateButton.setText(_translate("CalculatorWindow", "Рассчитать"))