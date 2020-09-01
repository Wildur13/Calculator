# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_calculator(object):
    def setupUi(self, calculator):
        if not calculator.objectName():
            calculator.setObjectName(u"calculator")
        calculator.resize(320, 480)
        calculator.setMinimumSize(QSize(320, 480))
        calculator.setMaximumSize(QSize(320, 480))
        calculator.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayout = QGridLayout(calculator)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_mult = QPushButton(calculator)
        self.btn_mult.setObjectName(u"btn_mult")
        self.btn_mult.setMinimumSize(QSize(80, 60))
        self.btn_mult.setMaximumSize(QSize(80, 60))
        self.btn_mult.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mult.setFlat(True)

        self.gridLayout.addWidget(self.btn_mult, 4, 3, 1, 1)

        self.btn_6 = QPushButton(calculator)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setMinimumSize(QSize(80, 60))
        self.btn_6.setMaximumSize(QSize(80, 60))
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setFlat(True)

        self.gridLayout.addWidget(self.btn_6, 6, 2, 1, 1)

        self.btn_virgule = QPushButton(calculator)
        self.btn_virgule.setObjectName(u"btn_virgule")
        self.btn_virgule.setMinimumSize(QSize(80, 60))
        self.btn_virgule.setMaximumSize(QSize(80, 60))
        self.btn_virgule.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_virgule.setFlat(True)

        self.gridLayout.addWidget(self.btn_virgule, 8, 2, 1, 1)

        self.btn_div = QPushButton(calculator)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setMinimumSize(QSize(80, 60))
        self.btn_div.setMaximumSize(QSize(80, 60))
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_div.setFlat(True)

        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)

        self.btn_ln = QPushButton(calculator)
        self.btn_ln.setObjectName(u"btn_ln")
        self.btn_ln.setMinimumSize(QSize(80, 60))
        self.btn_ln.setMaximumSize(QSize(80, 60))
        self.btn_ln.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ln.setFlat(True)

        self.gridLayout.addWidget(self.btn_ln, 3, 2, 1, 1)

        self.btn_moins = QPushButton(calculator)
        self.btn_moins.setObjectName(u"btn_moins")
        self.btn_moins.setMinimumSize(QSize(80, 60))
        self.btn_moins.setMaximumSize(QSize(80, 60))
        self.btn_moins.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_moins.setFlat(True)

        self.gridLayout.addWidget(self.btn_moins, 5, 3, 1, 1)

        self.btn_3 = QPushButton(calculator)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(80, 60))
        self.btn_3.setMaximumSize(QSize(80, 60))
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3.setFlat(True)

        self.gridLayout.addWidget(self.btn_3, 7, 2, 1, 1)

        self.btn_egal = QPushButton(calculator)
        self.btn_egal.setObjectName(u"btn_egal")
        self.btn_egal.setMinimumSize(QSize(80, 120))
        self.btn_egal.setMaximumSize(QSize(80, 60))
        self.btn_egal.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_egal.setFlat(True)

        self.gridLayout.addWidget(self.btn_egal, 7, 3, 1, 1)

        self.btn_plus = QPushButton(calculator)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setMinimumSize(QSize(80, 60))
        self.btn_plus.setMaximumSize(QSize(80, 60))
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plus.setFlat(True)

        self.gridLayout.addWidget(self.btn_plus, 6, 3, 1, 1)

        self.resultat = QLineEdit(calculator)
        self.resultat.setObjectName(u"resultat")
        self.resultat.setMinimumSize(QSize(0, 30))
        self.resultat.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.resultat.setFont(font)
        self.resultat.setMouseTracking(True)
        self.resultat.setTabletTracking(True)
        self.resultat.setFrame(False)
        self.resultat.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.resultat.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.resultat, 1, 0, 1, 4)

        self.btn_sin = QPushButton(calculator)
        self.btn_sin.setObjectName(u"btn_sin")
        self.btn_sin.setMinimumSize(QSize(80, 60))
        self.btn_sin.setMaximumSize(QSize(80, 60))
        self.btn_sin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sin.setFlat(True)

        self.gridLayout.addWidget(self.btn_sin, 3, 0, 1, 1)

        self.btn_tan = QPushButton(calculator)
        self.btn_tan.setObjectName(u"btn_tan")
        self.btn_tan.setMinimumSize(QSize(80, 60))
        self.btn_tan.setMaximumSize(QSize(80, 60))
        self.btn_tan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tan.setFlat(True)

        self.gridLayout.addWidget(self.btn_tan, 4, 1, 1, 1)

        self.btn_log = QPushButton(calculator)
        self.btn_log.setObjectName(u"btn_log")
        self.btn_log.setMinimumSize(QSize(80, 60))
        self.btn_log.setMaximumSize(QSize(80, 60))
        self.btn_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log.setFlat(True)

        self.gridLayout.addWidget(self.btn_log, 4, 2, 1, 1)

        self.btn_9 = QPushButton(calculator)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setMinimumSize(QSize(80, 60))
        self.btn_9.setMaximumSize(QSize(80, 60))
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_9.setFlat(True)

        self.gridLayout.addWidget(self.btn_9, 5, 2, 1, 1)

        self.btn_del = QPushButton(calculator)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMinimumSize(QSize(80, 60))
        self.btn_del.setMaximumSize(QSize(80, 60))
        self.btn_del.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_del.setFlat(True)

        self.gridLayout.addWidget(self.btn_del, 2, 0, 1, 1)

        self.bt_cos = QPushButton(calculator)
        self.bt_cos.setObjectName(u"bt_cos")
        self.bt_cos.setMinimumSize(QSize(80, 60))
        self.bt_cos.setMaximumSize(QSize(80, 60))
        self.bt_cos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cos.setFlat(True)

        self.gridLayout.addWidget(self.bt_cos, 3, 1, 1, 1)

        self.btn_carrerac = QPushButton(calculator)
        self.btn_carrerac.setObjectName(u"btn_carrerac")
        self.btn_carrerac.setMinimumSize(QSize(80, 60))
        self.btn_carrerac.setMaximumSize(QSize(80, 60))
        self.btn_carrerac.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_carrerac.setFlat(True)

        self.gridLayout.addWidget(self.btn_carrerac, 4, 0, 1, 1)

        self.operation = QLineEdit(calculator)
        self.operation.setObjectName(u"operation")
        self.operation.setMinimumSize(QSize(0, 30))
        self.operation.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.operation.setFont(font1)
        self.operation.setFrame(False)
        self.operation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.operation, 0, 0, 1, 4)

        self.btn_1 = QPushButton(calculator)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(80, 60))
        self.btn_1.setMaximumSize(QSize(80, 60))
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_1.setFlat(True)

        self.gridLayout.addWidget(self.btn_1, 7, 0, 1, 1)

        self.btn_2 = QPushButton(calculator)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(80, 60))
        self.btn_2.setMaximumSize(QSize(80, 60))
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2.setFlat(True)

        self.gridLayout.addWidget(self.btn_2, 7, 1, 1, 1)

        self.btn_0 = QPushButton(calculator)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setMinimumSize(QSize(80, 60))
        self.btn_0.setMaximumSize(QSize(80, 60))
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_0.setFlat(True)

        self.gridLayout.addWidget(self.btn_0, 8, 1, 1, 1)

        self.btn_pourcentage = QPushButton(calculator)
        self.btn_pourcentage.setObjectName(u"btn_pourcentage")
        self.btn_pourcentage.setMinimumSize(QSize(80, 60))
        self.btn_pourcentage.setMaximumSize(QSize(80, 60))
        self.btn_pourcentage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pourcentage.setFlat(True)

        self.gridLayout.addWidget(self.btn_pourcentage, 8, 0, 1, 1)

        self.btn_8 = QPushButton(calculator)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setMinimumSize(QSize(80, 60))
        self.btn_8.setMaximumSize(QSize(80, 60))
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_8.setFlat(True)

        self.gridLayout.addWidget(self.btn_8, 5, 1, 1, 1)

        self.btn_5 = QPushButton(calculator)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(80, 60))
        self.btn_5.setMaximumSize(QSize(80, 60))
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5.setFlat(True)

        self.gridLayout.addWidget(self.btn_5, 6, 1, 1, 1)

        self.pushButton = QPushButton(calculator)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 60))
        self.pushButton.setMaximumSize(QSize(80, 60))
        self.pushButton.setFlat(True)

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.btn_7 = QPushButton(calculator)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setMinimumSize(QSize(80, 60))
        self.btn_7.setMaximumSize(QSize(80, 60))
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_7.setFlat(True)

        self.gridLayout.addWidget(self.btn_7, 5, 0, 1, 1)

        self.btn_4 = QPushButton(calculator)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(80, 60))
        self.btn_4.setMaximumSize(QSize(80, 60))
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4.setFlat(True)

        self.gridLayout.addWidget(self.btn_4, 6, 0, 1, 1)

        self.btn_reset = QPushButton(calculator)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(80, 60))
        self.btn_reset.setMaximumSize(QSize(80, 60))
        self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset.setFlat(True)

        self.gridLayout.addWidget(self.btn_reset, 2, 3, 1, 1)

        self.btn_par_d = QPushButton(calculator)
        self.btn_par_d.setObjectName(u"btn_par_d")
        self.btn_par_d.setMinimumSize(QSize(80, 60))
        self.btn_par_d.setFlat(True)

        self.gridLayout.addWidget(self.btn_par_d, 2, 2, 1, 1)


        self.retranslateUi(calculator)

        self.btn_par_d.setDefault(False)


        QMetaObject.connectSlotsByName(calculator)
    # setupUi

    def retranslateUi(self, calculator):
        calculator.setWindowTitle(QCoreApplication.translate("calculator", u"calculator", None))
        self.btn_mult.setText(QCoreApplication.translate("calculator", u"*", None))
        self.btn_6.setText(QCoreApplication.translate("calculator", u"6", None))
        self.btn_virgule.setText(QCoreApplication.translate("calculator", u".", None))
        self.btn_div.setText(QCoreApplication.translate("calculator", u"/", None))
        self.btn_ln.setText(QCoreApplication.translate("calculator", u"ln", None))
        self.btn_moins.setText(QCoreApplication.translate("calculator", u"-", None))
        self.btn_3.setText(QCoreApplication.translate("calculator", u"3", None))
        self.btn_egal.setText(QCoreApplication.translate("calculator", u"=", None))
        self.btn_plus.setText(QCoreApplication.translate("calculator", u"+", None))
        self.resultat.setText("")
        self.btn_sin.setText(QCoreApplication.translate("calculator", u"sin", None))
        self.btn_tan.setText(QCoreApplication.translate("calculator", u"tan", None))
        self.btn_log.setText(QCoreApplication.translate("calculator", u"log", None))
        self.btn_9.setText(QCoreApplication.translate("calculator", u"9", None))
        self.btn_del.setText(QCoreApplication.translate("calculator", u"Del", None))
        self.bt_cos.setText(QCoreApplication.translate("calculator", u"cos", None))
        self.btn_carrerac.setText(QCoreApplication.translate("calculator", u"\u221a", None))
        self.btn_1.setText(QCoreApplication.translate("calculator", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("calculator", u"2", None))
        self.btn_0.setText(QCoreApplication.translate("calculator", u"0", None))
        self.btn_pourcentage.setText(QCoreApplication.translate("calculator", u"%", None))
        self.btn_8.setText(QCoreApplication.translate("calculator", u"8", None))
        self.btn_5.setText(QCoreApplication.translate("calculator", u"5", None))
        self.pushButton.setText(QCoreApplication.translate("calculator", u"Inv", None))
        self.btn_7.setText(QCoreApplication.translate("calculator", u"7", None))
        self.btn_4.setText(QCoreApplication.translate("calculator", u"4", None))
        self.btn_reset.setText(QCoreApplication.translate("calculator", u"AC", None))
        self.btn_par_d.setText(QCoreApplication.translate("calculator", u")", None))
    # retranslateUi

