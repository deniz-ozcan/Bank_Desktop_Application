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


class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Manager.sizePolicy().hasHeightForWidth())
        Manager.setSizePolicy(sizePolicy)
        Manager.setMinimumSize(QSize(0, 0))
        Manager.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/Images/assets/icons/deadlock.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        Manager.setWindowIcon(icon)
        self.centralwidget = QWidget(Manager)
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
            "#searchline{\n"
            "    background:transparent;\n"
            "    color:rgb(37, 150, 190);\n"
            "}\n"
            "\n"
            "#card1,#card2,#card3,#card4{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(17, 252, 253, 219));\n"
            "    border-radius:20px;\n"
            "}\n"
            "\n"
            "#latesttransactions,#quicktransactions{\n"
            "    background-color: rgb(254, 254, 255);\n"
            "    border-radius:20px;\n"
            "}\n"
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
            "#pb1,#pb2,#pb3{\n"
            "    padding:10px 5px;\n"
            "    text-align:left;\n"
            "}\n"
            "\n"
            "#menubringer,#searcher{\n"
            "    border-radius:20px;\n"
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
            "\n"
            "\n"
            ""
        )
        self.centralwidget.setObjectName("centralwidget")
        self.allframes = QWidget(self.centralwidget)
        self.allframes.setGeometry(QRect(100, 50, 1190, 600))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allframes.sizePolicy().hasHeightForWidth())
        self.allframes.setSizePolicy(sizePolicy)
        self.allframes.setMinimumSize(QSize(1190, 600))
        self.allframes.setMaximumSize(QSize(1190, 600))
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
            "#leftMenu{        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(17, 252, 253, 219));border-top-left-radius:20px;border-bottom-left-radius:20px;}                                                                                                                                        \n"
            "QLineEdit{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "    border:none;\n"
            "    border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "    border-radius:20px;\n"
            "    color:rgba(255, 255, 255, 255);\n"
            "    padding-left:5px;\n"
            "    padding-bottom:7px;\n"
            "}"
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
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(17, 252, 253, 219));\n"
            "    border-radius:50px;\n"
            "}\n"
            ""
        )
        self._4customeraddinfo.setObjectName("_4customeraddinfo")
        self.verticalLayout_7 = QVBoxLayout(self._4customeraddinfo)
        self.verticalLayout_7.setContentsMargins(-1, 9, -1, 17)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.registerlabelman = QLabel(self._4customeraddinfo)
        self.registerlabelman.setMinimumSize(QSize(190, 40))
        self.registerlabelman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.registerlabelman.setFont(font)
        self.registerlabelman.setStyleSheet("color: rgb(255, 255, 255);")
        self.registerlabelman.setScaledContents(True)
        self.registerlabelman.setAlignment(Qt.AlignCenter)
        self.registerlabelman.setObjectName("registerlabelman")
        self.verticalLayout_7.addWidget(
            self.registerlabelman, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.name_surnameman = QLineEdit(self._4customeraddinfo)
        self.name_surnameman.setMinimumSize(QSize(190, 40))
        self.name_surnameman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.name_surnameman.setFont(font)
        self.name_surnameman.setStyleSheet("")
        self.name_surnameman.setText("")
        self.name_surnameman.setCursorPosition(0)
        self.name_surnameman.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.name_surnameman.setClearButtonEnabled(False)
        self.name_surnameman.setObjectName("name_surnameman")
        self.verticalLayout_7.addWidget(self.name_surnameman, 0, Qt.AlignHCenter)
        self.telephoneman = QLineEdit(self._4customeraddinfo)
        self.telephoneman.setMinimumSize(QSize(190, 40))
        self.telephoneman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.telephoneman.setFont(font)
        self.telephoneman.setStyleSheet("")
        self.telephoneman.setMaxLength(10)
        self.telephoneman.setClearButtonEnabled(False)
        self.telephoneman.setObjectName("telephoneman")
        self.verticalLayout_7.addWidget(self.telephoneman, 0, Qt.AlignHCenter)
        self.citizenman = QLineEdit(self._4customeraddinfo)
        self.citizenman.setMinimumSize(QSize(190, 40))
        self.citizenman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.citizenman.setFont(font)
        self.citizenman.setStyleSheet("")
        self.citizenman.setMaxLength(11)
        self.citizenman.setClearButtonEnabled(False)
        self.citizenman.setObjectName("citizenman")
        self.verticalLayout_7.addWidget(self.citizenman, 0, Qt.AlignHCenter)
        self.addressman = QLineEdit(self._4customeraddinfo)
        self.addressman.setMinimumSize(QSize(190, 70))
        self.addressman.setMaximumSize(QSize(190, 70))
        font = QFont()
        font.setPointSize(12)
        self.addressman.setFont(font)
        self.addressman.setStyleSheet("")
        self.addressman.setText("")
        self.addressman.setCursorPosition(0)
        self.addressman.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.addressman.setClearButtonEnabled(False)
        self.addressman.setObjectName("addressman")
        self.verticalLayout_7.addWidget(self.addressman, 0, Qt.AlignHCenter)
        self.emailman = QLineEdit(self._4customeraddinfo)
        self.emailman.setMinimumSize(QSize(190, 40))
        self.emailman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.emailman.setFont(font)
        self.emailman.setStyleSheet("")
        self.emailman.setEchoMode(QLineEdit.Normal)
        self.emailman.setObjectName("emailman")
        self.verticalLayout_7.addWidget(self.emailman, 0, Qt.AlignHCenter)
        self.passwordman = QLineEdit(self._4customeraddinfo)
        self.passwordman.setMinimumSize(QSize(190, 40))
        self.passwordman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.passwordman.setFont(font)
        self.passwordman.setStyleSheet("")
        self.passwordman.setMaxLength(6)
        self.passwordman.setEchoMode(QLineEdit.Normal)
        self.passwordman.setObjectName("passwordman")
        self.verticalLayout_7.addWidget(self.passwordman, 0, Qt.AlignHCenter)
        self.confirmpasswordman = QLineEdit(self._4customeraddinfo)
        self.confirmpasswordman.setMinimumSize(QSize(190, 40))
        self.confirmpasswordman.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(12)
        self.confirmpasswordman.setFont(font)
        self.confirmpasswordman.setStyleSheet("")
        self.confirmpasswordman.setMaxLength(6)
        self.confirmpasswordman.setEchoMode(QLineEdit.Normal)
        self.confirmpasswordman.setObjectName("confirmpasswordman")
        self.verticalLayout_7.addWidget(self.confirmpasswordman, 0, Qt.AlignHCenter)
        self.registerbuttonman = QPushButton(self._4customeraddinfo)
        self.registerbuttonman.setMinimumSize(QSize(100, 40))
        self.registerbuttonman.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.registerbuttonman.setFont(font)
        self.registerbuttonman.setStyleSheet(
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
        self.registerbuttonman.setObjectName("registerbuttonman")
        self.verticalLayout_7.addWidget(
            self.registerbuttonman, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.verticalLayout_14.addWidget(
            self._4customeraddinfo, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignHCenter)
        self.mainBody = QWidget(self.allframes)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(0, 600))
        self.mainBody.setMaximumSize(QSize(750, 600))
        self.mainBody.setStyleSheet(
            "#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}"
        )
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout_18 = QVBoxLayout(self.mainBody)
        self.verticalLayout_18.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.headerFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QSize(734, 60))
        self.headerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.headerFrame.setStyleSheet("border-radius:20px;")
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_4.setContentsMargins(8, 2, 8, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.custaddbutton = QPushButton(self.headerFrame)
        self.custaddbutton.setMinimumSize(QSize(50, 50))
        self.custaddbutton.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.custaddbutton.setFont(font)
        self.custaddbutton.setStyleSheet("")
        self.custaddbutton.setText("")
        icon1 = QIcon()
        icon1.addPixmap(
            QPixmap(":/Images/assets/icons/b2.png"),
            QIcon.Normal,
            QIcon.Off,
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
        self.appHeader.setStyleSheet("\n" "color: rgb(50, 249, 251);")
        self.appHeader.setAlignment(Qt.AlignCenter)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_23.addWidget(self.appHeader)
        self.horizontalLayout_4.addWidget(self.maintitle)
        self.profilebutton = QPushButton(self.headerFrame)
        self.profilebutton.setMinimumSize(QSize(50, 50))
        self.profilebutton.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.profilebutton.setFont(font)
        self.profilebutton.setStyleSheet("border-radius:10px;\n" "")
        self.profilebutton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(":/Images/assets/icons/managerprof.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.profilebutton.setIcon(icon2)
        self.profilebutton.setIconSize(QSize(50, 50))
        self.profilebutton.setCheckable(True)
        self.profilebutton.setObjectName("profilebutton")
        self.horizontalLayout_4.addWidget(self.profilebutton, 0, Qt.AlignTop)
        self.verticalLayout_18.addWidget(self.headerFrame, 0, Qt.AlignHCenter)
        self.statusFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusFrame.sizePolicy().hasHeightForWidth())
        self.statusFrame.setSizePolicy(sizePolicy)
        self.statusFrame.setMinimumSize(QSize(734, 0))
        self.statusFrame.setMaximumSize(QSize(16777215, 16777215))
        self.statusFrame.setStyleSheet(
            "QLineEdit{\n"
            "    background-color:  qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "    border:none;\n"
            "    border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "    border-radius:20px;\n"
            "    color:rgba(255, 255, 255, 255);\n"
            "    padding-left:5px;\n"
            "    padding-bottom:7px;\n"
            "}"
        )
        self.statusFrame.setObjectName("statusFrame")
        self.horizontalLayout_26 = QHBoxLayout(self.statusFrame)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.card1 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card1.sizePolicy().hasHeightForWidth())
        self.card1.setSizePolicy(sizePolicy)
        self.card1.setMinimumSize(QSize(160, 0))
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_19 = QVBoxLayout(self.card1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_26 = QFrame(self.card1)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_32 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(6)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_65 = QLabel(self.frame_26)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_32.addWidget(self.label_65)
        self.incomeicon = QPushButton(self.frame_26)
        self.incomeicon.setMinimumSize(QSize(50, 50))
        self.incomeicon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.incomeicon.setFont(font)
        self.incomeicon.setStyleSheet("")
        self.incomeicon.setText("")
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(":/Images/assets/icons/incomdene.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.incomeicon.setIcon(icon3)
        self.incomeicon.setIconSize(QSize(50, 50))
        self.incomeicon.setCheckable(True)
        self.incomeicon.setObjectName("incomeicon")
        self.horizontalLayout_32.addWidget(self.incomeicon)
        self.verticalLayout_19.addWidget(self.frame_26)
        self.incomeclient = QLineEdit(self.card1)
        self.incomeclient.setMinimumSize(QSize(150, 40))
        self.incomeclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.incomeclient.setFont(font)
        self.incomeclient.setStyleSheet("")
        self.incomeclient.setText("")
        self.incomeclient.setCursorPosition(0)
        self.incomeclient.setReadOnly(True)
        self.incomeclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.incomeclient.setClearButtonEnabled(False)
        self.incomeclient.setObjectName("incomeclient")
        self.verticalLayout_19.addWidget(self.incomeclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card1, 0, Qt.AlignHCenter)
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
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_27 = QFrame(self.card2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_36 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_54 = QLabel(self.frame_27)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_36.addWidget(self.label_54)
        self.expenseicon = QPushButton(self.frame_27)
        self.expenseicon.setMinimumSize(QSize(50, 50))
        self.expenseicon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.expenseicon.setFont(font)
        self.expenseicon.setStyleSheet("border-radius:10px;\n" "")
        self.expenseicon.setText("")
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(":/Images/assets/icons/expense.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.expenseicon.setIcon(icon4)
        self.expenseicon.setIconSize(QSize(50, 50))
        self.expenseicon.setCheckable(True)
        self.expenseicon.setObjectName("expenseicon")
        self.horizontalLayout_36.addWidget(self.expenseicon)
        self.verticalLayout_20.addWidget(self.frame_27)
        self.expenseclient = QLineEdit(self.card2)
        self.expenseclient.setMinimumSize(QSize(150, 40))
        self.expenseclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.expenseclient.setFont(font)
        self.expenseclient.setStyleSheet("")
        self.expenseclient.setText("")
        self.expenseclient.setCursorPosition(0)
        self.expenseclient.setReadOnly(True)
        self.expenseclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.expenseclient.setClearButtonEnabled(False)
        self.expenseclient.setObjectName("expenseclient")
        self.verticalLayout_20.addWidget(self.expenseclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card2)
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
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_28 = QFrame(self.card3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_37 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setSpacing(6)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_67 = QLabel(self.frame_28)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_37.addWidget(self.label_67)
        self.profiticon = QPushButton(self.frame_28)
        self.profiticon.setMinimumSize(QSize(50, 50))
        self.profiticon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.profiticon.setFont(font)
        self.profiticon.setStyleSheet("border-radius:10px;\n" "")
        self.profiticon.setText("")
        icon5 = QIcon()
        icon5.addPixmap(
            QPixmap(":/Images/assets/icons/profit.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.profiticon.setIcon(icon5)
        self.profiticon.setIconSize(QSize(50, 50))
        self.profiticon.setCheckable(True)
        self.profiticon.setObjectName("profiticon")
        self.horizontalLayout_37.addWidget(self.profiticon)
        self.verticalLayout_21.addWidget(self.frame_28)
        self.profitclient = QLineEdit(self.card3)
        self.profitclient.setMinimumSize(QSize(150, 40))
        self.profitclient.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(17)
        self.profitclient.setFont(font)
        self.profitclient.setStyleSheet("")
        self.profitclient.setText("")
        self.profitclient.setCursorPosition(0)
        self.profitclient.setReadOnly(True)
        self.profitclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.profitclient.setClearButtonEnabled(False)
        self.profitclient.setObjectName("profitclient")
        self.verticalLayout_21.addWidget(self.profitclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card3)
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
        self.balanceicon.setMinimumSize(QSize(50, 50))
        self.balanceicon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.balanceicon.setFont(font)
        self.balanceicon.setStyleSheet("border-radius:10px;\n" "")
        self.balanceicon.setText("")
        icon6 = QIcon()
        icon6.addPixmap(
            QPixmap(":/Images/assets/icons/total.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.balanceicon.setIcon(icon6)
        self.balanceicon.setIconSize(QSize(50, 50))
        self.balanceicon.setCheckable(True)
        self.balanceicon.setObjectName("balanceicon")
        self.horizontalLayout_30.addWidget(self.balanceicon)
        self.verticalLayout_22.addWidget(self.frame_22)
        self.totalclient = QLineEdit(self.card4)
        self.totalclient.setMinimumSize(QSize(190, 40))
        self.totalclient.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(17)
        self.totalclient.setFont(font)
        self.totalclient.setStyleSheet("")
        self.totalclient.setText("")
        self.totalclient.setCursorPosition(0)
        self.totalclient.setReadOnly(True)
        self.totalclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.totalclient.setClearButtonEnabled(False)
        self.totalclient.setObjectName("totalclient")
        self.verticalLayout_22.addWidget(self.totalclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card4)
        self.verticalLayout_18.addWidget(
            self.statusFrame, 0, Qt.AlignHCenter | Qt.AlignTop
        )
        self.salaryCreditsFrame = QFrame(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.salaryCreditsFrame.sizePolicy().hasHeightForWidth()
        )
        self.salaryCreditsFrame.setSizePolicy(sizePolicy)
        self.salaryCreditsFrame.setMinimumSize(QSize(600, 240))
        self.salaryCreditsFrame.setMaximumSize(QSize(16777215, 16777215))
        self.salaryCreditsFrame.setFrameShape(QFrame.StyledPanel)
        self.salaryCreditsFrame.setFrameShadow(QFrame.Raised)
        self.salaryCreditsFrame.setObjectName("salaryCreditsFrame")
        self.gridLayout_12 = QGridLayout(self.salaryCreditsFrame)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 2)
        self.gridLayout_12.setHorizontalSpacing(17)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.cresalFrame = QFrame(self.salaryCreditsFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cresalFrame.sizePolicy().hasHeightForWidth())
        self.cresalFrame.setSizePolicy(sizePolicy)
        self.cresalFrame.setMinimumSize(QSize(320, 200))
        self.cresalFrame.setMaximumSize(QSize(320, 200))
        self.cresalFrame.setStyleSheet(
            "#cresalFrame{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(17, 252, 253, 219));\n"
            "    border-radius:20px;\n"
            "    border: 2px solid rgb(37, 150, 190);\n"
            "}\n"
            ""
        )
        self.cresalFrame.setFrameShape(QFrame.StyledPanel)
        self.cresalFrame.setFrameShadow(QFrame.Raised)
        self.cresalFrame.setObjectName("cresalFrame")
        self.gridLayout_13 = QGridLayout(self.cresalFrame)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.salaryCreditsTitle = QFrame(self.cresalFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.salaryCreditsTitle.sizePolicy().hasHeightForWidth()
        )
        self.salaryCreditsTitle.setSizePolicy(sizePolicy)
        self.salaryCreditsTitle.setMinimumSize(QSize(245, 45))
        self.salaryCreditsTitle.setMaximumSize(QSize(16777215, 16777215))
        self.salaryCreditsTitle.setFrameShape(QFrame.StyledPanel)
        self.salaryCreditsTitle.setFrameShadow(QFrame.Raised)
        self.salaryCreditsTitle.setObjectName("salaryCreditsTitle")
        self.horizontalLayout_16 = QHBoxLayout(self.salaryCreditsTitle)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(9)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.creditsicon = QPushButton(self.salaryCreditsTitle)
        self.creditsicon.setMinimumSize(QSize(40, 40))
        self.creditsicon.setMaximumSize(QSize(40, 40))
        self.creditsicon.setStyleSheet("border-radius:10px;\n" "")
        self.creditsicon.setText("")
        icon7 = QIcon()
        icon7.addPixmap(
            QPixmap(":/Images/assets/icons/statements_2.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.creditsicon.setIcon(icon7)
        self.creditsicon.setIconSize(QSize(40, 40))
        self.creditsicon.setObjectName("creditsicon")
        self.horizontalLayout_16.addWidget(self.creditsicon, 0, Qt.AlignHCenter)
        self.titleofsclabel = QLabel(self.salaryCreditsTitle)
        self.titleofsclabel.setMinimumSize(QSize(205, 30))
        self.titleofsclabel.setMaximumSize(QSize(205, 30))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.titleofsclabel.setFont(font)
        self.titleofsclabel.setStyleSheet("\n" "color: rgb(255, 255, 255);")
        self.titleofsclabel.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.titleofsclabel.setObjectName("titleofsclabel")
        self.horizontalLayout_16.addWidget(self.titleofsclabel)
        self.gridLayout_13.addWidget(
            self.salaryCreditsTitle,
            0,
            1,
            1,
            1,
            Qt.AlignHCenter | Qt.AlignTop,
        )
        self.editing = QFrame(self.cresalFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editing.sizePolicy().hasHeightForWidth())
        self.editing.setSizePolicy(sizePolicy)
        self.editing.setStyleSheet(
            "QLineEdit{\n"
            "    background-color:  qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "    border:none;\n"
            "    border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "    border-radius:20px;\n"
            "    color:rgba(255, 255, 255, 255);\n"
            "    padding-left:5px;\n"
            "    padding-bottom:7px;\n"
            "}"
        )
        self.editing.setFrameShape(QFrame.StyledPanel)
        self.editing.setFrameShadow(QFrame.Raised)
        self.editing.setObjectName("editing")
        self.gridLayout_14 = QGridLayout(self.editing)
        self.gridLayout_14.setContentsMargins(8, 2, 8, 0)
        self.gridLayout_14.setHorizontalSpacing(6)
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_2 = QLabel(self.editing)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_14.addWidget(self.label_2, 4, 0, 1, 1)
        self.label = QLabel(self.editing)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_14.addWidget(self.label, 0, 0, 1, 1)
        self.salaryedit = QLineEdit(self.editing)
        self.salaryedit.setMinimumSize(QSize(100, 40))
        self.salaryedit.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(12)
        self.salaryedit.setFont(font)
        self.salaryedit.setToolTip("")
        self.salaryedit.setStyleSheet("")
        self.salaryedit.setMaxLength(11)
        self.salaryedit.setClearButtonEnabled(False)
        self.salaryedit.setObjectName("salaryedit")
        self.gridLayout_14.addWidget(self.salaryedit, 4, 1, 1, 1)
        self.creditedit = QLineEdit(self.editing)
        self.creditedit.setMinimumSize(QSize(100, 40))
        self.creditedit.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(12)
        self.creditedit.setFont(font)
        self.creditedit.setToolTip("")
        self.creditedit.setStyleSheet("")
        self.creditedit.setMaxLength(5)
        self.creditedit.setClearButtonEnabled(False)
        self.creditedit.setObjectName("creditedit")
        self.gridLayout_14.addWidget(self.creditedit, 0, 1, 1, 1)
        self.label_3 = QLabel(self.editing)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_14.addWidget(self.label_3, 1, 0, 1, 1)
        self.overdueedit = QLineEdit(self.editing)
        self.overdueedit.setMinimumSize(QSize(100, 40))
        self.overdueedit.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(12)
        self.overdueedit.setFont(font)
        self.overdueedit.setToolTip("")
        self.overdueedit.setStyleSheet("")
        self.overdueedit.setMaxLength(5)
        self.overdueedit.setClearButtonEnabled(False)
        self.overdueedit.setObjectName("overdueedit")
        self.gridLayout_14.addWidget(self.overdueedit, 1, 1, 1, 1)
        self.savestatiko = QPushButton(self.editing)
        self.savestatiko.setMinimumSize(QSize(100, 40))
        self.savestatiko.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.savestatiko.setFont(font)
        self.savestatiko.setStyleSheet(
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
        self.savestatiko.setObjectName("savestatiko")
        self.gridLayout_14.addWidget(self.savestatiko, 1, 3, 1, 1)
        self.gridLayout_13.addWidget(self.editing, 1, 1, 1, 1)
        self.gridLayout_12.addWidget(self.cresalFrame, 0, 0, 1, 1, Qt.AlignHCenter)
        self.currencyFrame = QFrame(self.salaryCreditsFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.currencyFrame.sizePolicy().hasHeightForWidth()
        )
        self.currencyFrame.setSizePolicy(sizePolicy)
        self.currencyFrame.setMinimumSize(QSize(360, 200))
        self.currencyFrame.setMaximumSize(QSize(360, 200))
        self.currencyFrame.setStyleSheet(
            "#currencyFrame{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(17, 252, 253, 219));\n"
            "    border-radius:20px;\n"
            "    border: 2px solid rgb(37, 150, 190);\n"
            "\n"
            "}\n"
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
        self.currencyFrame.setFrameShape(QFrame.StyledPanel)
        self.currencyFrame.setFrameShadow(QFrame.Raised)
        self.currencyFrame.setObjectName("currencyFrame")
        self.gridLayout_3 = QGridLayout(self.currencyFrame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.currencyTitle = QFrame(self.currencyFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.currencyTitle.sizePolicy().hasHeightForWidth()
        )
        self.currencyTitle.setSizePolicy(sizePolicy)
        self.currencyTitle.setMinimumSize(QSize(245, 50))
        self.currencyTitle.setMaximumSize(QSize(16777215, 16777215))
        self.currencyTitle.setFrameShape(QFrame.StyledPanel)
        self.currencyTitle.setFrameShadow(QFrame.Raised)
        self.currencyTitle.setObjectName("currencyTitle")
        self.horizontalLayout_12 = QHBoxLayout(self.currencyTitle)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.currencyicon = QPushButton(self.currencyTitle)
        self.currencyicon.setMinimumSize(QSize(55, 55))
        self.currencyicon.setMaximumSize(QSize(55, 55))
        self.currencyicon.setStyleSheet(
            "border-radius:10px;\n" "background-color:transparent;"
        )
        self.currencyicon.setText("")
        icon8 = QIcon()
        icon8.addPixmap(
            QPixmap(":/Images/assets/icons/credit.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.currencyicon.setIcon(icon8)
        self.currencyicon.setIconSize(QSize(50, 50))
        self.currencyicon.setObjectName("currencyicon")
        self.horizontalLayout_12.addWidget(self.currencyicon, 0, Qt.AlignHCenter)
        self.titleofsclabel_2 = QLabel(self.currencyTitle)
        self.titleofsclabel_2.setMinimumSize(QSize(95, 30))
        self.titleofsclabel_2.setMaximumSize(QSize(95, 30))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.titleofsclabel_2.setFont(font)
        self.titleofsclabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleofsclabel_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.titleofsclabel_2.setObjectName("titleofsclabel_2")
        self.horizontalLayout_12.addWidget(self.titleofsclabel_2)
        self.frame = QFrame(self.currencyTitle)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.currencies = QComboBox(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currencies.sizePolicy().hasHeightForWidth())
        self.currencies.setSizePolicy(sizePolicy)
        self.currencies.setMinimumSize(QSize(150, 40))
        self.currencies.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(14)
        self.currencies.setFont(font)
        self.currencies.setStyleSheet(
            "#currencies{\n"
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(255, 255, 255, 255);\n"
            "border-radius:20px;\n"
            "padding-left:5px;\n"
            "padding-bottom:7px;}\n"
            "QAbstractItemView {\n"
            "border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "padding: 5 5 16 5;\n"
            "border-radius:5px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "color: #ffffff;\n"
            "font-size: 13px;\n"
            "}\n"
            "\n"
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
            "\n"
            "QScrollBar::handle:vertical {\n"
            "border-radius: 5px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
            "    min-width:10px;\n"
            "    max-width:10px;\n"
            "    min-height:10px;\n"
            "    max-height:10px;\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "height: 0px;\n"
            "subcontrol-position: bottom;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "height: 0px;\n"
            "subcontrol-position: top;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "background:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "}\n"
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
        self.currencies.setInsertPolicy(QComboBox.InsertAtBottom)
        self.currencies.setIconSize(QSize(40, 40))
        self.currencies.setPlaceholderText("")
        self.currencies.setObjectName("currencies")
        self.horizontalLayout_5.addWidget(self.currencies)
        self.horizontalLayout_12.addWidget(self.frame)
        self.gridLayout_3.addWidget(
            self.currencyTitle, 0, 1, 1, 1, Qt.AlignHCenter | Qt.AlignTop
        )
        self.editing_2 = QFrame(self.currencyFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editing_2.sizePolicy().hasHeightForWidth())
        self.editing_2.setSizePolicy(sizePolicy)
        self.editing_2.setStyleSheet("")
        self.editing_2.setFrameShape(QFrame.StyledPanel)
        self.editing_2.setFrameShadow(QFrame.Raised)
        self.editing_2.setObjectName("editing_2")
        self.gridLayout_4 = QGridLayout(self.editing_2)
        self.gridLayout_4.setContentsMargins(2, 11, 4, 27)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.currenciestable = QTableWidget(self.editing_2)
        self.currenciestable.setMinimumSize(QSize(237, 125))
        self.currenciestable.setMaximumSize(QSize(237, 125))
        font = QFont()
        font.setPointSize(10)
        self.currenciestable.setFont(font)
        self.currenciestable.setStyleSheet(
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
        self.currenciestable.setFrameShadow(QFrame.Sunken)
        self.currenciestable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.currenciestable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.currenciestable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.currenciestable.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.currenciestable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.currenciestable.setTextElideMode(Qt.ElideLeft)
        self.currenciestable.setGridStyle(Qt.CustomDashLine)
        self.currenciestable.setWordWrap(True)
        self.currenciestable.setCornerButtonEnabled(False)
        self.currenciestable.setRowCount(10)
        self.currenciestable.setColumnCount(2)
        self.currenciestable.setObjectName("currenciestable")
        item = QTableWidgetItem()
        self.currenciestable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.currenciestable.setHorizontalHeaderItem(1, item)
        self.currenciestable.horizontalHeader().setDefaultSectionSize(96)
        self.currenciestable.horizontalHeader().setMinimumSectionSize(96)
        self.currenciestable.verticalHeader().setDefaultSectionSize(30)
        self.currenciestable.verticalHeader().setHighlightSections(True)
        self.currenciestable.verticalHeader().setMinimumSectionSize(30)
        self.currenciestable.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_4.addWidget(self.currenciestable, 1, 3, 1, 1)
        self.savecurrency = QPushButton(self.editing_2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savecurrency.sizePolicy().hasHeightForWidth())
        self.savecurrency.setSizePolicy(sizePolicy)
        self.savecurrency.setMinimumSize(QSize(90, 40))
        self.savecurrency.setMaximumSize(QSize(90, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.savecurrency.setFont(font)
        self.savecurrency.setStyleSheet(
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
        self.savecurrency.setObjectName("savecurrency")
        self.gridLayout_4.addWidget(self.savecurrency, 2, 4, 1, 1)
        self.addcurrency = QPushButton(self.editing_2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addcurrency.sizePolicy().hasHeightForWidth())
        self.addcurrency.setSizePolicy(sizePolicy)
        self.addcurrency.setMinimumSize(QSize(90, 40))
        self.addcurrency.setMaximumSize(QSize(90, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addcurrency.setFont(font)
        self.addcurrency.setStyleSheet(
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
        self.addcurrency.setObjectName("addcurrency")
        self.gridLayout_4.addWidget(self.addcurrency, 1, 4, 1, 1)
        self.gridLayout_3.addWidget(self.editing_2, 1, 1, 1, 1)
        self.gridLayout_12.addWidget(
            self.currencyFrame,
            0,
            1,
            1,
            1,
            Qt.AlignHCenter | Qt.AlignVCenter,
        )
        self.verticalLayout_18.addWidget(self.salaryCreditsFrame, 0, Qt.AlignHCenter)
        self.mainFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QSize(734, 30))
        self.mainFrame.setMaximumSize(QSize(16777215, 230))
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
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
            "    background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(17, 252, 253, 219));\n"
            "    border-radius:20px;\n"
            "    border: 2px solid rgb(37, 150, 190);\n"
            "\n"
            "}\n"
            ""
        )
        self.monthlystatements.setObjectName("monthlystatements")
        self.verticalLayout_6 = QVBoxLayout(self.monthlystatements)
        self.verticalLayout_6.setContentsMargins(2, 3, 0, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_25 = QFrame(self.monthlystatements)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QSize(0, 40))
        self.frame_25.setMaximumSize(QSize(16777215, 16777215))
        self.frame_25.setStyleSheet(
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
            "}\n"
            ""
        )
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_35 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_35.setContentsMargins(2, 0, 6, 0)
        self.horizontalLayout_35.setSpacing(9)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        spacerItem = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem)
        self.statementicon = QPushButton(self.frame_25)
        self.statementicon.setMinimumSize(QSize(40, 40))
        self.statementicon.setMaximumSize(QSize(40, 40))
        self.statementicon.setStyleSheet("border-radius:10px;\n" "")
        self.statementicon.setText("")
        icon9 = QIcon()
        icon9.addPixmap(
            QPixmap(":/Images/assets/icons/statements.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.statementicon.setIcon(icon9)
        self.statementicon.setIconSize(QSize(50, 40))
        self.statementicon.setObjectName("statementicon")
        self.horizontalLayout_35.addWidget(self.statementicon)
        self.label_78 = QLabel(self.frame_25)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setMinimumSize(QSize(300, 40))
        self.label_78.setMaximumSize(QSize(300, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_78.setObjectName("label_78")
        self.horizontalLayout_35.addWidget(self.label_78)
        self.searchFrame = QFrame(self.frame_25)
        self.searchFrame.setMinimumSize(QSize(120, 40))
        self.searchFrame.setMaximumSize(QSize(120, 40))
        self.searchFrame.setStyleSheet("#searchline{border-radius:20px;}")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_3 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 114, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchline = QLineEdit(self.searchFrame)
        self.searchline.setMinimumSize(QSize(120, 40))
        self.searchline.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setPointSize(12)
        self.searchline.setFont(font)
        self.searchline.setStyleSheet(
            "QLineEdit{\n"
            "    background-color:  qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "    border:none;\n"
            "    border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "    border-radius:20px;\n"
            "    color:rgba(255, 255, 255, 255);\n"
            "    padding-left:5px;\n"
            "    padding-bottom:7px;\n"
            "}"
        )
        self.searchline.setMaxLength(8)
        self.searchline.setEchoMode(QLineEdit.Normal)
        self.searchline.setAlignment(Qt.AlignCenter)
        self.searchline.setObjectName("searchline")
        self.horizontalLayout_3.addWidget(
            self.searchline, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.searchicon = QPushButton(self.searchFrame)
        self.searchicon.setMinimumSize(QSize(25, 25))
        self.searchicon.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.searchicon.setFont(font)
        self.searchicon.setStyleSheet(
            "#showpasslog{background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "color:rgba(255, 255, 255, 240);\n"
            "padding-bottom:7px;}"
        )
        self.searchicon.setText("")
        icon10 = QIcon()
        icon10.addPixmap(
            QPixmap(":/Images/assets/icons/search.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.searchicon.setIcon(icon10)
        self.searchicon.setIconSize(QSize(25, 25))
        self.searchicon.setCheckable(True)
        self.searchicon.setObjectName("searchicon")
        self.horizontalLayout_3.addWidget(self.searchicon, 0, Qt.AlignVCenter)
        self.horizontalLayout_35.addWidget(self.searchFrame)
        self.addmorestate = QPushButton(self.frame_25)
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
        self.addmorestate.setObjectName("addmorestate")
        self.horizontalLayout_35.addWidget(self.addmorestate)
        spacerItem1 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.frame_25)
        self.frame_5 = QFrame(self.monthlystatements)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.statementtable = QTableWidget(self.frame_5)
        self.statementtable.setMinimumSize(QSize(717, 125))
        self.statementtable.setMaximumSize(QSize(717, 125))
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
        self.statementtable.setTabKeyNavigation(False)
        self.statementtable.setProperty("showDropIndicator", False)
        self.statementtable.setDragDropOverwriteMode(False)
        self.statementtable.setSelectionMode(QAbstractItemView.MultiSelection)
        self.statementtable.setTextElideMode(Qt.ElideMiddle)
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
        self.horizontalLayout_10.addWidget(self.statementtable)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.monthlystatements)
        self.verticalLayout_18.addWidget(self.mainFrame, 0, Qt.AlignHCenter)
        self.salaryCreditsFrame.raise_()
        self.headerFrame.raise_()
        self.mainFrame.raise_()
        self.statusFrame.raise_()
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
            "#rightMenu{        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(17, 252, 253, 219), stop:1 rgba(227, 76, 219, 226));border-top-right-radius:20px;border-bottom-right-radius:20px;}"
        )
        self.rightMenu.setObjectName("rightMenu")
        self.verticalLayout_27 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_27.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.profileframe = QFrame(self.rightMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileframe.sizePolicy().hasHeightForWidth())
        self.profileframe.setSizePolicy(sizePolicy)
        self.profileframe.setMinimumSize(QSize(210, 563))
        self.profileframe.setMaximumSize(QSize(210, 563))
        self.profileframe.setFrameShape(QFrame.StyledPanel)
        self.profileframe.setFrameShadow(QFrame.Raised)
        self.profileframe.setObjectName("profileframe")
        self.verticalLayout_28 = QVBoxLayout(self.profileframe)
        self.verticalLayout_28.setContentsMargins(1, 8, 1, -1)
        self.verticalLayout_28.setSpacing(13)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.username = QLineEdit(self.profileframe)
        self.username.setMinimumSize(QSize(180, 40))
        self.username.setMaximumSize(QSize(180, 40))
        font = QFont()
        font.setPointSize(19)
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
            ""
        )
        self.username.setCursorPosition(11)
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setReadOnly(True)
        self.username.setPlaceholderText("")
        self.username.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.verticalLayout_28.addWidget(
            self.username, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.coolguy = QPushButton(self.profileframe)
        self.coolguy.setMinimumSize(QSize(150, 300))
        self.coolguy.setMaximumSize(QSize(150, 300))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.coolguy.setFont(font)
        self.coolguy.setStyleSheet("border-radius:10px;\n" "")
        self.coolguy.setText("")
        icon11 = QIcon()
        icon11.addPixmap(
            QPixmap(":/Images/assets/icons/manager.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.coolguy.setIcon(icon11)
        self.coolguy.setIconSize(QSize(150, 300))
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
        icon12 = QIcon()
        icon12.addPixmap(
            QPixmap(":/Images/assets/icons/1053210.png"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.logout.setIcon(icon12)
        self.logout.setIconSize(QSize(24, 24))
        self.logout.setObjectName("logout")
        self.verticalLayout_28.addWidget(self.logout)
        self.advanceSystem = QPushButton(self.profileframe)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.advanceSystem.sizePolicy().hasHeightForWidth()
        )
        self.advanceSystem.setSizePolicy(sizePolicy)
        self.advanceSystem.setMinimumSize(QSize(150, 50))
        self.advanceSystem.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.advanceSystem.setFont(font)
        self.advanceSystem.setStyleSheet(
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
        self.advanceSystem.setObjectName("advanceSystem")
        self.verticalLayout_28.addWidget(self.advanceSystem, 0, Qt.AlignHCenter)
        self.deadlockcontrol = QPushButton(self.profileframe)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deadlockcontrol.sizePolicy().hasHeightForWidth()
        )
        self.deadlockcontrol.setSizePolicy(sizePolicy)
        self.deadlockcontrol.setMinimumSize(QSize(80, 80))
        self.deadlockcontrol.setMaximumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.deadlockcontrol.setFont(font)
        self.deadlockcontrol.setStyleSheet(
            "QPushButton{\n"
            "    background-color:transparent;\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:50px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color:  qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
            "    border-radius:40px;\n"
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
        self.deadlockcontrol.setText("")
        self.deadlockcontrol.setIcon(icon)
        self.deadlockcontrol.setIconSize(QSize(80, 80))
        self.deadlockcontrol.setObjectName("deadlockcontrol")
        self.verticalLayout_28.addWidget(self.deadlockcontrol, 0, Qt.AlignHCenter)
        self.verticalLayout_27.addWidget(
            self.profileframe, 0, Qt.AlignHCenter | Qt.AlignTop
        )
        self.horizontalLayout.addWidget(self.rightMenu, 0, Qt.AlignHCenter)
        Manager.setCentralWidget(self.centralwidget)

        self.retranslateUi(Manager)
        self.currencies.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        _translate = QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "SeaBank"))
        self.registerlabelman.setText(_translate("Manager", "Information"))
        self.name_surnameman.setPlaceholderText(
            _translate("Manager", "  First and Last Name")
        )
        self.telephoneman.setToolTip(
            _translate(
                "Manager",
                "<html><head/><body><p>Başında Sıfır olmadan giriniz.</p></body></html>",
            )
        )
        self.telephoneman.setPlaceholderText(_translate("Manager", "  Telephone No"))
        self.citizenman.setPlaceholderText(_translate("Manager", "  Citizenship No"))
        self.addressman.setPlaceholderText(_translate("Manager", " Address"))
        self.emailman.setPlaceholderText(_translate("Manager", "  E-mail Address"))
        self.passwordman.setToolTip(
            _translate(
                "Manager",
                "<html><head/><body><p>6 haneli sayı giriniz.</p></body></html>",
            )
        )
        self.passwordman.setPlaceholderText(_translate("Manager", "  Password"))
        self.confirmpasswordman.setPlaceholderText(
            _translate("Manager", "  Confirm Password")
        )
        self.registerbuttonman.setText(_translate("Manager", "Add"))
        self.appHeader.setText(_translate("Manager", "Welcome to SeaBank"))
        self.label_65.setText(_translate("Manager", "Income"))
        self.incomeclient.setPlaceholderText(_translate("Manager", "    Income"))
        self.label_54.setText(_translate("Manager", "Expense"))
        self.expenseclient.setPlaceholderText(_translate("Manager", "    Expense"))
        self.label_67.setText(_translate("Manager", "Profit"))
        self.profitclient.setPlaceholderText(_translate("Manager", "    Profit   "))
        self.label_60.setText(_translate("Manager", "Total Balance"))
        self.totalclient.setPlaceholderText(_translate("Manager", "    Total Balance"))
        self.titleofsclabel.setText(_translate("Manager", "Salary|Credit rates"))
        self.label_2.setText(_translate("Manager", "Salary:"))
        self.label.setText(_translate("Manager", "Interest:"))
        self.salaryedit.setPlaceholderText(_translate("Manager", "  Salary"))
        self.creditedit.setPlaceholderText(_translate("Manager", "  Interest"))
        self.label_3.setText(_translate("Manager", "Late:"))
        self.overdueedit.setPlaceholderText(_translate("Manager", "  Late "))
        self.savestatiko.setText(_translate("Manager", "Save"))
        self.titleofsclabel_2.setText(_translate("Manager", "Currency"))
        self.currenciestable.setSortingEnabled(False)
        item = self.currenciestable.horizontalHeaderItem(0)
        item.setText(_translate("Manager", "Currency"))
        item = self.currenciestable.horizontalHeaderItem(1)
        item.setText(_translate("Manager", "Worth"))
        self.savecurrency.setText(_translate("Manager", "Save"))
        self.addcurrency.setText(_translate("Manager", "Add"))
        self.label_78.setText(_translate("Manager", "Clients Monthly Statements"))
        self.searchline.setPlaceholderText(_translate("Manager", "Search"))
        self.addmorestate.setText(_translate("Manager", "Add More"))
        self.statementtable.setSortingEnabled(False)
        item = self.statementtable.horizontalHeaderItem(0)
        item.setText(_translate("Manager", "Source No"))
        item = self.statementtable.horizontalHeaderItem(1)
        item.setText(_translate("Manager", "Target No"))
        item = self.statementtable.horizontalHeaderItem(2)
        item.setText(_translate("Manager", "Procedure"))
        item = self.statementtable.horizontalHeaderItem(3)
        item.setText(_translate("Manager", "Balance"))
        item = self.statementtable.horizontalHeaderItem(4)
        item.setText(_translate("Manager", "S_Balance"))
        item = self.statementtable.horizontalHeaderItem(5)
        item.setText(_translate("Manager", "T_Balance"))
        item = self.statementtable.horizontalHeaderItem(6)
        item.setText(_translate("Manager", "Date"))
        self.username.setText(_translate("Manager", "Deniz Özcan"))
        self.logout.setText(_translate("Manager", "Log Out"))
        self.advanceSystem.setText(_translate("Manager", "Advance System"))


import res_rc_rc
