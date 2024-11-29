from window_py.CalculateWindow import Ui_CalculatorWindow
from window_py.output import Ui_WindowOutput
from PyQt5 import QtWidgets

class WindowLogs(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowOutput()
        self.ui.setupUi(self)

class CalculateWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CalculatorWindow()
        self.ui.setupUi(self)
        self.output_window = WindowLogs()
        self.start_signal_text()

    def calculate_sum_credit(self):
        """Вычисляет сумму кредита на основе цены и первоначального взноса."""
        price_text = self.ui.price.text()
        first_deposit_text = self.ui.first_deposit.text()

        if price_text and first_deposit_text:
            try:
                price = int(price_text)
                first_deposit = int(first_deposit_text)
                credit = price - first_deposit
                self.ui.label_loan_amount.setText(str(credit))
            except ValueError:
                self.ui.label_loan_amount.setText('Введите целое число')
        elif price_text:
            try:
                price = int(price_text)
                self.ui.label_loan_amount.setText(str(price))
            except ValueError:
                self.ui.label_loan_amount.setText('Введите целое число')
        else:
            self.ui.label_loan_amount.setText('0')

    def start_signal_text(self):
        """Подключает сигналы для изменения текста."""
        self.ui.price.textChanged.connect(self.calculate_sum_credit)
        self.ui.first_deposit.textChanged.connect(self.calculate_sum_credit)
        self.ui.CalculateButton.clicked.connect(self.calculate_payments)

    def calculate_payments(self):
        """Вычисляет платежи в зависимости от типа платежа."""
        type_payment = self.ui.list_type.currentItem()
        type_payment = type_payment.text() if type_payment else 'Аннуитетные'

        try:
            credit = int(self.ui.label_loan_amount.text())
            annual_interest_rate = int(self.ui.interest_rate.text()) / 100  
            mortgage_interest_rate = annual_interest_rate / 12
            all_pay = int(self.ui.term.text()) * 12

            if type_payment == 'Аннуитетные':
                monthly_payment = (credit * mortgage_interest_rate) / (1 - (1 + mortgage_interest_rate) ** (-all_pay))
                total_payment = monthly_payment * all_pay
                self.output_window.ui.textBrowser.clear()
                self.output_window.ui.textBrowser.append(f'В месяц по: {monthly_payment:.2f}р.\nОбщий платеж за весь срок: {total_payment:.2f} р.')
            elif type_payment == 'Дифференцированные':
                main_payment = credit / all_pay
                total_payments = []
                self.output_window.ui.textBrowser.clear()
                for i in range(1, all_pay + 1):
                    remaining_debt = credit - (i - 1) * main_payment
                    interest_paid = remaining_debt * mortgage_interest_rate
                    monthly_payment = main_payment + interest_paid
                    total_payments.append(monthly_payment)
                    self.output_window.ui.textBrowser.append(f'Платеж за месяц {i}: {monthly_payment:.2f}р.')
                self.output_window.ui.textBrowser.append(f'Общий платеж за весь срок: {sum(total_payments):.2f}р.')
            self.output_window.show()

        except Exception as ex:
            self.output_window.ui.textBrowser.clear()
            self.output_window.ui.textBrowser.append(str(ex))
            self.output_window.show()
