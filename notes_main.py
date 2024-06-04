from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QListWidget, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout,QInputDialog,QLineEdit
import json

with open('file_main.py','r',encoding='UTF-8') as file:
    notes = json.load(file)

def show_note():
    name = list1.selectedItems()[0].text()
    editor.setText(notes[name]['text'])
    list2.clear()
    if notes[name]['teg'] != []:
        list2.addItems(notes[name]['teg'])

def delete0():
    if len(list1.selectedItems()) > 0:
        name = list1.selectedItems()[0].text()
        del notes [name]
        with open('file_main.py','w',encoding='UTF-8') as file:
            json.dump(notes,file)
            list1.clear()
            list1.addItems(notes)
    
def save0():
    if len(list1.selectedItems()) > 0:
        name = list1.selectedItems()[0].text()
        notes[name]['text'] = editor.toPlainText()
        with open('file_main.py','w',encoding='UTF-8') as file:
            json.dump(notes,file)
            list1.clear()
            list1.addItems(notes)
    

def add0():
    note_name, line = QInputDialog.getText(window,'add','note name')
    notes[note_name] = {'text':'','teg':[]}
    with open('file_main.py','w',encoding='UTF-8') as file:
        json.dump(notes,file)
        list1.clear()
        list1.addItems(notes)

def add_teg():
    if len(liner.text()) > 0:
        if len(list1.selectedItems()) > 0:
            name = list1.selectedItems()[0].text()
            if not liner.text() in notes:
                line_text = notes[name]['teg']
                line_text.append(liner.text())
                notes[name]['teg'] = line_text
                with open('file_main.py','w',encoding='UTF-8') as file:
                    json.dump(notes,file)
                list2.clear()
                list2.addItems(notes[name]['teg'])


def del_teg():
    if len(list2.selectedItems()) > 0:
        namu = list1.selectedItems()[0].text()
        name = list2.selectedItems()[0].text()
        notes[namu]['teg'].remove(name)
        with open('file_main.py','w',encoding='UTF-8') as file:
            json.dump(notes,file)
        list2.clear()
        list2.addItems(notes[namu]['teg'])

def search_teg():
    if search.text() == 'sch':
        list_search = list()
        if len(liner.text()) > 0:
            for i in notes:
                if liner.text() in notes[i]['teg']:
                    list_search.append(i)
                    list1.clear()
                    list1.addItems(list_search)
                    search.setText('clr')
    else:
        list1.clear()
        list1.addItems(notes)
        search.setText('sch')


app = QApplication([])
window = QWidget()
list1 = QListWidget() #notes
list1.addItems(list(notes.keys()))
list2 = QListWidget() #tegs
liner = QLineEdit() #tegs edit
editor = QTextEdit() #notes text edit
search = QPushButton('sch')
save = QPushButton('sv')
delete = QPushButton('del')
create = QPushButton('cr')
change = QPushButton('ch')
dechange = QPushButton('dech')
m_layout = QVBoxLayout()
lay1 = QHBoxLayout()
lay2 = QHBoxLayout()
lay3 = QHBoxLayout()
lay1.addWidget(list1,alignment = Qt.AlignCenter)
lay1.addWidget(create,alignment = Qt.AlignCenter)
lay1.addWidget(delete,alignment = Qt.AlignCenter)
lay1.addWidget(save,alignment = Qt.AlignCenter)
lay2.addWidget(list2,alignment = Qt.AlignCenter)
lay2.addWidget(search,alignment = Qt.AlignCenter)
lay2.addWidget(change,alignment = Qt.AlignCenter)
lay2.addWidget(dechange,alignment = Qt.AlignCenter)
lay3.addWidget(editor,alignment = Qt.AlignCenter)
lay3.addWidget(liner,alignment = Qt.AlignCenter)
m_layout.addLayout(lay1)
m_layout.addLayout(lay2)
m_layout.addLayout(lay3)
window.setLayout(m_layout)
list1.clicked.connect(show_note)
save.clicked.connect(save0)
create.clicked.connect(add0)
delete.clicked.connect(delete0)
change.clicked.connect(add_teg)
dechange.clicked.connect(del_teg)
search.clicked.connect(search_teg)

window.show()
app.exec_()