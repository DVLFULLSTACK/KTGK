import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QWidget
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Calculator")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #2c2c2c;")
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(80)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                font-size: 36px;
                border: 2px solid #2c2c2c;
                padding-right: 10px;
            }
        """)

        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()

        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '+': (3, 2), '=': (3, 3),
            'AC': (4, 0), '(': (4, 1), ')': (4, 2), '%': (4, 3)
        }

        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 80)
            self.buttons[btnText].setStyleSheet("""
                QPushButton {
                    background-color: #3e3e3e;
                    color: white;
                    font-size: 24px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #4e4e4e;
                }
                QPushButton:pressed {
                    background-color: #5e5e5e;
                }
            """)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText("")

class CalculatorCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == "error":
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'AC'}:
                btn.clicked.connect(lambda _, exp=btnText: self._buildExpression(exp))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.buttons['AC'].clicked.connect(self._view.clearDisplay)

def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = "error"

    return result

def main():
    app = QApplication(sys.argv)

    view = Calculator()
    view.show()

    model = evaluateExpression
    CalculatorCtrl(model=model, view=view)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
