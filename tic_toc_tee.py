from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial
from random import randint
cl=[]
bot , bar =  0 , 0

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 320)
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.915, y1:0.909091, x2:1, y2:1, stop:0.298507 rgba(155, 194, 215, 255), stop:0.318408 rgba(255, 255, 255, 255), stop:0.60199 rgba(0, 0, 0, 255), stop:0.621891 rgba(217, 217, 217, 255), stop:0.905473 rgba(255, 169, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        self.b1o1 = QtWidgets.QPushButton(parent=Form)
        self.b1o1.setGeometry(QtCore.QRect(20, 20, 93, 81))
        self.b1o1.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b1o1.setObjectName("b1o1")
        self.b1o2 = QtWidgets.QPushButton(parent=Form)
        self.b1o2.setGeometry(QtCore.QRect(120, 20, 93, 81))
        self.b1o2.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b1o2.setObjectName("b1o2")
        self.b1o3 = QtWidgets.QPushButton(parent=Form)
        self.b1o3.setGeometry(QtCore.QRect(220, 20, 93, 81))
        self.b1o3.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b1o3.setObjectName("b1o3")
        self.b2o1 = QtWidgets.QPushButton(parent=Form)
        self.b2o1.setGeometry(QtCore.QRect(20, 110, 93, 81))
        self.b2o1.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b2o1.setObjectName("b2o1")
        self.b3o1 = QtWidgets.QPushButton(parent=Form)
        self.b3o1.setGeometry(QtCore.QRect(20, 200, 93, 81))
        self.b3o1.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b3o1.setObjectName("b3o1")
        self.b2o2 = QtWidgets.QPushButton(parent=Form)
        self.b2o2.setGeometry(QtCore.QRect(120, 110, 93, 81))
        self.b2o2.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b2o2.setObjectName("b2o2")
        self.b3o2 = QtWidgets.QPushButton(parent=Form)
        self.b3o2.setGeometry(QtCore.QRect(120, 200, 93, 81))
        self.b3o2.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b3o2.setObjectName("b3o2")
        self.b2o3 = QtWidgets.QPushButton(parent=Form)
        self.b2o3.setGeometry(QtCore.QRect(220, 110, 93, 81))
        self.b2o3.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b2o3.setObjectName("b2o3")
        self.b3o3 = QtWidgets.QPushButton(parent=Form)
        self.b3o3.setGeometry(QtCore.QRect(220, 200, 93, 81))
        self.b3o3.setStyleSheet("background: white ;border-radius: 10px;border-bottom: 4px solid ;")
        self.b3o3.setObjectName("b3o3")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 141, 28))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.74, fx:0.5, fy:0.5, stop:0.174129 rgba(67, 255, 79, 255), stop:0.800995 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(172, 290, 141, 28))
        self.pushButton_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.74, fx:0.5, fy:0.5, stop:0.0547264 rgba(255, 0, 0, 255), stop:0.721393 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1o1.setText(_translate("Form", "1,1"))
        self.b1o2.setText(_translate("Form", "1,2"))
        self.b1o3.setText(_translate("Form", "1,3"))
        self.b2o1.setText(_translate("Form", "2,1"))
        self.b3o1.setText(_translate("Form", "3,1"))
        self.b2o2.setText(_translate("Form", "2,2"))
        self.b3o2.setText(_translate("Form", "3,2"))
        self.b2o3.setText(_translate("Form", "2,3"))
        self.b3o3.setText(_translate("Form", "3,3"))
        self.pushButton.setText(_translate("Form", "reset"))
        self.pushButton_2.setText(_translate("Form", "qite"))

        self.b1o1.clicked.connect(partial(self.cli, number = 1))
        self.b1o2.clicked.connect(partial(self.cli, number = 2))
        self.b1o3.clicked.connect(partial(self.cli, number = 3))
        self.b2o1.clicked.connect(partial(self.cli, number = 4))
        self.b2o2.clicked.connect(partial(self.cli, number = 5))
        self.b2o3.clicked.connect(partial(self.cli, number = 6))
        self.b3o1.clicked.connect(partial(self.cli, number = 7))
        self.b3o2.clicked.connect(partial(self.cli, number = 8))
        self.b3o3.clicked.connect(partial(self.cli, number = 9))
        self.pushButton.clicked.connect(partial(self.cli, number = -1))
        self.pushButton_2.clicked.connect(self.qu)

    
    
    def reset(self):
            cl = []
            
    def qu(self):
            quit()
    
    def cli(self , number ):
        if number == -1 :
                del cl[0:-1]
                del cl[0]
                Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.915, y1:0.909091, x2:1, y2:1, stop:0.298507 rgba(155, 194, 215, 255), stop:0.318408 rgba(255, 255, 255, 255), stop:0.60199 rgba(0, 0, 0, 255), stop:0.621891 rgba(217, 217, 217, 255), stop:0.905473 rgba(255, 169, 169, 255), stop:1 rgba(255, 255, 255, 255));")
                self.b1o1.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b1o2.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b1o3.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b2o1.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b2o2.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b2o3.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b3o1.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b3o2.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                self.b3o3.setStyleSheet("background-color : white ;border-radius: 10px;border-bottom: 4px solid ;")
                
        can = True 
        for it in cl :
                if it == number :
                        print("you cant do it")
                        can = False
                        break
        
        if can :
                cl.append(number)
                if cl[-1] == 1 :
                        self.b1o1.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 2 :
                        self.b1o2.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 3 :
                        self.b1o3.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 4 :
                        self.b2o1.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 5 :
                        self.b2o2.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 6 :
                        self.b2o3.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 7 :
                        self.b3o1.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 8 :
                        self.b3o2.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")
                elif cl[-1] == 9 :
                        self.b3o3.setStyleSheet("background-color : #E74C3C ;border-radius: 10px;border-bottom: 4px solid ;")


        if len(cl) < 9 :
                while can :
                        bot = randint(1,9)
                        for it in cl :
                                if it == bot :
                                        can = True
                                        break
                                        
                                else :
                                        can = False
                                
                        if can == False :
                                cl.append(bot)
                                if cl[-1] == 1 :
                                        self.b1o1.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 2 :
                                        self.b1o2.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 3 :
                                        self.b1o3.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 4 :
                                        self.b2o1.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 5 :
                                        self.b2o2.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 6 :
                                        self.b2o3.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 7 :
                                        self.b3o1.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 8 :
                                        self.b3o2.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                elif cl[-1] == 9 :
                                        self.b3o3.setStyleSheet("background-color : #21618C ;border-radius: 10px;border-bottom: 4px solid ;")
                                        
                                        
        if len(cl) > 5 :
                cl1 = []
                cl2 = []
                for i in range(len(cl)): 
                        if i % 2 == 1:
                                cl1.append(cl[i])
                        else :
                                cl2.append(cl[i])
                                

                if 1 in cl1 and 2 in cl1 and 3 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 1 in cl1 and 4 in cl1 and 7 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 1 in cl1 and 5 in cl1 and 9 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 2 in cl1 and 5 in cl1 and 8 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 3 in cl1 and 6 in cl1 and 9 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 3 in cl1 and 5 in cl1 and 7 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 4 in cl1 and 5 in cl1 and 6 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                elif 7 in cl1 and 8 in cl1 and 9 in cl1 :
                        Form.setStyleSheet("background-color: #3498DB ;")
                        
                if 1 in cl2 and 2 in cl2 and 3 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 1 in cl2 and 4 in cl2 and 7 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 1 in cl2 and 5 in cl2 and 9 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 2 in cl2 and 5 in cl2 and 8 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 3 in cl2 and 6 in cl2 and 9 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 3 in cl2 and 5 in cl2 and 7 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 4 in cl2 and 5 in cl2 and 6 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                elif 7 in cl2 and 8 in cl2 and 9 in cl2 :
                        Form.setStyleSheet("background-color: #CD6155 ;")
                        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
