from PyQt5.QtWidgets import (
    QLineEdit,
    QWidget,
    QSizePolicy,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QComboBox,
    QAbstractScrollArea,
    QTextEdit,
)

from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QFont,
)
from PyQt5.QtCore import (
    Qt,
    QSize,
    QCoreApplication,
    QMetaObject,
    QRect,
)


class Ui_loginpage(object):
    def setupUi(self, loginpage):
        loginpage.setObjectName("loginpage")
        loginpage.resize(687, 577)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/Images/assets/icons/mainico.png"), QIcon.Normal, QIcon.Off
        )
        loginpage.setWindowIcon(icon)
        self.widget = QWidget(loginpage)
        self.widget.setGeometry(QRect(0, 0, 651, 541))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.widget.setFont(font)
        self.widget.setStyleSheet(
            "QPushButton#loginbutton,#sendforgot, #registerbutton, #changingbutton,#aquitbutton,#registerbutton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "\n"
            "QPushButton#loginbutton:hover,#sendforgot:hover, #registerbutton:hover,#registerbutton:hover, #changingbutton:hover,#aquitbutton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#loginbutton:pressed,#sendforgot:pressed,#registerbutton:pressed, #registerbutton:pressed, #changingbutton:pressed,#aquitbutton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.widget.setObjectName("widget")
        self.leftback = QLabel(self.widget)
        self.leftback.setGeometry(QRect(20, 30, 315, 511))
        self.leftback.setStyleSheet(
            "border-image: url(:/Images/assets/images/background.jpg);\n"
            "border-top-left-radius: 50px;\n"
            "border-bottom-left-radius: 50px;"
        )
        self.leftback.setText("")
        self.leftback.setObjectName("leftback")
        self.rightback = QLabel(self.widget)
        self.rightback.setGeometry(QRect(335, 30, 315, 511))
        self.rightback.setStyleSheet(
            "background-color:rgba(255, 255, 255, 255);\n"
            "border-image: url(:/Images/assets/images/background.png);\n"
            "border-bottom-right-radius: 50px;\n"
            "border-top-right-radius: 50px;"
        )
        self.rightback.setText("")
        self.rightback.setObjectName("rightback")
        self.changingbutton = QPushButton(self.widget)
        self.changingbutton.setGeometry(QRect(313, 110, 41, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.changingbutton.setFont(font)
        self.changingbutton.setStyleSheet(
            "QPushButton{\n"
            "    background-color: transparent;\n"
            "    border-radius:10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px;\n"
            "}"
        )
        self.changingbutton.setText("")
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(":/Images/assets/icons/Purple (1).png"), QIcon.Normal, QIcon.Off
        )
        self.changingbutton.setIcon(icon1)
        self.changingbutton.setIconSize(QSize(50, 50))
        self.changingbutton.setCheckable(True)
        self.changingbutton.setObjectName("changingbutton")
        self.middletran = QLabel(self.widget)
        self.middletran.setGeometry(QRect(20, 30, 631, 511))
        self.middletran.setStyleSheet(
            "background-color:rgba(0, 0, 0, 100);\n" "border-radius: 50px;\n" ""
        )
        self.middletran.setText("")
        self.middletran.setScaledContents(True)
        self.middletran.setObjectName("middletran")
        self.forgotwidget = QWidget(self.widget)
        self.forgotwidget.setGeometry(QRect(60, 250, 235, 171))
        self.forgotwidget.setStyleSheet(
            "QLineEdit,QTextEdit,#selectperson{\n" "    border-radius:20px;\n" "}"
        )
        self.forgotwidget.setObjectName("forgotwidget")
        self.verticalLayout_2 = QVBoxLayout(self.forgotwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resetforgot = QLabel(self.forgotwidget)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.resetforgot.setFont(font)
        self.resetforgot.setStyleSheet("color:rgba(255, 255, 255, 240);")
        self.resetforgot.setObjectName("resetforgot")
        self.verticalLayout_2.addWidget(self.resetforgot, 0, Qt.AlignHCenter)
        self.citizenforgot = QLineEdit(self.forgotwidget)
        self.citizenforgot.setMinimumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.citizenforgot.setFont(font)
        self.citizenforgot.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.citizenforgot.setText("")
        self.citizenforgot.setMaxLength(11)
        self.citizenforgot.setObjectName("citizenforgot")
        self.verticalLayout_2.addWidget(self.citizenforgot, 0, Qt.AlignHCenter)
        self.emailforgot = QLineEdit(self.forgotwidget)
        self.emailforgot.setMinimumSize(QSize(190, 40))
        self.emailforgot.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.emailforgot.setFont(font)
        self.emailforgot.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.emailforgot.setText("")
        self.emailforgot.setEchoMode(QLineEdit.Normal)
        self.emailforgot.setObjectName("emailforgot")
        self.verticalLayout_2.addWidget(self.emailforgot, 0, Qt.AlignHCenter)
        self.sendforgot = QPushButton(self.forgotwidget)
        self.sendforgot.setMinimumSize(QSize(150, 40))
        self.sendforgot.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.sendforgot.setFont(font)
        self.sendforgot.setObjectName("sendforgot")
        self.verticalLayout_2.addWidget(self.sendforgot, 0, Qt.AlignHCenter)
        self.brandi = QPushButton(self.widget)
        self.brandi.setGeometry(QRect(65, 40, 231, 211))
        self.brandi.setMinimumSize(QSize(150, 40))
        self.brandi.setMaximumSize(QSize(414141, 414141))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.brandi.setFont(font)
        self.brandi.setStyleSheet(
            "QPushButton{\n"
            "    background-color: transparent;\n"
            "    border-radius:10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px;\n"
            "}"
        )
        self.brandi.setText("")
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(":/Images/assets/icons/brandico.png"), QIcon.Normal, QIcon.Off
        )
        self.brandi.setIcon(icon2)
        self.brandi.setIconSize(QSize(240, 220))
        self.brandi.setObjectName("brandi")
        self.aquitbutton = QPushButton(self.widget)
        self.aquitbutton.setGeometry(QRect(596, 46, 41, 41))
        self.aquitbutton.setMinimumSize(QSize(41, 41))
        self.aquitbutton.setMaximumSize(QSize(41, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.aquitbutton.setFont(font)
        self.aquitbutton.setStyleSheet(
            "QPushButton#aquitbutton{\n"
            "border-radius:20px;\n"
            "background:transparent;\n"
            "}\n"
            "\n"
            "QPushButton#aquitbutton:hover{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px;\n"
            "}\n"
            "QPushButton#aquitbutton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px;\n"
            "}\n"
            ""
        )
        self.aquitbutton.setText("")
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(":/Images/assets/icons/Purple (5).png"), QIcon.Normal, QIcon.Off
        )
        self.aquitbutton.setIcon(icon3)
        self.aquitbutton.setIconSize(QSize(40, 40))
        self.aquitbutton.setObjectName("aquitbutton")
        self.registerwidget = QWidget(self.widget)
        self.registerwidget.setGeometry(QRect(380, 40, 210, 400))
        self.registerwidget.setMinimumSize(QSize(210, 400))
        self.registerwidget.setMaximumSize(QSize(210, 400))
        self.registerwidget.setStyleSheet(
            "#_4customeraddinfo{    \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(42, 72, 77, 219), stop:1 rgba(24, 42, 43, 226));\n"
            "    border-radius:50px;\n"
            "}\n"
            "\n"
            "QLineEdit,QTextEdit{\n"
            "    border-radius:20px;\n"
            "}\n"
            "\n"
            ""
        )
        self.registerwidget.setObjectName("registerwidget")
        self.verticalLayout_4 = QVBoxLayout(self.registerwidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.registerlabel = QLabel(self.registerwidget)
        self.registerlabel.setMinimumSize(QSize(190, 40))
        self.registerlabel.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.registerlabel.setFont(font)
        self.registerlabel.setStyleSheet("\n" "color: rgb(255, 255, 255);")
        self.registerlabel.setScaledContents(True)
        self.registerlabel.setAlignment(Qt.AlignCenter)
        self.registerlabel.setObjectName("registerlabel")
        self.verticalLayout_4.addWidget(self.registerlabel, 0, Qt.AlignHCenter)
        self.name_surname = QLineEdit(self.registerwidget)
        self.name_surname.setMinimumSize(QSize(190, 40))
        self.name_surname.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.name_surname.setFont(font)
        self.name_surname.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.name_surname.setText("")
        self.name_surname.setCursorPosition(0)
        self.name_surname.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.name_surname.setClearButtonEnabled(False)
        self.name_surname.setObjectName("name_surname")
        self.verticalLayout_4.addWidget(self.name_surname, 0, Qt.AlignHCenter)
        self.telephone = QLineEdit(self.registerwidget)
        self.telephone.setMinimumSize(QSize(190, 40))
        self.telephone.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.telephone.setFont(font)
        self.telephone.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.telephone.setMaxLength(10)
        self.telephone.setClearButtonEnabled(False)
        self.telephone.setObjectName("telephone")
        self.verticalLayout_4.addWidget(self.telephone, 0, Qt.AlignHCenter)
        self.citizenreg = QLineEdit(self.registerwidget)
        self.citizenreg.setMinimumSize(QSize(190, 40))
        self.citizenreg.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.citizenreg.setFont(font)
        self.citizenreg.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.citizenreg.setMaxLength(11)
        self.citizenreg.setClearButtonEnabled(False)
        self.citizenreg.setObjectName("citizenreg")
        self.verticalLayout_4.addWidget(self.citizenreg, 0, Qt.AlignHCenter)
        self.adressreg = QTextEdit(self.registerwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adressreg.sizePolicy().hasHeightForWidth())
        self.adressreg.setSizePolicy(sizePolicy)
        self.adressreg.setMinimumSize(QSize(190, 60))
        self.adressreg.setMaximumSize(QSize(190, 60))
        font = QFont()
        font.setPointSize(10)
        self.adressreg.setFont(font)
        self.adressreg.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.adressreg.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.adressreg.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.adressreg.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.adressreg.setObjectName("adressreg")
        self.verticalLayout_4.addWidget(self.adressreg, 0, Qt.AlignHCenter)
        self.emailreg = QLineEdit(self.registerwidget)
        self.emailreg.setMinimumSize(QSize(190, 40))
        self.emailreg.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.emailreg.setFont(font)
        self.emailreg.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.emailreg.setEchoMode(QLineEdit.Normal)
        self.emailreg.setObjectName("emailreg")
        self.verticalLayout_4.addWidget(self.emailreg, 0, Qt.AlignHCenter)
        self.passwordreg = QLineEdit(self.registerwidget)
        self.passwordreg.setMinimumSize(QSize(190, 40))
        self.passwordreg.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.passwordreg.setFont(font)
        self.passwordreg.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.passwordreg.setMaxLength(6)
        self.passwordreg.setEchoMode(QLineEdit.Normal)
        self.passwordreg.setObjectName("passwordreg")
        self.verticalLayout_4.addWidget(self.passwordreg, 0, Qt.AlignHCenter)
        self.confirmpassword = QLineEdit(self.registerwidget)
        self.confirmpassword.setMinimumSize(QSize(190, 40))
        self.confirmpassword.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.confirmpassword.setFont(font)
        self.confirmpassword.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.confirmpassword.setMaxLength(6)
        self.confirmpassword.setEchoMode(QLineEdit.Normal)
        self.confirmpassword.setObjectName("confirmpassword")
        self.verticalLayout_4.addWidget(self.confirmpassword, 0, Qt.AlignHCenter)
        self.registerbutton = QPushButton(self.registerwidget)
        self.registerbutton.setMinimumSize(QSize(100, 40))
        self.registerbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.registerbutton.setFont(font)
        self.registerbutton.setStyleSheet("color:rgb(255, 255, 255);")
        self.registerbutton.setObjectName("registerbutton")
        self.verticalLayout_4.addWidget(
            self.registerbutton, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.loginwidget = QWidget(self.widget)
        self.loginwidget.setGeometry(QRect(380, 140, 210, 260))
        self.loginwidget.setMinimumSize(QSize(210, 260))
        self.loginwidget.setMaximumSize(QSize(210, 260))
        self.loginwidget.setStyleSheet(
            "QLineEdit,QTextEdit,#selectperson{\n"
            "    border-radius:20px;\n"
            "}\n"
            "\n"
            "QAbstractItemView {\n"
            "border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "padding: 5 5 16 5;\n"
            "border-radius:5px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "color: #ffffff;\n"
            "font-size: 13px;\n"
            "}\n"
            "QComboBox {\n"
            "border: none;\n"
            "}\n"
            "QScrollBar:vertical {\n"
            "border-radius: 5px;\n"
            "background:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "width:10px;\n"
            "margin: 0px 0px 0px 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "border-radius: 5px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
            "    min-width:10px;\n"
            "    max-width:10px;\n"
            "    min-height:10px;\n"
            "    max-height:10px;\n"
            "}\n"
            "QScrollBar::add-line:vertical {\n"
            "height: 0px;\n"
            "subcontrol-position: bottom;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical {\n"
            "height: 0px;\n"
            "subcontrol-position: top;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "background:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url(:/Images/assets/icons/caret-circle-down .png);\n"
            "    min-width:20px;\n"
            "    max-width:20px;\n"
            "    min-height:20px;\n"
            "    max-height:20px;\n"
            "    margin-right:2px;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    border:none;\n"
            "    background:transparent;\n"
            "}"
        )
        self.loginwidget.setObjectName("loginwidget")
        self.verticalLayout = QVBoxLayout(self.loginwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loglabel = QLabel(self.loginwidget)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.loglabel.setFont(font)
        self.loglabel.setStyleSheet("color:rgba(255, 255, 255, 240);")
        self.loglabel.setObjectName("loglabel")
        self.verticalLayout.addWidget(self.loglabel, 0, Qt.AlignHCenter)
        self.citizenlog = QLineEdit(self.loginwidget)
        self.citizenlog.setMinimumSize(QSize(190, 40))
        self.citizenlog.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.citizenlog.setFont(font)
        self.citizenlog.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.citizenlog.setMaxLength(11)
        self.citizenlog.setObjectName("citizenlog")
        self.verticalLayout.addWidget(self.citizenlog, 0, Qt.AlignHCenter)
        self.frame = QFrame(self.loginwidget)
        self.frame.setMaximumSize(QSize(192, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 11, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passwordlog = QLineEdit(self.frame)
        self.passwordlog.setMinimumSize(QSize(190, 40))
        self.passwordlog.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.passwordlog.setFont(font)
        self.passwordlog.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.passwordlog.setMaxLength(6)
        self.passwordlog.setEchoMode(QLineEdit.Password)
        self.passwordlog.setObjectName("passwordlog")
        self.horizontalLayout.addWidget(self.passwordlog, 0, Qt.AlignHCenter)
        self.showpasslog = QPushButton(self.frame)
        self.showpasslog.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.showpasslog.setFont(font)
        self.showpasslog.setStyleSheet(
            "#showpasslog{background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "color:rgba(255, 255, 255, 240);\n"
            "padding-bottom:7px;}"
        )
        self.showpasslog.setText("")
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(":/Images/assets/icons/eye.svg"), QIcon.Normal, QIcon.Off
        )
        self.showpasslog.setIcon(icon4)
        self.showpasslog.setIconSize(QSize(30, 30))
        self.showpasslog.setCheckable(True)
        self.showpasslog.setObjectName("showpasslog")
        self.horizontalLayout.addWidget(self.showpasslog, 0, Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)
        self.selectperson = QComboBox(self.loginwidget)
        self.selectperson.setMinimumSize(QSize(190, 45))
        self.selectperson.setMaximumSize(QSize(190, 45))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectperson.setFont(font)
        self.selectperson.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            ""
        )
        self.selectperson.setCurrentText("")
        self.selectperson.setMaxVisibleItems(10)
        self.selectperson.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.selectperson.setMinimumContentsLength(6)
        self.selectperson.setIconSize(QSize(37, 37))
        self.selectperson.setObjectName("selectperson")
        icon5 = QIcon()
        icon5.addPixmap(
            QPixmap(":/Images/assets/icons/manager.png"), QIcon.Normal, QIcon.Off
        )
        self.selectperson.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addPixmap(
            QPixmap(":/Images/assets/icons/repres.png"), QIcon.Normal, QIcon.Off
        )
        self.selectperson.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addPixmap(
            QPixmap(":/Images/assets/icons/customer.png"), QIcon.Normal, QIcon.Off
        )
        self.selectperson.addItem(icon7, "")
        self.verticalLayout.addWidget(self.selectperson, 0, Qt.AlignHCenter)
        self.loginbutton = QPushButton(self.loginwidget)
        self.loginbutton.setMinimumSize(QSize(120, 40))
        self.loginbutton.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setObjectName("loginbutton")
        self.verticalLayout.addWidget(self.loginbutton, 0, Qt.AlignHCenter)
        self.forgotbutton = QPushButton(self.loginwidget)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.forgotbutton.setFont(font)
        self.forgotbutton.setStyleSheet(
            "border-radius:7px;\n" "color: rgb(255, 255, 255);\n" ""
        )
        self.forgotbutton.setCheckable(True)
        self.forgotbutton.setObjectName("forgotbutton")
        self.verticalLayout.addWidget(self.forgotbutton, 0, Qt.AlignHCenter)
        self.socialmedia = QFrame(self.widget)
        self.socialmedia.setGeometry(QRect(380, 460, 218, 55))
        self.socialmedia.setMinimumSize(QSize(218, 55))
        self.socialmedia.setMaximumSize(QSize(218, 55))
        self.socialmedia.setStyleSheet(
            "QPushButton{\n"
            "    background-color: transparent;\n"
            "    border-radius:10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-bottom:5px;\n"
            "}\n"
            "\n"
            "#socialmedia{\n"
            "    border-radius:20px;\n"
            "}\n"
            "\n"
            ""
        )
        self.socialmedia.setFrameShape(QFrame.StyledPanel)
        self.socialmedia.setFrameShadow(QFrame.Raised)
        self.socialmedia.setObjectName("socialmedia")
        self.horizontalLayout_6 = QHBoxLayout(self.socialmedia)
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.facebookbutton = QPushButton(self.socialmedia)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.facebookbutton.sizePolicy().hasHeightForWidth()
        )
        self.facebookbutton.setSizePolicy(sizePolicy)
        self.facebookbutton.setMinimumSize(QSize(52, 52))
        self.facebookbutton.setMaximumSize(QSize(52, 52))
        self.facebookbutton.setStyleSheet("")
        self.facebookbutton.setText("")
        icon8 = QIcon()
        icon8.addPixmap(
            QPixmap(":/Images/assets/icons/face.png"), QIcon.Normal, QIcon.Off
        )
        self.facebookbutton.setIcon(icon8)
        self.facebookbutton.setIconSize(QSize(50, 50))
        self.facebookbutton.setObjectName("facebookbutton")
        self.horizontalLayout_6.addWidget(self.facebookbutton)
        self.instagrambutton = QPushButton(self.socialmedia)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.instagrambutton.sizePolicy().hasHeightForWidth()
        )
        self.instagrambutton.setSizePolicy(sizePolicy)
        self.instagrambutton.setMinimumSize(QSize(52, 52))
        self.instagrambutton.setMaximumSize(QSize(52, 52))
        self.instagrambutton.setStyleSheet("")
        self.instagrambutton.setText("")
        icon9 = QIcon()
        icon9.addPixmap(
            QPixmap(":/Images/assets/icons/ins.png"), QIcon.Normal, QIcon.Off
        )
        self.instagrambutton.setIcon(icon9)
        self.instagrambutton.setIconSize(QSize(50, 50))
        self.instagrambutton.setObjectName("instagrambutton")
        self.horizontalLayout_6.addWidget(self.instagrambutton)
        self.twitterbutton = QPushButton(self.socialmedia)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.twitterbutton.sizePolicy().hasHeightForWidth()
        )
        self.twitterbutton.setSizePolicy(sizePolicy)
        self.twitterbutton.setMinimumSize(QSize(52, 52))
        self.twitterbutton.setMaximumSize(QSize(52, 52))
        self.twitterbutton.setStyleSheet("")
        self.twitterbutton.setText("")
        icon10 = QIcon()
        icon10.addPixmap(
            QPixmap(":/Images/assets/icons/tw.png"), QIcon.Normal, QIcon.Off
        )
        self.twitterbutton.setIcon(icon10)
        self.twitterbutton.setIconSize(QSize(50, 50))
        self.twitterbutton.setObjectName("twitterbutton")
        self.horizontalLayout_6.addWidget(self.twitterbutton)
        self.whatsappbutton = QPushButton(self.socialmedia)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.whatsappbutton.sizePolicy().hasHeightForWidth()
        )
        self.whatsappbutton.setSizePolicy(sizePolicy)
        self.whatsappbutton.setMinimumSize(QSize(52, 52))
        self.whatsappbutton.setMaximumSize(QSize(52, 52))
        self.whatsappbutton.setStyleSheet("")
        self.whatsappbutton.setText("")
        icon11 = QIcon()
        icon11.addPixmap(
            QPixmap(":/Images/assets/icons/wp.png"), QIcon.Normal, QIcon.Off
        )
        self.whatsappbutton.setIcon(icon11)
        self.whatsappbutton.setIconSize(QSize(50, 50))
        self.whatsappbutton.setObjectName("whatsappbutton")
        self.horizontalLayout_6.addWidget(self.whatsappbutton)
        self.leftback.raise_()
        self.rightback.raise_()
        self.middletran.raise_()
        self.changingbutton.raise_()
        self.forgotwidget.raise_()
        self.brandi.raise_()
        self.aquitbutton.raise_()
        self.registerwidget.raise_()
        self.loginwidget.raise_()
        self.socialmedia.raise_()

        self.retranslateUi(loginpage)
        self.selectperson.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(loginpage)

    def retranslateUi(self, loginpage):
        _translate = QCoreApplication.translate
        loginpage.setWindowTitle(_translate("loginpage", "SeaBank"))
        self.changingbutton.setToolTip(
            _translate("loginpage", "Haven't you registered yet?")
        )
        self.resetforgot.setText(_translate("loginpage", "Password Reset"))
        self.citizenforgot.setPlaceholderText(
            _translate("loginpage", "  Citizenship No")
        )
        self.emailforgot.setPlaceholderText(_translate("loginpage", "  E-mail Address"))
        self.sendforgot.setText(_translate("loginpage", "Send E-Mail"))
        self.registerlabel.setText(_translate("loginpage", "Register"))
        self.name_surname.setPlaceholderText(
            _translate("loginpage", "  First and Last Name")
        )
        self.telephone.setToolTip(
            _translate(
                "loginpage",
                "<html><head/><body><p>Başında Sıfır olmadan giriniz.</p></body></html>",
            )
        )
        self.telephone.setPlaceholderText(_translate("loginpage", "  Telephone No"))
        self.citizenreg.setPlaceholderText(_translate("loginpage", "  Citizenship No"))
        self.adressreg.setPlaceholderText(_translate("loginpage", "  Adress"))
        self.emailreg.setPlaceholderText(_translate("loginpage", "  E-mail Address"))
        self.passwordreg.setToolTip(
            _translate(
                "loginpage",
                "<html><head/><body><p>6 haneli sayı giriniz.</p></body></html>",
            )
        )
        self.passwordreg.setPlaceholderText(_translate("loginpage", "  Password"))
        self.confirmpassword.setPlaceholderText(
            _translate("loginpage", "  Confirm Password")
        )
        self.registerbutton.setText(_translate("loginpage", "Add"))
        self.loglabel.setText(_translate("loginpage", "Log In"))
        self.citizenlog.setPlaceholderText(_translate("loginpage", "  Citizenship No"))
        self.passwordlog.setPlaceholderText(_translate("loginpage", "  Password"))
        self.selectperson.setItemText(0, _translate("loginpage", "Manager"))
        self.selectperson.setItemText(1, _translate("loginpage", "Representative"))
        self.selectperson.setItemText(2, _translate("loginpage", "Customer"))
        self.loginbutton.setText(_translate("loginpage", "L o g  I n"))
        self.forgotbutton.setText(_translate("loginpage", "Forgot Your Password?"))


import res_rc_rc
