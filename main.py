from core.calculator_logic import CalculateWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    calculator_window = CalculateWindow()
    calculator_window.show()  

    sys.exit(app.exec_())   