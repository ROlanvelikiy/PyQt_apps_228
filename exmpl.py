from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.show()

text = QLabel('ПРОСТО ТЕКСТ')
btn1 = QPushButton('1')
btn2 = QPushButton('2')

layout_h = QHBoxLayout()

layout_h.addWidget(btn1, alignment=Qt.AlignCenter)
layout_h.addWidget(btn2, alignment=Qt.AlignCenter)

layout_v = QVBoxLayout()

layout_v.addWidget(text, alignment=Qt.AlignCenter)
layout_v.addLayout(layout_h)



window.setLayout(layout_v)

def replace_text():
    text.setText('ООООООООООООООООЛОЧДЖФЫОДФОЫВ')


btn1.clicked.connect(replace_text)

app.exec()