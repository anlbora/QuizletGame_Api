from PyQt5 import QtGui, QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)  # Adjusted size to accommodate new elements
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        MainWindow.setStyleSheet("background-color: #375362;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.txt_score = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_score.setFont(font)
        self.txt_score.setStyleSheet("color: white;")
        self.txt_score.setTextFormat(QtCore.Qt.RichText)
        self.txt_score.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_score.setObjectName("txt_score")
        self.horizontalLayout_2.addWidget(self.txt_score)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.lbl_question = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_question.setFont(font)
        self.lbl_question.setStyleSheet("color: white;")
        self.lbl_question.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_question.setWordWrap(True)  # Enable word wrapping
        self.lbl_question.setObjectName("lbl_question")
        self.horizontalLayout_3.addWidget(self.lbl_question)
        self.verticalLayout_2.addWidget(self.groupBox)

        # Group box to hold option buttons
        self.options_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.options_groupbox.setTitle("")
        self.options_groupbox.setObjectName("options_groupbox")
        self.verticalLayout_options = QtWidgets.QVBoxLayout(self.options_groupbox)
        self.verticalLayout_options.setObjectName("verticalLayout_options")

        # Adding four option buttons
        self.option_buttons = []
        for i in range(4):
            btn = QtWidgets.QPushButton(self.options_groupbox)
            btn.setText(f"{i+1}")
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            btn.setStyleSheet("background-color: white; color: black; border: 1px solid gray; padding: 5px; font-size: 15px;")
            btn.setObjectName(f"btn_option_{i+1}")
            self.verticalLayout_options.addWidget(btn)
            self.option_buttons.append(btn)

        self.verticalLayout_2.addWidget(self.options_groupbox)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.btn_correct = QtWidgets.QPushButton(self.centralwidget)
        self.btn_correct.setAutoFillBackground(False)
        self.btn_correct.setStyleSheet("border: None;")
        self.btn_correct.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\OneDrive\\Masaüstü\\projects\\Quizlet\\images\\True.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_correct.setIcon(icon)
        self.btn_correct.setIconSize(QtCore.QSize(64, 64))
        self.btn_correct.setFlat(True)
        self.btn_correct.setObjectName("btn_correct")
        self.horizontalLayout.addWidget(self.btn_correct)
        
        self.btn_wrong = QtWidgets.QPushButton(self.centralwidget)
        self.btn_wrong.setAutoFillBackground(False)
        self.btn_wrong.setStyleSheet("border: None;")
        self.btn_wrong.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\OneDrive\\Masaüstü\\projects\\Quizlet\\images\\False.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_wrong.setIcon(icon1)
        self.btn_wrong.setIconSize(QtCore.QSize(64, 64))
        self.btn_wrong.setCheckable(False)
        self.btn_wrong.setAutoDefault(False)
        self.btn_wrong.setDefault(False)
        self.btn_wrong.setFlat(True)
        self.btn_wrong.setObjectName("btn_wrong")
        self.horizontalLayout.addWidget(self.btn_wrong)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quizlet"))
        self.txt_score.setText(_translate("MainWindow", "Score: 0"))
        self.lbl_question.setText(_translate("MainWindow", "Question"))
