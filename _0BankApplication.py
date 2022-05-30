from _1Manager import Ui_Manager
from _2Representative import Ui_Represent
from _3Customer import Ui_Customer
from _5Diagram import Ui_diagram
from _6Login import Ui_loginpage
from random import randint
from bs4 import BeautifulSoup
from lxml.etree import HTML
from requests import get
from sys import exit, argv
from time import sleep
from numpy_financial import pmt
from datetime import datetime
from dateutil.relativedelta import relativedelta
from mysql.connector import Error
import _4DatabaseConnection
from PyQt5.QtGui import QRegExpValidator, QPixmap, QIcon, QColor, QDesktopServices
from PyQt5.QtCore import (
    QRegExp,
    QPropertyAnimation,
    Qt,
    QEasingCurve,
    QThread,
    pyqtSignal,
    QUrl,
)
from PyQt5.QtWidgets import (
    QLineEdit,
    QTableWidgetItem,
    QApplication,
    QWidget,
    QMainWindow,
    QMessageBox,
    QGraphicsDropShadowEffect as effect,
    QGraphicsOpacityEffect as glory,
)


class ThreadClass(QThread):
    any_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.is_running = True

    def run(self):
        cnt = 0
        while True:
            cnt += 0
            if cnt == 100:
                cnt = 0
            sleep(0.5)
            self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        self.terminate()


class Managerpage(QMainWindow, Ui_Manager):
    showborder = 1
    msstart = 0
    msfinish = 20

    def __init__(self, tc_no, password):
        super(Managerpage, self).__init__()
        self.setupUi(self)
        self.tc_no = tc_no
        self.password = password
        self.logout.clicked.connect(self.close)
        intreg = QRegExp("^[0-9]{11}$")
        integervalidator = QRegExpValidator(intreg, self)
        strreg = QRegExp("^[a-z-A-Z ]{30}$")
        stringvalidator = QRegExpValidator(strreg, self)
        payreg = QRegExp("^[0-9.]{11}$")
        payregvalidator = QRegExpValidator(payreg, self)
        self.creditedit.setValidator(payregvalidator)
        self.overdueedit.setValidator(payregvalidator)
        self.salaryedit.setValidator(payregvalidator)
        self.citizenman.setValidator(integervalidator)
        self.passwordman.setValidator(integervalidator)
        self.confirmpasswordman.setValidator(integervalidator)
        self.telephoneman.setValidator(integervalidator)
        self.name_surnameman.setValidator(stringvalidator)
        self.revealinfo()
        self.searchline.textChanged.connect(self.search)

        self._4customeraddinfo.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.cresalFrame.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.currencyFrame.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.monthlystatements.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.card1.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card2.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card3.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card4.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.profileframe.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.rightMenu.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.leftMenu.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.registerbuttonman.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )

        self.savestatiko.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.addmorestate.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.addcurrency.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.savecurrency.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.profilebutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.custaddbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )

        self.deadlockcontrol.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.advanceSystem.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.coolguy.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.incomeicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.expenseicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.profiticon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.balanceicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.creditsicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.statementicon.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.currencyicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))

        self.coolguy.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.custaddbutton.clicked.connect(self.custaddmenu)
        self.profilebutton.clicked.connect(self.profilMenu)
        self.addmorestate.clicked.connect(self.monthlystatementsxxzz)
        self.savestatiko.clicked.connect(self.updateproblem)
        self.addcurrency.clicked.connect(self.currencyadding)
        self.savecurrency.clicked.connect(self.currencyproblem)
        self.deadlockcontrol.clicked.connect(self.deadlockshow)

    def search(self, s):
        self.statementtable.setCurrentItem(None)
        if not s:
            return
        matching_items = self.statementtable.findItems(
            s, Qt.MatchContains
        )  # MatchExactly
        if matching_items:
            item = matching_items[0]
            self.statementtable.setCurrentItem(item)

    def deadlockshow(self):
        count = self.statementtable.rowCount()
        liste = []
        deadlist = []
        for i in range(0, count):
            liste.append(
                (
                    self.statementtable.item(i, 0).text(),
                    self.statementtable.item(i, 1).text(),
                )
            )
            deadlist.append(
                (
                    self.statementtable.item(i, 1).text(),
                    self.statementtable.item(i, 0).text(),
                )
            )
        deadlock = []
        for x in range(0, len(liste)):
            for y in range(0, len(deadlist)):
                if liste[x][0] != liste[x][1]:
                    if liste[x] == deadlist[y]:
                        deadlock.append((int(x + 1), deadlist[y], int(y + 1)))
        deadlist.clear()
        liste.clear()

        for a in deadlock:
            liste.append(deadlock.index((a[2], (a[1][1], a[1][0]), a[0])))
        critical = []
        for q in range(0, len(liste)):
            if (q, liste[q]) not in critical and (liste[q], q) not in critical:
                critical.append((q, liste[q]))
        problem = []
        for x in critical:
            deadlist.append((deadlock[x[0]], deadlock[x[1]]))
            problem.append(deadlock[x[0]][0])
        count = 0
        deadlock.clear()
        xx = []
        for x in problem:
            if problem.count(x) == 1:
                xx.append((f"({deadlist[count][0][0]}-{deadlist[count][1][0]})"))
                item = self.statementtable.item(deadlist[count][1][0], 1)
                icon6 = QIcon()
                icon6.addPixmap(
                    QPixmap(":/Images/assets/icons/deadlock.png"),
                    QIcon.Normal,
                    QIcon.Off,
                )
                item.setIcon(icon6)
            if problem.count(x) == 2:
                xx.append((f"({deadlist[count][0][0]}-{deadlist[count][1][0]})"))
                item = self.statementtable.item(deadlist[count][1][0], 1)
                icon6 = QIcon()
                icon6.addPixmap(
                    QPixmap(":/Images/assets/icons/deadlock.png"),
                    QIcon.Normal,
                    QIcon.Off,
                )
                item.setIcon(icon6)
            count += 1

        QMessageBox.about(
            self,
            "Deadlock",
            '<p><span style=" font-size:12pt; font-weight:600;">Deadlock Counts:'
            + str(len(xx))
            + '\n</span></p><p><span style=" font-size:12pt; font-weight:600;">Transactions:'
            + str(xx)
            + "</span></p>",
        )

    def custaddmenu(self):
        width = self.leftMenu.maximumWidth()
        if width == 0:
            newWidth = 220
            Managerpage.showborder *= 3
        else:
            newWidth = 0
            Managerpage.showborder = int(Managerpage.showborder / 3)
        self.animation = QPropertyAnimation(self.leftMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        allwidth = self.allframes.maximumWidth()
        if Managerpage.showborder % 5 == 0 and Managerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);}"
            )
            newmainwidth = 1152
        if Managerpage.showborder % 5 != 0 and Managerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-right-radius:20px;border-bottom-right-radius:20px;}"
            )
            newmainwidth = 970
        if Managerpage.showborder % 5 == 0 and Managerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-left-radius:20px;border-bottom-left-radius:20px;}"
            )
            newmainwidth = 935
        if Managerpage.showborder % 5 != 0 and Managerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
            )
            newmainwidth = 750
        self.problem = QPropertyAnimation(self.allframes, b"maximumWidth")
        self.problem.setDuration(500)
        self.problem.setStartValue(allwidth)
        self.problem.setEndValue(newmainwidth)
        self.problem.setEasingCurve(QEasingCurve.InOutQuart)
        self.problem.start()

    def profilMenu(self):
        width = self.rightMenu.maximumWidth()
        if width == 0:
            newWidth = 220
            Managerpage.showborder *= 5
        else:
            newWidth = 0
            Managerpage.showborder = int(Managerpage.showborder / 5)

        self.animation = QPropertyAnimation(self.rightMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        allwidth = self.allframes.maximumWidth()

        if Managerpage.showborder % 5 == 0 and Managerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-left-radius:20px;border-bottom-left-radius:20px;}"
            )
            newmainwidth = 970
        if Managerpage.showborder % 5 != 0 and Managerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-right-radius:20px;border-bottom-right-radius:20px;}"
            )
            newmainwidth = 935
        if Managerpage.showborder % 5 == 0 and Managerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);}"
            )
            newmainwidth = 1152
        if Managerpage.showborder % 5 != 0 and Managerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
            )
            newmainwidth = 750
        self.problem = QPropertyAnimation(self.allframes, b"maximumWidth")
        self.problem.setDuration(500)
        self.problem.setStartValue(allwidth)
        self.problem.setEndValue(newmainwidth)
        self.problem.setEasingCurve(QEasingCurve.InOutQuart)
        self.problem.start()

    def monthlystatementsxxzz(self):
        tablecontents = []
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date FROM  _5statements as ms ORDER BY ms.Date ASC"""
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()
            for i in result:
                x = str(i[6])
                tablecontents.append(
                    (
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[3]),
                        str(i[4]),
                        str(i[5]),
                        x[0:10],
                    )
                )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        if Managerpage.msstart > len(tablecontents) or Managerpage.msfinish > len(
            tablecontents
        ):
            Managerpage.msfinish = len(tablecontents)
            pass
        if Managerpage.msstart < len(tablecontents) or Managerpage.msfinish < len(
            tablecontents
        ):
            self.statementtable.setRowCount(Managerpage.msfinish)
            for info in range(Managerpage.msstart, Managerpage.msfinish):
                self.statementtable.setItem(
                    info, 0, QTableWidgetItem(tablecontents[info][0])
                )
                self.statementtable.setItem(
                    info, 1, QTableWidgetItem(tablecontents[info][1])
                )
                self.statementtable.setItem(
                    info, 2, QTableWidgetItem(tablecontents[info][2])
                )
                self.statementtable.setItem(
                    info, 3, QTableWidgetItem(tablecontents[info][3])
                )
                self.statementtable.setItem(
                    info, 4, QTableWidgetItem(tablecontents[info][4])
                )
                self.statementtable.setItem(
                    info, 5, QTableWidgetItem(tablecontents[info][5])
                )
                self.statementtable.setItem(
                    info, 6, QTableWidgetItem(tablecontents[info][6])
                )
            Managerpage.msstart += 20
            Managerpage.msfinish += 20

    def clientsadder(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT p.Citizenship_No FROM _0personalinfo AS p WHERE Citizenship_No!=%s"""
        params = (self.tc_no,)
        cursor.execute(sqlsyn, params)
        resultyy = cursor.fetchall()
        for rep in resultyy:
            sqlsyn = (
                """SELECT p.W_C FROM _1customerinfo AS p WHERE Citizenship_No!=%s"""
            )
            params = (rep[0],)
            cursor.execute(sqlsyn, params)
            resultxx = cursor.fetchall()
            customers = []
            for cus in resultxx:
                customers.append(int(cus[0]))
        myList = []
        for rep in resultyy:
            myList.append((rep[0], customers.count(rep[0])))

        myList = list(dict.fromkeys(myList))

        def takeSecond(elem):
            return elem[1]

        myList.sort(key=takeSecond, reverse=False)
        mySql_insert_query = """INSERT INTO  _1customerinfo (Name,Surname, Tel_No, Citizenship_No, Adress, E_mail, Password, W_C) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            self.name_surnameman.text().split()[0],
            self.name_surnameman.text().split()[1],
            int(self.telephoneman.text()),
            int(self.citizenman.text()),
            self.addressman.text(),
            self.emailman.text(),
            int(self.passwordman.text()),
            myList[0][0],
        )
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """SELECT Acco_No FROM _2status ORDER BY Acco_No ASC"""
        cursor.execute(mySql_insert_query)
        systemaccounts = []
        try:
            result = cursor.fetchall()
            for i in result:
                systemaccounts.append(int(i[0]))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """INSERT INTO  _2status (Citizenship_No,Acco_No, Income, Expense, Total_Balance, currency) VALUES(%s,%s,%s,%s,%s,%s)"""
        a = randint(10000000, 99999999)
        if systemaccounts.count(a) > 0:
            a = randint(10000000, 99999999)
            if systemaccounts.count(a) > 0:
                a = randint(10000000, 99999999)
                if systemaccounts.count(a) > 0:
                    a = randint(10000000, 99999999)

        to_insert = (int(self.citizenman.text()), a, 0, 0, 0, 3)
        cursor.execute(mySql_insert_query, to_insert)
        try:
            connection.commit()

        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.name_surnameman.setText("")
        self.telephoneman.setText("")
        self.citizenman.setText("")
        self.addressman.setText("")
        self.emailman.ssetText("")
        self.passwordman.setText("")
        self.confirmpasswordman.setText("")

    def updateproblem(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        salary = float(self.salaryedit.text())
        interest = float(self.creditedit.text())
        late = float(self.overdueedit.text())
        sqlxx = "UPDATE _0persalary SET Salary =%s WHERE id=%s"
        params = (salary, 0)
        cursor.execute(sqlxx, params)
        connection.commit()
        sqlxx = "UPDATE _7rates SET Credit_Rate =%s WHERE id=%s"
        params = (interest, 1)
        cursor.execute(sqlxx, params)
        connection.commit()
        sqlxx = "UPDATE _7rates SET Overdue_Rate =%s WHERE id=%s"
        params = (late, 1)
        cursor.execute(sqlxx, params)
        connection.commit()
        creditIncomes = []
        sqlsyn = """SELECT Installment FROM _3creditsstarter WHERE Approval_Status=%s"""
        params = ("Approved",)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            for res in result:
                creditIncomes.append(float(res[0]))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        totalIncomes = 0
        for i in creditIncomes:
            totalIncomes += i
        sqlxx = "UPDATE _2status SET Income=%s,Expense =%s WHERE Acco_No=%s"
        params = ((totalIncomes), (salary * 5), 99999999)
        cursor.execute(sqlxx, params)
        connection.commit()

    def currencyadding(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        a = int(self.currenciestable.rowCount())
        self.currenciestable.setRowCount(a + 2)
        x = str(self.currencies.currentData())
        y = str(self.currencies.currentText())
        item1 = QTableWidgetItem(x)
        icon6 = QIcon()
        icon6.addPixmap(
            QPixmap(":/Images/assets/moneys/" + x + ".png"),
            QIcon.Normal,
            QIcon.Off,
        )
        item1.setIcon(icon6)
        self.currenciestable.setItem(a + 1, 0, item1)
        self.currenciestable.setItem(a + 1, 1, QTableWidgetItem(y))
        mySql_insert_query = """INSERT INTO  _6currency (Type, Worth) VALUES(%s,%s)"""
        values = (
            x,
            y,
        )
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.currenciestable.removeRow(a)
        self.currencies.removeItem(self.currencies.currentIndex())

    def currencyproblem(self):
        currencies = []
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        for i in range(0, int(self.currenciestable.rowCount())):
            a = str(self.currenciestable.item(i, 0).text())
            b = float(self.currenciestable.item(i, 1).text())
            currencies.append((a, b, a))
        sqlxx = "UPDATE _6currency SET Type=%s ,Worth =%s WHERE Type=%s"
        params = currencies
        cursor.executemany(sqlxx, params)
        connection.commit()

    def revealinfo(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT st.Income,st.Expense,st.Total_Balance FROM _0personalinfo AS p INNER JOIN _1customerinfo AS c INNER JOIN _2status as st ON c.W_C  = p.Citizenship_No AND c.Citizenship_No=st.Citizenship_No WHERE p.Citizenship_No=%s and p.Password=%s  and c.Citizenship_No=%s"""
        params = (self.tc_no, self.password, 99999999999)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
            cinfo = {}
            cinfo.update(
                {
                    "Income": round(float(result[0]), 2),
                    "Expense": round(float(result[1]), 2),
                    "Profit": round(float(result[0] - result[1]), 2),
                    "Total": round(float(result[2]), 2),
                }
            )
            self.incomeclient.setText("  " + str(cinfo["Income"]) + "₺")
            self.expenseclient.setText("  " + str(cinfo["Expense"]) + "₺")
            self.profitclient.setText("  " + str(cinfo["Profit"]) + "₺")
            self.totalclient.setText("  " + str(cinfo["Total"]) + "₺")
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT cr.Credit_Rate, cr.Overdue_Rate FROM _7rates AS cr"""
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()
            if len(result) > 0:
                self.creditedit.setText(str(float(result[0][0])))
                self.overdueedit.setText(str(float(result[0][1])))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT cr.Salary FROM _0persalary AS cr"""
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()
            if len(result) > 0:
                self.salaryedit.setText(str(float(result[0][0])))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT MAX(cr.id) FROM _6currency AS cr"""
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()

        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        currenciexs = []

        sqlsyn = """SELECT cr.id, cr.Type, cr.Worth FROM  _6currency AS cr WHERE id>1 ORDER BY cr.id ASC """
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()
            if len(result) > 0:
                self.currenciestable.setRowCount(int(result[0][0] - 3))
                for info in range(0, len(result)):
                    item1 = QTableWidgetItem(str(result[info][1]))
                    icon6 = QIcon()
                    icon6.addPixmap(
                        QPixmap(
                            ":/Images/assets/moneys/" + str(result[info][1]) + ".png"
                        ),
                        QIcon.Normal,
                        QIcon.Off,
                    )
                    item1.setIcon(icon6)
                    self.currenciestable.setItem(info, 0, item1)
                    self.currenciestable.setItem(
                        info, 1, QTableWidgetItem(str(result[info][2]))
                    )
                    currenciexs.append((str(result[info][1]), result[info][2]))

        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT MAX(cr.id) FROM  _6currency AS cr"""
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()
            maxid = result[0][0]
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        currencykeys = [
            "AUD",
            "BGN",
            "CAD",
            "CNY",
            "CZK",
            "DKK",
            "EUR",
            "HUF",
            "INR",
            "JPY",
            "KRW",
            "KWD",
            "PLN",
            "QAR",
            "RUB",
            "CHF",
            "GBP",
            "USD",
        ]
        URL = "https://www.x-rates.com/table/?from=TRY&amount=1"

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        }

        webpage = get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        dom = HTML(str(soup))
        currencyrate = {}
        for x in range(1, 54):
            for y in currencykeys:
                if (
                    dom.xpath(
                        '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr['
                        + str(x)
                        + "]/td[3]/a//@href"
                    )[0][36:39]
                    == y
                ):
                    currencyrate.update(
                        {
                            dom.xpath(
                                '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr['
                                + str(x)
                                + "]/td[3]/a//@href"
                            )[0][36:39]: {
                                "country": dom.xpath(
                                    '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr['
                                    + str(x)
                                    + "]/td[1]"
                                )[0].text,
                                "worth": dom.xpath(
                                    '//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr['
                                    + str(x)
                                    + "]/td[3]/a"
                                )[0].text,
                            }
                        }
                    )
        for q in currenciexs:
            currencyrate.pop(q[0])
        for x, y in currencyrate.items():
            a = str(round(float(y["worth"]), 2))
            self.currencies.addItem(
                QIcon(":/Images/assets/moneys/" + x + ".png"), a, str(x)
            )


class RepresentPage(QMainWindow, Ui_Represent):
    showborder = 1
    creditstate = []
    monthy = []
    msstart = 0
    msfinish = 5
    paymentdate = 0

    def __init__(self, tc_no, password):
        super(RepresentPage, self).__init__()
        self.tc_no = tc_no
        self.password = password
        self.setupUi(self)
        self.logout.clicked.connect(self.close)
        intreg = QRegExp("^[0-9]{11}$")
        integervalidator = QRegExpValidator(intreg, self)
        strreg = QRegExp("^[a-z-A-Z ]{30}$")
        stringvalidator = QRegExpValidator(strreg, self)
        payreg = QRegExp("^[0-9.]{11}$")
        payregvalidator = QRegExpValidator(payreg, self)
        self.telephonerep.setValidator(integervalidator)
        self.passwordrep.setValidator(integervalidator)
        self.confirmpasswordrep.setValidator(integervalidator)
        self.citizenrep.setValidator(integervalidator)
        self.name_surnamerep.setValidator(stringvalidator)

        self._4customeraddinfo.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.clientFrame.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.demandlFrame.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0, color=QColor(0, 0, 0, 255))
        )
        self.monthlystatements.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.card1.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card2.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card3.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card4.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.profileframe.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.rightMenu.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.leftMenu.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.registerbuttonrep.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )

        self.saveclients.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.addmorestate.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.deleteclients.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.addclients.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.demandapprove.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.demanddeny.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.delstate.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.profilebutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.custaddbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.coolguy.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.incomeicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.expenseicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.profiticon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.balanceicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.demandsicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.statementicon.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.personicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.coolguy.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.custaddbutton.clicked.connect(self.custaddmenu)
        self.profilebutton.clicked.connect(self.profilMenu)
        self.information()
        self.addclients.clicked.connect(self.clientsshower)
        self.saveclients.clicked.connect(self.clientssaver)
        self.registerbuttonrep.clicked.connect(self.clientsadder)
        self.deleteclients.clicked.connect(self.clientsdeleter)
        self.demandapprove.clicked.connect(self.installment)
        self.demanddeny.clicked.connect(self.denialapprove)
        self.addmorestate.clicked.connect(self.monthlystatementsxxxx)
        self.delstate.clicked.connect(self.monthdeletion)

    def information(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT p.Name,p.Surname, c.Name,c.Surname,c.Citizenship_No FROM _0personalinfo AS p INNER JOIN _1customerinfo AS c ON c.W_C = p.Citizenship_No  WHERE p.Citizenship_No=%s and p.Password=%s"""
        params = (self.tc_no, self.password)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            for i in result:
                self.username.setText("   " + str(i[0]) + " " + str(i[1]))
                self.selectclients.addItem((str(i[2]) + str(i[3])), i[4])
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT c.Name,c.Surname,cs.Money,cs.Month,c.Citizenship_No FROM _0personalinfo AS p INNER JOIN _1customerinfo AS c INNER JOIN _3creditsstarter AS cs ON c.W_C = p.Citizenship_No AND c.Citizenship_No=cs.Citizenship_No  WHERE p.Citizenship_No=%s AND p.Password=%s AND cs.Approval_Status=%s"""
        params = (self.tc_no, self.password, "Processing")
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            for i in result:
                self.demandsbox.addItem(
                    (
                        str(i[0])
                        + " "
                        + str(i[1])
                        + " "
                        + str(i[2])
                        + "₺ "
                        + str(i[3])
                        + " months"
                    ),
                    str(i[4]),
                )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def clientsshower(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT c.Name,c.Surname, c.Tel_No, c.Citizenship_No, c.Adress, c.E_mail,st.Acco_No,st.Income,st.Expense,st.Total_Balance,cr.Worth FROM _0personalinfo AS p INNER JOIN _1customerinfo AS c INNER JOIN _2status as st INNER JOIN _6currency as cr ON c.W_C  = p.Citizenship_No AND c.Citizenship_No=st.Citizenship_No AND st.Currency=cr.id WHERE p.Citizenship_No=%s and p.Password=%s  and c.Citizenship_No=%s"""
        params = (self.tc_no, self.password, self.selectclients.currentData())
        try:
            cinfo = {}
            accounts = []
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            toplamincomes = 0
            toplamexpenses = 0
            toplamprofits = 0
            toplamtotal_balances = 0
            a = len(result)
            for i in result:
                cinfo.update(
                    {
                        "Name_Surname": i[0] + " " + i[1],
                        "Tel_No": int(i[2]),
                        "Citizenship_No": int(i[3]),
                        "Adress": i[4],
                        "E_mail": i[5],
                    }
                )
            for i in range(0, a):
                accounts.append(
                    (
                        int(result[i][6]),
                        int(result[i][7]),
                        int(result[i][8]),
                        int(result[i][9]),
                        int(result[i][10]),
                    )
                )
            for i in range(0, a):
                if accounts[i][4] > 1.00:
                    toplamincomes += accounts[i][1] * accounts[i][4]
                    toplamexpenses += accounts[i][2] * accounts[i][4]
                    toplamprofits += (accounts[i][1] - accounts[i][2]) * accounts[i][4]
                    toplamtotal_balances += accounts[i][3] * accounts[i][4]
                else:
                    toplamincomes += accounts[i][1]
                    toplamexpenses += accounts[i][2]
                    toplamprofits += accounts[i][1] - accounts[i][2]
                    toplamtotal_balances += accounts[i][3]
            cinfo.update(
                {
                    "Income": toplamincomes,
                    "Expense": toplamexpenses,
                    "Profit": toplamprofits,
                    "Total": toplamtotal_balances,
                }
            )
            self.incomeclient.setText("  " + str(cinfo["Income"]) + "₺")
            self.expenseclient.setText("  " + str(cinfo["Expense"]) + "₺")
            self.profitclient.setText("  " + str(cinfo["Profit"]) + "₺")
            self.totalclient.setText("  " + str(cinfo["Total"]) + "₺")
            self.nameclient.setText("  " + str(cinfo["Name_Surname"]))
            self.telephoneclient.setText("  " + str(cinfo["Tel_No"]))
            self.citizenclient.setText("   " + str(cinfo["Citizenship_No"]))
            self.adressclient.setText("  " + str(cinfo["Adress"]))
            self.emailclient.setText("  " + str(cinfo["E_mail"]))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def clientsadder(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO  _1customerinfo (Name,Surname, Tel_No, Citizenship_No, Adress, E_mail, Password, W_C) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            self.name_surnamerep.text().split()[0],
            self.name_surnamerep.text().split()[1],
            int(self.telephonerep.text()),
            int(self.citizenrep.text()),
            self.addressrep.text(),
            self.emailrep.text(),
            int(self.passwordrep.text()),
            self.tc_no,
        )
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """SELECT Acco_No FROM _2status ORDER BY Acco_No ASC"""
        cursor.execute(mySql_insert_query)
        systemaccounts = []
        try:
            result = cursor.fetchall()
            for i in result:
                systemaccounts.append(int(i[0]))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """INSERT INTO  _2status (Citizenship_No,Acco_No, Income, Expense, Total_Balance, currency) VALUES(%s,%s,%s,%s,%s,%s)"""
        a = randint(10000000, 99999999)
        if systemaccounts.count(a) > 0:
            a = randint(10000000, 99999999)
            if systemaccounts.count(a) > 0:
                a = randint(10000000, 99999999)
                if systemaccounts.count(a) > 0:
                    a = randint(10000000, 99999999)

        to_insert = (int(self.citizenrep.text()), a, 0, 0, 0, 3)
        cursor.execute(mySql_insert_query, to_insert)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.name_surnamerep.setText("")
        self.telephonerep.setText("")
        self.citizenrep.setText("")
        self.addressrep.setText("")
        self.emailrep.ssetText("")
        self.passwordrep.setText("")
        self.confirmpasswordrep.setText("")

    def clientssaver(self):
        mydb = _4DatabaseConnection.mydb
        mycursor = mydb.cursor()
        sqlxx = "UPDATE _1customerinfo SET Tel_No=%s, Adress=%s, E_mail=%s WHERE Citizenship_No = %s"
        params = (
            int(self.telephoneclient.text()),
            self.adressclient.text().strip(),
            self.emailclient.text().strip(),
            self.citizenclient.text(),
        )
        mycursor.execute(sqlxx, params)
        try:
            mydb.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def clientsdeleter(self):
        self.selectclients.removeItem(self.selectclients.currentIndex())
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = (
            "DELETE FROM _1customerinfo INNER JOIN _2status WHERE Citizenship_No = %s"
        )
        params = (self.citizenclient.text().strip(),)
        try:
            cursor.execute(sqlsyn, params)
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def custaddmenu(self):
        width = self.leftMenu.maximumWidth()
        if width == 0:
            newWidth = 220
            RepresentPage.showborder *= 3
        else:
            newWidth = 0
            RepresentPage.showborder = int(RepresentPage.showborder / 3)
        self.animation = QPropertyAnimation(self.leftMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        allwidth = self.allframes.maximumWidth()
        if RepresentPage.showborder % 5 == 0 and RepresentPage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);}"
            )
            newmainwidth = 1152
        if RepresentPage.showborder % 5 != 0 and RepresentPage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-right-radius:20px;border-bottom-right-radius:20px;}"
            )
            newmainwidth = 970
        if RepresentPage.showborder % 5 == 0 and RepresentPage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-left-radius:20px;border-bottom-left-radius:20px;}"
            )
            newmainwidth = 935
        if RepresentPage.showborder % 5 != 0 and RepresentPage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
            )
            newmainwidth = 780
        self.problem = QPropertyAnimation(self.allframes, b"maximumWidth")
        self.problem.setDuration(500)
        self.problem.setStartValue(allwidth)
        self.problem.setEndValue(newmainwidth)
        self.problem.setEasingCurve(QEasingCurve.InOutQuart)
        self.problem.start()

    def profilMenu(self):
        width = self.rightMenu.maximumWidth()
        if width == 0:
            newWidth = 220
            RepresentPage.showborder *= 5
        else:
            newWidth = 0
            RepresentPage.showborder = int(RepresentPage.showborder / 5)

        self.animation = QPropertyAnimation(self.rightMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        allwidth = self.allframes.maximumWidth()

        if RepresentPage.showborder % 5 == 0 and RepresentPage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-left-radius:20px;border-bottom-left-radius:20px;}"
            )
            newmainwidth = 970
        if RepresentPage.showborder % 5 != 0 and RepresentPage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-right-radius:20px;border-bottom-right-radius:20px;}"
            )
            newmainwidth = 935
        if RepresentPage.showborder % 5 == 0 and RepresentPage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);}"
            )
            newmainwidth = 1152
        if RepresentPage.showborder % 5 != 0 and RepresentPage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
            )
            newmainwidth = 750
        self.problem = QPropertyAnimation(self.allframes, b"maximumWidth")
        self.problem.setDuration(500)
        self.problem.setStartValue(allwidth)
        self.problem.setEndValue(newmainwidth)
        self.problem.setEasingCurve(QEasingCurve.InOutQuart)
        self.problem.start()

    def installment(self):
        a = self.demandsbox.currentData()
        self.demandsbox.removeItem(self.demandsbox.currentIndex())
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = (
            "SELECT cs.Money,cs.Month,cs.id FROM _3creditsstarter AS cs WHERE Citizenship_No=%s"
            ""
        )
        params = (a,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT cr.Credit_Rate FROM _7rates AS cr WHERE id='1'"""
        try:
            cursor.execute(sqlsyn)
            resultxxq = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        RUSFRATE = 0.15
        BITTRATE = 0.05
        INTERESTRATE = float(resultxxq[0]) / 100
        CREDIT = int(result[0])
        MONTH = int(result[1])
        INSTALLMENT = round(
            pmt(INTERESTRATE * (1 + RUSFRATE + BITTRATE), MONTH, -CREDIT, 0), 2
        )
        now = datetime.now().date()
        for i in range(1, MONTH + 1):
            xx = now + relativedelta(months=i)
            RepresentPage.monthy.append(xx)
        RepresentPage.creditinterest(
            int(result[2]), INSTALLMENT, CREDIT, MONTH, INTERESTRATE, RUSFRATE, BITTRATE
        )
        sqlxx = "UPDATE _3creditsstarter SET Approval_Status=%s WHERE id = %s"
        params = ("Approved", result[2])
        cursor.execute(sqlxx, params)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    @classmethod
    def creditinterest(
        self, idx, INSTALLMENT, CREDIT, MONTH, INTERESTRATE, RUSFRATE, BITTRATE
    ):
        INTEREST = round((CREDIT * INTERESTRATE), 2)  # FAIZ
        RUSF = round(INTEREST * RUSFRATE, 2)  # KKDF
        BITT = round(INTEREST * BITTRATE, 2)  # BSMV
        PRINCIPAL = round(INSTALLMENT - INTEREST - RUSF - BITT, 3)
        CREDIT = round(CREDIT - PRINCIPAL, 2)
        if MONTH > 0:
            if CREDIT <= 0:
                RepresentPage.creditstate.append(
                    (
                        MONTH,
                        idx,
                        float(PRINCIPAL),
                        float(INTEREST),
                        float(RUSF),
                        float(BITT),
                        float(0),
                        "Unpaid",
                        RepresentPage.monthy[RepresentPage.paymentdate],
                    )
                )
                RepresentPage.paymentdate += 1
            else:
                RepresentPage.creditstate.append(
                    (
                        MONTH,
                        idx,
                        float(PRINCIPAL),
                        float(INTEREST),
                        float(RUSF),
                        float(BITT),
                        float(CREDIT),
                        "Unpaid",
                        RepresentPage.monthy[RepresentPage.paymentdate],
                    )
                )
                RepresentPage.paymentdate += 1

        if CREDIT > 0:
            MONTH -= 1
            self.creditinterest(
                idx, INSTALLMENT, CREDIT, MONTH, INTERESTRATE, RUSFRATE, BITTRATE
            )
        else:
            self.creditsprint(RepresentPage.creditstate)
            RepresentPage.paymentdate = 0
            return 1

    @classmethod
    def creditsprint(self, list):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO  _4credits (Month,id, Principal, Interest, RUSF, BITT, Remaining_debt,Payment_Status,Due_Date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = list
        cursor.executemany(mySql_insert_query, values)
        try:
            connection.commit()

        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        RepresentPage.creditstate.clear()

    def denialapprove(self):
        a = self.demandsbox.currentData()
        self.demandsbox.removeItem(self.demandsbox.currentIndex())
        mydb = _4DatabaseConnection.mydb
        mycursor = mydb.cursor()
        sqlxx = (
            "UPDATE _3creditsstarter SET Approval_Status=%s WHERE Citizenship_No = %s"
        )
        params = ("Denied", 0, a)
        mycursor.execute(sqlxx, params)
        try:
            mydb.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def monthlystatementsxxxx(self):
        tablecontents = []
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date FROM _0personalinfo AS p INNER JOIN _1customerinfo AS c INNER JOIN _2status as st INNER JOIN _5statements as ms ON c.W_C  = p.Citizenship_No AND c.Citizenship_No=st.Citizenship_No AND st.Acco_No=ms.Target_No  WHERE p.Citizenship_No=%s and p.Password=%s  and c.Citizenship_No=%s ORDER BY ms.Date ASC"""
        params = (self.tc_no, self.password, self.selectclients.currentData())
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            for i in result:
                x = str(i[6])
                tablecontents.append(
                    (
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[3]),
                        str(i[4]),
                        str(i[5]),
                        x[0:10],
                    )
                )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date FROM _0personalinfo AS p INNER JOIN _1customerinfo AS c INNER JOIN _2status as st INNER JOIN _5statements as ms ON c.W_C  = p.Citizenship_No AND c.Citizenship_No=st.Citizenship_No AND st.Acco_No=ms.Source_No  WHERE p.Citizenship_No=%s and p.Password=%s  and c.Citizenship_No=%s ORDER BY ms.Date ASC"""
        params = (self.tc_no, self.password, self.selectclients.currentData())
        try:

            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            for i in result:
                x = str(i[6])
                tablecontents.append(
                    (
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[3]),
                        str(i[4]),
                        str(i[5]),
                        x[0:10],
                    )
                )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.statementtable.setRowCount(RepresentPage.msfinish)
        if RepresentPage.msfinish > len(tablecontents) or RepresentPage.msstart > len(
            tablecontents
        ):
            for info in range(RepresentPage.msstart, len(tablecontents) - 1):
                self.statementtable.setItem(
                    info, 0, QTableWidgetItem(tablecontents[info][0])
                )
                self.statementtable.setItem(
                    info, 1, QTableWidgetItem(tablecontents[info][1])
                )
                self.statementtable.setItem(
                    info, 2, QTableWidgetItem(tablecontents[info][2])
                )
                self.statementtable.setItem(
                    info, 3, QTableWidgetItem(tablecontents[info][3])
                )
                self.statementtable.setItem(
                    info, 4, QTableWidgetItem(tablecontents[info][4])
                )
                self.statementtable.setItem(
                    info, 5, QTableWidgetItem(tablecontents[info][5])
                )
                self.statementtable.setItem(
                    info, 6, QTableWidgetItem(tablecontents[info][6])
                )
        else:
            for info in range(RepresentPage.msstart, RepresentPage.msfinish):
                self.statementtable.setItem(
                    info, 0, QTableWidgetItem(tablecontents[info][0])
                )
                self.statementtable.setItem(
                    info, 1, QTableWidgetItem(tablecontents[info][1])
                )
                self.statementtable.setItem(
                    info, 2, QTableWidgetItem(tablecontents[info][2])
                )
                self.statementtable.setItem(
                    info, 3, QTableWidgetItem(tablecontents[info][3])
                )
                self.statementtable.setItem(
                    info, 4, QTableWidgetItem(tablecontents[info][4])
                )
                self.statementtable.setItem(
                    info, 5, QTableWidgetItem(tablecontents[info][5])
                )
                self.statementtable.setItem(
                    info, 6, QTableWidgetItem(tablecontents[info][6])
                )
        RepresentPage.msstart += 5
        RepresentPage.msfinish += 5

    def monthdeletion(self):
        self.statementtable.setRowCount(0)
        RepresentPage.msstart = 0
        RepresentPage.msfinish = 5


class Customerpage(QMainWindow, Ui_Customer):
    showborder = 1
    msstart = 0
    msfinish = 5

    def __init__(self, tc_no, password):
        super(Customerpage, self).__init__()
        self.setupUi(self)
        self.tc_no = tc_no
        self.password = password
        self.revealinfo()
        self.logout.clicked.connect(self.close)
        intreg = QRegExp("^[0-9]{11}$")
        integervalidator = QRegExpValidator(intreg, self)
        strreg = QRegExp("^[a-z-A-Z ]{30}$")
        stringvalidator = QRegExpValidator(strreg, self)
        payreg = QRegExp("^[0-9.]{11}$")
        payregvalidator = QRegExpValidator(payreg, self)
        self.creditbalance.setValidator(payregvalidator)
        self.depositbalance.setValidator(payregvalidator)
        self.takeoutbalance.setValidator(payregvalidator)
        self.withdrawbalance.setValidator(payregvalidator)
        self.transferaccountno.setValidator(integervalidator)
        self.transferbalance.setValidator(payregvalidator)
        self.transfernamesurname.setValidator(stringvalidator)
        self.leftMenu.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.rightMenu.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self._4customeraddinfo.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.profileframe.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card1.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card2.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card3.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.card4.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.creditsFrame.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.statements.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.transfertitle.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.frame.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.credit.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.delaccount.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.deposit.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.moneytransfer.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.newaccount.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.takeout.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.withdraw.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.alltransactions.setGraphicsEffect(
            effect(blurRadius=25, xOffset=0, yOffset=0)
        )
        self.creditbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.delbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.depositbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.transferbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.accoopenbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.takeoutbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.withdrawbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.transbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.profilebutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.trainbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.addmorestate.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.cusbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.coolguy.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.myProfile.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.incomeicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.expenseicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.profiticon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.balanceicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.creditsicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.statementicon.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.transacicon.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.transbutton.clicked.connect(self.transactions)
        self.trainbutton.clicked.connect(self.transactionsmenus)
        self.profilebutton.clicked.connect(self.profilMenu)
        self.withdraw.hide()
        self.deposit.hide()
        self.moneytransfer.hide()
        self.takeout.hide()
        self.credit.hide()
        self.newaccount.hide()
        self.delaccount.hide()
        self.takeouttype.activated.connect(self.takeoutproblem)
        self.paymenttype.activated.connect(self.paymentproblem)
        self.withdrawbutton.clicked.connect(self.withdrawtrans)
        self.depositbutton.clicked.connect(self.deposittrans)
        self.transferbutton.clicked.connect(self.transfermoney)
        self.takeoutbutton.clicked.connect(self.takeoutcredit)
        self.accoopenbutton.clicked.connect(self.newaccountopen)
        self.creditbutton.clicked.connect(self.creditpayment)
        self.addmorestate.clicked.connect(self.monthlystatementsxxyy)
        self.myProfile.clicked.connect(self.custoinfo)
        self.delbutton.clicked.connect(self.accountdeletion)

    def transactionsmenus(self):
        width = self.leftMenu.maximumWidth()
        if width == 0:
            newWidth = 220
            Customerpage.showborder *= 3
        else:
            newWidth = 0
            Customerpage.showborder = int(Customerpage.showborder / 3)
        self.animation = QPropertyAnimation(self.leftMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        allwidth = self.allframes.maximumWidth()
        if Customerpage.showborder % 5 == 0 and Customerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);}"
            )
            newmainwidth = 1180
        if Customerpage.showborder % 5 != 0 and Customerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-right-radius:20px;border-bottom-right-radius:20px;}"
            )
            newmainwidth = 960
        if Customerpage.showborder % 5 == 0 and Customerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-left-radius:20px;border-bottom-left-radius:20px;}"
            )
            newmainwidth = 960
        if Customerpage.showborder % 5 != 0 and Customerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
            )
            newmainwidth = 740
        self.problem = QPropertyAnimation(self.allframes, b"maximumWidth")
        self.problem.setDuration(500)
        self.problem.setStartValue(allwidth)
        self.problem.setEndValue(newmainwidth)
        self.problem.setEasingCurve(QEasingCurve.InOutQuart)
        self.problem.start()

    def profilMenu(self):
        width = self.rightMenu.maximumWidth()
        if width == 0:
            newWidth = 220
            Customerpage.showborder *= 5
        else:
            newWidth = 0
            Customerpage.showborder = int(Customerpage.showborder / 5)

        self.animation = QPropertyAnimation(self.rightMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        allwidth = self.allframes.maximumWidth()
        if Customerpage.showborder % 5 == 0 and Customerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);}"
            )
            newmainwidth = 1180
        if Customerpage.showborder % 5 != 0 and Customerpage.showborder % 3 == 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-right-radius:20px;border-bottom-right-radius:20px;}"
            )
            newmainwidth = 960
        if Customerpage.showborder % 5 == 0 and Customerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-top-left-radius:20px;border-bottom-left-radius:20px;}"
            )
            newmainwidth = 960
        if Customerpage.showborder % 5 != 0 and Customerpage.showborder % 3 != 0:
            self.mainBody.setStyleSheet(
                "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
            )
            newmainwidth = 740
        self.problem = QPropertyAnimation(self.allframes, b"maximumWidth")
        self.problem.setDuration(500)
        self.problem.setStartValue(allwidth)
        self.problem.setEndValue(newmainwidth)
        self.problem.setEasingCurve(QEasingCurve.InOutQuart)
        self.problem.start()

    def withdrawtrans(self):
        now = datetime.now().date()
        money_amount = int(self.withdrawbalance.text())
        acco_no = int(self.withdrawaccotype.currentText())
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT st.Total_Balance,cr.Worth FROM  _2status AS st INNER JOIN _6currency as cr ON cr.id=st.Currency WHERE st.Acco_No=%s"""
        params = (acco_no,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        currency = float(result[1])
        moneyhave = float(result[0]) * currency
        sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
        params = (int((moneyhave - money_amount) / (currency)), acco_no)
        cursor.execute(sqlxx, params)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """INSERT INTO _5statements (Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            acco_no,
            acco_no,
            "Withdraw",
            money_amount,
            int((moneyhave - money_amount) / (currency)),
            0,
            now,
        )
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
            print(
                cursor.rowcount, "Record inserted successfully into _5statements table"
            )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.withdrawbalance.setText("")
        self.revealinfo()

    def transfermoney(self):
        now = datetime.now().date()
        money_amount = int(self.transferbalance.text())
        acco_no = int(self.traaccotype.currentText())
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT st.Total_Balance,cr.Worth FROM  _2status AS st INNER JOIN _6currency as cr ON cr.id=st.Currency WHERE st.Acco_No=%s"""
        params = (acco_no,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        currency = float(result[1])
        moneyhave = float(result[0]) * currency
        sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
        params = (int((moneyhave - money_amount) / (currency)), acco_no)
        cursor.execute(sqlxx, params)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        acco_no2 = int(self.transferaccountno.text())
        sqlsyn = """SELECT st.Total_Balance,cr.Worth FROM  _2status AS st INNER JOIN _6currency as cr ON cr.id=st.Currency WHERE st.Acco_No=%s"""
        params = (acco_no2,)
        try:
            cursor.execute(sqlsyn, params)
            result2 = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        currency2 = float(result2[1])
        moneyhave2 = float(result2[0]) * currency2
        sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
        params = (int((moneyhave2 + money_amount) / (currency2)), acco_no2)
        cursor.execute(sqlxx, params)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """INSERT INTO _5statements (Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            acco_no,
            acco_no2,
            "Transfer",
            money_amount,
            int((moneyhave - money_amount) / (currency)),
            int((moneyhave2 + money_amount) / (currency2)),
            now,
        )
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.transferbalance.setText("")
        self.explanation.setText("")
        self.transferaccountno.setText("")
        self.transfernamesurname.setText("")
        self.revealinfo()

    def deposittrans(self):
        now = datetime.now().date()
        money_amount = int(self.depositbalance.text())
        acco_no = int(self.depositaccotype.currentText())
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT st.Total_Balance,cr.Worth FROM  _2status AS st INNER JOIN _6currency as cr ON cr.id=st.Currency WHERE st.Acco_No=%s"""
        params = (acco_no,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        currency = float(result[1])
        moneyhave = float(result[0]) * currency
        sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
        params = ((moneyhave + money_amount) / (currency), acco_no)
        cursor.execute(sqlxx, params)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """INSERT INTO _5statements (Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            acco_no,
            acco_no,
            "Withdraw",
            money_amount,
            int((moneyhave + money_amount) / (currency)),
            0,
            now,
        )
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.depositbalance.setText("")
        self.revealinfo()

    def takeoutcredit(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO _3creditsstarter (Citizenship_No, Money, Month,Approval_Status,Rates) VALUES(%s,%s,%s,%s,%s)"""
        values = (
            self.tc_no,
            self.takeoutbalance.text(),
            self.takeoutmonths.currentText(),
            "Processing",
            1,
        )
        cursor.execute(mySql_insert_query, values)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def creditpayment(self):
        now = datetime.now().date()
        acco_no = int(self.creditaccotype.currentText())
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor(buffered=True)
        sqlsyn = """SELECT st.Total_Balance,cr.Worth FROM  _2status AS st INNER JOIN _6currency as cr ON cr.id=st.Currency WHERE st.Acco_No=%s"""
        params = (acco_no,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT MAX(cr.Month) FROM  _1customerinfo AS c INNER JOIN _3creditsstarter AS cs INNER JOIN _4credits AS cr ON c.Citizenship_No  = cs.Citizenship_No AND cs.id=cr.id WHERE c.Citizenship_No=%s AND cr.Payment_Status=%s ORDER BY cr.Month DESC"""
        params = (self.tc_no, "Unpaid")
        try:
            cursor.execute(sqlsyn, params)
            resultxx = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        month = int(resultxx[0])
        sqlsyn = (
            "SELECT cs.Money,cs.Month,cs.id FROM _3creditsstarter AS cs WHERE Citizenship_No=%s"
            ""
        )
        params = (self.tc_no,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchone()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        id = result[2]
        installment = float(self.creditnecessary.text())
        currency = float(result[1])
        moneyhave = round(float(result[0]) * currency, 2)
        moneygive = round(float(self.creditbalance.text()), 2)
        x = self.paymenttype.currentIndex()
        if x == 0 and moneygive >= installment and moneyhave >= installment:
            if moneygive > installment:
                QMessageBox.warning(self, "Warning", "Much more money you will pay")
            else:
                sqlxx = "UPDATE _4credits SET Payment_Status =%s, Pay_Date=%s WHERE id=%s AND Month=%s"
                params = ("Paid", now, id, month)
                try:
                    cursor.execute(sqlxx, params)
                    connection.commit()
                except Error:
                    QMessageBox.warning(
                        self,
                        "Warning",
                        "Incorrect entry",
                        QMessageBox.Yes,
                        QMessageBox.No,
                    )
                sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
                params = (int(moneyhave - moneygive) / (currency), acco_no)
                cursor.execute(sqlxx, params)
                try:
                    connection.commit()
                except Error:
                    QMessageBox.warning(
                        self,
                        "Warning",
                        "Incorrect entry",
                        QMessageBox.Yes,
                        QMessageBox.No,
                    )
                mySql_insert_query = """INSERT INTO _5statements (Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
                values = (
                    acco_no,
                    99999999,
                    "Payment",
                    moneygive,
                    int((moneyhave - moneygive) / (currency)),
                    0,
                    now,
                )
                cursor.execute(mySql_insert_query, values)
                try:
                    connection.commit()
                except Error:
                    QMessageBox.warning(
                        self,
                        "Warning",
                        "Incorrect entry",
                        QMessageBox.Yes,
                        QMessageBox.No,
                    )
                self.creditstable.removeRow(1)
                self.creditbalance.setText("")
                self.creditnecessary.setText("")

        if x == 0 and moneygive < installment:
            sqlxx = "UPDATE _4credits SET Payment_Status =%s, Pay_Date=%s WHERE id=%s AND Month=%s"
            params = ("Paid", now, id, month)
            try:
                cursor.execute(sqlxx, params)
                connection.commit()
            except Error:
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Incorrect entry",
                    QMessageBox.Yes,
                    QMessageBox.No,
                )
            sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
            params = (int(moneyhave - moneygive) / (currency), acco_no)
            cursor.execute(sqlxx, params)
            try:
                connection.commit()
            except Error:
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Incorrect entry",
                    QMessageBox.Yes,
                    QMessageBox.No,
                )
            mySql_insert_query = """INSERT INTO _5statements (Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            values = (
                acco_no,
                99999999,
                "Payment",
                moneygive,
                int((moneyhave - moneygive) / (currency)),
                0,
                now,
            )
            cursor.execute(mySql_insert_query, values)
            try:
                connection.commit()
            except Error:
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Incorrect entry",
                    QMessageBox.Yes,
                    QMessageBox.No,
                )
            sqlsyn = """SELECT cr.id, cr.Type, cr.Worth FROM  _6currency AS cr WHERE id='1'"""
            try:
                cursor.execute(sqlsyn)
                resultxxq = cursor.fetchone()
            except Error:
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Incorrect entry",
                    QMessageBox.Yes,
                    QMessageBox.No,
                )
            a = installment + ((installment - moneygive) * (float(resultxxq[2]) / 100))
            x = int(month) - 1
            sqlxx = "UPDATE _4credits SET Late_Interest=%s WHERE id=%s AND Month=%s"
            params = (a, id, x)
            try:
                cursor.execute(sqlxx, params)
                connection.commit()
            except Error:
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Incorrect entry",
                    QMessageBox.Yes,
                    QMessageBox.No,
                )

        if (
            x == 1
            and moneygive >= installment * month
            and moneyhave >= installment * month
        ):
            if moneygive > installment * month:
                QMessageBox.warning(self, "Warning", "Much more money you will pay")
            else:
                sqlxx = "UPDATE _4credits SET Payment_Status =%s,Pay_Date=%s WHERE Installment = %s AND Month=%s"
                for i in range(1, month + 1):
                    params = ("Paid", now, id, i)

                    try:
                        cursor.execute(sqlxx, params)
                        connection.commit()
                    except Error:
                        QMessageBox.warning(
                            self,
                            "Warning",
                            "Incorrect entry",
                            QMessageBox.Yes,
                            QMessageBox.No,
                        )
                sqlxx = "UPDATE _2status SET Total_Balance =%s WHERE Acco_No = %s"
                params = ((moneyhave - moneygive) / (currency), acco_no)

                try:
                    cursor.execute(sqlxx, params)
                    connection.commit()
                except Error:
                    QMessageBox.warning(
                        self,
                        "Warning",
                        "Incorrect entry",
                        QMessageBox.Yes,
                        QMessageBox.No,
                    )
                mySql_insert_query = """INSERT INTO _5statements (Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
                values = (
                    acco_no,
                    99999999,
                    "Payment",
                    moneygive,
                    int((moneyhave - moneygive) / (currency)),
                    0,
                    now,
                )
                cursor.execute(mySql_insert_query, values)
                try:
                    connection.commit()
                except Error:
                    QMessageBox.warning(
                        self,
                        "Warning",
                        "Incorrect entry",
                        QMessageBox.Yes,
                        QMessageBox.No,
                    )
                self.creditbalance.setText("")
                self.creditnecessary.setText("")
        self.revealinfo()

    def newaccountopen(self):
        curre = int(self.currencytype.currentIndex()) + 1
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        mySql_insert_query = """SELECT Acco_No FROM _2status ORDER BY Acco_No ASC"""
        cursor.execute(mySql_insert_query)
        systemaccounts = []
        try:
            result = cursor.fetchall()
            for i in result:
                systemaccounts.append(int(i[0]))
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        mySql_insert_query = """INSERT INTO  _2status (Citizenship_No,Acco_No, Income, Expense, Total_Balance, currency) VALUES(%s,%s,%s,%s,%s,%s)"""
        a = randint(10000000, 99999999)
        if systemaccounts.count(a) > 0:
            a = randint(10000000, 99999999)
            if systemaccounts.count(a) > 0:
                a = randint(10000000, 99999999)
                if systemaccounts.count(a) > 0:
                    a = randint(10000000, 99999999)

        to_insert = (self.citizencus.text(), a, 0, 0, 0, curre)
        cursor.execute(mySql_insert_query, to_insert)
        try:
            connection.commit()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def monthlystatementsxxyy(self):
        tablecontents = []
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date FROM _1customerinfo AS c INNER JOIN _2status as st INNER JOIN _5statements as ms ON c.Citizenship_No=st.Citizenship_No AND st.Acco_No=ms.Source_No  WHERE c.Citizenship_No=%s and c.Password=%s ORDER BY ms.Date ASC"""
        params = (self.tc_no, self.password)
        try:

            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            for i in result:
                x = str(i[6])
                if i[5] == 0:
                    tablecontents.append(
                        (
                            str(i[0]),
                            str(i[1]),
                            str(i[2]),
                            str(i[3]),
                            str(i[4]),
                            str("Null"),
                            x[0:10],
                        )
                    )
                elif i[4] == 0:
                    tablecontents.append(
                        (
                            str(i[0]),
                            str(i[1]),
                            str(i[2]),
                            str(i[3]),
                            str("Null"),
                            str(i[5]),
                            x[0:10],
                        )
                    )
                elif i[1] == 99999999:
                    tablecontents.append(
                        (
                            str(i[0]),
                            str("Bank"),
                            str(i[2]),
                            str(i[3]),
                            str(i[4]),
                            str("Null"),
                            x[0:10],
                        )
                    )
                else:
                    tablecontents.append(
                        (
                            str(i[0]),
                            str(i[1]),
                            str(i[2]),
                            str(i[3]),
                            str(i[4]),
                            str(i[5]),
                            x[0:10],
                        )
                    )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT Source_No, Target_No, Pro, Balance, Source_Balance, Target_Balance, Date FROM _1customerinfo AS c INNER JOIN _2status as st INNER JOIN _5statements as ms ON c.Citizenship_No=st.Citizenship_No AND st.Acco_No=ms.Target_No  WHERE c.Citizenship_No=%s and c.Password=%s ORDER BY ms.Date ASC"""
        params = (self.tc_no, self.password)
        try:

            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            count = 0
            for i in result:
                x = str(i[6])
                tablecontents.append(
                    (
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[3]),
                        str(i[4]),
                        str(i[5]),
                        x[0:10],
                    )
                )
                count += 1
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.statementtable.setRowCount(Customerpage.msfinish)
        if Customerpage.msfinish >= count or Customerpage.msstart >= count:
            for info in range(Customerpage.msstart, count):
                self.statementtable.setItem(
                    info, 0, QTableWidgetItem(tablecontents[info][0])
                )
                self.statementtable.setItem(
                    info, 1, QTableWidgetItem(tablecontents[info][1])
                )
                self.statementtable.setItem(
                    info, 2, QTableWidgetItem(tablecontents[info][2])
                )
                self.statementtable.setItem(
                    info, 3, QTableWidgetItem(tablecontents[info][3])
                )
                self.statementtable.setItem(
                    info, 4, QTableWidgetItem(tablecontents[info][4])
                )
                self.statementtable.setItem(
                    info, 5, QTableWidgetItem(tablecontents[info][5])
                )
                self.statementtable.setItem(
                    info, 6, QTableWidgetItem(tablecontents[info][6])
                )
        else:
            for info in range(Customerpage.msstart, Customerpage.msfinish):
                self.statementtable.setItem(
                    info, 0, QTableWidgetItem(tablecontents[info][0])
                )
                self.statementtable.setItem(
                    info, 1, QTableWidgetItem(tablecontents[info][1])
                )
                self.statementtable.setItem(
                    info, 2, QTableWidgetItem(tablecontents[info][2])
                )
                self.statementtable.setItem(
                    info, 3, QTableWidgetItem(tablecontents[info][3])
                )
                self.statementtable.setItem(
                    info, 4, QTableWidgetItem(tablecontents[info][4])
                )
                self.statementtable.setItem(
                    info, 5, QTableWidgetItem(tablecontents[info][5])
                )
                self.statementtable.setItem(
                    info, 6, QTableWidgetItem(tablecontents[info][6])
                )
        Customerpage.msstart += 5
        Customerpage.msfinish += 5

    def revealinfo(self):
        self.accountstype.clear()
        self.withdrawaccotype.clear()
        self.depositaccotype.clear()
        self.traaccotype.clear()
        self.creditaccotype.clear()
        self.currencytype.clear()
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT  c.Name,c.Surname, c.Tel_No, c.Citizenship_No, c.Adress, c.E_mail,st.Acco_No,st.Income,st.Expense,st.Total_Balance,cr.Worth,cr.Type FROM  _1customerinfo AS c INNER JOIN _2status AS st INNER JOIN _6currency AS cr ON c.Citizenship_No  = st.Citizenship_No AND cr.id=st.Currency WHERE c.Citizenship_No=%s and c.Password=%s"""
        params = (self.tc_no, self.password)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            cinfo = {}
            accounts = []
            toplamincomes = 0
            toplamexpenses = 0
            toplamprofits = 0
            toplamtotal_balances = 0
            a = len(result)
            for i in result:
                cinfo.update(
                    {
                        "Name_Surname": i[0] + " " + i[1],
                        "Tel_No": int(i[2]),
                        "Citizenship_No": int(i[3]),
                        "Adress": i[4],
                        "E_mail": i[5],
                    }
                )
            for i in range(0, a):
                self.accountstype.addItem(
                    QIcon(":/Images/assets/moneys/" + str(result[i][11]) + ".png"),
                    str(result[i][6]),
                )
                self.creditaccotype.addItem(
                    QIcon(":/Images/assets/moneys/" + str(result[i][11]) + ".png"),
                    str(result[i][6]),
                    str(result[i][10]),
                )
                self.withdrawaccotype.addItem(
                    QIcon(":/Images/assets/moneys/" + str(result[i][11]) + ".png"),
                    str(result[i][6]),
                    str(result[i][10]),
                )
                self.depositaccotype.addItem(
                    QIcon(":/Images/assets/moneys/" + str(result[i][11]) + ".png"),
                    str(result[i][6]),
                    str(result[i][10]),
                )
                self.traaccotype.addItem(
                    QIcon(":/Images/assets/moneys/" + str(result[i][11]) + ".png"),
                    str(result[i][6]),
                    str(result[i][10]),
                )
            for i in range(0, a):
                accounts.append(
                    (
                        int(result[i][6]),
                        int(result[i][7]),
                        int(result[i][8]),
                        int(result[i][9]),
                        int(result[i][10]),
                    )
                )
            for i in range(0, a):
                if accounts[i][4] > 1.00:
                    toplamincomes += accounts[i][1] * accounts[i][4]
                    toplamexpenses += accounts[i][2] * accounts[i][4]
                    toplamprofits += (accounts[i][1] - accounts[i][2]) * accounts[i][4]
                    toplamtotal_balances += accounts[i][3] * accounts[i][4]
                else:
                    toplamincomes += accounts[i][1]
                    toplamexpenses += accounts[i][2]
                    toplamprofits += accounts[i][1] - accounts[i][2]
                    toplamtotal_balances += accounts[i][3]
            cinfo.update(
                {
                    "Income": toplamincomes,
                    "Expense": toplamexpenses,
                    "Profit": toplamprofits,
                    "Total": toplamtotal_balances,
                }
            )
            self.incomeclient.setText("  " + str(cinfo["Income"]) + "₺")
            self.expenseclient.setText("  " + str(cinfo["Expense"]) + "₺")
            self.profitclient.setText("  " + str(cinfo["Profit"]) + "₺")
            self.totalclient.setText("  " + str(cinfo["Total"]) + "₺")
            self.username.setText("  " + str(cinfo["Name_Surname"]))
            self.name_surnamecus.setText("  " + str(cinfo["Name_Surname"]))
            self.telephonecus.setText("  " + str(cinfo["Tel_No"]))
            self.citizencus.setText("   " + str(cinfo["Citizenship_No"]))
            self.addresscus.setText("  " + str(cinfo["Adress"]))
            self.emailcus.setText("  " + str(cinfo["E_mail"]))

        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT MAX(cr.Month) FROM  _1customerinfo AS c INNER JOIN _3creditsstarter AS cs INNER JOIN _4credits AS cr ON c.Citizenship_No  = cs.Citizenship_No AND cs.id=cr.id WHERE c.Citizenship_No=%s"""
        params = (self.tc_no,)
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            maxmonth = result[0][0]
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        self.creditstable.setRowCount(0)
        sqlsyn = """SELECT cr.Principal, cr.Interest, cr.RUSF, cr.BITT, cr.Remaining_debt,cr.Payment_Status,cr.Pay_Date,cr.Due_Date,cr.Late_Interest FROM  _1customerinfo AS c INNER JOIN _3creditsstarter AS cs INNER JOIN _4credits AS cr ON c.Citizenship_No  = cs.Citizenship_No AND cs.id=cr.id WHERE c.Citizenship_No=%s AND cr.Payment_Status=%s ORDER BY cr.Month DESC"""
        params = (self.tc_no, "Unpaid")
        try:
            cursor.execute(sqlsyn, params)
            result = cursor.fetchall()
            if len(result) > 0:
                self.creditstable.setRowCount(int(maxmonth))
                for info in range(0, len(result)):
                    x = str(result[info][6])
                    y = str(result[info][7])
                    z = round(
                        float(result[info][1])
                        + float(result[info][2])
                        + float(result[info][3]),
                        2,
                    )
                    t = round(
                        float(result[info][0]) + float(z) + float(result[info][8]), 2
                    )
                    self.creditstable.setItem(info, 0, QTableWidgetItem(str(t)))
                    self.creditstable.setItem(
                        info, 1, QTableWidgetItem(str(result[info][0]))
                    )
                    self.creditstable.setItem(info, 2, QTableWidgetItem(str(z)))
                    self.creditstable.setItem(
                        info, 3, QTableWidgetItem(str(result[info][4]))
                    )
                    self.creditstable.setItem(
                        info, 4, QTableWidgetItem(str(result[info][5]))
                    )
                    self.creditstable.setItem(info, 5, QTableWidgetItem(x[0:10]))
                    self.creditstable.setItem(info, 6, QTableWidgetItem(y[0:10]))
                    self.creditstable.setItem(
                        info, 7, QTableWidgetItem(str(result[info][8]))
                    )
            else:
                self.creditsFrame.hide()
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        sqlsyn = """SELECT cr.id, cr.Type, cr.Worth FROM  _6currency AS cr ORDER BY cr.id ASC"""
        try:
            cursor.execute(sqlsyn)
            result = cursor.fetchall()
            if len(result) > 0:
                for info in range(0, len(result)):
                    self.currencytype.addItem(
                        QIcon(
                            ":/Images/assets/moneys/" + str(result[info][1]) + ".png"
                        ),
                        str(result[info][2]),
                        str(result[info][1]),
                    )
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )

    def paymentproblem(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        sqlsyn = """SELECT MAX(cr.Month) FROM  _1customerinfo AS c INNER JOIN _3creditsstarter AS cs INNER JOIN _4credits AS cr ON c.Citizenship_No  = cs.Citizenship_No AND cs.id=cr.id WHERE c.Citizenship_No=%s AND cr.Payment_Status=%s"""
        params = (self.tc_no, "Unpaid")
        try:
            cursor.execute(sqlsyn, params)
            resultxx = cursor.fetchall()
            maxmonth = resultxx[0][0]
        except Error:
            QMessageBox.warning(
                self,
                "Warning",
                "Incorrect entry",
                QMessageBox.Yes,
                QMessageBox.No,
            )
        month = int(maxmonth)
        installment = float(self.creditstable.item(0, 0).text())
        x = self.paymenttype.currentIndex()
        if x == 0:
            self.creditnecessary.setText(str(installment))
        if x == 1:
            self.creditnecessary.setText(str(round(installment * month, 2)))

    def takeoutproblem(self):
        if self.takeouttype.currentIndex() == 0:
            self.takeoutmonths.clear()
            listofmonths = [3, 6, 9, 12, 18, 24, 30, 36]
            for i in range(0, 8):
                self.takeoutmonths.addItem(f"{listofmonths[i]}")
        if self.takeouttype.currentIndex() == 1:
            self.takeoutmonths.clear()
            listofmonths = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
            for i in range(0, 10):
                self.takeoutmonths.addItem(f"{listofmonths[i]}")
        if self.takeouttype.currentIndex() == 2:
            self.takeoutmonths.clear()
            listofmonths = [3, 6, 9, 12, 18, 24, 30, 36, 42, 48]
            for i in range(0, 10):
                self.takeoutmonths.addItem(f"{listofmonths[i]}")

    def custoinfo(self):
        width = self._4customeraddinfo.maximumWidth()
        if width == 0:
            newWidth = 210
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self._4customeraddinfo, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def transactions(self):
        width = self.alltransactions.maximumWidth()
        if width == 0:
            newWidth = 210
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.alltransactions, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        currentpoint = self.transfertype.currentIndex()
        if currentpoint == 0:
            self.withdraw.show()
            self.deposit.hide()
            self.moneytransfer.hide()
            self.takeout.hide()
            self.credit.hide()
            self.newaccount.hide()
            self.delaccount.hide()
        if currentpoint == 1:
            self.withdraw.hide()
            self.deposit.show()
            self.moneytransfer.hide()
            self.takeout.hide()
            self.credit.hide()
            self.newaccount.hide()
            self.delaccount.hide()
        if currentpoint == 2:
            self.withdraw.hide()
            self.deposit.hide()
            self.moneytransfer.show()
            self.takeout.hide()
            self.credit.hide()
            self.newaccount.hide()
            self.delaccount.hide()
        if currentpoint == 3:
            self.withdraw.hide()
            self.deposit.hide()
            self.moneytransfer.hide()
            self.takeout.show()
            self.credit.hide()
            self.newaccount.hide()
            self.delaccount.hide()
        if currentpoint == 4:
            self.withdraw.hide()
            self.deposit.hide()
            self.moneytransfer.hide()
            self.takeout.hide()
            self.credit.show()
            self.newaccount.hide()
            self.delaccount.hide()
        if currentpoint == 5:
            self.withdraw.hide()
            self.deposit.hide()
            self.moneytransfer.hide()
            self.takeout.hide()
            self.credit.hide()
            self.newaccount.show()
            self.delaccount.hide()
        if currentpoint == 6:
            self.withdraw.hide()
            self.deposit.hide()
            self.moneytransfer.hide()
            self.takeout.hide()
            self.credit.hide()
            self.newaccount.hide()
            self.delaccount.show()

    def accountdeletion(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()
        acco_no = int(self.accountstype.currentText())
        sqlsyn = """SELECT st.Total_Balance FROM _2status AS st WHERE st.Acco_No=%s"""
        params = (acco_no,)
        try:
            cursor.execute(sqlsyn, params)
            resultx = cursor.fetchone()
            if float(resultx[0]) == 0:
                try:
                    sqxxl = "DELETE FROM _2status WHERE Acco_No = %s"
                    params = (acco_no,)
                    cursor.execute(sqxxl, params)
                    connection.commit()
                    self.revealinfo()
                except Error:
                    QMessageBox.warning(
                        self,
                        "Warning",
                        "Incorrect entry",
                        QMessageBox.Yes,
                        QMessageBox.No,
                    )
        except Error:
            QMessageBox.about(self, "", "Incorrect Deletion")


class DiagramPage(QMainWindow, Ui_diagram):
    def __init__(self):
        super(DiagramPage, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.aquitbutton.clicked.connect(self.close)
        self._0persal.pressed.connect(self.effection00s)
        self._0persal.released.connect(self.effection01s)
        self._0personal.pressed.connect(self.effection00)
        self._0personal.released.connect(self.effection01)
        self._1customer.pressed.connect(self.effection10)
        self._1customer.released.connect(self.effection11)
        self._2status.pressed.connect(self.effection20)
        self._2status.released.connect(self.effection21)
        self._3credit.pressed.connect(self.effection30)
        self._3credit.released.connect(self.effection31)
        self._4credit.pressed.connect(self.effection40)
        self._4credit.released.connect(self.effection41)
        self._5statement.pressed.connect(self.effection50)
        self._5statement.released.connect(self.effection51)
        self._6currency.pressed.connect(self.effection60)
        self._6currency.released.connect(self.effection61)
        self._7rates.pressed.connect(self.effection70)
        self._7rates.released.connect(self.effection71)
        self._0000getqna.clicked.connect(self.getQna)
        self.aquitbutton.show()
        self._000QNA.hide()
        self.qna = True

    def getQna(self):
        if self.qna:
            self._000QNA.show()
            self.aquitbutton.hide()
            icon1 = QIcon()
            icon1.addPixmap(
                QPixmap(":/Images/assets/icons/lamp2.png"),
                QIcon.Normal,
                QIcon.Off,
            )
            self._0000getqna.setIcon(icon1)
            self._0000getqna.setStyleSheet(
                "#_0000getqna{background-color:rgb(213, 69, 201);border-top-right-radius:0px;border-bottom-right-radius:0px;border-top-left-radius:30px;border-bottom-left-radius:30px;}#_0000getqna:hover{padding-left:5px;padding-bottom:5px;}"
            )
            self.qna = False
        else:
            self._000QNA.hide()
            self.aquitbutton.show()
            icon1 = QIcon()
            icon1.addPixmap(
                QPixmap(":/Images/assets/icons/lamp1.png"),
                QIcon.Normal,
                QIcon.Off,
            )
            self._0000getqna.setIcon(icon1)
            self._0000getqna.setStyleSheet(
                "#_0000getqna{background-color: rgb(62, 192, 203);border-radius:30px;}#_0000getqna:hover{padding-left:5px;padding-bottom:5px;}"
            )
            self.qna = True

    def effection00s(self):
        self.frame_82.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_80.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_52.setStyleSheet("background-color: rgba(60, 177, 255,180);")

    def effection01s(self):
        self.frame_82.setStyleSheet("background-color: transparent;")
        self.frame_80.setStyleSheet("background-color: transparent;")
        self.label_52.setStyleSheet("background-color: transparent;")

    def effection00(self):
        self.frame_44.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_31.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_10.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_82.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_80.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_52.setStyleSheet("background-color: rgba(60, 214, 71,180);")

    def effection01(self):
        self.frame_82.setStyleSheet("background-color: transparent;")
        self.frame_80.setStyleSheet("background-color: transparent;")
        self.label_52.setStyleSheet("background-color: transparent;")
        self.frame_44.setStyleSheet("background-color: transparent;")
        self.frame_31.setStyleSheet("background-color: transparent;")
        self.label_10.setStyleSheet("background-color: transparent;")

    def effection10(self):
        self.frame_25.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_34.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_39.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_44.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_31.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_10.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_32.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_19.setStyleSheet("background-color: rgba(60, 177, 255,180);")

    def effection11(self):
        self.frame_44.setStyleSheet("background-color: transparent;")
        self.frame_31.setStyleSheet("background-color: transparent;")
        self.label_10.setStyleSheet("background-color: transparent;")
        self.frame_25.setStyleSheet("background-color: transparent;")
        self.frame_34.setStyleSheet("background-color: transparent;")
        self.frame_39.setStyleSheet("background-color: transparent;")
        self.label_32.setStyleSheet("background-color: transparent;")
        self.label_19.setStyleSheet("background-color: transparent;")

    def effection20(self):
        self.frame_40.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_49.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_50.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_57.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_43.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_25.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_39.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_9.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_32.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_26.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_29.setStyleSheet("background-color: rgba(60, 177, 255,180);")

    def effection21(self):
        self.frame_40.setStyleSheet("background-color: transparent;")
        self.frame_49.setStyleSheet("background-color: transparent;")
        self.frame_50.setStyleSheet("background-color: transparent;")
        self.frame_57.setStyleSheet("background-color: transparent;")
        self.frame_43.setStyleSheet("background-color: transparent;")
        self.frame_25.setStyleSheet("background-color: transparent;")
        self.frame_39.setStyleSheet("background-color: transparent;")
        self.label_9.setStyleSheet("background-color: transparent;")
        self.label_32.setStyleSheet("background-color: transparent;")
        self.label_26.setStyleSheet("background-color: transparent;")
        self.label_29.setStyleSheet("background-color: transparent;")

    def effection30(self):
        self.frame_25.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_34.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_37.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_69.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_33.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_56.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_19.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_31.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_39.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_35.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_44.setStyleSheet("background-color: rgba(60, 214, 71,180);")

    def effection31(self):
        self.frame_25.setStyleSheet("background-color: transparent;")
        self.frame_34.setStyleSheet("background-color: transparent;")
        self.frame_37.setStyleSheet("background-color: transparent;")
        self.frame_69.setStyleSheet("background-color: transparent;")
        self.frame_33.setStyleSheet("background-color: transparent;")
        self.frame_56.setStyleSheet("background-color: transparent;")
        self.label_19.setStyleSheet("background-color: transparent;")
        self.label_31.setStyleSheet("background-color: transparent;")
        self.label_35.setStyleSheet("background-color: transparent;")
        self.label_39.setStyleSheet("background-color: transparent;")
        self.label_44.setStyleSheet("background-color: transparent;")

    def effection40(self):
        self.frame_69.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_33.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_31.setStyleSheet("background-color: rgba(60, 214, 71,180);")

    def effection41(self):
        self.frame_69.setStyleSheet("background-color: transparent;")
        self.frame_33.setStyleSheet("background-color: transparent;")
        self.label_31.setStyleSheet("background-color: transparent;")

    def effection50(self):
        self.frame_40.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_49.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.frame_50.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_26.setStyleSheet("background-color: rgba(60, 214, 71,180);")
        self.label_29.setStyleSheet("background-color: rgba(60, 214, 71,180);")

    def effection51(self):
        self.frame_40.setStyleSheet("background-color: transparent;")
        self.frame_49.setStyleSheet("background-color: transparent;")
        self.frame_50.setStyleSheet("background-color: transparent;")
        self.label_26.setStyleSheet("background-color: transparent;")
        self.label_29.setStyleSheet("background-color: transparent;")

    def effection60(self):
        self.frame_57.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_43.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_9.setStyleSheet("background-color: rgba(60, 177, 255,180);")

    def effection61(self):
        self.frame_57.setStyleSheet("background-color: transparent;")
        self.frame_43.setStyleSheet("background-color: transparent;")
        self.label_9.setStyleSheet("background-color: transparent;")

    def effection70(self):
        self.frame_56.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.frame_37.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_39.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_35.setStyleSheet("background-color: rgba(60, 177, 255,180);")
        self.label_44.setStyleSheet("background-color: rgba(60, 177, 255,180);")

    def effection71(self):
        self.frame_56.setStyleSheet("background-color: transparent;")
        self.frame_37.setStyleSheet("background-color: transparent;")
        self.label_39.setStyleSheet("background-color: transparent;")
        self.label_35.setStyleSheet("background-color: transparent;")
        self.label_44.setStyleSheet("background-color: transparent;")


class LoginApp(QWidget, Ui_loginpage):
    count = 3

    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.twitterbutton.setGraphicsEffect(glory(opacity=0.0))
        self.whatsappbutton.setGraphicsEffect(glory(opacity=0.0))
        self.instagrambutton.setGraphicsEffect(glory(opacity=0.0))
        self.facebookbutton.setGraphicsEffect(glory(opacity=0.0))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.aquitbutton.clicked.connect(self.close)
        intreg = QRegExp("^[0-9]{11}$")
        integervalidator = QRegExpValidator(intreg, self)
        strreg = QRegExp("^[a-z-A-Z ]{30}$")
        stringvalidator = QRegExpValidator(strreg, self)
        self.citizenforgot.setValidator(integervalidator)
        self.citizenlog.setValidator(integervalidator)
        self.citizenreg.setValidator(integervalidator)
        self.passwordlog.setValidator(integervalidator)
        self.passwordreg.setValidator(integervalidator)
        self.confirmpassword.setValidator(integervalidator)
        self.telephone.setValidator(integervalidator)
        self.name_surname.setValidator(stringvalidator)
        self.leftback.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.rightback.setGraphicsEffect(effect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.registerbutton.setGraphicsEffect(
            effect(blurRadius=25, xOffset=3, yOffset=3)
        )
        self.sendforgot.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.forgotbutton.setGraphicsEffect(effect(blurRadius=25, xOffset=3, yOffset=3))
        self.forgotwidget.hide()
        self.registerwidget.hide()
        self.forgotbutton.clicked.connect(self.changeForm)
        self.changingbutton.clicked.connect(self.changeForm)
        self.showpasslog.clicked.connect(self.changeForm)
        self.loginbutton.clicked.connect(self.accessBypass)
        self.brandi.clicked.connect(self.diagramshow)
        self.selectperson.currentIndexChanged.connect(self.styleofselection)
        self.citizenlog.textChanged.connect(self.citstyle)
        self.passwordlog.textChanged.connect(self.passstyle)
        self.twitterbutton.clicked.connect(self.openlink)
        self.whatsappbutton.clicked.connect(self.openlink)
        self.instagrambutton.clicked.connect(self.openlink)
        self.facebookbutton.clicked.connect(self.openlink)
        self.loginbutton.clicked.connect(self.stopthreads)
        self.thread = {}
        self.thread[1] = ThreadClass(parent=None)
        self.thread[1].any_signal.connect(self.whatsapp)
        self.thread[1].start()

    def openlink(self):
        QDesktopServices.openUrl(QUrl("http://stackoverflow.com"))

    def stopthreads(self):
        self.thread[1].stop()
        self.twitterbutton.setGraphicsEffect(glory(opacity=1.0))
        self.whatsappbutton.setGraphicsEffect(glory(opacity=1.0))
        self.instagrambutton.setGraphicsEffect(glory(opacity=1.0))
        self.facebookbutton.setGraphicsEffect(glory(opacity=1.0))

    def whatsapp(self):
        if LoginApp.count % 3 == 0:
            self.whatsappbutton.setGraphicsEffect(glory(opacity=0.3))
            self.facebookbutton.setGraphicsEffect(glory(opacity=1.0))
            self.instagrambutton.setGraphicsEffect(glory(opacity=0.3))
            self.twitterbutton.setGraphicsEffect(glory(opacity=0.3))
            LoginApp.count = 5
        elif LoginApp.count % 5 == 0:
            self.whatsappbutton.setGraphicsEffect(glory(opacity=0.3))
            self.facebookbutton.setGraphicsEffect(glory(opacity=0.3))
            self.instagrambutton.setGraphicsEffect(glory(opacity=1.0))
            self.twitterbutton.setGraphicsEffect(glory(opacity=0.3))
            LoginApp.count = 7
        elif LoginApp.count % 7 == 0:
            self.whatsappbutton.setGraphicsEffect(glory(opacity=0.3))
            self.facebookbutton.setGraphicsEffect(glory(opacity=0.3))
            self.instagrambutton.setGraphicsEffect(glory(opacity=0.3))
            self.twitterbutton.setGraphicsEffect(glory(opacity=1.0))
            LoginApp.count = 11
        else:
            self.whatsappbutton.setGraphicsEffect(glory(opacity=1.0))
            self.twitterbutton.setGraphicsEffect(glory(opacity=0.3))
            self.instagrambutton.setGraphicsEffect(glory(opacity=0.3))
            self.facebookbutton.setGraphicsEffect(glory(opacity=0.3))
            LoginApp.count = 3

    # def instagram(self):
    #     if LoginApp.count % 2 == 0:
    #         self.instagrambutton.setGraphicsEffect(glory(opacity=1.0))
    #         LoginApp.count += 1
    #     else:
    #         self.instagrambutton.setGraphicsEffect(glory(opacity=0.0))
    #         LoginApp.count += 1

    # def twitter(self):
    #     if LoginApp.count % 2 == 0:
    #         self.twitterbutton.setGraphicsEffect(glory(opacity=0.0))
    #         LoginApp.count += 1
    #     else:
    #         self.twitterbutton.setGraphicsEffect(glory(opacity=1.0))
    #         LoginApp.count += 1

    def citstyle(self):
        a = str(self.citizenlog.text())
        if len(a) == 11:
            self.citizenlog.setStyleSheet(
                "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(255, 255, 255, 255);padding-left:5px;padding-bottom:7px;"
            )
        else:
            self.citizenlog.setStyleSheet(
                "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(255, 255, 255, 255);padding-left:5px;padding-bottom:7px;"
            )

    def passstyle(self):
        a = str(self.passwordlog.text())
        if len(a) == 6:
            self.passwordlog.setStyleSheet(
                "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(255, 255, 255, 255);padding-left:5px;padding-bottom:7px;"
            )
        else:
            self.passwordlog.setStyleSheet(
                "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(255, 255, 255, 255);padding-left:5px;padding-bottom:7px;"
            )

    def styleofselection(self):
        self.selectperson.setStyleSheet(
            "QAbstractItemView {background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));background-color:}#selectperson{background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(255, 255, 255, 255);padding-left:0px;}"
        )

    def diagramshow(self):
        self.accesspanel = DiagramPage()
        self.accesspanel.show()

    def accessBypass(self):
        connection = _4DatabaseConnection.mydb
        cursor = connection.cursor()

        tc_no = self.citizenlog.text()
        password = self.passwordlog.text()
        pertype = self.selectperson.currentIndex()
        if pertype == 0 or pertype == 1:
            sqlsyn = """SELECT p.W_C FROM _1customerinfo AS p WHERE W_C=%s"""
            params = (tc_no,)
            try:
                cursor.execute(sqlsyn, params)
                resultxx = cursor.fetchall()
                if len(resultxx) == 1:
                    self.accesspanel = Managerpage(tc_no, password)
                    self.accesspanel.show()
                    self.close()
                if len(resultxx) > 1:
                    self.accesspanel = RepresentPage(tc_no, password)
                    self.accesspanel.show()
                    self.close()
                if len(resultxx) < 1:
                    QMessageBox.critical(
                        self, "", "Incorrect entry", QMessageBox.Yes, QMessageBox.No
                    )
            except Error:
                QMessageBox.critical(
                    self, "", "Incorrect entry", QMessageBox.Yes, QMessageBox.No
                )
        else:
            sqlsyn = """SELECT p.W_C FROM _1customerinfo AS p WHERE W_C=%s"""
            params = (tc_no,)
            try:
                cursor.execute(sqlsyn, params)
                resultxx = cursor.fetchall()
                if len(resultxx) == 1:
                    QMessageBox.critical(
                        self, "", "Incorrect entry", QMessageBox.Yes, QMessageBox.No
                    )
                if len(resultxx) > 1:
                    QMessageBox.critical(
                        self, "", "Incorrect entry", QMessageBox.Yes, QMessageBox.No
                    )
                if len(resultxx) == 0:
                    self.accesspanel = Customerpage(tc_no, password)
                    self.accesspanel.show()
                    self.close()
            except Error:
                QMessageBox.critical(
                    self, "", "Incorrect entry", QMessageBox.Yes, QMessageBox.No
                )

    def changeForm(self):
        if self.changingbutton.isChecked():
            self.loginwidget.hide()
            self.registerwidget.show()
            self.changingbutton.setText("")
            icon1 = QIcon()
            icon1.addPixmap(
                QPixmap(":/Images/assets/icons/Purple (2).png"),
                QIcon.Normal,
                QIcon.Off,
            )
            self.changingbutton.setIcon(icon1)
        else:
            self.loginwidget.show()
            self.registerwidget.hide()
            self.changingbutton.setText("")
            icon1 = QIcon()
            icon1.addPixmap(
                QPixmap(":/Images/assets/icons/Purple (1).png"),
                QIcon.Normal,
                QIcon.Off,
            )
            self.changingbutton.setIcon(icon1)

        if self.forgotbutton.isChecked():
            self.forgotwidget.show()
        else:
            self.forgotwidget.hide()

        if self.showpasslog.isChecked():
            self.passwordlog.setEchoMode(QLineEdit.Normal)
            icon4 = QIcon()
            icon4.addPixmap(
                QPixmap(":/Images/assets/icons/eye-slash.svg"),
                QIcon.Normal,
                QIcon.Off,
            )
            self.showpasslog.setIcon(icon4)
        else:
            self.passwordlog.setEchoMode(QLineEdit.Password)
            icon4 = QIcon()
            icon4.addPixmap(
                QPixmap(":/Images/assets/icons/eye.svg"),
                QIcon.Normal,
                QIcon.Off,
            )
            self.showpasslog.setIcon(icon4)


if __name__ == "__main__":
    app = QApplication(argv)
    Form = LoginApp()
    Form.show()
    exit(app.exec_())
