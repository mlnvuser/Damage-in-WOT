from PyQt5 import QtGui, QtWidgets
from damage import Ui_MainWindow
import sys, time, threading

class window(QtWidgets.QMainWindow):
    '''Главное графическое окно'''

    def __init__(self):
        super(window,self).__init__()
        self.ui = Ui_MainWindow() #Работа с импортированным классом будет происходить при помощи данной переменной;
        self.ui.setupUi(self) #Вызвали метод в котором создано графическое окно;
        self.setWindowTitle('Рассчет статиста')
        self.setWindowIcon(QtGui.QIcon('icons/swords_24dp_FILL0_wght400_GRAD0_opsz24.svg'))
        self.ui.pushButton_2.clicked.connect(self.click_calculate) #При нажатии на кнопку
        self.ui.pushButton.clicked.connect(self.click_set_to_zero) #При нажатии на кнопку

    def click_calculate(self):
        '''При нажатии на кнопку рассчёта'''

        if self.check_include_le(self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4):
            qty_now = int(self.ui.lineEdit.text())
            dmg_now = int(self.ui.lineEdit_2.text())
            battle = int(self.ui.lineEdit_3.text())
            top_dmg = int(self.ui.lineEdit_4.text())
            x = (top_dmg * (qty_now + battle) - qty_now * dmg_now) / battle
            self.ui.lineEdit_5.setText(str(int(x)))

    def click_set_to_zero(self):
        '''При нажатии на кнопку обнулить'''

        le = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4, self.ui.lineEdit_5]
        for i in le:
            i.setText('')
            i.setStyleSheet("border: 1px solid #000000; font: 10pt Georgia")

    def check_include_le(self, *obj):
        """Проверка на наличие и правильности записей в формах ввода"""

        check = True
        null_obj = []
        for i in obj:
            if len(i.text()) == 0:
                i.setStyleSheet("border: 1px solid #ff0000; font: 10pt Georgia")
                check = False
                null_obj.append(i)
            else:
                try:
                    int(i.text())/1
                except:
                    i.setStyleSheet("border: 1px solid #ff0000; font: 10pt Georgia")
                    check = False
                else:
                    i.setStyleSheet("border: 1px solid #000000; font: 10pt Georgia")
        if not check:
            p = threading.Thread(target=self.warning,
                                     args=(null_obj,))  # Запуск функции-потока с передачей параметров;
            p.start()
        return check

    def warning(self,obj):
        '''Функция-поток, меняющая окрас LineEdit'''

        time.sleep(3)  # сек.
        for i in obj:
            i.setStyleSheet("border: 1px solid #000000; font: 10pt Georgia")


    def closeEvent(self, event):
        """При закрытии приложения"""

        reply = QtWidgets.QMessageBox.question(self, 'Выход!?', "Вы действительно хотите выйти?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__': #Если данный файл не является вызываемым модулем, а исполняемым файлом;
    app = QtWidgets.QApplication(sys.argv)
    application = window()
    application.setStyleSheet("#MainWindow{border-image:url(images/t54.jpg)}")
    application.show() #Показать графическое окно;

    sys.exit(app.exec()) #Правильный выход из приложения.

