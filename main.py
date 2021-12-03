import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow



pm_list = []
percent_list = []

E = [0,0,0,0,0]
N = [0,0,0,0,0]
T = [0,0,0,0,0]
P = [0,0,0,0,0]

tmp = False
result = ""


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUI()

    def setupUI(self):
        global UI_set, UI_q1, UI_q2, UI_q3, UI_q4, UI_result

        UI_set = QtUiTools.QUiLoader().load(resource_path("first.ui"))
        UI_q1 = QtUiTools.QUiLoader().load(resource_path("question1.ui"))
        UI_q2 = QtUiTools.QUiLoader().load(resource_path("question2.ui"))
        UI_q3 = QtUiTools.QUiLoader().load(resource_path("question3.ui"))
        UI_q4 = QtUiTools.QUiLoader().load(resource_path("question4.ui"))
        UI_result = QtUiTools.QUiLoader().load(resource_path("result.ui"))


        self.setCentralWidget(UI_set)
        self.setWindowTitle("UI TEST")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))
        self.resize(503,503)

        self.show()

        UI_set.pushButton.clicked.connect(main_q1)
        UI_q1.pushButton.clicked.connect(q1_q2)
        UI_q2.pushButton.clicked.connect(q2_q3)
        UI_q2.pushButton_2.clicked.connect(q2_q1)
        UI_q3.pushButton.clicked.connect(q3_q4)
        UI_q3.pushButton_2.clicked.connect(q3_q2)
        UI_q4.pushButton.clicked.connect(q4_result)
        UI_q4.pushButton_2.clicked.connect(q4_q3)



def main_q1():

    UI_set.close()
    UI_q1.show()



def q1_q2():

    q1_put()
    UI_q2.show()
    UI_q1.close()


def q2_q1():

    q2_put()
    UI_q2.close()
    UI_q1.show()


def q2_q3():
    q2_put()
    UI_q2.close()
    UI_q3.show()


def q3_q2():
    q3_put()
    UI_q3.close()
    UI_q2.show()


def q3_q4():
    q3_put()
    UI_q3.close()
    UI_q4.show()

def q4_q3():
    q4_put()
    UI_q4.close()
    UI_q3.show()


def q4_result():
    q4_put()
    result = show_result()
    UI_q4.close()
    UI_result.show()
    UI_result.textBrowser.setPlainText(result)

    result_percentage = f"외향성 : {percent_list[0]} \n직관 : {percent_list[1]} \n생각 : {percent_list[2]} \n생활 : {percent_list[3]}"

    UI_result.textBrowser_2.setPlainText(result_percentage)





def q1_put():
    value = []
    tmp = UI_q1.horizontalSlider_1.value()
    value.append(tmp / 10)
    tmp = UI_q1.horizontalSlider_2.value()
    value.append(tmp / 10)
    tmp = UI_q1.horizontalSlider_3.value()
    value.append(tmp / 10)
    tmp = UI_q1.horizontalSlider_4.value()
    value.append(tmp / 10)
    tmp = UI_q1.horizontalSlider_5.value()
    value.append(tmp / 10)
    plus_minus(value, 0)
    #print("value : ",value,end='\n\n\n')


def q2_put():
    value = []
    tmp = UI_q2.horizontalSlider_1.value()
    value.append(tmp / 10)
    tmp = UI_q2.horizontalSlider_2.value()
    value.append(tmp / 10)
    tmp = UI_q2.horizontalSlider_3.value()
    value.append(tmp / 10)
    tmp = UI_q2.horizontalSlider_4.value()
    value.append(tmp / 10)
    tmp = UI_q2.horizontalSlider_5.value()
    value.append(tmp / 10)
    plus_minus(value, 1)
    #print("value : ",value,end='\n\n\n')

def q3_put():
    value = []
    tmp = UI_q3.horizontalSlider_1.value()
    value.append(tmp / 10)
    tmp = UI_q3.horizontalSlider_2.value()
    value.append(tmp / 10)
    tmp = UI_q3.horizontalSlider_3.value()
    value.append(tmp / 10)
    tmp = UI_q3.horizontalSlider_4.value()
    value.append(tmp / 10)
    tmp = UI_q3.horizontalSlider_5.value()
    value.append(tmp / 10)
    plus_minus(value, 2)
    #print("value : ",value,end='\n\n\n')



def q4_put():
    value = []
    tmp = UI_q4.horizontalSlider_1.value()
    value.append(tmp / 10)
    tmp = UI_q4.horizontalSlider_2.value()
    value.append(tmp / 10)
    tmp = UI_q4.horizontalSlider_3.value()
    value.append(tmp / 10)
    tmp = UI_q4.horizontalSlider_4.value()
    value.append(tmp / 10)
    tmp = UI_q4.horizontalSlider_5.value()
    value.append(tmp / 10)
    plus_minus(value, 3)
    #print("value : ",value,end='\n\n\n')




def plus_minus(value,i):
    index = range(i*5, (i+1)*5)
    for k in index:
        temp = pm_list[k]
        m = k%5
        j = int(temp[2])
        if(temp[0] == 'E'):
            if(temp[1] == '+'):
                E[j] = value[m]
            else:
                E[j] = -value[m]

        if (temp[0] == 'N'):
            if (temp[1] == '+'):
                N[j] = value[m]
            else:
                N[j] = -value[m]


        if (temp[0] == 'T'):
            if (temp[1] == '+'):
                T[j] = value[m]
            else:
                T[j] = -value[m]


        if(temp[0] == 'P'):
            if (temp[1] == '+'):
                P[j] = value[m]
            else:
                P[j] = -value[m]


    #print("E:",E)
    #print("N:",N)
    #print("T",T)
    #print("P",P)


def show_result():
    Extro = 50
    recog = 50
    jucge = 50      # typo 복사 붙여넣기 떄문에 그냥 둠
    life = 50
    result = ""

    for i in E:
        Extro += i

    for l in N:
        recog += l

    for t in T:
        jucge += t

    for a in P:
        life += a

    if(Extro > 50):
        result += "E"
    else:
        result += "I"
    percent_list.append(Extro)


    if (recog > 50):
        result += "N"
    else:
        result += "S"
    percent_list.append(recog)

    if (jucge > 50):
        result += "T"
    else:
        result += "F"
    percent_list.append(jucge)

    if (life > 50):
        result += "P"
    else:
        result += "J"
    percent_list.append(life)

    return result






def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':

    f = open('mbti_pm.txt', 'r')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        if not line:
            break
        pm_list.append(line)

    f.close()


    app = QApplication(sys.argv)

    main = MainView()

    # main.show()

    sys.exit(app.exec_())