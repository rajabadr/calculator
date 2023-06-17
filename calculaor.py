import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculatrice')
        self.resize(300, 400)
        self.layout = QVBoxLayout()
        self.current_value = ""
        self.result = 0
        self.operator = ""
        
        self.create_ui()
        
    def create_ui(self):
        self.label = QLabel("0")
        self.label.setStyleSheet("font-size: 24px; padding: 10px;")
        self.layout.addWidget(self.label)
        
        grid = QGridLayout()
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]
        
        positions = [(i, j) for i in range(4) for j in range(4)]
        
        for position, button in zip(positions, buttons):
            if button == "=":
                btn = QPushButton(button)
                btn.setStyleSheet("background-color: #ff9933; font-size: 18px; padding: 10px;")
                btn.clicked.connect(self.calculate_result)
            elif button == "C":
                btn = QPushButton(button)
                btn.setStyleSheet("background-color: #ff6666; font-size: 18px; padding: 10px;")
                btn.clicked.connect(self.clear)
            else:
                btn = QPushButton(button)
                btn.setStyleSheet("font-size: 18px; padding: 10px;")
                btn.clicked.connect(lambda _, b=button: self.append_value(b))
            
            grid.addWidget(btn, *position)
        
        self.layout.addLayout(grid)
        self.setLayout(self.layout)
        
    def append_value(self, value):
        self.current_value += value
        self.label.setText(self.current_value)
        
    def calculate_result(self):
        try:
            self.result = eval(self.current_value)
            self.label.setText(str(self.result))
            self.current_value = ""
        except ZeroDivisionError:
            self.label.setText("Error")
        except Exception:
            self.label.setText("Invalid Expression")
            
    def clear(self):
        self.current_value = ""
        self.result = 0
        self.label.setText("0")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
