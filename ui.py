# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sg-util.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGraphicsView, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(195, 586)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(195, 586))
        MainWindow.setMaximumSize(QSize(195, 586))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 100, 156, 148))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.EnableBloodHelper = QCheckBox(self.groupBox)
        self.EnableBloodHelper.setObjectName(u"EnableBloodHelper")
        self.EnableBloodHelper.setChecked(True)

        self.gridLayout.addWidget(self.EnableBloodHelper, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.CurrentBloodPicture = QGraphicsView(self.groupBox)
        self.CurrentBloodPicture.setObjectName(u"CurrentBloodPicture")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CurrentBloodPicture.sizePolicy().hasHeightForWidth())
        self.CurrentBloodPicture.setSizePolicy(sizePolicy1)
        self.CurrentBloodPicture.setMaximumSize(QSize(80, 21))

        self.gridLayout.addWidget(self.CurrentBloodPicture, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.MinBloodKeySelecter = QComboBox(self.groupBox)
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem(u"A")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.setObjectName(u"MinBloodKeySelecter")
        self.MinBloodKeySelecter.setMaximumSize(QSize(80, 21))
        self.MinBloodKeySelecter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinBloodKeySelecter.setEditable(False)

        self.gridLayout.addWidget(self.MinBloodKeySelecter, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.MinBloodPrecentageSelecter = QComboBox(self.groupBox)
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.setObjectName(u"MinBloodPrecentageSelecter")

        self.gridLayout.addWidget(self.MinBloodPrecentageSelecter, 3, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 260, 156, 121))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.EnableMagicHelper = QCheckBox(self.groupBox_2)
        self.EnableMagicHelper.setObjectName(u"EnableMagicHelper")
        self.EnableMagicHelper.setChecked(True)

        self.gridLayout_2.addWidget(self.EnableMagicHelper, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.CurrentMagicPicture = QGraphicsView(self.groupBox_2)
        self.CurrentMagicPicture.setObjectName(u"CurrentMagicPicture")
        self.CurrentMagicPicture.setMaximumSize(QSize(80, 21))

        self.gridLayout_2.addWidget(self.CurrentMagicPicture, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.MinMagicKeySelecter = QComboBox(self.groupBox_2)
        self.MinMagicKeySelecter.addItem("")
        self.MinMagicKeySelecter.addItem("")
        self.MinMagicKeySelecter.addItem("")
        self.MinMagicKeySelecter.setObjectName(u"MinMagicKeySelecter")
        self.MinMagicKeySelecter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MinMagicKeySelecter.setEditable(False)

        self.gridLayout_2.addWidget(self.MinMagicKeySelecter, 2, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 390, 151, 160))
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.Tick4 = QComboBox(self.groupBox_3)
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.setObjectName(u"Tick4")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Tick4)

        self.Tick2 = QComboBox(self.groupBox_3)
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.setObjectName(u"Tick2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.Tick2)

        self.Tick3 = QComboBox(self.groupBox_3)
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.setObjectName(u"Tick3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.Tick3)

        self.Tick1 = QComboBox(self.groupBox_3)
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.setObjectName(u"Tick1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.Tick1)

        self.StuckKeyStatus = QCheckBox(self.groupBox_3)
        self.StuckKeyStatus.setObjectName(u"StuckKeyStatus")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.StuckKeyStatus)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 10, 144, 86))
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.WindowSelecter = QComboBox(self.groupBox_4)
        self.WindowSelecter.setObjectName(u"WindowSelecter")
        self.WindowSelecter.setMaximumSize(QSize(80, 21))
        self.WindowSelecter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.WindowSelecter.setEditable(False)

        self.gridLayout_4.addWidget(self.WindowSelecter, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.CurrentRolePicture = QGraphicsView(self.groupBox_4)
        self.CurrentRolePicture.setObjectName(u"CurrentRolePicture")
        self.CurrentRolePicture.setMaximumSize(QSize(80, 21))
        self.CurrentRolePicture.setLineWidth(8)
        self.CurrentRolePicture.setInteractive(False)

        self.gridLayout_4.addWidget(self.CurrentRolePicture, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e09\u56fd\u9b54\u624b", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8840\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\uff1a", None))
        self.EnableBloodHelper.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8840\u6761\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u836f\u54c1\u680f\uff1a", None))
        self.MinBloodKeySelecter.setItemText(0, QCoreApplication.translate("MainWindow", u"R", None))
        self.MinBloodKeySelecter.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))
        self.MinBloodKeySelecter.setItemText(3, QCoreApplication.translate("MainWindow", u"B", None))
        self.MinBloodKeySelecter.setItemText(4, QCoreApplication.translate("MainWindow", u"C", None))
        self.MinBloodKeySelecter.setItemText(5, QCoreApplication.translate("MainWindow", u"D", None))
        self.MinBloodKeySelecter.setItemText(6, QCoreApplication.translate("MainWindow", u"Q", None))
        self.MinBloodKeySelecter.setItemText(7, QCoreApplication.translate("MainWindow", u"W", None))
        self.MinBloodKeySelecter.setItemText(8, QCoreApplication.translate("MainWindow", u"T", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u767e\u5206\u6bd4\uff1a", None))
        self.MinBloodPrecentageSelecter.setItemText(0, QCoreApplication.translate("MainWindow", u"40", None))
        self.MinBloodPrecentageSelecter.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.MinBloodPrecentageSelecter.setItemText(2, QCoreApplication.translate("MainWindow", u"60", None))
        self.MinBloodPrecentageSelecter.setItemText(3, QCoreApplication.translate("MainWindow", u"80", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u84dd\u91cf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\uff1a", None))
        self.EnableMagicHelper.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u84dd\u6761\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u836f\u54c1\u680f\uff1a", None))
        self.MinMagicKeySelecter.setItemText(0, QCoreApplication.translate("MainWindow", u"T", None))
        self.MinMagicKeySelecter.setItemText(1, QCoreApplication.translate("MainWindow", u"R", None))
        self.MinMagicKeySelecter.setItemText(2, QCoreApplication.translate("MainWindow", u"E", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5361\u952e Ctrl + ` \u542f\u7528", None))
        self.Tick4.setItemText(0, "")
        self.Tick4.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick4.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick4.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick4.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick4.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick4.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick4.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick4.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick4.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))

        self.Tick2.setItemText(0, "")
        self.Tick2.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick2.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick2.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick2.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick2.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick2.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick2.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick2.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick2.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))

        self.Tick3.setItemText(0, "")
        self.Tick3.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick3.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick3.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick3.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick3.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick3.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick3.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick3.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick3.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))

        self.Tick1.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick1.setItemText(1, "")
        self.Tick1.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick1.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick1.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick1.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick1.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick1.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick1.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick1.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))

        self.StuckKeyStatus.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\uff1a", None))
    # retranslateUi

