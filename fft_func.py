from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

class Input_Noise:
    def __init__(self):
        pass
    def import_dialogue(self):
        self.F_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Otwórz Plik', 'C:\\Users\\Cheap Mouse\\Desktop\\Intro\\IT\\Python\\Projekty\\DataAnalysis', '(*.xml, *.csv *.json *.txt)')[0]
        self.base_name = os.path.basename(self.F_name)
        self.title_name = os.path.splitext(self.base_name)[0]

        if self.title_name != '':
            print('PLIK',self.title_name)
            db = pd.read_csv(self.F_name,encoding = 'latin-1').fillna(0)
            return db 
        else:
            print('Nie załadowano żadnego pliku')

class Input_Spec:
    def __init__(self):
        pass
    def import_dialogue(self):
        self.F_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Otwórz Plik', 'C:\\Users\\Cheap Mouse\\Desktop\\Intro\\IT\\Python\\Projekty\\DataAnalysis', '(*.xml, *.csv *.json *.txt)')[0]
        self.base_name = os.path.basename(self.F_name)
        self.title_name = os.path.splitext(self.base_name)[0]

        if self.title_name != '':
            print('PLIK',self.title_name)
            db = pd.read_csv(self.F_name,encoding = 'latin-1').fillna(0)
            return db 
        else:
            print('Nie załadowano żadnego pliku')

class Generate_Spectral(QtWidgets.QMainWindow):
    def __init__(self, fft_mem, fft_to_inv, fft_label):
        super().__init__()
        self.fft_to_inv = fft_to_inv
        self.fft_label = fft_label  
        self.fft_mem = fft_mem
        self.window_execute()

    def window_execute(self):

        userprofile = os.environ['USERPROFILE']
        self.path = os.path.join(userprofile, 'Pictures')
        self.setObjectName("MainWindow")
        self.resize(500, 300)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 300))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background-color:rgb(81, 81, 81);")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 441, 111))
        self.listWidget.setStyleSheet("QListWidget{\n"
"\n"
"border: 2px solid rgba(224, 17, 95, 0.5); \n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"Color: white;\n"
"}\n"
"QListWidget::item {outline: 0;border:none;}\n"
"QListWidget::item:hover {background-color:rgb(224, 17, 95);}\n"
"QListWidget::item:selected {\n"
"border: 0px;\n"
"outline: 0;\n"
"background-color:rgb(132, 25, 34);\n"
"\n"
"}\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 271, 21))
        self.label_1.setStyleSheet("font-size: 14px;\n"
"font-family: Arial;\n"
"Color: white;\n"
"border: None;")
        self.label_1.setObjectName("label_1")
        self.BTN_take = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_take.setGeometry(QtCore.QRect(190, 190, 121, 27))
        self.BTN_take.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid rgb(132, 25, 34); \n"
"font-size: 14px;\n"
"\n"
"font-family: Arial;\n"
"background: rgb(224, 17, 95); ")
        self.BTN_take.setObjectName("BTN_take")
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Dodaj widmo"))
        self.label_1.setText(_translate("MainWindow", "Wybierz wygenerowane wcześniej widmo"))
        self.BTN_take.setText(_translate("MainWindow", "Wybierz"))

        def event_add_to_list():
            for cd, id in enumerate(self.fft_mem, 1):
                self.listWidget.addItem(f"({cd}: {id[2]})")

        def event_take_spectral():
            if self.listWidget.count() > 0 and self.listWidget is not None:
                idx = self.listWidget.currentRow()
                event_get_spectral_plot(self.fft_mem[idx])
            
        def event_get_spectral_plot(fft):
            self.fft_to_inv.clear()
            self.fft_to_inv.append([fft[0],fft[1]])
            ###
            plt.close('all')
            plt.plot(fft[0]['Hz'].to_numpy(), fft[0]['Amplituda'].to_numpy(), color='red')
            plt.xlabel("Częstotliwość (Hz)") 
            plt.ylabel("Amplituda (-)")
            plt.show()
            
            fp = plt.figure()
            fp.set_figwidth(4)
            fp.set_figheight(1)
            plt.plot(fft[0]['Hz'].to_numpy(), fft[0]['Amplituda'].to_numpy())
            plt.xlabel("") 
            plt.ylabel("")
            plt.savefig(self.path+'/img_temp_gs.jpeg')
            pixmap_temp_gs = QtGui.QPixmap(self.path+'/img_temp_gs.jpeg')
            self.fft_label.setPixmap(pixmap_temp_gs)
            self.close()

        event_add_to_list()
        self.BTN_take.clicked.connect(lambda: event_take_spectral())


class Generate_Noise(QtWidgets.QMainWindow):
    def __init__(self, list, mem, samp):
        super().__init__()
        self.mem = mem
        self.mem_samp = samp
        self.list = list
        self.window_execute()

    def window_execute(self):
        self.setWindowTitle("Generator Szumu")
        userprofile = os.environ['USERPROFILE']
        self.path = os.path.join(userprofile, 'Pictures')
        self.setObjectName("MainWindow")
        self.resize(490, 550)
        self.setMinimumSize(QtCore.QSize(490, 550))
        self.setMaximumSize(QtCore.QSize(490, 550))
        self.setStyleSheet("background-color:rgb(81, 81, 81);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(490, 410))
        self.centralwidget.setMaximumSize(QtCore.QSize(490, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GN_main = QtWidgets.QFrame(self.centralwidget)
        self.GN_main.setStyleSheet("border-radius: 6px;\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"Color: white;\n"
"border: None;\n"
"border: 4px solid rgba(224, 17, 95, 0.5); ")
        self.GN_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GN_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GN_main.setObjectName("GN_main")
        self.frame = QtWidgets.QFrame(self.GN_main)
        self.frame.setGeometry(QtCore.QRect(20, 250, 411, 131))
        self.frame.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);\n"
"border-radius: 0px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_plot = QtWidgets.QLabel(self.frame)
        self.label_plot.setGeometry(QtCore.QRect(0, 0, 411, 131))
        self.label_plot.setText("")
        self.label_plot.setScaledContents(True)
        self.label_plot.setObjectName("label_plot")

        self.textEdit = QtWidgets.QTextEdit(self.GN_main)
        self.textEdit.setGeometry(QtCore.QRect(210, 120, 141, 31))
        self.textEdit.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);\n"
"border-radius: 6px;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.GN_main)
        self.label.setGeometry(QtCore.QRect(70, 80, 131, 31))
        self.label.setStyleSheet("border: none;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.GN_main)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 131, 31))
        self.label_2.setStyleSheet("border: none;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.GN_main)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.label_3.setStyleSheet("border: none;")
        self.label_3.setObjectName("label_3")

        self.checkBox_1 = QtWidgets.QCheckBox(self.GN_main)
        self.checkBox_1.setGeometry(QtCore.QRect(170, 10, 131, 31))
        self.checkBox_1.setStyleSheet("border: none;")
        self.checkBox_1.setObjectName("checkBox_1")


        self.textEdit_2 = QtWidgets.QTextEdit(self.GN_main)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 80, 141, 31))
        self.textEdit_2.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);\n"
"border-radius: 6px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.GN_main)
        self.pushButton.setGeometry(QtCore.QRect(60, 400, 131, 31))
        self.pushButton.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid rgb(132, 25, 34); \n"
"font-size: 14px;\n"
"color: black;\n"
"\n"
"font-family: Arial;\n"
"background: rgb(224, 17, 95); ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.GN_main)
        self.pushButton_1.setGeometry(QtCore.QRect(260, 400, 131, 31))
        self.pushButton_1.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid rgb(132, 25, 34); \n"
"font-size: 14px;\n"
"color: black;\n"
"\n"
"font-family: Arial;\n"
"background: rgb(224, 17, 95); ")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_4 = QtWidgets.QLabel(self.GN_main)
        self.label_4.setGeometry(QtCore.QRect(70, 450, 321, 41))
        self.label_4.setStyleSheet("border: none;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.GN_main)
        self.label_5.setGeometry(QtCore.QRect(70, 160, 131, 31))
        self.label_5.setStyleSheet("border: none;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.GN_main)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 160, 61, 31))
        self.textEdit_3.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);\n"
"border-radius: 6px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.GN_main)
        self.textEdit_4.setGeometry(QtCore.QRect(290, 160, 61, 31))
        self.textEdit_4.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);\n"
"border-radius: 6px;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.GN_main)
        self.textEdit_5.setGeometry(QtCore.QRect(210, 200, 141, 31))
        self.textEdit_5.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);\n"
"border-radius: 6px;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_6 = QtWidgets.QLabel(self.GN_main)
        self.label_6.setGeometry(QtCore.QRect(70, 200, 131, 31))
        self.label_6.setStyleSheet("border: none;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.GN_main)
        self.setCentralWidget(self.centralwidget)


        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Dodaj Szum"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Częstotliwość (Hz)"))
        self.label_2.setText(_translate("MainWindow", "Amplituda (-)"))
        self.label_3.setText(_translate("MainWindow", "Wygeneruj sinusoidę"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "50"))
        self.pushButton.setText(_translate("MainWindow", "Wykonaj"))
        self.pushButton_1.setText(_translate("MainWindow", "Dodaj"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Zakresy (x1, x2)"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "2*pi"))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "0.001"))
        self.label_6.setText(_translate("MainWindow", "Interwał czasowy (-)"))
        self.checkBox_1.setText(_translate("MainWindow", "Losowy szum"))

        self.change_state_flag_noerror = False
        self.plot_generated = False
        self.mem_temp = []

        def change_state():
            self.change_state_flag_noerror = False
            self.err_textHZ = False
            self.err_textAM = False
            self.err_textX1 = False
            self.err_textX2 = False
            self.err_textSM = False
            self.err_input_arr = [self.err_textHZ, self.err_textAM, self.err_textX1, self.err_textX2, self.err_textSM]
            self.err_desc_full = ""

            try:
                self.textHZ = float(self.textEdit_2.toPlainText())
                self.err_txt_HZ = ""
            except:       
                self.err_input_arr[0] = True
                self.err_txt_HZ = "Częstotliwość "
            
            self.err_desc_full += self.err_txt_HZ

            try:
                self.textAM = float(self.textEdit.toPlainText())
                self.err_txt_AM = ""

            except:
                self.err_input_arr[1] = True
                self.err_txt_AM = "Amplituda "

            self.err_desc_full += self.err_txt_AM


            if len(self.mem) == 0:
                try:
                    self.textX1 = float(self.textEdit_3.toPlainText())
                    self.err_txt_X1 = ""

                except:
                    self.err_input_arr[2] = True
                    self.err_txt_X1 = "Pierwszy zakres "

                self.err_desc_full += self.err_txt_X1

                try:
                    self.textX2 = float(self.textEdit_4.toPlainText())
                    self.err_txt_X2 = ""

                except:
                    self.err_input_arr[3] = True
                    self.err_txt_X2 = "Drugi zakres "

                self.err_desc_full += self.err_txt_X2

                try:
                    self.textSM = float(self.textEdit_5.toPlainText())
                    self.err_txt_SM = ""

                except:
                    self.err_input_arr[4] = True
                    self.err_txt_SM = "Interwał czasowy "

                self.err_desc_full += self.err_txt_SM

            else:
                self.textX1 = self.mem_samp[0]
                self.textX2 = self.mem_samp[1]
                self.textSM = self.mem_samp[2]


            if len(np.where(self.err_input_arr)[0]) != 0:
                self.label_4.setText("Błąd we wprowadzaniu parametrów: " + self.err_desc_full)

            
            else:
                if self.textX1 < self.textX2:
                    if self.textSM >= 0.0001:
                        self.change_state_flag_noerror = True
                        self.label_4.setText("Wykonano charakterystykę")
                    else:
                        self.label_4.setText("Nieprawidłowe próbkowanie - oczekiwanie na więcej niż 0.0001")
                else:
                    self.label_4.setText("Wprowadzono nieodpowiednie zakresy")

        def execute_plot():
            if self.change_state_flag_noerror:
                plt.close('all')
                x = np.arange(self.textX1, self.textX2, self.textSM)

                if self.checkBox_1.isChecked():
                    y = np.round((np.sin(2*np.pi*self.textHZ*x)*self.textAM+np.random.randn(x.size)),2)
                else:
                    y = np.sin(2*np.pi*self.textHZ*x)*self.textAM

                fp = plt.figure()
                plt.plot(x,y,color='r')
                fp.set_figwidth(4)
                fp.set_figheight(1)
                #plt.xlabel("Czas (sekuna)") 
                #plt.ylabel("Amplituda (-)")
                plt.xlim(self.textX1, self.textX2)
                plt.draw()
                plt.savefig(self.path+'/img_temp_gn.jpeg')
                pixmap_temp_gn = QtGui.QPixmap(self.path+'/img_temp_gn.jpeg')
                self.label_plot.setPixmap(pixmap_temp_gn)
                self.plot_generated = True
                #os.remove('img_temp_gn.jpeg')
                self.mem_temp = [x,y]
                #plt.show()
                plt.close('all')
                
            else:
                self.plot_generated = False
                self.label_4.setText("Wprowadzono nieodpowiednie zakresy")

        def add_plot_to_list():
            if self.plot_generated:
    
                if len(self.mem) == 0:  
                    self.mem_samp.clear()
                    self.mem_samp += [float(self.textEdit_3.toPlainText()), float(self.textEdit_4.toPlainText()), float(self.textEdit_5.toPlainText())]
                self.list.addItem(f"Szum: Częst: {self.textEdit_2.toPlainText()} / Amp: {self.textEdit.toPlainText()} / Zakr: {self.textEdit_3.toPlainText()}-{self.textEdit_4.toPlainText()} / Int: {self.textEdit_5.toPlainText()}")
                self.mem.append(self.mem_temp)
                self.close()


        if len(self.mem) > 0:
            self.textEdit_3.setDisabled(True)
            self.textEdit_4.setDisabled(True)
            self.textEdit_5.setDisabled(True)
            self.textEdit_3.setPlaceholderText(_translate("MainWindow", str(self.mem_samp[0])))
            self.textEdit_4.setPlaceholderText(_translate("MainWindow", str(self.mem_samp[1])))
            self.textEdit_5.setPlaceholderText(_translate("MainWindow", str(self.mem_samp[2])))
            self.label_4.setText(f"Zdefiniowano przedział: ({self.mem_samp[0]}/{self.mem_samp[1]}) oraz Interwał: ({self.mem_samp[2]})")
        else:
            self.textEdit_3.setDisabled(False)
            self.textEdit_4.setDisabled(False)
            self.textEdit_5.setDisabled(False)
            self.textEdit_3.setPlaceholderText(_translate("MainWindow", "0"))
            self.textEdit_4.setPlaceholderText(_translate("MainWindow", "2*pi"))
            self.textEdit_5.setPlaceholderText(_translate("MainWindow", "0.001"))
            self.label_4.setText("Wprowadź odpowiednie parametry by wygenerować sygnał")
        
        self.textEdit.textChanged.connect(lambda: change_state())
        self.textEdit_2.textChanged.connect(lambda: change_state())
        self.textEdit_3.textChanged.connect(lambda: change_state())
        self.textEdit_4.textChanged.connect(lambda: change_state())
        self.textEdit_5.textChanged.connect(lambda: change_state())
        self.pushButton.clicked.connect(lambda: execute_plot())
        self.pushButton_1.clicked.connect(lambda: add_plot_to_list())
        
