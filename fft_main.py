import string
from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from fft_func import *
import numpy as np
import scipy as si
from datetime import datetime
from scipy.fft import fft, fftfreq, ifft


class Ui_MainWindow(object):
        def __init__(self):

                self.IN = Input_Noise()
                self.IS = Input_Spec()

                self.db_N = None
                self.db_S = None

                self.mem_N = []
                self.mem_S = []
                self.mem_SAMP = []

                self.fft_av = False
                self.fft_done = False
                self.fft_sp = []

                self.fft_hat_av = False
                self.fft_hat_done = False

                self.fft_DB = []
                self.fft_DB_memory = []
                self.fft_DB_to_inverse = []
                self.fft_hat_DB = []

        def setupUi(self, MainWindow):

                userprofile = os.environ['USERPROFILE']
                self.path = os.path.join(userprofile, 'Pictures')
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 700)
                MainWindow.setMinimumSize(QtCore.QSize(800, 700))
                MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setMinimumSize(QtCore.QSize(800, 700))
                self.centralwidget.setStyleSheet("background-color:rgb(81, 81, 81);")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setContentsMargins(25, 25, 25, 25)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.Submain_frame = QtWidgets.QFrame(self.centralwidget)
                self.Submain_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Submain_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Submain_frame.setObjectName("Submain_frame")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Submain_frame)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.Tab_widget = QtWidgets.QTabWidget(self.Submain_frame)
                self.Tab_widget.setMinimumSize(QtCore.QSize(0, 0))
                self.Tab_widget.setStyleSheet("QTabWidget::pane {\n"
        "  border-top: 4px solid rgb(224, 17, 95); \n"
        "} \n"
        "\n"
        "QTabBar::tab {\n"
        "     background: rgb(132, 25, 34); \n"
        "    width: 200px;\n"
        "    \n"
        "    font: 10pt \"Arial\";\n"
        "     padding-right: 5px; \n"
        "    padding-left: 5px; \n"
        "     padding-top: 5px; \n"
        "    padding-bottom: 5px; \n"
        "} \n"
        "\n"
        "QTabBar::tab:selected { \n"
        "  background: rgb(224, 17, 95); \n"
        "  margin-bottom: -1px; \n"
        "}\n"
        "\n"
        "")
                self.Tab_widget.setUsesScrollButtons(True)
                self.Tab_widget.setObjectName("Tab_widget")
                self.AS_widget = QtWidgets.QWidget()
                self.AS_widget.setObjectName("AS_widget")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.AS_widget)
                self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.AW_date_manage_main = QtWidgets.QFrame(self.AS_widget)
                self.AW_date_manage_main.setMaximumSize(QtCore.QSize(16777215, 150))
                self.AW_date_manage_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_date_manage_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_date_manage_main.setObjectName("AW_date_manage_main")
                self.AW_date_import_main = QtWidgets.QFrame(self.AW_date_manage_main)
                self.AW_date_import_main.setGeometry(QtCore.QRect(26, 16, 332, 118))
                self.AW_date_import_main.setStyleSheet("border: 4px solid rgba(224, 17, 95, 0.5); ")
                self.AW_date_import_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_date_import_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_date_import_main.setObjectName("AW_date_import_main")
                self.AW_label_1 = QtWidgets.QLabel(self.AW_date_import_main)
                self.AW_label_1.setGeometry(QtCore.QRect(10, 10, 311, 20))
                self.AW_label_1.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_1.setAlignment(QtCore.Qt.AlignCenter)
                self.AW_label_1.setObjectName("AW_label_1")
                self.BTN_generate = QtWidgets.QPushButton(self.AW_date_import_main)
                self.BTN_generate.setGeometry(QtCore.QRect(180, 50, 131, 31))
                self.BTN_generate.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_generate.setObjectName("BTN_generate")
                self.BTN_import = QtWidgets.QPushButton(self.AW_date_import_main)
                self.BTN_import.setGeometry(QtCore.QRect(30, 50, 131, 31))
                self.BTN_import.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_import.setObjectName("BTN_import")
                self.AW_date_save_main = QtWidgets.QFrame(self.AW_date_manage_main)
                self.AW_date_save_main.setGeometry(QtCore.QRect(368, 16, 332, 118))
                self.AW_date_save_main.setStyleSheet("border: 4px solid rgba(224, 17, 95, 0.5);")
                self.AW_date_save_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_date_save_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_date_save_main.setObjectName("AW_date_save_main")
                self.AW_label_2 = QtWidgets.QLabel(self.AW_date_save_main)
                self.AW_label_2.setGeometry(QtCore.QRect(10, 10, 311, 20))
                self.AW_label_2.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.AW_label_2.setObjectName("AW_label_2")
                self.BTN_FFT = QtWidgets.QPushButton(self.AW_date_save_main)
                self.BTN_FFT.setGeometry(QtCore.QRect(30, 50, 131, 31))
                self.BTN_FFT.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_FFT.setObjectName("BTN_FFT")
                self.BTN_save = QtWidgets.QPushButton(self.AW_date_save_main)
                self.BTN_save.setGeometry(QtCore.QRect(180, 50, 131, 31))
                self.BTN_save.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_save.setObjectName("BTN_save")
                self.verticalLayout_3.addWidget(self.AW_date_manage_main)
                self.AW_plots_frame_main = QtWidgets.QFrame(self.AS_widget)
                self.AW_plots_frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_plots_frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_plots_frame_main.setObjectName("AW_plots_frame_main")
                self.AW_plots_sub_0 = QtWidgets.QFrame(self.AW_plots_frame_main)
                self.AW_plots_sub_0.setGeometry(QtCore.QRect(20, 10, 681, 381))
                self.AW_plots_sub_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_plots_sub_0.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_plots_sub_0.setObjectName("AW_plots_sub_0")
                self.AW_sample_list = QtWidgets.QListWidget(self.AW_plots_sub_0)
                self.AW_sample_list.setGeometry(QtCore.QRect(6, 30, 331, 131))
                self.AW_sample_list.setStyleSheet("QListWidget{\n"
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
        "\n"
        "")
                self.AW_sample_list.setObjectName("AW_sample_list")
                self.AW_label_3 = QtWidgets.QLabel(self.AW_plots_sub_0)
                self.AW_label_3.setGeometry(QtCore.QRect(90, 0, 161, 16))
                self.AW_label_3.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_3.setObjectName("AW_label_3")
                self.AW_label_5 = QtWidgets.QLabel(self.AW_plots_sub_0)
                self.AW_label_5.setGeometry(QtCore.QRect(100, 180, 161, 16))
                self.AW_label_5.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_5.setObjectName("AW_label_5")
                self.AW_label_6 = QtWidgets.QLabel(self.AW_plots_sub_0)
                self.AW_label_6.setGeometry(QtCore.QRect(460, 180, 111, 16))
                self.AW_label_6.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_6.setObjectName("AW_label_6")
                self.AW_list_actions_main = QtWidgets.QFrame(self.AW_plots_sub_0)
                self.AW_list_actions_main.setGeometry(QtCore.QRect(350, 30, 331, 131))
                self.AW_list_actions_main.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);")
                self.AW_list_actions_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_list_actions_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_list_actions_main.setObjectName("AW_list_actions_main")
                self.BTN_clear_list = QtWidgets.QPushButton(self.AW_list_actions_main)
                self.BTN_clear_list.setGeometry(QtCore.QRect(20, 10, 121, 27))
                self.BTN_clear_list.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_clear_list.setObjectName("BTN_clear_list")

                self.BTN_gen_sign = QtWidgets.QPushButton(self.AW_list_actions_main)
                self.BTN_gen_sign.setGeometry(QtCore.QRect(180, 10, 121, 27))
                self.BTN_gen_sign.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_gen_sign.setObjectName("BTN_gen_sign")


                self.BTN_show_sample = QtWidgets.QPushButton(self.AW_list_actions_main)
                self.BTN_show_sample.setGeometry(QtCore.QRect(20, 90, 121, 27))
                self.BTN_show_sample.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_show_sample.setObjectName("BTN_show_sample")
                self.BTN_remove_sing = QtWidgets.QPushButton(self.AW_list_actions_main)
                self.BTN_remove_sing.setGeometry(QtCore.QRect(20, 50, 121, 27))
                self.BTN_remove_sing.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_remove_sing.setObjectName("BTN_remove_sing")
                self.AW_label_4 = QtWidgets.QLabel(self.AW_plots_sub_0)
                self.AW_label_4.setGeometry(QtCore.QRect(420, 0, 191, 20))
                self.AW_label_4.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_4.setObjectName("AW_label_4")
                self.AW_generated_sign_frame = QtWidgets.QFrame(self.AW_plots_sub_0)
                self.AW_generated_sign_frame.setGeometry(QtCore.QRect(6, 210, 331, 131))
                self.AW_generated_sign_frame.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);")
                self.AW_generated_sign_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_generated_sign_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_generated_sign_frame.setObjectName("AW_generated_sign_frame")

                self.AW_generated_sign_frame_plot = QtWidgets.QLabel(self.AW_generated_sign_frame)
                self.AW_generated_sign_frame_plot.setGeometry(QtCore.QRect(0, 0, 331, 131))
                #self.AW_generated_sign_frame_plot.setStyleSheet("border: none;")
                self.AW_generated_sign_frame_plot.setText("")
                self.AW_generated_sign_frame_plot.setScaledContents(True)
                self.AW_generated_sign_frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_generated_sign_frame_plot.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_generated_sign_frame_plot.setObjectName("AW_generated_sign_frame_plot")

                self.AW_spectral_signal_main = QtWidgets.QFrame(self.AW_plots_sub_0)
                self.AW_spectral_signal_main.setGeometry(QtCore.QRect(350, 210, 331, 131))
                self.AW_spectral_signal_main.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);")
                self.AW_spectral_signal_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_spectral_signal_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_spectral_signal_main.setObjectName("AW_spectral_signal_main")

                self.AW_spectral_signal_main_plot = QtWidgets.QLabel(self.AW_spectral_signal_main)
                self.AW_spectral_signal_main_plot.setGeometry(QtCore.QRect(0, 0, 331, 131))
                self.AW_spectral_signal_main_plot.setText("")
                self.AW_spectral_signal_main_plot.setScaledContents(True)
                self.AW_spectral_signal_main_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_spectral_signal_main_plot.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_spectral_signal_main_plot.setObjectName("AW_spectral_signal_main_plot")

                self.AW_logs = QtWidgets.QLabel(self.AW_plots_frame_main)
                self.AW_logs.setGeometry(QtCore.QRect(30, 370, 671, 51))
                self.AW_logs.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_logs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.AW_logs.setWordWrap(True)
                self.AW_logs.setObjectName("AW_logs")
                self.verticalLayout_3.addWidget(self.AW_plots_frame_main)
                self.Tab_widget.addTab(self.AS_widget, "")
                self.AW_widget = QtWidgets.QWidget()
                self.AW_widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                self.AW_widget.setObjectName("AW_widget")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.AW_widget)
                self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.AS_date_manage_main = QtWidgets.QFrame(self.AW_widget)
                self.AS_date_manage_main.setMaximumSize(QtCore.QSize(16777215, 150))
                self.AS_date_manage_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AS_date_manage_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AS_date_manage_main.setObjectName("AS_date_manage_main")
                self.AW_date_save_main_2 = QtWidgets.QFrame(self.AS_date_manage_main)
                self.AW_date_save_main_2.setGeometry(QtCore.QRect(368, 16, 332, 118))
                self.AW_date_save_main_2.setStyleSheet("border: 4px solid rgba(224, 17, 95, 0.5);")
                self.AW_date_save_main_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_date_save_main_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_date_save_main_2.setObjectName("AW_date_save_main_2")
                self.AW_label_7 = QtWidgets.QLabel(self.AW_date_save_main_2)
                self.AW_label_7.setGeometry(QtCore.QRect(10, 10, 311, 20))
                self.AW_label_7.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_7.setAlignment(QtCore.Qt.AlignCenter)
                self.AW_label_7.setObjectName("AW_label_7")
                self.BTN_FFT_2 = QtWidgets.QPushButton(self.AW_date_save_main_2)
                self.BTN_FFT_2.setGeometry(QtCore.QRect(30, 50, 131, 31))
                self.BTN_FFT_2.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_FFT_2.setObjectName("BTN_FFT_2")
                self.BTN_save_2 = QtWidgets.QPushButton(self.AW_date_save_main_2)
                self.BTN_save_2.setGeometry(QtCore.QRect(180, 50, 131, 31))
                self.BTN_save_2.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_save_2.setObjectName("BTN_save_2")
                self.AW_date_import_main_2 = QtWidgets.QFrame(self.AS_date_manage_main)
                self.AW_date_import_main_2.setGeometry(QtCore.QRect(26, 16, 332, 118))
                self.AW_date_import_main_2.setStyleSheet("border: 4px solid rgba(224, 17, 95, 0.5); ")
                self.AW_date_import_main_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_date_import_main_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_date_import_main_2.setObjectName("AW_date_import_main_2")
                self.AW_label_8 = QtWidgets.QLabel(self.AW_date_import_main_2)
                self.AW_label_8.setGeometry(QtCore.QRect(10, 10, 311, 20))
                self.AW_label_8.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_8.setAlignment(QtCore.Qt.AlignCenter)
                self.AW_label_8.setObjectName("AW_label_8")
                self.BTN_generate_2 = QtWidgets.QPushButton(self.AW_date_import_main_2)
                self.BTN_generate_2.setGeometry(QtCore.QRect(180, 50, 131, 31))
                self.BTN_generate_2.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_generate_2.setObjectName("BTN_generate_2")
                self.BTN_import_2 = QtWidgets.QPushButton(self.AW_date_import_main_2)
                self.BTN_import_2.setGeometry(QtCore.QRect(30, 50, 131, 31))
                self.BTN_import_2.setStyleSheet("border-radius: 6px;\n"
        "border: 2px solid rgb(132, 25, 34); \n"
        "font-size: 14px;\n"
        "\n"
        "font-family: Arial;\n"
        "background: rgb(224, 17, 95); ")
                self.BTN_import_2.setObjectName("BTN_import_2")
                self.verticalLayout_4.addWidget(self.AS_date_manage_main)
                self.AS_plots_frame_main = QtWidgets.QFrame(self.AW_widget)
                self.AS_plots_frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AS_plots_frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AS_plots_frame_main.setObjectName("AS_plots_frame_main")

                self.AW_spectral_signal_main_2 = QtWidgets.QFrame(self.AS_plots_frame_main)
                self.AW_spectral_signal_main_2.setGeometry(QtCore.QRect(370, 40, 331, 131))
                self.AW_spectral_signal_main_2.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);")
                self.AW_spectral_signal_main_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_spectral_signal_main_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_spectral_signal_main_2.setObjectName("AW_spectral_signal_main_2")

                self.AW_spectral_signal_main_2_plot = QtWidgets.QLabel(self.AW_spectral_signal_main_2)
                self.AW_spectral_signal_main_2_plot.setGeometry(QtCore.QRect(0, 0, 331, 131))
                self.AW_spectral_signal_main_2_plot.setText("")
                self.AW_spectral_signal_main_2_plot.setScaledContents(True)
                self.AW_spectral_signal_main_2_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_spectral_signal_main_2_plot.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_spectral_signal_main_2_plot.setObjectName("AW_spectral_signal_main_2_plot")


                self.AW_label_11 = QtWidgets.QLabel(self.AS_plots_frame_main)
                self.AW_label_11.setGeometry(QtCore.QRect(480, 10, 111, 16))
                self.AW_label_11.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_11.setObjectName("AW_label_11")
                self.AW_generated_sign_frame_2 = QtWidgets.QFrame(self.AS_plots_frame_main)
                self.AW_generated_sign_frame_2.setGeometry(QtCore.QRect(26, 40, 331, 131))
                self.AW_generated_sign_frame_2.setStyleSheet("border: 2px solid rgba(224, 17, 95, 0.5);")
                self.AW_generated_sign_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_generated_sign_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_generated_sign_frame_2.setObjectName("AW_generated_sign_frame_2")

                self.AW_generated_sign_frame_2_plot = QtWidgets.QLabel(self.AW_generated_sign_frame_2)
                self.AW_generated_sign_frame_2_plot.setGeometry(QtCore.QRect(0, 0, 331, 131))
                #self.AW_generated_sign_frame_2_plot.setStyleSheet("border: None;")
                self.AW_generated_sign_frame_2_plot.setText("")
                self.AW_generated_sign_frame_2_plot.setScaledContents(True)
                self.AW_generated_sign_frame_2_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.AW_generated_sign_frame_2_plot.setFrameShadow(QtWidgets.QFrame.Raised)
                self.AW_generated_sign_frame_2_plot.setObjectName("AW_generated_sign_frame_2_plot")
                



                self.AW_label_12 = QtWidgets.QLabel(self.AS_plots_frame_main)
                self.AW_label_12.setGeometry(QtCore.QRect(120, 10, 161, 16))
                self.AW_label_12.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AW_label_12.setObjectName("AW_label_12")
                self.AS_logs = QtWidgets.QLabel(self.AS_plots_frame_main)
                self.AS_logs.setGeometry(QtCore.QRect(30, 190, 671, 61))
                self.AS_logs.setStyleSheet("font-size: 14px;\n"
        "font-family: Arial;\n"
        "Color: white;\n"
        "border: None;")
                self.AS_logs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.AS_logs.setWordWrap(True)
                self.AS_logs.setObjectName("AS_logs")
                self.verticalLayout_4.addWidget(self.AS_plots_frame_main)
                self.Tab_widget.addTab(self.AW_widget, "")
                self.verticalLayout_2.addWidget(self.Tab_widget)
                self.verticalLayout.addWidget(self.Submain_frame)
                self.copy_label = QtWidgets.QLabel(self.centralwidget)
                self.copy_label.setStyleSheet("color: white;")
                self.copy_label.setObjectName("copy_label")
                self.verticalLayout.addWidget(self.copy_label)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.Tab_widget.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.button_events()

        def event_import_noise(self):
                self.db_N = self.IN.import_dialogue()

        def event_import_spectral(self):
                self.db_S = self.IS.import_dialogue()

        def event_generate_noise(self):
                self.EGN = Generate_Noise(self.AW_sample_list, self.mem_N, self.mem_SAMP)
                self.EGN.show()

        def event_FFT_execute(self):
                #Operacja FFT
                if self.fft_av:
                        plt.close('all')
                        dt = self.mem_SAMP[2]
                        x2 = self.mem_SAMP[1]
                        x1 = self.mem_SAMP[0]
                        Np = len(np.arange(0,1,dt))
                        t = np.arange(0,1,dt)

                        f_hat = fft(self.fft_sp, Np)
                        PSD = f_hat * np.conj(f_hat)/Np
                        freq = (1/(dt*Np))*np.arange(Np)
                        L = np.arange(1,np.floor(Np/2),dtype='int')

                        fp = plt.figure()
                        plt.plot(freq[L], PSD[L], color='r', label='Widmo')
                        plt.xlim(freq[L[0]],freq[L[-1]])
                        plt.show()
                        fp.set_figwidth(4)
                        fp.set_figheight(1)
                        plt.savefig(self.path+'/img_fft.jpeg')
                        pixmap_fft = QtGui.QPixmap(self.path+'/img_fft.jpeg')
                        self.AW_spectral_signal_main_plot.setPixmap(pixmap_fft)

                        self.fft_DB = pd.DataFrame({
                                "Hz": freq[L], 
                                "Amplituda":PSD[L]
                        })
                        print(self.fft_DB.head(5))
                        self.fft_done = True
                        
                        indices = PSD > 100
                        f_hat = indices*f_hat
                        fft_inv_db = [t,ifft(f_hat)]
                        self.fft_DB_memory.append([self.fft_DB, fft_inv_db,datetime.now()])

                        ind_idx = np.where(indices == True)
                        ind_str = ""
                        for i in ind_idx:
                                ind_str += f" {i}"
                        if len(ind_idx) > 0:
                                self.AW_logs.setText("Znalezono sygnały o częstoliwościach:" + ind_str)
                        else:
                                self.AW_logs.setText("Nie znalezono żadnych sygnałów w widmie")
                        

        def event_FFT_save(self):
                if self.fft_done:
                        self.filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', filter='*.csv')[0]
                        if self.filename == '':
                                pass
                        else:
                                
                                self.fft_DB.to_csv(self.filename, index = False)
                                print('Saved: '+self.filename)
                                self.AW_logs.setText("Zapiano w lokalizacji: "+self.filename)
                else:
                        self.AW_logs.setText("Nie zapisano FFT, wygeneruj widmo by następnie zapisać w formacie .csv")

        def event_iFFT_save(self):
                if self.fft_hat_done:
                        self.filename = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', filter='*.csv')[0]
                        if self.filename == '':
                                pass
                        else:
                                self.ifft_DB = pd.DataFrame({
                                        "Czas": self.fft_DB_to_inverse[0][1][0], 
                                        "Amplituda":self.fft_DB_to_inverse[0][1][1]
                                })
                                self.ifft_DB.to_csv(self.filename, index = False)
                                print('Saved: '+self.filename)
                                self.AS_logs.setText("Zapiano w lokalizacji: "+self.filename)
                else:
                        self.AS_logs.setText("Nie zapisano iFFT, wygeneruj widmo by następnie zapisać w formacie .csv")

        def event_clear_list(self):
                if self.AW_sample_list.count() > 0 and self.AW_sample_list is not None:
                        self.AW_sample_list.clear()
                        self.mem_N.clear()
                        self.AW_generated_sign_frame_plot.clear()
                        self.AW_spectral_signal_main_plot.clear()
                        self.fft_av = False
                        self.fft_done = False

        def event_remove_single(self):
                if len(self.AW_sample_list.selectedItems()) == 1 and self.AW_sample_list is not None:
                        idx = self.AW_sample_list.currentRow()
                        self.AW_sample_list.takeItem(idx)
                        del self.mem_N[idx]

        def event_show_sample_single(self):
                if self.AW_sample_list.count() > 0 and self.AW_sample_list is not None:
                        idx = self.AW_sample_list.currentRow()
                        fp = plt.figure()
                        plt.plot(self.mem_N[idx][0], self.mem_N[idx][1])
                        plt.show()
        
        def event_combine_spectral_plot(self):
                self.EGS = Generate_Spectral(self.fft_DB_memory, self.fft_DB_to_inverse, self.AW_generated_sign_frame_2_plot)
                self.EGS.show()

        def event_combine_noise_plot(self):
                if len(self.mem_N) > 0:
                        try:
                                #Pobranie dane pierwej próbki
                                plot_dx_temp = self.mem_N[0][0]
                                plot_dy_temp = self.mem_N[0][1]

                                if len(self.mem_N) > 1:
                                        for i in range(1, len(self.mem_N)):
                                                plot_dy_temp = np.add(plot_dy_temp, self.mem_N[i][1])
                                
                                plt.close('all')
                                fp = plt.figure()
                                plt.plot(plot_dx_temp, plot_dy_temp, color='r')
                                plt.xlim(plot_dx_temp[0], plot_dx_temp[-1])
                                fp.set_figwidth(4)
                                fp.set_figheight(1)
                                plt.draw()
                                plt.savefig(self.path+'/img_temp_main.jpeg')
                                pixmap_temp_gn = QtGui.QPixmap(self.path+'/img_temp_main.jpeg')
                                self.AW_generated_sign_frame_plot.setPixmap(pixmap_temp_gn)
                                plt.title("Wygenerowany szum")
                                plt.show()
                                self.fft_av = True
                                self.fft_sp = plot_dy_temp
                                
                        except:
                                self.fft_av = False
                                self.fft_done = False
                                self.AW_logs.setText("Nieprawidłowe dane szumów, Upewnij się, że wprowadzono odpowiednie próbkowanie oraz zakresy, muszą być jednakowe")

                else:
                        self.fft_av = False
                        self.fft_done = False
                        self.AW_logs.setText("Brak danych do FFT. Dodaj szum by następnie wykonać FFT")
        
        def event_iFFT_execute(self):
                if len(self.fft_DB_to_inverse) > 0:

                        t = self.fft_DB_to_inverse[0][1][0]
                        f_hat = self.fft_DB_to_inverse[0][1][1]
                        plt.close('all')
                        plt.plot(t, f_hat, color='r')
                        plt.xlabel("Czas (s)") 
                        plt.ylabel("Amplituda (-)")
                        plt.title("iFFT")
                        plt.show()
                        fp = plt.figure()
                        fp.set_figwidth(4)
                        fp.set_figheight(1)
                        plt.plot(t, f_hat, color='r')
                        plt.xlabel("") 
                        plt.ylabel("")
                        plt.savefig(self.path+'/img_temp_clean_ifft.jpeg')
                        pixmap_temp_gn = QtGui.QPixmap(self.path+'/img_temp_clean_ifft.jpeg')
                        self.AW_spectral_signal_main_2_plot.setPixmap(pixmap_temp_gn)
                        plt.title("")
                        self.fft_hat_done = True
                        self.AS_logs.setText("Wykonano odwróconą transforatę Fouriera iFFT")
                else:
                        self.fft_hat_done = False
                        self.AS_logs.setText("Brakuje widma w bazie danych, wygeneruj bądź zaimportuj widmo by nastepnie wykonać operację iFFT")

        def button_events(self):
                self.BTN_import.clicked.connect(self.event_import_noise)
                self.BTN_import_2.clicked.connect(self.event_import_spectral)
                self.BTN_gen_sign.clicked.connect(self.event_generate_noise)
                self.BTN_FFT.clicked.connect(self.event_FFT_execute)
                self.BTN_save.clicked.connect(self.event_FFT_save) 
                self.BTN_save_2.clicked.connect(self.event_iFFT_save) 
                self.BTN_clear_list.clicked.connect(self.event_clear_list)
                self.BTN_remove_sing.clicked.connect(self.event_remove_single)
                self.BTN_show_sample.clicked.connect(self.event_show_sample_single)
                self.BTN_generate.clicked.connect(self.event_combine_noise_plot)
                self.BTN_generate_2.clicked.connect(self.event_combine_spectral_plot)
                self.BTN_FFT_2.clicked.connect(self.event_iFFT_execute)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Transformata Fouriera"))
                self.AW_label_1.setText(_translate("MainWindow", "Próbki wejściowe"))
                self.BTN_generate.setText(_translate("MainWindow", "Generator szumu"))
                self.BTN_import.setText(_translate("MainWindow", "Importuj szum"))
                self.AW_label_2.setText(_translate("MainWindow", "Próbki wyjściowe"))
                self.BTN_FFT.setText(_translate("MainWindow", "Wykonaj FFT"))
                self.BTN_save.setText(_translate("MainWindow", "Zapisz wyniki"))
                self.AW_label_3.setText(_translate("MainWindow", "Lista próbek wejściowych"))
                self.AW_label_5.setText(_translate("MainWindow", "Wygenerowany szum"))
                self.AW_label_6.setText(_translate("MainWindow", "Sygnał widmowy"))
                self.BTN_clear_list.setText(_translate("MainWindow", "Wyczyść listę"))
                self.BTN_gen_sign.setText(_translate("MainWindow", "Dodaj szum"))
                self.BTN_show_sample.setText(_translate("MainWindow", "Podgląd próbki"))
                self.BTN_remove_sing.setText(_translate("MainWindow", "Usuń zaznaczony"))
                self.AW_label_4.setText(_translate("MainWindow", "Opreacje na próbkach z listy"))
                self.AW_logs.setText(_translate("MainWindow", "Logs"))
                self.Tab_widget.setTabText(self.Tab_widget.indexOf(self.AS_widget), _translate("MainWindow", "Analiza szumu"))
                self.AW_label_7.setText(_translate("MainWindow", "Próbki wyjściowe"))
                self.BTN_FFT_2.setText(_translate("MainWindow", "Wykonaj i-FFT"))
                self.BTN_save_2.setText(_translate("MainWindow", "Zapisz wyniki"))
                self.AW_label_8.setText(_translate("MainWindow", "Próbki wejściowe"))
                self.BTN_generate_2.setText(_translate("MainWindow", "Generator widma"))
                self.BTN_import_2.setText(_translate("MainWindow", "Importuj widmo"))
                self.AW_label_11.setText(_translate("MainWindow", "Sygnał pierwotny"))
                self.AW_label_12.setText(_translate("MainWindow", "Wygenerowane widmo"))
                self.AS_logs.setText(_translate("MainWindow", "Logs"))
                self.Tab_widget.setTabText(self.Tab_widget.indexOf(self.AW_widget), _translate("MainWindow", "Analiza widmowa"))
                self.copy_label.setText(_translate("MainWindow", " Copyright Ⓒ 2022 Grzegorz Jakimiuk. All Right Reserved"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
