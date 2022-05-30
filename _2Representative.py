from PyQt5.QtWidgets import (
    QLineEdit,
    QTableWidgetItem,
    QWidget,
    QSizePolicy,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QGridLayout,
    QComboBox,
    QTableWidget,
    QAbstractScrollArea,
    QAbstractItemView,
    QSpacerItem,
    QLayout,
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


class Ui_Represent(object):
    def setupUi(self, Represent):
        Represent.setObjectName("Represent")
        Represent.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Represent.sizePolicy().hasHeightForWidth())
        Represent.setSizePolicy(sizePolicy)
        Represent.setMinimumSize(QSize(1202, 600))
        Represent.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/Images/assets/icons/mainico.png"), QIcon.Normal, QIcon.Off
        )
        Represent.setWindowIcon(icon)
        self.centralwidget = QWidget(Represent)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(
            "*{\n"
            "    color:#000;\n"
            "    border:none;\n"
            "}\n"
            "\n"
            "\n"
            "#appHeader{\n"
            "    color:rgb(37, 150, 190);\n"
            "}\n"
            "#card1,#card2,#card3,#card4{\n"
            "        background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
            "    border-radius:20px;\n"
            "}\n"
            "\n"
            "\n"
            "#headerFrame{    \n"
            "    background-color: rgb(254, 254, 255);\n"
            "}\n"
            "#homeBtn{\n"
            "    background-color: rgb(254, 254, 255);\n"
            "    padding:10px 5px;\n"
            "    border-top-left-radius:20px;\n"
            "    text-align:left;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "#pb1,#pb2,#pb3{\n"
            "    padding:10px 5px;\n"
            "    text-align:left;\n"
            "}\n"
            "\n"
            "#menubringer,#searcher{\n"
            "    border-radius:20px;\n"
            "}\n"
            "\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "    margin: 0px 0px 0px 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: lightgray;\n"
            "    min-width: 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:horizontal {\n"
            "    background: none;\n"
            "    width: 0px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    background: none;\n"
            "    width: 0px;\n"
            "    subcontrol-position: top left;\n"
            "    subcontrol-origin: margin;\n"
            "    position: absolute;\n"
            "}\n"
            "\n"
            "QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "/* VERTICAL */\n"
            "QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "    width: 15px;\n"
            "    margin: 26px 0 26px 0;\n"
            "}\n"
            "QScrollBar::handle\n"
            "{\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:10px;\n"
            "    min-height: 26px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:6px;\n"
            "    width:20px;\n"
            "    height:20px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: top left;\n"
            "    subcontrol-origin: margin;\n"
            "    position: absolute;\n"
            "}\n"
            "\n"
            "QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    background: transparent;\n"
            "    border:none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: transparent;\n"
            "}\n"
            "QWidget {\n"
            "        background-color:transparent;\n"
            "    color: #fffff8;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "    padding-left: 4px;\n"
            "    padding-right: 4px;\n"
            "    padding-top: 4px;\n"
            "    padding-bottom: 4px;\n"
            "    font-size: 10pt;\n"
            "}\n"
            "\n"
            "QTableWidget {\n"
            "    gridline-color: #ffffff;\n"
            "    font-size: 10pt;\n"
            "}\n"
            "QTableWidget QTableCornerButton{\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "}\n"
            "\n"
            "QTableWidget QTableCornerButton::section {\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "}\n"
            "\n"
            ""
        )
        self.centralwidget.setObjectName("centralwidget")
        self.allframes = QWidget(self.centralwidget)
        self.allframes.setGeometry(QRect(100, 50, 1220, 600))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allframes.sizePolicy().hasHeightForWidth())
        self.allframes.setSizePolicy(sizePolicy)
        self.allframes.setMinimumSize(QSize(1220, 600))
        self.allframes.setMaximumSize(QSize(1220, 600))
        self.allframes.setStyleSheet("")
        self.allframes.setObjectName("allframes")
        self.horizontalLayout = QHBoxLayout(self.allframes)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QWidget(self.allframes)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        self.leftMenu.setMinimumSize(QSize(0, 600))
        self.leftMenu.setMaximumSize(QSize(0, 600))
        self.leftMenu.setStyleSheet(
            "#leftMenu{background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));border-top-left-radius:20px;border-bottom-left-radius:20px;}"
        )
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_14 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_14.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self._4customeraddinfo = QWidget(self.leftMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self._4customeraddinfo.sizePolicy().hasHeightForWidth()
        )
        self._4customeraddinfo.setSizePolicy(sizePolicy)
        self._4customeraddinfo.setMinimumSize(QSize(210, 450))
        self._4customeraddinfo.setMaximumSize(QSize(210, 450))
        self._4customeraddinfo.setStyleSheet(
            "#_4customeraddinfo{    \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
            "    border-radius:50px;\n"
            "}\n"
            "\n"
            "QLineEdit,QTextEdit{\n"
            "    border-radius:20px;\n"
            "}\n"
            ""
        )
        self._4customeraddinfo.setObjectName("_4customeraddinfo")
        self.verticalLayout_4 = QVBoxLayout(self._4customeraddinfo)
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, 17)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.registerlabelrep = QLabel(self._4customeraddinfo)
        self.registerlabelrep.setMinimumSize(QSize(190, 40))
        self.registerlabelrep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.registerlabelrep.setFont(font)
        self.registerlabelrep.setStyleSheet("color: rgb(255, 255, 255);")
        self.registerlabelrep.setScaledContents(True)
        self.registerlabelrep.setAlignment(Qt.AlignCenter)
        self.registerlabelrep.setObjectName("registerlabelrep")
        self.verticalLayout_4.addWidget(self.registerlabelrep, 0, Qt.AlignHCenter)
        self.name_surnamerep = QLineEdit(self._4customeraddinfo)
        self.name_surnamerep.setMinimumSize(QSize(190, 40))
        self.name_surnamerep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.name_surnamerep.setFont(font)
        self.name_surnamerep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.name_surnamerep.setText("")
        self.name_surnamerep.setCursorPosition(0)
        self.name_surnamerep.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.name_surnamerep.setClearButtonEnabled(False)
        self.name_surnamerep.setObjectName("name_surnamerep")
        self.verticalLayout_4.addWidget(self.name_surnamerep, 0, Qt.AlignHCenter)
        self.telephonerep = QLineEdit(self._4customeraddinfo)
        self.telephonerep.setMinimumSize(QSize(190, 40))
        self.telephonerep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.telephonerep.setFont(font)
        self.telephonerep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.telephonerep.setMaxLength(10)
        self.telephonerep.setClearButtonEnabled(False)
        self.telephonerep.setObjectName("telephonerep")
        self.verticalLayout_4.addWidget(self.telephonerep, 0, Qt.AlignHCenter)
        self.citizenrep = QLineEdit(self._4customeraddinfo)
        self.citizenrep.setMinimumSize(QSize(190, 40))
        self.citizenrep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.citizenrep.setFont(font)
        self.citizenrep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.citizenrep.setMaxLength(11)
        self.citizenrep.setClearButtonEnabled(False)
        self.citizenrep.setObjectName("citizenrep")
        self.verticalLayout_4.addWidget(self.citizenrep, 0, Qt.AlignHCenter)
        self.addressrep = QLineEdit(self._4customeraddinfo)
        self.addressrep.setMinimumSize(QSize(190, 70))
        self.addressrep.setMaximumSize(QSize(190, 70))
        font = QFont()
        font.setPointSize(12)
        self.addressrep.setFont(font)
        self.addressrep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:40px;"
        )
        self.addressrep.setText("")
        self.addressrep.setCursorPosition(0)
        self.addressrep.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.addressrep.setClearButtonEnabled(False)
        self.addressrep.setObjectName("addressrep")
        self.verticalLayout_4.addWidget(self.addressrep, 0, Qt.AlignHCenter)
        self.emailrep = QLineEdit(self._4customeraddinfo)
        self.emailrep.setMinimumSize(QSize(190, 40))
        self.emailrep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.emailrep.setFont(font)
        self.emailrep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.emailrep.setEchoMode(QLineEdit.Normal)
        self.emailrep.setObjectName("emailrep")
        self.verticalLayout_4.addWidget(self.emailrep, 0, Qt.AlignHCenter)
        self.passwordrep = QLineEdit(self._4customeraddinfo)
        self.passwordrep.setMinimumSize(QSize(190, 40))
        self.passwordrep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.passwordrep.setFont(font)
        self.passwordrep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.passwordrep.setMaxLength(6)
        self.passwordrep.setEchoMode(QLineEdit.Normal)
        self.passwordrep.setObjectName("passwordrep")
        self.verticalLayout_4.addWidget(self.passwordrep, 0, Qt.AlignHCenter)
        self.confirmpasswordrep = QLineEdit(self._4customeraddinfo)
        self.confirmpasswordrep.setMinimumSize(QSize(190, 40))
        self.confirmpasswordrep.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.confirmpasswordrep.setFont(font)
        self.confirmpasswordrep.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.confirmpasswordrep.setMaxLength(6)
        self.confirmpasswordrep.setEchoMode(QLineEdit.Normal)
        self.confirmpasswordrep.setObjectName("confirmpasswordrep")
        self.verticalLayout_4.addWidget(self.confirmpasswordrep, 0, Qt.AlignHCenter)
        self.registerbuttonrep = QPushButton(self._4customeraddinfo)
        self.registerbuttonrep.setMinimumSize(QSize(100, 40))
        self.registerbuttonrep.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.registerbuttonrep.setFont(font)
        self.registerbuttonrep.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}"
        )
        self.registerbuttonrep.setObjectName("registerbuttonrep")
        self.verticalLayout_4.addWidget(
            self.registerbuttonrep, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.verticalLayout_14.addWidget(self._4customeraddinfo, 0, Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignHCenter)
        self.mainBody = QWidget(self.allframes)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(780, 600))
        self.mainBody.setMaximumSize(QSize(780, 600))
        self.mainBody.setStyleSheet(
            "#mainBody{background-color: rgb(255, 255, 255);border-radius:20px;}"
        )
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout_18 = QVBoxLayout(self.mainBody)
        self.verticalLayout_18.setContentsMargins(4, 0, 4, 10)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.headerFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QSize(740, 60))
        self.headerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.headerFrame.setStyleSheet("border-radius:20px;\n" "")
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_4.setContentsMargins(8, 2, 8, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.custaddbutton = QPushButton(self.headerFrame)
        self.custaddbutton.setMinimumSize(QSize(55, 55))
        self.custaddbutton.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.custaddbutton.setFont(font)
        self.custaddbutton.setStyleSheet("")
        self.custaddbutton.setText("")
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(":/Images/assets/icons/b2.png"), QIcon.Normal, QIcon.Off
        )
        self.custaddbutton.setIcon(icon1)
        self.custaddbutton.setIconSize(QSize(50, 50))
        self.custaddbutton.setCheckable(True)
        self.custaddbutton.setObjectName("custaddbutton")
        self.horizontalLayout_4.addWidget(self.custaddbutton)
        self.maintitle = QWidget(self.headerFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintitle.sizePolicy().hasHeightForWidth())
        self.maintitle.setSizePolicy(sizePolicy)
        self.maintitle.setStyleSheet("")
        self.maintitle.setObjectName("maintitle")
        self.horizontalLayout_23 = QHBoxLayout(self.maintitle)
        self.horizontalLayout_23.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.appHeader = QLabel(self.maintitle)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.appHeader.setFont(font)
        self.appHeader.setStyleSheet("color: rgb(7, 61, 247);")
        self.appHeader.setAlignment(Qt.AlignCenter)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_23.addWidget(self.appHeader)
        self.horizontalLayout_4.addWidget(self.maintitle)
        self.profilebutton = QPushButton(self.headerFrame)
        self.profilebutton.setMinimumSize(QSize(55, 55))
        self.profilebutton.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.profilebutton.setFont(font)
        self.profilebutton.setStyleSheet("")
        self.profilebutton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(":/Images/assets/icons/userprof.png"), QIcon.Normal, QIcon.Off
        )
        self.profilebutton.setIcon(icon2)
        self.profilebutton.setIconSize(QSize(55, 55))
        self.profilebutton.setCheckable(True)
        self.profilebutton.setObjectName("profilebutton")
        self.horizontalLayout_4.addWidget(self.profilebutton, 0, Qt.AlignTop)
        self.verticalLayout_18.addWidget(self.headerFrame, 0, Qt.AlignTop)
        self.statusFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusFrame.sizePolicy().hasHeightForWidth())
        self.statusFrame.setSizePolicy(sizePolicy)
        self.statusFrame.setMinimumSize(QSize(785, 130))
        self.statusFrame.setMaximumSize(QSize(16777215, 130))
        self.statusFrame.setObjectName("statusFrame")
        self.horizontalLayout_26 = QHBoxLayout(self.statusFrame)
        self.horizontalLayout_26.setContentsMargins(0, 0, 12, 0)
        self.horizontalLayout_26.setSpacing(8)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.card1 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card1.sizePolicy().hasHeightForWidth())
        self.card1.setSizePolicy(sizePolicy)
        self.card1.setMinimumSize(QSize(160, 114))
        self.card1.setStyleSheet(
            "QLineEdit{\n"
            "    background-color:transparent;\n"
            "    border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "    color:rgba(0, 0, 0, 255);\n"
            "}\n"
            ""
        )
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_19 = QVBoxLayout(self.card1)
        self.verticalLayout_19.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_19 = QFrame(self.card1)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_27 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_51 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_27.addWidget(self.label_51)
        self.incomeicon = QPushButton(self.frame_19)
        self.incomeicon.setMinimumSize(QSize(55, 55))
        self.incomeicon.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.incomeicon.setFont(font)
        self.incomeicon.setStyleSheet("")
        self.incomeicon.setText("")
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(":/Images/assets/icons/incomdene.png"), QIcon.Normal, QIcon.Off
        )
        self.incomeicon.setIcon(icon3)
        self.incomeicon.setIconSize(QSize(55, 55))
        self.incomeicon.setCheckable(True)
        self.incomeicon.setObjectName("incomeicon")
        self.horizontalLayout_27.addWidget(self.incomeicon)
        self.verticalLayout_19.addWidget(self.frame_19)
        self.incomeclient = QLineEdit(self.card1)
        self.incomeclient.setMinimumSize(QSize(150, 40))
        self.incomeclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.incomeclient.setFont(font)
        self.incomeclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "border-radius:20px;\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.incomeclient.setText("")
        self.incomeclient.setCursorPosition(0)
        self.incomeclient.setReadOnly(True)
        self.incomeclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.incomeclient.setClearButtonEnabled(False)
        self.incomeclient.setObjectName("incomeclient")
        self.verticalLayout_19.addWidget(self.incomeclient)
        self.horizontalLayout_26.addWidget(self.card1, 0, Qt.AlignVCenter)
        self.card2 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card2.sizePolicy().hasHeightForWidth())
        self.card2.setSizePolicy(sizePolicy)
        self.card2.setMinimumSize(QSize(160, 0))
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_20 = QVBoxLayout(self.card2)
        self.verticalLayout_20.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_20 = QFrame(self.card2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_28 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_54 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_28.addWidget(self.label_54)
        self.expenseicon = QPushButton(self.frame_20)
        self.expenseicon.setMinimumSize(QSize(55, 55))
        self.expenseicon.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.expenseicon.setFont(font)
        self.expenseicon.setStyleSheet("")
        self.expenseicon.setText("")
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(":/Images/assets/icons/expense.png"), QIcon.Normal, QIcon.Off
        )
        self.expenseicon.setIcon(icon4)
        self.expenseicon.setIconSize(QSize(55, 55))
        self.expenseicon.setCheckable(True)
        self.expenseicon.setObjectName("expenseicon")
        self.horizontalLayout_28.addWidget(self.expenseicon)
        self.verticalLayout_20.addWidget(self.frame_20)
        self.expenseclient = QLineEdit(self.card2)
        self.expenseclient.setMinimumSize(QSize(150, 40))
        self.expenseclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.expenseclient.setFont(font)
        self.expenseclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "border-radius:20px;\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.expenseclient.setText("")
        self.expenseclient.setCursorPosition(0)
        self.expenseclient.setReadOnly(True)
        self.expenseclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.expenseclient.setClearButtonEnabled(False)
        self.expenseclient.setObjectName("expenseclient")
        self.verticalLayout_20.addWidget(self.expenseclient)
        self.horizontalLayout_26.addWidget(self.card2, 0, Qt.AlignVCenter)
        self.card3 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card3.sizePolicy().hasHeightForWidth())
        self.card3.setSizePolicy(sizePolicy)
        self.card3.setMinimumSize(QSize(160, 0))
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_21 = QVBoxLayout(self.card3)
        self.verticalLayout_21.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_21 = QFrame(self.card3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_29 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setSpacing(6)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_57 = QLabel(self.frame_21)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_29.addWidget(self.label_57)
        self.profiticon = QPushButton(self.frame_21)
        self.profiticon.setMinimumSize(QSize(55, 55))
        self.profiticon.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.profiticon.setFont(font)
        self.profiticon.setStyleSheet("")
        self.profiticon.setText("")
        icon5 = QIcon()
        icon5.addPixmap(
            QPixmap(":/Images/assets/icons/profit.png"), QIcon.Normal, QIcon.Off
        )
        self.profiticon.setIcon(icon5)
        self.profiticon.setIconSize(QSize(55, 55))
        self.profiticon.setCheckable(True)
        self.profiticon.setObjectName("profiticon")
        self.horizontalLayout_29.addWidget(self.profiticon)
        self.verticalLayout_21.addWidget(self.frame_21)
        self.profitclient = QLineEdit(self.card3)
        self.profitclient.setMinimumSize(QSize(150, 40))
        self.profitclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.profitclient.setFont(font)
        self.profitclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "border-radius:20px;\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.profitclient.setText("")
        self.profitclient.setCursorPosition(0)
        self.profitclient.setReadOnly(True)
        self.profitclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.profitclient.setClearButtonEnabled(False)
        self.profitclient.setObjectName("profitclient")
        self.verticalLayout_21.addWidget(self.profitclient)
        self.horizontalLayout_26.addWidget(self.card3, 0, Qt.AlignVCenter)
        self.card4 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card4.sizePolicy().hasHeightForWidth())
        self.card4.setSizePolicy(sizePolicy)
        self.card4.setMinimumSize(QSize(160, 0))
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_22 = QVBoxLayout(self.card4)
        self.verticalLayout_22.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_22 = QFrame(self.card4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(7)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_60 = QLabel(self.frame_22)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_30.addWidget(self.label_60)
        self.balanceicon = QPushButton(self.frame_22)
        self.balanceicon.setMinimumSize(QSize(55, 55))
        self.balanceicon.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.balanceicon.setFont(font)
        self.balanceicon.setStyleSheet("")
        self.balanceicon.setText("")
        icon6 = QIcon()
        icon6.addPixmap(
            QPixmap(":/Images/assets/icons/total.png"), QIcon.Normal, QIcon.Off
        )
        self.balanceicon.setIcon(icon6)
        self.balanceicon.setIconSize(QSize(55, 55))
        self.balanceicon.setCheckable(True)
        self.balanceicon.setObjectName("balanceicon")
        self.horizontalLayout_30.addWidget(self.balanceicon)
        self.verticalLayout_22.addWidget(self.frame_22)
        self.totalclient = QLineEdit(self.card4)
        self.totalclient.setMinimumSize(QSize(150, 40))
        self.totalclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.totalclient.setFont(font)
        self.totalclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "border-radius:20px;\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.totalclient.setText("")
        self.totalclient.setCursorPosition(0)
        self.totalclient.setReadOnly(True)
        self.totalclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.totalclient.setClearButtonEnabled(False)
        self.totalclient.setObjectName("totalclient")
        self.verticalLayout_22.addWidget(self.totalclient)
        self.horizontalLayout_26.addWidget(self.card4, 0, Qt.AlignVCenter)
        self.verticalLayout_18.addWidget(
            self.statusFrame, 0, Qt.AlignHCenter | Qt.AlignTop
        )
        self.generalframe = QFrame(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generalframe.sizePolicy().hasHeightForWidth())
        self.generalframe.setSizePolicy(sizePolicy)
        self.generalframe.setMinimumSize(QSize(740, 210))
        self.generalframe.setMaximumSize(QSize(16777215, 16777215))
        self.generalframe.setFrameShape(QFrame.StyledPanel)
        self.generalframe.setFrameShadow(QFrame.Raised)
        self.generalframe.setObjectName("generalframe")
        self.horizontalLayout_2 = QHBoxLayout(self.generalframe)
        self.horizontalLayout_2.setContentsMargins(2, 0, 4, 20)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clientFrame = QFrame(self.generalframe)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientFrame.sizePolicy().hasHeightForWidth())
        self.clientFrame.setSizePolicy(sizePolicy)
        self.clientFrame.setMinimumSize(QSize(360, 200))
        self.clientFrame.setMaximumSize(QSize(360, 200))
        self.clientFrame.setStyleSheet(
            "#clientFrame{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
            "    border-radius:20px;\n"
            "    border: 2px solid rgb(37, 150, 190);\n"
            "\n"
            "}\n"
            "QLineEdit,QTextEdit,#selectclients,#selectrow{\n"
            "    border-radius:20px;\n"
            "}\n"
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}"
        )
        self.clientFrame.setFrameShape(QFrame.StyledPanel)
        self.clientFrame.setFrameShadow(QFrame.Raised)
        self.clientFrame.setObjectName("clientFrame")
        self.verticalLayout_2 = QVBoxLayout(self.clientFrame)
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CurrencyTitle = QFrame(self.clientFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CurrencyTitle.sizePolicy().hasHeightForWidth()
        )
        self.CurrencyTitle.setSizePolicy(sizePolicy)
        self.CurrencyTitle.setMinimumSize(QSize(360, 55))
        self.CurrencyTitle.setMaximumSize(QSize(360, 55))
        self.CurrencyTitle.setStyleSheet(
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
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: transparent;\n"
            "}\n"
            "QScrollBar::handle::vertical {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:6px;\n"
            "    width:20px;\n"
            "    height:20px;\n"
            "}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "    width: 15px;\n"
            "    margin: 26px 0 26px 0;\n"
            "}\n"
            "QScrollBar::handle\n"
            "{\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:10px;\n"
            "    min-height: 26px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: top left;\n"
            "    subcontrol-origin: margin;\n"
            "    position: absolute;\n"
            "}\n"
            "\n"
            "QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "    width: 10px;\n"
            "    height: 10px;\n"
            "    background: transparent;\n"
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
        self.CurrencyTitle.setFrameShape(QFrame.StyledPanel)
        self.CurrencyTitle.setFrameShadow(QFrame.Raised)
        self.CurrencyTitle.setObjectName("CurrencyTitle")
        self.horizontalLayout_9 = QHBoxLayout(self.CurrencyTitle)
        self.horizontalLayout_9.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.personicon = QPushButton(self.CurrencyTitle)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personicon.sizePolicy().hasHeightForWidth())
        self.personicon.setSizePolicy(sizePolicy)
        self.personicon.setMinimumSize(QSize(50, 50))
        self.personicon.setMaximumSize(QSize(50, 50))
        self.personicon.setStyleSheet("background-color:transparent;")
        self.personicon.setText("")
        icon7 = QIcon()
        icon7.addPixmap(
            QPixmap(":/Images/assets/icons/account.png"), QIcon.Normal, QIcon.Off
        )
        self.personicon.setIcon(icon7)
        self.personicon.setIconSize(QSize(50, 50))
        self.personicon.setObjectName("personicon")
        self.horizontalLayout_9.addWidget(self.personicon)
        self.selectclients = QComboBox(self.CurrencyTitle)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.selectclients.sizePolicy().hasHeightForWidth()
        )
        self.selectclients.setSizePolicy(sizePolicy)
        self.selectclients.setMinimumSize(QSize(190, 40))
        self.selectclients.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.selectclients.setFont(font)
        self.selectclients.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.selectclients.setInsertPolicy(QComboBox.InsertAtBottom)
        self.selectclients.setIconSize(QSize(40, 40))
        self.selectclients.setPlaceholderText("")
        self.selectclients.setObjectName("selectclients")
        self.horizontalLayout_9.addWidget(self.selectclients)
        self.addclients = QPushButton(self.CurrencyTitle)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addclients.sizePolicy().hasHeightForWidth())
        self.addclients.setSizePolicy(sizePolicy)
        self.addclients.setMinimumSize(QSize(70, 40))
        self.addclients.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addclients.setFont(font)
        self.addclients.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1 rgba(0, 0, 255, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            ""
        )
        self.addclients.setObjectName("addclients")
        self.horizontalLayout_9.addWidget(self.addclients)
        self.verticalLayout_2.addWidget(
            self.CurrencyTitle, 0, Qt.AlignHCenter | Qt.AlignTop
        )
        self.clientsinfo = QFrame(self.clientFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientsinfo.sizePolicy().hasHeightForWidth())
        self.clientsinfo.setSizePolicy(sizePolicy)
        self.clientsinfo.setStyleSheet("")
        self.clientsinfo.setFrameShape(QFrame.StyledPanel)
        self.clientsinfo.setFrameShadow(QFrame.Raised)
        self.clientsinfo.setObjectName("clientsinfo")
        self.gridLayout_5 = QGridLayout(self.clientsinfo)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.adressclient = QLineEdit(self.clientsinfo)
        self.adressclient.setMinimumSize(QSize(200, 40))
        self.adressclient.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(12)
        self.adressclient.setFont(font)
        self.adressclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.adressclient.setText("")
        self.adressclient.setEchoMode(QLineEdit.Normal)
        self.adressclient.setObjectName("adressclient")
        self.gridLayout_5.addWidget(self.adressclient, 1, 0, 1, 1)
        self.frame_3 = QFrame(self.clientsinfo)
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveclients = QPushButton(self.frame_3)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveclients.sizePolicy().hasHeightForWidth())
        self.saveclients.setSizePolicy(sizePolicy)
        self.saveclients.setMinimumSize(QSize(70, 40))
        self.saveclients.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saveclients.setFont(font)
        self.saveclients.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1 rgba(0, 0, 255, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            ""
        )
        self.saveclients.setObjectName("saveclients")
        self.horizontalLayout_3.addWidget(self.saveclients)
        self.deleteclients = QPushButton(self.frame_3)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deleteclients.sizePolicy().hasHeightForWidth()
        )
        self.deleteclients.setSizePolicy(sizePolicy)
        self.deleteclients.setMinimumSize(QSize(70, 40))
        self.deleteclients.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.deleteclients.setFont(font)
        self.deleteclients.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1  rgba(255, 0, 0, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            "\n"
            ""
        )
        self.deleteclients.setObjectName("deleteclients")
        self.horizontalLayout_3.addWidget(self.deleteclients)
        self.gridLayout_5.addWidget(self.frame_3, 3, 3, 1, 1)
        self.citizenclient = QLineEdit(self.clientsinfo)
        self.citizenclient.setMinimumSize(QSize(140, 40))
        self.citizenclient.setMaximumSize(QSize(140, 40))
        font = QFont()
        font.setPointSize(12)
        self.citizenclient.setFont(font)
        self.citizenclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.citizenclient.setMaxLength(16)
        self.citizenclient.setReadOnly(True)
        self.citizenclient.setClearButtonEnabled(False)
        self.citizenclient.setObjectName("citizenclient")
        self.gridLayout_5.addWidget(self.citizenclient, 0, 3, 1, 1)
        self.nameclient = QLineEdit(self.clientsinfo)
        self.nameclient.setMinimumSize(QSize(200, 40))
        self.nameclient.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(12)
        self.nameclient.setFont(font)
        self.nameclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.nameclient.setText("")
        self.nameclient.setCursorPosition(0)
        self.nameclient.setReadOnly(True)
        self.nameclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.nameclient.setClearButtonEnabled(False)
        self.nameclient.setObjectName("nameclient")
        self.gridLayout_5.addWidget(self.nameclient, 0, 0, 1, 1)
        self.telephoneclient = QLineEdit(self.clientsinfo)
        self.telephoneclient.setMinimumSize(QSize(140, 40))
        self.telephoneclient.setMaximumSize(QSize(140, 40))
        font = QFont()
        font.setPointSize(12)
        self.telephoneclient.setFont(font)
        self.telephoneclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.telephoneclient.setMaxLength(17)
        self.telephoneclient.setClearButtonEnabled(False)
        self.telephoneclient.setObjectName("telephoneclient")
        self.gridLayout_5.addWidget(self.telephoneclient, 1, 3, 1, 1)
        self.emailclient = QLineEdit(self.clientsinfo)
        self.emailclient.setMinimumSize(QSize(200, 40))
        self.emailclient.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(12)
        self.emailclient.setFont(font)
        self.emailclient.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.emailclient.setText("")
        self.emailclient.setEchoMode(QLineEdit.Normal)
        self.emailclient.setObjectName("emailclient")
        self.gridLayout_5.addWidget(self.emailclient, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.clientsinfo)
        self.horizontalLayout_2.addWidget(self.clientFrame, 0, Qt.AlignTop)
        self.demandlFrame = QFrame(self.generalframe)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demandlFrame.sizePolicy().hasHeightForWidth())
        self.demandlFrame.setSizePolicy(sizePolicy)
        self.demandlFrame.setMinimumSize(QSize(360, 200))
        self.demandlFrame.setMaximumSize(QSize(360, 200))
        self.demandlFrame.setStyleSheet(
            "#demandlFrame{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
            "    border-radius:20px;\n"
            "    border: 2px solid rgb(37, 150, 190);\n"
            "\n"
            "}\n"
            "#demandsbox{border-radius:20px;}\n"
            "QPushButton{\n"
            "    background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}"
        )
        self.demandlFrame.setFrameShape(QFrame.StyledPanel)
        self.demandlFrame.setFrameShadow(QFrame.Raised)
        self.demandlFrame.setObjectName("demandlFrame")
        self.gridLayout_3 = QGridLayout(self.demandlFrame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.demandstitle = QFrame(self.demandlFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demandstitle.sizePolicy().hasHeightForWidth())
        self.demandstitle.setSizePolicy(sizePolicy)
        self.demandstitle.setMinimumSize(QSize(245, 45))
        self.demandstitle.setMaximumSize(QSize(16777215, 16777215))
        self.demandstitle.setFrameShape(QFrame.StyledPanel)
        self.demandstitle.setFrameShadow(QFrame.Raised)
        self.demandstitle.setObjectName("demandstitle")
        self.horizontalLayout_12 = QHBoxLayout(self.demandstitle)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.demandsicon = QPushButton(self.demandstitle)
        self.demandsicon.setMinimumSize(QSize(55, 55))
        self.demandsicon.setMaximumSize(QSize(55, 55))
        self.demandsicon.setStyleSheet("background-color:transparent;")
        self.demandsicon.setText("")
        icon8 = QIcon()
        icon8.addPixmap(
            QPixmap(":/Images/assets/icons/credit.png"), QIcon.Normal, QIcon.Off
        )
        self.demandsicon.setIcon(icon8)
        self.demandsicon.setIconSize(QSize(50, 50))
        self.demandsicon.setObjectName("demandsicon")
        self.horizontalLayout_12.addWidget(self.demandsicon, 0, Qt.AlignHCenter)
        self.titleofsclabel_3 = QLabel(self.demandstitle)
        self.titleofsclabel_3.setMinimumSize(QSize(205, 30))
        self.titleofsclabel_3.setMaximumSize(QSize(205, 30))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.titleofsclabel_3.setFont(font)
        self.titleofsclabel_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleofsclabel_3.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.titleofsclabel_3.setObjectName("titleofsclabel_3")
        self.horizontalLayout_12.addWidget(self.titleofsclabel_3)
        self.gridLayout_3.addWidget(
            self.demandstitle, 0, 1, 1, 1, Qt.AlignHCenter | Qt.AlignTop
        )
        self.editing = QFrame(self.demandlFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editing.sizePolicy().hasHeightForWidth())
        self.editing.setSizePolicy(sizePolicy)
        self.editing.setStyleSheet(
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
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: transparent;\n"
            "}\n"
            "QScrollBar::handle::vertical {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:6px;\n"
            "    width:20px;\n"
            "    height:20px;\n"
            "}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "    width: 15px;\n"
            "    margin: 26px 0 26px 0;\n"
            "}\n"
            "QScrollBar::handle\n"
            "{\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:10px;\n"
            "    min-height: 26px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: top left;\n"
            "    subcontrol-origin: margin;\n"
            "    position: absolute;\n"
            "}\n"
            "\n"
            "QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "    width: 10px;\n"
            "    height: 10px;\n"
            "    background: transparent;\n"
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
        self.editing.setFrameShape(QFrame.StyledPanel)
        self.editing.setFrameShadow(QFrame.Raised)
        self.editing.setObjectName("editing")
        self.gridLayout_4 = QGridLayout(self.editing)
        self.gridLayout_4.setContentsMargins(2, 11, 2, 6)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QFrame(self.editing)
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.demanddeny = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demanddeny.sizePolicy().hasHeightForWidth())
        self.demanddeny.setSizePolicy(sizePolicy)
        self.demanddeny.setMinimumSize(QSize(100, 40))
        self.demanddeny.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.demanddeny.setFont(font)
        self.demanddeny.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1  rgba(255, 0, 0, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            "\n"
            ""
        )
        self.demanddeny.setObjectName("demanddeny")
        self.horizontalLayout_5.addWidget(self.demanddeny)
        self.demandapprove = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.demandapprove.sizePolicy().hasHeightForWidth()
        )
        self.demandapprove.setSizePolicy(sizePolicy)
        self.demandapprove.setMinimumSize(QSize(100, 40))
        self.demandapprove.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.demandapprove.setFont(font)
        self.demandapprove.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1 rgba(0, 0, 255, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            ""
        )
        self.demandapprove.setObjectName("demandapprove")
        self.horizontalLayout_5.addWidget(self.demandapprove)
        self.gridLayout_4.addWidget(
            self.frame, 1, 0, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.demandsbox = QComboBox(self.editing)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demandsbox.sizePolicy().hasHeightForWidth())
        self.demandsbox.setSizePolicy(sizePolicy)
        self.demandsbox.setMinimumSize(QSize(350, 40))
        self.demandsbox.setMaximumSize(QSize(350, 40))
        font = QFont()
        font.setPointSize(14)
        self.demandsbox.setFont(font)
        self.demandsbox.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.demandsbox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.demandsbox.setIconSize(QSize(40, 40))
        self.demandsbox.setPlaceholderText("")
        self.demandsbox.setObjectName("demandsbox")
        self.gridLayout_4.addWidget(self.demandsbox, 0, 0, 1, 1, Qt.AlignHCenter)
        self.gridLayout_3.addWidget(self.editing, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.demandlFrame, 0, Qt.AlignTop)
        self.verticalLayout_18.addWidget(
            self.generalframe, 0, Qt.AlignHCenter | Qt.AlignTop
        )
        self.mainFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QSize(788, 0))
        self.mainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.monthlystatements = QWidget(self.mainFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.monthlystatements.sizePolicy().hasHeightForWidth()
        )
        self.monthlystatements.setSizePolicy(sizePolicy)
        self.monthlystatements.setMinimumSize(QSize(740, 0))
        self.monthlystatements.setMaximumSize(QSize(740, 16777215))
        self.monthlystatements.setStyleSheet(
            "#selectrowstatus{\n"
            "    border-radius:20px;\n"
            "}\n"
            "#monthlystatements{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
            "    border-radius:20px;\n"
            "    border: 2px solid rgb(37, 150, 190);\n"
            "\n"
            "}\n"
            "\n"
            "QWidget {\n"
            "        background-color:transparent;\n"
            "    color: #fffff8;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "    padding-left: 4px;\n"
            "    padding-right: 4px;\n"
            "    padding-top: 4px;\n"
            "    padding-bottom: 4px;\n"
            "    font-size: 10pt;\n"
            "}\n"
            "\n"
            "QTableWidget {\n"
            "    gridline-color: #ffffff;\n"
            "    font-size: 10pt;\n"
            "}\n"
            "QTableWidget QTableCornerButton{\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "}\n"
            "\n"
            "QTableWidget QTableCornerButton::section {\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "}"
        )
        self.monthlystatements.setObjectName("monthlystatements")
        self.verticalLayout = QVBoxLayout(self.monthlystatements)
        self.verticalLayout.setContentsMargins(2, 3, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_23 = QFrame(self.monthlystatements)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QSize(0, 40))
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setStyleSheet(
            "#addmorestate{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "#addmorestate:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "\n"
            "#addmorestate:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}"
        )
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_33 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_33.setContentsMargins(2, 0, 6, 0)
        self.horizontalLayout_33.setSpacing(9)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem)
        self.statementicon = QPushButton(self.frame_23)
        self.statementicon.setMinimumSize(QSize(40, 40))
        self.statementicon.setMaximumSize(QSize(40, 40))
        self.statementicon.setText("")
        icon9 = QIcon()
        icon9.addPixmap(
            QPixmap(":/Images/assets/icons/statements.png"), QIcon.Normal, QIcon.Off
        )
        self.statementicon.setIcon(icon9)
        self.statementicon.setIconSize(QSize(50, 40))
        self.statementicon.setObjectName("statementicon")
        self.horizontalLayout_33.addWidget(self.statementicon)
        self.label_76 = QLabel(self.frame_23)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setMinimumSize(QSize(300, 40))
        self.label_76.setMaximumSize(QSize(300, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_76.setObjectName("label_76")
        self.horizontalLayout_33.addWidget(self.label_76)
        self.addmorestate = QPushButton(self.frame_23)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addmorestate.sizePolicy().hasHeightForWidth())
        self.addmorestate.setSizePolicy(sizePolicy)
        self.addmorestate.setMinimumSize(QSize(100, 40))
        self.addmorestate.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addmorestate.setFont(font)
        self.addmorestate.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1 rgba(0, 0, 255, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            ""
        )
        self.addmorestate.setObjectName("addmorestate")
        self.horizontalLayout_33.addWidget(self.addmorestate)
        self.delstate = QPushButton(self.frame_23)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delstate.sizePolicy().hasHeightForWidth())
        self.delstate.setSizePolicy(sizePolicy)
        self.delstate.setMinimumSize(QSize(100, 40))
        self.delstate.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delstate.setFont(font)
        self.delstate.setStyleSheet(
            "QPushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(85, 81, 84, 226), stop:1  rgba(255, 0, 0, 219));\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            "\n"
            ""
        )
        self.delstate.setObjectName("delstate")
        self.horizontalLayout_33.addWidget(self.delstate)
        spacerItem1 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_23)
        self.frame_2 = QFrame(self.monthlystatements)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.statementtable = QTableWidget(self.frame_2)
        self.statementtable.setMinimumSize(QSize(613, 125))
        self.statementtable.setMaximumSize(QSize(720, 125))
        font = QFont()
        font.setPointSize(10)
        self.statementtable.setFont(font)
        self.statementtable.setStyleSheet(
            "QWidget {\n"
            "        background-color:transparent;\n"
            "    color: #fffff8;\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "    padding-left: 4px;\n"
            "    padding-right: 4px;\n"
            "    padding-top: 4px;\n"
            "    padding-bottom: 4px;\n"
            "    font-size: 10pt;\n"
            "}\n"
            "\n"
            "QTableWidget {\n"
            "    gridline-color: #ffffff;\n"
            "    font-size: 10pt;\n"
            "}\n"
            "QTableWidget QTableCornerButton{\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "}\n"
            "\n"
            "QTableWidget QTableCornerButton::section {\n"
            "    background-color:rgba(0, 0, 0, 100);\n"
            "}\n"
            "\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: none;\n"
            "    height: 0px;\n"
            "    margin: 0px 0px 0px 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: lightgray;\n"
            "    min-width: 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:horizontal {\n"
            "    background: none;\n"
            "    width: 0px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    background: none;\n"
            "    width: 0px;\n"
            "    subcontrol-position: top left;\n"
            "    subcontrol-origin: margin;\n"
            "    position: absolute;\n"
            "}\n"
            "\n"
            "QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "/* VERTICAL */\n"
            "QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "    width: 15px;\n"
            "    margin: 26px 0 26px 0;\n"
            "}\n"
            "QScrollBar::handle\n"
            "{\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:10px;\n"
            "    min-height: 26px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    border-radius:6px;\n"
            "    width:20px;\n"
            "    height:20px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "    background: transparent;\n"
            "    height: 10px;\n"
            "    subcontrol-position: top left;\n"
            "    subcontrol-origin: margin;\n"
            "    position: absolute;\n"
            "}\n"
            "\n"
            "QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    background: transparent;\n"
            "    border:none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: transparent;\n"
            "}\n"
            ""
        )
        self.statementtable.setFrameShadow(QFrame.Sunken)
        self.statementtable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.statementtable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.statementtable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.statementtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.statementtable.setGridStyle(Qt.CustomDashLine)
        self.statementtable.setWordWrap(True)
        self.statementtable.setCornerButtonEnabled(False)
        self.statementtable.setRowCount(10)
        self.statementtable.setColumnCount(7)
        self.statementtable.setObjectName("statementtable")
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.statementtable.setHorizontalHeaderItem(6, item)
        self.statementtable.horizontalHeader().setDefaultSectionSize(96)
        self.statementtable.horizontalHeader().setMinimumSectionSize(96)
        self.statementtable.verticalHeader().setDefaultSectionSize(30)
        self.statementtable.verticalHeader().setHighlightSections(True)
        self.statementtable.verticalHeader().setMinimumSectionSize(30)
        self.statementtable.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_7.addWidget(self.statementtable)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(
            self.monthlystatements, 0, Qt.AlignHCenter | Qt.AlignTop
        )
        self.verticalLayout_18.addWidget(self.mainFrame, 0, Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.mainBody, 0, Qt.AlignHCenter)
        self.rightMenu = QWidget(self.allframes)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightMenu.sizePolicy().hasHeightForWidth())
        self.rightMenu.setSizePolicy(sizePolicy)
        self.rightMenu.setMinimumSize(QSize(0, 600))
        self.rightMenu.setMaximumSize(QSize(0, 600))
        self.rightMenu.setStyleSheet(
            "#rightMenu{background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));border-top-right-radius:20px;border-bottom-right-radius:20px;}\n"
            "\n"
            "#username{\n"
            "    border-radius:20px;\n"
            "}"
        )
        self.rightMenu.setObjectName("rightMenu")
        self.verticalLayout_27 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_27.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.profileframe = QFrame(self.rightMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileframe.sizePolicy().hasHeightForWidth())
        self.profileframe.setSizePolicy(sizePolicy)
        self.profileframe.setMinimumSize(QSize(210, 0))
        self.profileframe.setMaximumSize(QSize(210, 16777215))
        self.profileframe.setFrameShape(QFrame.StyledPanel)
        self.profileframe.setFrameShadow(QFrame.Raised)
        self.profileframe.setObjectName("profileframe")
        self.verticalLayout_28 = QVBoxLayout(self.profileframe)
        self.verticalLayout_28.setContentsMargins(1, 8, 1, -1)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.username = QLineEdit(self.profileframe)
        self.username.setMinimumSize(QSize(180, 40))
        self.username.setMaximumSize(QSize(180, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "border-radius:20px;\n"
            "color:rgba(255, 255, 255, 255);\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;"
        )
        self.username.setText("")
        self.username.setCursorPosition(0)
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setReadOnly(True)
        self.username.setPlaceholderText("")
        self.username.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.verticalLayout_28.addWidget(self.username, 0, Qt.AlignHCenter)
        self.coolguy = QPushButton(self.profileframe)
        self.coolguy.setMinimumSize(QSize(140, 240))
        self.coolguy.setMaximumSize(QSize(140, 240))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.coolguy.setFont(font)
        self.coolguy.setStyleSheet("")
        self.coolguy.setText("")
        icon10 = QIcon()
        icon10.addPixmap(
            QPixmap(":/Images/assets/icons/repres.png"), QIcon.Normal, QIcon.Off
        )
        self.coolguy.setIcon(icon10)
        self.coolguy.setIconSize(QSize(140, 240))
        self.coolguy.setCheckable(True)
        self.coolguy.setObjectName("coolguy")
        self.verticalLayout_28.addWidget(self.coolguy, 0, Qt.AlignHCenter)
        self.logout = QPushButton(self.profileframe)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.logout.setFont(font)
        self.logout.setStyleSheet("color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addPixmap(
            QPixmap(":/Images/assets/icons/1053210.png"), QIcon.Normal, QIcon.Off
        )
        self.logout.setIcon(icon11)
        self.logout.setIconSize(QSize(24, 24))
        self.logout.setObjectName("logout")
        self.verticalLayout_28.addWidget(self.logout)
        self.verticalLayout_27.addWidget(self.profileframe, 0, Qt.AlignTop)
        self.horizontalLayout.addWidget(self.rightMenu, 0, Qt.AlignHCenter)
        Represent.setCentralWidget(self.centralwidget)

        self.retranslateUi(Represent)
        self.selectclients.setCurrentIndex(-1)
        self.demandsbox.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(Represent)

    def retranslateUi(self, Represent):
        _translate = QCoreApplication.translate
        Represent.setWindowTitle(_translate("Represent", "SeaBank"))
        self.registerlabelrep.setText(_translate("Represent", "Information"))
        self.name_surnamerep.setPlaceholderText(
            _translate("Represent", "  First and Last Name")
        )
        self.telephonerep.setToolTip(
            _translate(
                "Represent",
                "<html><head/><body><p>Başında Sıfır olmadan giriniz.</p></body></html>",
            )
        )
        self.telephonerep.setPlaceholderText(_translate("Represent", "  Telephone No"))
        self.citizenrep.setPlaceholderText(_translate("Represent", "  Citizenship No"))
        self.addressrep.setPlaceholderText(_translate("Represent", " Address"))
        self.emailrep.setPlaceholderText(_translate("Represent", "  E-mail Address"))
        self.passwordrep.setToolTip(
            _translate(
                "Represent",
                "<html><head/><body><p>6 haneli sayı giriniz.</p></body></html>",
            )
        )
        self.passwordrep.setPlaceholderText(_translate("Represent", "  Password"))
        self.confirmpasswordrep.setPlaceholderText(
            _translate("Represent", "  Confirm Password")
        )
        self.registerbuttonrep.setText(_translate("Represent", "Add"))
        self.appHeader.setText(_translate("Represent", "Welcome to SeaBank"))
        self.label_51.setText(_translate("Represent", "Income"))
        self.incomeclient.setPlaceholderText(_translate("Represent", "    Income"))
        self.label_54.setText(_translate("Represent", "Expense"))
        self.expenseclient.setPlaceholderText(_translate("Represent", "    Expense"))
        self.label_57.setText(_translate("Represent", "Profit"))
        self.profitclient.setPlaceholderText(_translate("Represent", "    Profit   "))
        self.label_60.setText(_translate("Represent", "Balance"))
        self.totalclient.setPlaceholderText(_translate("Represent", "    Balance"))
        self.addclients.setText(_translate("Represent", "Show"))
        self.adressclient.setPlaceholderText(_translate("Represent", "    Address"))
        self.saveclients.setText(_translate("Represent", "Save"))
        self.deleteclients.setText(_translate("Represent", "Delete"))
        self.citizenclient.setPlaceholderText(
            _translate("Represent", "    Citizenship No")
        )
        self.nameclient.setPlaceholderText(
            _translate("Represent", "    First and Last Name")
        )
        self.telephoneclient.setToolTip(
            _translate(
                "Represent",
                "<html><head/><body><p>Başında Sıfır olmadan giriniz.</p></body></html>",
            )
        )
        self.telephoneclient.setPlaceholderText(
            _translate("Represent", "    Telephone No")
        )
        self.emailclient.setPlaceholderText(
            _translate("Represent", "    E-mail Address")
        )
        self.titleofsclabel_3.setText(_translate("Represent", "Credit Demands"))
        self.demanddeny.setText(_translate("Represent", "Deny"))
        self.demandapprove.setText(_translate("Represent", "Approve"))
        self.label_76.setText(_translate("Represent", "Clients Monthly Statements"))
        self.addmorestate.setText(_translate("Represent", "Add More"))
        self.delstate.setText(_translate("Represent", "Clean"))
        self.statementtable.setSortingEnabled(False)
        item = self.statementtable.horizontalHeaderItem(0)
        item.setText(_translate("Represent", "Source No"))
        item = self.statementtable.horizontalHeaderItem(1)
        item.setText(_translate("Represent", "Target No"))
        item = self.statementtable.horizontalHeaderItem(2)
        item.setText(_translate("Represent", "Procedure"))
        item = self.statementtable.horizontalHeaderItem(3)
        item.setText(_translate("Represent", "Balance"))
        item = self.statementtable.horizontalHeaderItem(4)
        item.setText(_translate("Represent", "Source Balance"))
        item = self.statementtable.horizontalHeaderItem(5)
        item.setText(_translate("Represent", "Target Balance"))
        item = self.statementtable.horizontalHeaderItem(6)
        item.setText(_translate("Represent", "Date"))
        self.logout.setText(_translate("Represent", "Log Out"))


import res_rc_rc
