#создай приложение для запоминания информациb
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QButtonGroup, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QGroupBox, QPushButton
from random import randint
class Question():
    def __init__(self, q, r_a, w_a1, w_a2, w_a3):
        self.q = q
        self.r_a = r_a
        self.w_a1 = w_a1
        self.w_a2 = w_a2
        self.w_a3 = w_a3
spisok = list()
serf = Question('а','б','г','в','а')
spisok.append(serf)
serf = Question('Какая кошка самая большая на планете?','Тигр','Гепард','Лев','Барс')
spisok.append(serf)
serf = Question('Какое животное самое крупное на Земле?','Синий кит',' Кашалот',' Гигантский кальмар','Африканский слон')
spisok.append(serf)
serf = Question('Какая планета самая большая в Солнечной системе?','Юпитер','Сатурн','Нептун','Меркурий')
spisok.append(serf)
serf = Question('На какой планете самый короткий день?',' Юпитер','Земля','Нептун','Меркурий')
spisok.append(serf)
serf = Question('Какая звезда ближе всего к Земле?','Солнце','Полярная звезда','Сириус','Cbkbwbev')
spisok.append(serf)
serf = Question('Как называется метеорит, который упал на Землю 15 февраля 2013 года?','Челябинский','Гоба','Тунгусский','Альенде')
spisok.append(serf)
z = 0

a = QApplication([])
w = QWidget()
w.setWindowTitle('Memory Card')
w.resize(1,1)
l = QLabel('Какой национальности не существует?')
g1 = QGroupBox('Варианты ответов')
group = QButtonGroup()
r1 = QRadioButton('Энцы')
r2 = QRadioButton('Смурфы')
r3 = QRadioButton('Чулымцы')
r4 = QRadioButton('Алеуты ')
group.addButton(r1)
group.addButton(r2)
group.addButton(r3)
group.addButton(r4)
h1 = QHBoxLayout()
h1.addWidget(r1, alignment = Qt.AlignLeft)
h1.addWidget(r3, alignment = Qt.AlignLeft)
h2 = QHBoxLayout()
h2.addWidget(r2, alignment = Qt.AlignLeft)
h2.addWidget(r4, alignment = Qt.AlignLeft)
v1 = QVBoxLayout()
v1.addLayout(h1)
v1.addLayout(h2)
g1.setLayout(v1)
g2 = QGroupBox('Результата теста')
l1 = QLabel('Правильно\Неправильно')
l2 = QLabel('Правильный ответ')
v3 = QVBoxLayout()
v3.addWidget(l1, alignment = Qt.AlignLeft)
v3.addWidget(l2, alignment = Qt.AlignCenter)
g2.setLayout(v3)
g2.hide()
p = QPushButton('Ответить')
v2 = QVBoxLayout()
v2.addWidget(l, alignment = Qt.AlignVCenter)
v2.addWidget(g1, alignment = Qt.AlignVCenter)
v2.addWidget(g2, alignment = Qt.AlignVCenter)
v2.addWidget(p, alignment = Qt.AlignVCenter)
def show_result():
    try:
        check_ans()
        g1.hide()
        g2.show()
        p.setText('Следующий вопрос')
        
    except:
        win = QMessageBox()
        win.setText('Ты глупый? На ответ нажми.')
        win.exec_()
def show_q():
    g1.show()
    g2.hide()
    p.setText('Ответить')
    group.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    group.setExclusive(True)
    ask(spisok[randint(0,len(spisok)-1)])
def start_test():
    if p.text() == 'Ответить':
        show_result()
    else:
        show_q()
        w.total += 1
def ask(q: Question):
    l.setText(q.q)
    rand = randint(0,3)
    if rand == 0:
        r1.setText(q.r_a)
        r2.setText(q.w_a1)
        r3.setText(q.w_a2)
        r4.setText(q.w_a3)
    elif rand == 1:
        r1.setText(q.w_a1)
        r2.setText(q.r_a)
        r3.setText(q.w_a2)
        r4.setText(q.w_a3)
    elif rand == 2:
        r1.setText(q.w_a2)
        r2.setText(q.w_a1)
        r3.setText(q.r_a)
        r4.setText(q.w_a3)
    elif rand == 3:
        r1.setText(q.w_a3)
        r2.setText(q.w_a1)
        r3.setText(q.w_a2)
        r4.setText(q.r_a)
    l2.setText(q.r_a)
def check_ans():
    if l2.text() == group.checkedButton().text():
        l1.setText('Правильно')
        w.score += 1
    else:
        l1.setText('Неверно')
    print('Всего вопросов:',w.total)
    print('Правильных ответов:', w.score)
    print('Рейтинг:', w.score/w.total*100)
p.clicked.connect(start_test)
ask(spisok[z])
w.total = 1
w.score = 0
w.setLayout(v2)
w.show()
a.exec_()
