from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from math import factorial


# класс, реализующий окно калькулятора:
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # установка размеров окна:
        self.setGeometry(200, 200, 390, 400)
        # название окна:
        self.setWindowTitle("Калькулятор.")
        self.UiComponents()
        # отображение виджетов:
        self.show()

        # методы для виджетов калькулятора:

    def UiComponents(self):
        self.label = QLabel(self)
        # настройка размеров:
        self.label.setGeometry(5, 5, 375, 85)
        self.label.setWordWrap(True)
        # настройка пространства для ввода, толщины и цвета рамки пространства для ввода:
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 2 solid black;"
                                 "background : gray;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)
        # выбор шрифта, настройка его размера:
        self.label.setFont(QFont('Arial', 20))

        # добавление функциональных кнопок калькулятора:
        # создание кнопки "0":
        button0 = QPushButton("0", self)
        button0.setGeometry(5, 300, 90, 45)
        # добавление функции кнопке:
        button0.clicked.connect(self.action0)

        # создание кнопки "1":
        button1 = QPushButton("1", self)
        button1.setGeometry(5, 150, 90, 45)
        # добавление функции кнопке:
        button1.clicked.connect(self.action1)

        # создание кнопки "2":
        button2 = QPushButton("2", self)
        button2.setGeometry(100, 150, 90, 45)
        # добавление функции кнопке:
        button2.clicked.connect(self.action2)

        # создание кнопки "3":
        button3 = QPushButton("3", self)
        button3.setGeometry(195, 150, 90, 45)
        # добавление функции кнопке:
        button3.clicked.connect(self.action3)

        # создание кнопки "4":
        button4 = QPushButton("4", self)
        button4.setGeometry(5, 200, 90, 45)
        # добавление функции кнопке:
        button4.clicked.connect(self.action4)

        # создание кнопки "5":
        button5 = QPushButton("5", self)
        button5.setGeometry(100, 200, 90, 45)
        # добавление функции кнопке:
        button5.clicked.connect(self.action5)

        # создание кнопки "6":
        button6 = QPushButton("6", self)
        button6.setGeometry(195, 200, 90, 45)
        # добавление функции кнопке:
        button6.clicked.connect(self.action6)

        # создание кнопки "7":
        button7 = QPushButton("7", self)
        button7.setGeometry(5, 250, 90, 45)
        # добавление функции кнопке:
        button7.clicked.connect(self.action7)

        # создание кнопки "8":
        button8 = QPushButton("8", self)
        button8.setGeometry(100, 250, 90, 45)
        # добавление функции кнопке:
        button8.clicked.connect(self.action8)

        # создание кнопки "9":
        button9 = QPushButton("9", self)
        button9.setGeometry(195, 250, 90, 45)
        # добавление функции кнопке:
        button9.clicked.connect(self.action9)

        # создание кнопок действий:
        # создание кнопки "=":
        button_equal = QPushButton("=", self)
        button_equal.setGeometry(290, 350, 90, 45)
        # создание цветового эффекта для кнопки "=":
        red_effect_equal = QGraphicsColorizeEffect()
        red_effect_equal.setColor(Qt.red)
        button_equal.setGraphicsEffect(red_effect_equal)
        # добавление функции кнопке:
        button_equal.clicked.connect(self.action_equal)

        # создание кнопки "+":
        button_plus = QPushButton("+", self)
        button_plus.setGeometry(290, 250, 90, 45)
        # создание цветового эффекта для кнопки "+":
        blue_effect_plus = QGraphicsColorizeEffect()
        blue_effect_plus.setColor(Qt.blue)
        button_plus.setGraphicsEffect(blue_effect_plus)
        # добавление функции кнопке:
        button_plus.clicked.connect(self.action_plus)

        # создание кнопки "-":
        button_minus = QPushButton("-", self)
        button_minus.setGeometry(290, 200, 90, 45)
        # создание цветового эффекта для кнопки "-":
        blue_effect_minus = QGraphicsColorizeEffect()
        blue_effect_minus.setColor(Qt.blue)
        button_minus.setGraphicsEffect(blue_effect_minus)
        # добавление функции кнопке:
        button_minus.clicked.connect(self.action_minus)

        # создание кнопки "*":
        button_mul = QPushButton("*", self)
        button_mul.setGeometry(290, 150, 90, 45)
        # создание цветового эффекта для кнопки "*":
        blue_effect_mul = QGraphicsColorizeEffect()
        blue_effect_mul.setColor(Qt.blue)
        button_mul.setGraphicsEffect(blue_effect_mul)
        # добавление функции кнопке:
        button_mul.clicked.connect(self.action_mul)

        # создание кнопки "/":
        button_div = QPushButton("/", self)
        button_div.setGeometry(195, 300, 90, 45)
        # создание цветового эффекта для кнопки "/":
        blue_effect_div = QGraphicsColorizeEffect()
        blue_effect_div.setColor(Qt.blue)
        button_div.setGraphicsEffect(blue_effect_div)
        # добавление функции кнопке:
        button_div.clicked.connect(self.action_div)

        # создание кнопки "!":
        button_fact = QPushButton("!", self)
        button_fact.setGeometry(5, 350, 90, 45)
        # создание цветового эффекта для кнопки "!":
        blue_effect_fact = QGraphicsColorizeEffect()
        blue_effect_fact.setColor(Qt.blue)
        button_fact.setGraphicsEffect(blue_effect_fact)
        # добавление функции кнопке:
        button_fact.clicked.connect(self.action_fact)

        # создание кнопки "^":
        button_degree = QPushButton("^", self)
        button_degree.setGeometry(195, 350, 90, 45)
        # создание цветового эффекта для кнопки "^":
        blue_effect_degree = QGraphicsColorizeEffect()
        blue_effect_degree.setColor(Qt.blue)
        button_degree.setGraphicsEffect(blue_effect_degree)
        # добавление функции кнопке:
        button_degree.clicked.connect(self.action_degree)

        # создание кнопки "bin":
        button_bin = QPushButton("bin", self)
        button_bin.setGeometry(290, 300, 90, 45)
        # создание цветового эффекта для кнопки "bin":
        blue_effect_bin = QGraphicsColorizeEffect()
        blue_effect_bin.setColor(Qt.blue)
        button_bin.setGraphicsEffect(blue_effect_bin)
        # добавление функции кнопке:
        button_bin.clicked.connect(self.action_bin)

        # создание кнопки "√":
        button_sqrt = QPushButton("√", self)
        button_sqrt.setGeometry(100, 350, 90, 45)
        # создание цветового эффекта для кнопки "√":
        blue_effect_sqrt = QGraphicsColorizeEffect()
        blue_effect_sqrt.setColor(Qt.blue)
        button_sqrt.setGraphicsEffect(blue_effect_sqrt)
        # добавление функции кнопке:
        button_sqrt.clicked.connect(self.action_sqrt)

        # создание кнопки ".":
        button_point = QPushButton(".", self)
        button_point.setGeometry(100, 300, 90, 45)
        # создание цветового эффекта для кнопки ".":
        blue_effect_point = QGraphicsColorizeEffect()
        blue_effect_point.setColor(Qt.blue)
        button_point.setGraphicsEffect(blue_effect_point)
        # добавление функции кнопке:
        button_point.clicked.connect(self.action_point)

        # создание кнопки "Очистить.":
        button_clear = QPushButton("Очистить.", self)
        button_clear.setGeometry(5, 100, 185, 40)
        # создание цветового эффекта для кнопки "Очистить.":
        red_effect_clear = QGraphicsColorizeEffect()
        red_effect_clear.setColor(Qt.red)
        button_clear.setGraphicsEffect(red_effect_clear)
        # добавление функции кнопке:
        button_clear.clicked.connect(self.action_clear)

        # создание кнопки "Удалить символ.":
        button_del = QPushButton("Удалить символ.", self)
        button_del.setGeometry(195, 100, 185, 40)
        # создание цветового эффекта для кнопки "Удалить символ.":
        red_effect_del = QGraphicsColorizeEffect()
        red_effect_del.setColor(Qt.red)
        button_del.setGraphicsEffect(red_effect_del)
        # добавление функции кнопке:
        button_del.clicked.connect(self.action_del)

    # появление символов на экране:

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def action_clear(self):
        self.label.setText("")

    def action_fact(self):
        text = self.label.text()
        self.label.setText(f"factorial({text})")

    def action_sqrt(self):
        text = self.label.text()
        self.label.setText(text + "** 0.5")

    def action_degree(self):
        text = self.label.text()
        self.label.setText(text + "**")

    def action_bin(self):
        text = self.label.text()
        self.label.setText(f"bin({text})")

    def action_del(self):
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])

    def action_equal(self):
        equation = self.label.text()
        try:
            # получение ответа:
            ans = eval(equation)
            self.label.setText(str(ans))
        except:
            # текст при наличии ошибки:
            self.label.setText("Ошибка.")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())