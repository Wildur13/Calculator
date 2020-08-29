from PySide2 import QtGui, QtWidgets
from functools import partial
# from antlr4 import Lexer, Parser, ParseTreeVisitor
from calcul.calculatorS import Ui_calculator
import math


class Calculator(Ui_calculator, QtWidgets.QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.btns_nombres = []
        self.setupUi(self)
        self.buttonPressed()
        self.modificationSetupUi()
        self.setupConnections()
        self.setupRaccourciClavier()
        self.css()
        self.show()

    def modificationSetupUi(self):

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setStyleSheet('QPushButton:hover {color: blue;'
                                     'background-color: white;}')
                # widget.setFont(Custom_font)
            if isinstance(widget, QtWidgets.QPushButton) and widget.text().isdigit():
                self.btns_nombres.append(widget)

    def setupConnections(self):
        for btn in self.btns_nombres:
            btn.clicked.connect(partial(self.btnNombrePressed, str(btn.text())))

        self.btn_moins.clicked.connect(partial(self.btnOperationPressed, str(self.btn_moins.text())))
        self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
        self.btn_mult.clicked.connect(partial(self.btnOperationPressed, str(self.btn_mult.text())))
        self.btn_div.clicked.connect(partial(self.btnOperationPressed, str(self.btn_div.text())))
        self.btn_virgule.clicked.connect(partial(self.btnOperationPressed, str(self.btn_virgule.text())))
        self.btn_del.clicked.connect(self.buttonPressed)
        self.btn_carrerac.clicked.connect(self.wurzel)
        self.btn_sin.clicked.connect(self.sin)
        self.bt_cos.clicked.connect(self.cos)
        self.btn_tan.clicked.connect(self.tan)
        self.btn_log.clicked.connect(self.log)
        self.btn_ln.clicked.connect(self.ln)
        self.btn_pourcentage.clicked.connect(partial(self.btnOperationPressed, str(self.btn_pourcentage.text())))
        self.pushButton.clicked.connect(self.inversed)

        self.btn_egal.clicked.connect(self.calculOperation)
        self.btn_reset.clicked.connect(self.supprimerResultat)

    def setupRaccourciClavier(self):
        for btn in range(10):
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.btnNombrePressed, str(btn)))

        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_plus.text())), self, partial(self.btnOperationPressed, str(self.btn_plus.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_moins.text())), self, partial(self.btnOperationPressed, str(self.btn_moins.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_div.text())), self, partial(self.btnOperationPressed, str(self.btn_div.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_mult.text())), self, partial(self.btnOperationPressed, str(self.btn_mult.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self, self.calculOperation)
        QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self, self.supprimerResultat)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)
        QtWidgets.QShortcut(QtGui.QKeySequence('.'), self, partial(self.btnOperationPressed, str(self.btn_virgule.text())))

    def buttonPressed(self):
        get = str(self.resultat.text())
        if len(get) == 1:
            self.resultat.setText('0')
        else:
            self.resultat.setText(get[:-1])

    def inversed(self):
        state = self.pushButton.text()
        if state == 'Inv':
            self.bt_cos.setText('cos^-1')
            self.btn_sin.setText('sin^-1')
            self.btn_tan.setText('tan^-1')
            self.btn_ln.setText('e^x')
            self.btn_log.setText('10^x')
            self.pushButton.setText('inv')
        else:
            self.bt_cos.setText('cos')
            self.btn_sin.setText('sin')
            self.btn_tan.setText('tan')
            self.btn_ln.setText('ln')
            self.btn_log.setText('log')
            self.pushButton.setText('Inv')

    def btnNombrePressed(self, bouton):
        """Activated when we press 0 .. 9"""

        # On recupere le texte dans le LineEdit resultat
        resultats = str(self.resultat.text())

        if resultats == '0' or resultats == '':
            # Si le resultat est egal a 0 on met le nombre du bouton
            # que l'utilisateur a presse dans le LineEdit resultat
            self.resultat.setText(bouton)
        else:
            # Si le resultat contient autre chose que zero,
            # On ajoute le texte du bouton a celui dans le LineEdit resultat
            self.resultat.setText(resultats + bouton)

    def btnOperationPressed(self, operation):
        """
        Fonction activee quand l'utilisateur appuie sur
        une touche d'operation (+, -, /, *)
        """

        # On recupere le texte dans le LineEdit operation
        operationText = str(self.operation.text())
        # On recupere le texte dans le LineEdit resultat
        resultats = str(self.resultat.text())

        # On additionne l'operation en cours avec le texte dans le resultat
        # et on ajoute a la fin le signe de l'operation qu'on a choisie
        self.resultat.setText(operationText + resultats + operation)

    def wurzel(self):
        get = (self.resultat.text())
        self.operation.setText('√' + str(get))
        res = str(math.sqrt(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def sin(self):
        state = self.btn_sin.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'sin':
            res = str(math.sin(eval(str(get))))
        else:
            res = str(math.asin(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def cos(self):
        state = self.bt_cos.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'cos':
            res = str(math.cos(eval(str(get))))
        else:
            res = str(math.acos(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def tan(self):
        state = self.btn_tan.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'tan':
            res = str(math.tan(eval(str(get))))
        else:
            res = str(math.atan(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def log(self):
        state = self.btn_log.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'log':
            res = str(math.log10(eval(str(get))))
        else:
            res = str(math.pow(10, eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def ln(self):
        state = self.btn_ln.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'ln':
            res = str(math.log(eval(str(get)), 2.7182818281))
        else:
            res = str(math.pow(10, eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def supprimerResultat(self):
        """On reset le texte des deux LineEdit"""

        self.resultat.setText('0')
        self.operation.setText('')

    def calculOperation(self):
        # On recupere le texte dans le LineEdit resultat
        resultats = str(self.resultat.text())

        # On ajoute le nombre actuel dans le LineEdit resultat
        # au LineEdit operation
        str(self.operation.setText(self.operation.text() + resultats))
        res = self.operation.text()
        # On evalue le resultat de l'operation
        if res.endswith('%'):
            resultatOperation = str(float(res[:-1]) / 100)
            if resultatOperation.endswith('.0'):
                self.resultat.setText(resultatOperation[:-2])
            else:
                self.resultat.setText(str(resultatOperation))
        else:
            resultatOperation = str(eval(str(res)))
            if resultatOperation.endswith('.0'):
                self.resultat.setText(str(resultatOperation[:-2]))
            else:
                self.resultat.setText(str(resultatOperation))

    def css(self):
        self.setStyleSheet('''
        background-color: gray;
        ''')
        self.resultat.setStyleSheet('''
        background-color: white;
        color: red;
        ''')
        self.operation.setStyleSheet('''
        background-color: white;
        ''')


app = QtWidgets.QApplication([])
win = Calculator()
app.exec_()
