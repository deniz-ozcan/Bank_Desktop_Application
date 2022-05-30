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
    QDateEdit,
    QAbstractSpinBox,
    QDateTimeEdit,
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

class Ui_Customer(object):
    def setupUi(self, Customer):
        Customer.setObjectName("Customer")
        Customer.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Customer.sizePolicy().hasHeightForWidth())
        Customer.setSizePolicy(sizePolicy)
        Customer.setMinimumSize(QSize(0, 0))
        Customer.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/Images/assets/icons/mainico.png"), QIcon.Normal, QIcon.Off)
        Customer.setWindowIcon(icon)
        self.centralwidget = QWidget(Customer)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet("*{\n"
"    color:#000;\n"
"    border:none;\n"
"}\n"
"#appHeader{\n"
"    color:rgb(37, 150, 190);\n"
"}\n"
"#card1,#card2,#card3,#card4{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
"    border-radius:20px;\n"
"}\n"
"#homeBtn{\n"
"    background-color: rgb(254, 254, 255);\n"
"    padding:10px 5px;\n"
"    border-top-left-radius:20px;\n"
"    text-align:left;\n"
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
"")
        self.centralwidget.setObjectName("centralwidget")
        self.allframes = QWidget(self.centralwidget)
        self.allframes.setGeometry(QRect(100, 50, 1180, 600))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allframes.sizePolicy().hasHeightForWidth())
        self.allframes.setSizePolicy(sizePolicy)
        self.allframes.setMinimumSize(QSize(1180, 600))
        self.allframes.setMaximumSize(QSize(1180, 600))
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
        self.leftMenu.setStyleSheet("#leftMenu{background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));border-top-left-radius:20px;border-bottom-left-radius:20px;}\n"
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
"}\n"
"QLineEdit,QTextEdit{\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"#traaccotype{\n"
"    border-radius:20px;\n"
"}")
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_11 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QFrame(self.leftMenu)
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_56 = QLabel(self.frame)
        self.label_56.setMinimumSize(QSize(129, 0))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_3.addWidget(self.label_56)
        self.transacicon = QPushButton(self.frame)
        self.transacicon.setMinimumSize(QSize(50, 50))
        self.transacicon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.transacicon.setFont(font)
        self.transacicon.setStyleSheet("background:transparent;")
        self.transacicon.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/Images/assets/icons/brandico.png"), QIcon.Normal, QIcon.Off)
        self.transacicon.setIcon(icon1)
        self.transacicon.setIconSize(QSize(50, 50))
        self.transacicon.setCheckable(True)
        self.transacicon.setObjectName("transacicon")
        self.horizontalLayout_3.addWidget(self.transacicon)
        self.verticalLayout_11.addWidget(self.frame)
        self.transfertitle = QFrame(self.leftMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transfertitle.sizePolicy().hasHeightForWidth())
        self.transfertitle.setSizePolicy(sizePolicy)
        self.transfertitle.setMinimumSize(QSize(210, 100))
        self.transfertitle.setMaximumSize(QSize(16777215, 100))
        self.transfertitle.setStyleSheet("#transfertitle{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"    border-radius:20px;\n"
"    border: 2px solid rgb(37, 150, 190);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:  qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
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
"}\n"
"\n"
"#transfertype{\n"
"    border-radius:20px;\n"
"}\n"
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
"}")
        self.transfertitle.setFrameShape(QFrame.StyledPanel)
        self.transfertitle.setFrameShadow(QFrame.Raised)
        self.transfertitle.setObjectName("transfertitle")
        self.verticalLayout_6 = QVBoxLayout(self.transfertitle)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.transfertype = QComboBox(self.transfertitle)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transfertype.sizePolicy().hasHeightForWidth())
        self.transfertype.setSizePolicy(sizePolicy)
        self.transfertype.setMinimumSize(QSize(160, 50))
        self.transfertype.setMaximumSize(QSize(160, 50))
        font = QFont()
        font.setPointSize(14)
        self.transfertype.setFont(font)
        self.transfertype.setLayoutDirection(Qt.LeftToRight)
        self.transfertype.setStyleSheet("#transfertype{\n"
"background-color:transparent;\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:15px;\n"
"\n"
"}\n"
"\n"
"")
        self.transfertype.setMaxVisibleItems(10)
        self.transfertype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.transfertype.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.transfertype.setIconSize(QSize(40, 40))
        self.transfertype.setPlaceholderText("")
        self.transfertype.setObjectName("transfertype")
        self.transfertype.addItem("")
        self.transfertype.addItem("")
        self.transfertype.addItem("")
        self.transfertype.addItem("")
        self.transfertype.addItem("")
        self.transfertype.addItem("")
        self.transfertype.addItem("")
        self.verticalLayout_6.addWidget(self.transfertype, 0, Qt.AlignHCenter)
        self.transbutton = QPushButton(self.transfertitle)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transbutton.sizePolicy().hasHeightForWidth())
        self.transbutton.setSizePolicy(sizePolicy)
        self.transbutton.setMinimumSize(QSize(70, 40))
        self.transbutton.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.transbutton.setFont(font)
        self.transbutton.setStyleSheet("color:rgb(255, 255, 255);")
        self.transbutton.setObjectName("transbutton")
        self.verticalLayout_6.addWidget(self.transbutton, 0, Qt.AlignHCenter)
        self.verticalLayout_11.addWidget(self.transfertitle)
        self.alltransactions = QFrame(self.leftMenu)
        self.alltransactions.setMinimumSize(QSize(0, 440))
        self.alltransactions.setMaximumSize(QSize(0, 440))
        self.alltransactions.setFrameShape(QFrame.StyledPanel)
        self.alltransactions.setFrameShadow(QFrame.Raised)
        self.alltransactions.setObjectName("alltransactions")
        self.credit = QWidget(self.alltransactions)
        self.credit.setGeometry(QRect(0, 40, 210, 280))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credit.sizePolicy().hasHeightForWidth())
        self.credit.setSizePolicy(sizePolicy)
        self.credit.setMinimumSize(QSize(210, 280))
        self.credit.setMaximumSize(QSize(210, 280))
        self.credit.setStyleSheet("#credit{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
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
"}\n"
"#paymenttype{\n"
"    border-radius:20px;\n"
"}\n"
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
"}\n"
"\n"
"#creditaccotype{\n"
"    border-radius:20px;\n"
"}")
        self.credit.setObjectName("credit")
        self.verticalLayout_9 = QVBoxLayout(self.credit)
        self.verticalLayout_9.setContentsMargins(13, 9, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.creditlabel = QLabel(self.credit)
        self.creditlabel.setMinimumSize(QSize(190, 40))
        self.creditlabel.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.creditlabel.setFont(font)
        self.creditlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.creditlabel.setScaledContents(True)
        self.creditlabel.setAlignment(Qt.AlignCenter)
        self.creditlabel.setObjectName("creditlabel")
        self.verticalLayout_9.addWidget(self.creditlabel)
        self.creditaccotype = QComboBox(self.credit)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creditaccotype.sizePolicy().hasHeightForWidth())
        self.creditaccotype.setSizePolicy(sizePolicy)
        self.creditaccotype.setMinimumSize(QSize(190, 40))
        self.creditaccotype.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.creditaccotype.setFont(font)
        self.creditaccotype.setStyleSheet("#creditaccotype{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.creditaccotype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.creditaccotype.setIconSize(QSize(40, 40))
        self.creditaccotype.setPlaceholderText("")
        self.creditaccotype.setObjectName("creditaccotype")
        self.verticalLayout_9.addWidget(self.creditaccotype)
        self.paymenttype = QComboBox(self.credit)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paymenttype.sizePolicy().hasHeightForWidth())
        self.paymenttype.setSizePolicy(sizePolicy)
        self.paymenttype.setMinimumSize(QSize(190, 40))
        self.paymenttype.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.paymenttype.setFont(font)
        self.paymenttype.setStyleSheet("#paymenttype{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.paymenttype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.paymenttype.setIconSize(QSize(40, 40))
        self.paymenttype.setPlaceholderText("")
        self.paymenttype.setObjectName("paymenttype")
        self.paymenttype.addItem("")
        self.paymenttype.addItem("")
        self.verticalLayout_9.addWidget(self.paymenttype)
        self.creditnecessary = QLineEdit(self.credit)
        self.creditnecessary.setMinimumSize(QSize(190, 40))
        self.creditnecessary.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(13)
        self.creditnecessary.setFont(font)
        self.creditnecessary.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.creditnecessary.setMaxLength(11)
        self.creditnecessary.setClearButtonEnabled(False)
        self.creditnecessary.setObjectName("creditnecessary")
        self.verticalLayout_9.addWidget(self.creditnecessary)
        self.creditbalance = QLineEdit(self.credit)
        self.creditbalance.setMinimumSize(QSize(190, 40))
        self.creditbalance.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(13)
        self.creditbalance.setFont(font)
        self.creditbalance.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.creditbalance.setMaxLength(11)
        self.creditbalance.setClearButtonEnabled(False)
        self.creditbalance.setObjectName("creditbalance")
        self.verticalLayout_9.addWidget(self.creditbalance)
        self.creditbutton = QPushButton(self.credit)
        self.creditbutton.setMinimumSize(QSize(100, 40))
        self.creditbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.creditbutton.setFont(font)
        self.creditbutton.setStyleSheet("")
        self.creditbutton.setObjectName("creditbutton")
        self.verticalLayout_9.addWidget(self.creditbutton, 0, Qt.AlignHCenter)
        self.deposit = QWidget(self.alltransactions)
        self.deposit.setGeometry(QRect(0, 40, 210, 200))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deposit.sizePolicy().hasHeightForWidth())
        self.deposit.setSizePolicy(sizePolicy)
        self.deposit.setMinimumSize(QSize(210, 200))
        self.deposit.setMaximumSize(QSize(210, 200))
        self.deposit.setStyleSheet("#deposit{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
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
"}\n"
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
"}\n"
"\n"
"#depositaccotype{\n"
"    border-radius:20px;\n"
"}")
        self.deposit.setObjectName("deposit")
        self.verticalLayout_7 = QVBoxLayout(self.deposit)
        self.verticalLayout_7.setContentsMargins(13, 9, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.depositlabel = QLabel(self.deposit)
        self.depositlabel.setMinimumSize(QSize(190, 40))
        self.depositlabel.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.depositlabel.setFont(font)
        self.depositlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.depositlabel.setScaledContents(True)
        self.depositlabel.setAlignment(Qt.AlignCenter)
        self.depositlabel.setObjectName("depositlabel")
        self.verticalLayout_7.addWidget(self.depositlabel)
        self.depositaccotype = QComboBox(self.deposit)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depositaccotype.sizePolicy().hasHeightForWidth())
        self.depositaccotype.setSizePolicy(sizePolicy)
        self.depositaccotype.setMinimumSize(QSize(190, 40))
        self.depositaccotype.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.depositaccotype.setFont(font)
        self.depositaccotype.setStyleSheet("#depositaccotype{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;\n"
"}\n"
"\n"
"\n"
"")
        self.depositaccotype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.depositaccotype.setIconSize(QSize(40, 40))
        self.depositaccotype.setPlaceholderText("")
        self.depositaccotype.setObjectName("depositaccotype")
        self.verticalLayout_7.addWidget(self.depositaccotype)
        self.depositbalance = QLineEdit(self.deposit)
        self.depositbalance.setMinimumSize(QSize(190, 40))
        self.depositbalance.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.depositbalance.setFont(font)
        self.depositbalance.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.depositbalance.setMaxLength(11)
        self.depositbalance.setClearButtonEnabled(False)
        self.depositbalance.setObjectName("depositbalance")
        self.verticalLayout_7.addWidget(self.depositbalance)
        self.depositbutton = QPushButton(self.deposit)
        self.depositbutton.setMinimumSize(QSize(100, 40))
        self.depositbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.depositbutton.setFont(font)
        self.depositbutton.setStyleSheet("color:rgb(255, 255, 255);")
        self.depositbutton.setObjectName("depositbutton")
        self.verticalLayout_7.addWidget(self.depositbutton, 0, Qt.AlignHCenter)
        self.takeout = QWidget(self.alltransactions)
        self.takeout.setGeometry(QRect(0, 40, 210, 300))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeout.sizePolicy().hasHeightForWidth())
        self.takeout.setSizePolicy(sizePolicy)
        self.takeout.setMinimumSize(QSize(210, 300))
        self.takeout.setMaximumSize(QSize(210, 300))
        self.takeout.setStyleSheet("#takeout{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
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
"}\n"
"QLineEdit,QTextEdit{\n"
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
"}\n"
"\n"
"#takeouttype{\n"
"    border-radius:20px;\n"
"}\n"
"#takeoutmonths{\n"
"    border-radius:20px;\n"
"}")
        self.takeout.setObjectName("takeout")
        self.verticalLayout_15 = QVBoxLayout(self.takeout)
        self.verticalLayout_15.setContentsMargins(13, 9, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.takeoutlabel = QLabel(self.takeout)
        self.takeoutlabel.setMinimumSize(QSize(190, 40))
        self.takeoutlabel.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.takeoutlabel.setFont(font)
        self.takeoutlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.takeoutlabel.setScaledContents(True)
        self.takeoutlabel.setAlignment(Qt.AlignCenter)
        self.takeoutlabel.setObjectName("takeoutlabel")
        self.verticalLayout_15.addWidget(self.takeoutlabel)
        self.takeouttype = QComboBox(self.takeout)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeouttype.sizePolicy().hasHeightForWidth())
        self.takeouttype.setSizePolicy(sizePolicy)
        self.takeouttype.setMinimumSize(QSize(190, 40))
        self.takeouttype.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.takeouttype.setFont(font)
        self.takeouttype.setStyleSheet("#takeouttype{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;\n"
"\n"
"}")
        self.takeouttype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.takeouttype.setIconSize(QSize(30, 30))
        self.takeouttype.setPlaceholderText("")
        self.takeouttype.setObjectName("takeouttype")
        self.takeouttype.addItem("")
        self.takeouttype.addItem("")
        self.takeouttype.addItem("")
        self.verticalLayout_15.addWidget(self.takeouttype)
        self.takeoutmonths = QComboBox(self.takeout)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeoutmonths.sizePolicy().hasHeightForWidth())
        self.takeoutmonths.setSizePolicy(sizePolicy)
        self.takeoutmonths.setMinimumSize(QSize(190, 40))
        self.takeoutmonths.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.takeoutmonths.setFont(font)
        self.takeoutmonths.setStyleSheet("#takeoutmonths{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;\n"
"\n"
"}\n"
"")
        self.takeoutmonths.setInsertPolicy(QComboBox.InsertAtBottom)
        self.takeoutmonths.setIconSize(QSize(30, 30))
        self.takeoutmonths.setPlaceholderText("")
        self.takeoutmonths.setObjectName("takeoutmonths")
        self.verticalLayout_15.addWidget(self.takeoutmonths)
        self.takeoutbalance = QLineEdit(self.takeout)
        self.takeoutbalance.setMinimumSize(QSize(190, 40))
        self.takeoutbalance.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.takeoutbalance.setFont(font)
        self.takeoutbalance.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.takeoutbalance.setMaxLength(11)
        self.takeoutbalance.setClearButtonEnabled(False)
        self.takeoutbalance.setObjectName("takeoutbalance")
        self.verticalLayout_15.addWidget(self.takeoutbalance)
        self.takeoutbutton = QPushButton(self.takeout)
        self.takeoutbutton.setMinimumSize(QSize(100, 40))
        self.takeoutbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.takeoutbutton.setFont(font)
        self.takeoutbutton.setStyleSheet("color:rgb(255, 255, 255);")
        self.takeoutbutton.setObjectName("takeoutbutton")
        self.verticalLayout_15.addWidget(self.takeoutbutton, 0, Qt.AlignHCenter)
        self.newaccount = QWidget(self.alltransactions)
        self.newaccount.setGeometry(QRect(0, 40, 210, 210))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newaccount.sizePolicy().hasHeightForWidth())
        self.newaccount.setSizePolicy(sizePolicy)
        self.newaccount.setMinimumSize(QSize(210, 210))
        self.newaccount.setMaximumSize(QSize(210, 210))
        self.newaccount.setStyleSheet("#newaccount{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
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
"}\n"
"\n"
"QComboBox{\n"
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
"}")
        self.newaccount.setObjectName("newaccount")
        self.verticalLayout_10 = QVBoxLayout(self.newaccount)
        self.verticalLayout_10.setContentsMargins(2, 10, 2, 10)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.newaccotitle = QLabel(self.newaccount)
        self.newaccotitle.setMinimumSize(QSize(190, 40))
        self.newaccotitle.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.newaccotitle.setFont(font)
        self.newaccotitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.newaccotitle.setScaledContents(True)
        self.newaccotitle.setAlignment(Qt.AlignCenter)
        self.newaccotitle.setObjectName("newaccotitle")
        self.verticalLayout_10.addWidget(self.newaccotitle, 0, Qt.AlignHCenter)
        self.accounttype = QComboBox(self.newaccount)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounttype.sizePolicy().hasHeightForWidth())
        self.accounttype.setSizePolicy(sizePolicy)
        self.accounttype.setMinimumSize(QSize(200, 40))
        self.accounttype.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(14)
        self.accounttype.setFont(font)
        self.accounttype.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:8px;")
        self.accounttype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.accounttype.setIconSize(QSize(30, 30))
        self.accounttype.setPlaceholderText("")
        self.accounttype.setObjectName("accounttype")
        self.accounttype.addItem("")
        self.accounttype.addItem("")
        self.accounttype.addItem("")
        self.accounttype.addItem("")
        self.accounttype.addItem("")
        self.verticalLayout_10.addWidget(self.accounttype, 0, Qt.AlignHCenter)
        self.currencytype = QComboBox(self.newaccount)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currencytype.sizePolicy().hasHeightForWidth())
        self.currencytype.setSizePolicy(sizePolicy)
        self.currencytype.setMinimumSize(QSize(200, 45))
        self.currencytype.setMaximumSize(QSize(200, 45))
        font = QFont()
        font.setPointSize(14)
        self.currencytype.setFont(font)
        self.currencytype.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;")
        self.currencytype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.currencytype.setIconSize(QSize(40, 40))
        self.currencytype.setPlaceholderText("")
        self.currencytype.setObjectName("currencytype")
        self.verticalLayout_10.addWidget(self.currencytype, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.accoopenbutton = QPushButton(self.newaccount)
        self.accoopenbutton.setMinimumSize(QSize(100, 40))
        self.accoopenbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.accoopenbutton.setFont(font)
        self.accoopenbutton.setStyleSheet("")
        self.accoopenbutton.setObjectName("accoopenbutton")
        self.verticalLayout_10.addWidget(self.accoopenbutton, 0, Qt.AlignHCenter)
        self.delaccount = QFrame(self.alltransactions)
        self.delaccount.setGeometry(QRect(0, 50, 210, 150))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delaccount.sizePolicy().hasHeightForWidth())
        self.delaccount.setSizePolicy(sizePolicy)
        self.delaccount.setMinimumSize(QSize(210, 150))
        self.delaccount.setMaximumSize(QSize(210, 150))
        self.delaccount.setStyleSheet("#delaccount{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"#accountstype{\n"
"    border-radius:20px;\n"
"}\n"
"")
        self.delaccount.setFrameShape(QFrame.StyledPanel)
        self.delaccount.setFrameShadow(QFrame.Raised)
        self.delaccount.setObjectName("delaccount")
        self.verticalLayout_2 = QVBoxLayout(self.delaccount)
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 15, 0, 12)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_59 = QLabel(self.delaccount)
        self.label_59.setMinimumSize(QSize(129, 0))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_59.setObjectName("label_59")
        self.verticalLayout_2.addWidget(self.label_59, 0, Qt.AlignHCenter|Qt.AlignTop)
        self.accountFrame = QFrame(self.delaccount)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountFrame.sizePolicy().hasHeightForWidth())
        self.accountFrame.setSizePolicy(sizePolicy)
        self.accountFrame.setMinimumSize(QSize(210, 55))
        self.accountFrame.setMaximumSize(QSize(210, 55))
        self.accountFrame.setStyleSheet("\n"
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
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    min-width:10px;\n"
"    max-width:10px;\n"
"    min-height:10px;\n"
"    max-height:10px;\n"
"}\n"
"\n"
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
"\n"
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
"}")
        self.accountFrame.setFrameShape(QFrame.StyledPanel)
        self.accountFrame.setFrameShadow(QFrame.Raised)
        self.accountFrame.setObjectName("accountFrame")
        self.horizontalLayout_9 = QHBoxLayout(self.accountFrame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.accountstype = QComboBox(self.accountFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountstype.sizePolicy().hasHeightForWidth())
        self.accountstype.setSizePolicy(sizePolicy)
        self.accountstype.setMinimumSize(QSize(200, 45))
        self.accountstype.setMaximumSize(QSize(200, 45))
        font = QFont()
        font.setPointSize(14)
        self.accountstype.setFont(font)
        self.accountstype.setStyleSheet("#accountstype{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"\n"
"}\n"
"\n"
"")
        self.accountstype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.accountstype.setIconSize(QSize(40, 40))
        self.accountstype.setPlaceholderText("")
        self.accountstype.setObjectName("accountstype")
        self.horizontalLayout_9.addWidget(self.accountstype, 0, Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.accountFrame, 0, Qt.AlignHCenter|Qt.AlignTop)
        self.delbutton = QPushButton(self.delaccount)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delbutton.sizePolicy().hasHeightForWidth())
        self.delbutton.setSizePolicy(sizePolicy)
        self.delbutton.setMinimumSize(QSize(70, 40))
        self.delbutton.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delbutton.setFont(font)
        self.delbutton.setStyleSheet("QPushButton{\n"
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
"}")
        self.delbutton.setObjectName("delbutton")
        self.verticalLayout_2.addWidget(self.delbutton, 0, Qt.AlignHCenter)
        self.moneytransfer = QWidget(self.alltransactions)
        self.moneytransfer.setGeometry(QRect(0, 10, 210, 410))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moneytransfer.sizePolicy().hasHeightForWidth())
        self.moneytransfer.setSizePolicy(sizePolicy)
        self.moneytransfer.setMinimumSize(QSize(210, 410))
        self.moneytransfer.setMaximumSize(QSize(210, 410))
        self.moneytransfer.setStyleSheet("#moneytransfer{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
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
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"QLineEdit,QTextEdit{\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"#traaccotype{\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"")
        self.moneytransfer.setObjectName("moneytransfer")
        self.verticalLayout_4 = QVBoxLayout(self.moneytransfer)
        self.verticalLayout_4.setContentsMargins(13, 9, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.transferlabel = QLabel(self.moneytransfer)
        self.transferlabel.setMinimumSize(QSize(190, 40))
        self.transferlabel.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.transferlabel.setFont(font)
        self.transferlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.transferlabel.setScaledContents(True)
        self.transferlabel.setAlignment(Qt.AlignCenter)
        self.transferlabel.setObjectName("transferlabel")
        self.verticalLayout_4.addWidget(self.transferlabel)
        self.traaccotype = QComboBox(self.moneytransfer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traaccotype.sizePolicy().hasHeightForWidth())
        self.traaccotype.setSizePolicy(sizePolicy)
        self.traaccotype.setMinimumSize(QSize(190, 40))
        self.traaccotype.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.traaccotype.setFont(font)
        self.traaccotype.setStyleSheet("#traaccotype{background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;}\n"
"\n"
"QAbstractItemView {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"padding: 5 5 16 5;\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
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
"}")
        self.traaccotype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.traaccotype.setIconSize(QSize(40, 40))
        self.traaccotype.setPlaceholderText("")
        self.traaccotype.setObjectName("traaccotype")
        self.verticalLayout_4.addWidget(self.traaccotype)
        self.transfernamesurname = QLineEdit(self.moneytransfer)
        self.transfernamesurname.setMinimumSize(QSize(190, 40))
        self.transfernamesurname.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.transfernamesurname.setFont(font)
        self.transfernamesurname.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.transfernamesurname.setText("")
        self.transfernamesurname.setCursorPosition(0)
        self.transfernamesurname.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.transfernamesurname.setClearButtonEnabled(False)
        self.transfernamesurname.setObjectName("transfernamesurname")
        self.verticalLayout_4.addWidget(self.transfernamesurname)
        self.transferaccountno = QLineEdit(self.moneytransfer)
        self.transferaccountno.setMinimumSize(QSize(190, 40))
        self.transferaccountno.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.transferaccountno.setFont(font)
        self.transferaccountno.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.transferaccountno.setMaxLength(8)
        self.transferaccountno.setClearButtonEnabled(False)
        self.transferaccountno.setObjectName("transferaccountno")
        self.verticalLayout_4.addWidget(self.transferaccountno)
        self.transferbalance = QLineEdit(self.moneytransfer)
        self.transferbalance.setMinimumSize(QSize(190, 40))
        self.transferbalance.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.transferbalance.setFont(font)
        self.transferbalance.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.transferbalance.setMaxLength(11)
        self.transferbalance.setClearButtonEnabled(False)
        self.transferbalance.setObjectName("transferbalance")
        self.verticalLayout_4.addWidget(self.transferbalance)
        self.explanation = QLineEdit(self.moneytransfer)
        self.explanation.setMinimumSize(QSize(190, 70))
        self.explanation.setMaximumSize(QSize(190, 70))
        font = QFont()
        font.setPointSize(12)
        self.explanation.setFont(font)
        self.explanation.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:40px;")
        self.explanation.setText("")
        self.explanation.setCursorPosition(0)
        self.explanation.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.explanation.setClearButtonEnabled(False)
        self.explanation.setObjectName("explanation")
        self.verticalLayout_4.addWidget(self.explanation)
        self.transferdate = QDateEdit(self.moneytransfer)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transferdate.sizePolicy().hasHeightForWidth())
        self.transferdate.setSizePolicy(sizePolicy)
        self.transferdate.setMinimumSize(QSize(190, 40))
        self.transferdate.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.transferdate.setFont(font)
        self.transferdate.setLayoutDirection(Qt.LeftToRight)
        self.transferdate.setAutoFillBackground(False)
        self.transferdate.setStyleSheet("#transferdate{background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:15px;\n"
"}\n"
"QDateEdit{\n"
"border-radius: 20px;\n"
"}\n"
"QDateEdit::drop-down{border:none;}\n"
"QDateEdit::down-arrow{\n"
"    image: url(:/Images/assets/icons/caret-circle-down .png);\n"
"    min-width:20px;\n"
"    max-width:20px;\n"
"    min-height:20px;\n"
"    max-height:20px;\n"
"    margin-right:2px;\n"
"}\n"
"QAbstractItemView {\n"
"    border-bottom: 2px solid white;\n"
"    border-left: 2px solid white;\n"
"    border-right: 2px solid white;\n"
"     background-color:rgb(37, 183, 196);\n"
"    font-size: 14px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{ \n"
"      background-color:rgb(37, 183, 196);\n"
"    border-top: 2px solid white;\n"
"    border-left: 2px solid white;\n"
"    border-right: 2px solid white;\n"
"    color:white;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_calendarview{ \n"
"      background-color:rgb(37, 183, 196);\n"
"    border-bottom: 2px solid white;\n"
"    border-left: 2px solid white;\n"
"    border-right: 2px solid white;\n"
"    padding-left:4px;\n"
"    font-size: 13px;\n"
"    color:black;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_monthbar{ \n"
"      background-color:rgb(37, 183, 196);\n"
"    border-top: 2px solid white;\n"
"    border-left: 2px solid white;\n"
"    border-right: 2px solid white;\n"
"    color:white;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth,#qt_calendar_nextmonth{\n"
"    border: none;\n"
"    qproperty-icon: none;\n"
"    min-width:13px;\n"
"    max-width:13px;\n"
"    min-height:13px;\n"
"    max-height:13px;\n"
"    border-radius:5px;\n"
"    background:rgb(37, 183, 196);\n"
"    padding:5px;\n"
"    color:white;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth:hover,#qt_calendar_nextmonth:hover{\n"
"    background-color:rgb(255, 93, 96);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth:pressed,#qt_calendar_nextmonth:pressed{\n"
"    background:rgb(255, 85, 88);\n"
"    padding-left:2px;    \n"
"    padding-bottom:2px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth{\n"
"    margin-left:5px;\n"
"    image: url(:/Images/assets/icons//circle-arrow-left.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth{\n"
"    margin-right:5px;\n"
"    image: url(:/Images/assets/icons/circle-arrow-right.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton{\n"
"    color:#000;\n"
"    margin: 5px;\n"
"    border-radius:5px;\n"
"    font-size:13px;\n"
"    padding:0px 10px;\n"
"    background:rgb(37, 183, 196);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton{\n"
"    width:110px;\n"
"    color:#000;\n"
"    margin: 5px 0px;\n"
"    border-radius:5px;\n"
"        background:rgb(37, 183, 196);\n"
"    font-size:13px;\n"
"    padding:0 2px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton:hover,#qt_calendar_monthbutton:hover{\n"
"    background-color:rgb(255, 93, 96);\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton:pressed,#qt_calendar_monthbutton:pressed{\n"
"    background:rgb(255, 85, 88);\n"
"    padding-left:2px;    \n"
"    padding-bottom:2px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::down-button{\n"
"    image:url(:/Images/assets/icons/caret-circle-down .png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::up-button{\n"
"    image:url(:/Images/assets/icons//caret-circle-up.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::up-button,#qt_calendar_yearedit::down-button{    \n"
"    border: none;\n"
"    qproperty-icon: none;\n"
"    min-width:5px;\n"
"    max-width:5px;\n"
"    min-height:5px;\n"
"    max-height:5px;\n"
"    border-radius:3px;\n"
"    background-color:transparent;\n"
"    padding:1px;\n"
"}")
        self.transferdate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.transferdate.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.transferdate.setAccelerated(False)
        self.transferdate.setProperty("showGroupSeparator", False)
        self.transferdate.setCurrentSection(QDateTimeEdit.DaySection)
        self.transferdate.setCalendarPopup(True)
        self.transferdate.setDate(QDateEdit(2022, 10, 14))
        self.transferdate.setObjectName("transferdate")
        self.verticalLayout_4.addWidget(self.transferdate)
        self.transferbutton = QPushButton(self.moneytransfer)
        self.transferbutton.setMinimumSize(QSize(100, 40))
        self.transferbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.transferbutton.setFont(font)
        self.transferbutton.setStyleSheet("")
        self.transferbutton.setObjectName("transferbutton")
        self.verticalLayout_4.addWidget(self.transferbutton, 0, Qt.AlignHCenter)
        self.transferlabel.raise_()
        self.traaccotype.raise_()
        self.transfernamesurname.raise_()
        self.transferbalance.raise_()
        self.explanation.raise_()
        self.transferdate.raise_()
        self.transferbutton.raise_()
        self.transferaccountno.raise_()
        self.withdraw = QWidget(self.alltransactions)
        self.withdraw.setGeometry(QRect(0, 40, 210, 200))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.withdraw.sizePolicy().hasHeightForWidth())
        self.withdraw.setSizePolicy(sizePolicy)
        self.withdraw.setMinimumSize(QSize(210, 200))
        self.withdraw.setMaximumSize(QSize(210, 200))
        self.withdraw.setStyleSheet("#withdraw{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(227, 76, 219, 226));\n"
"    border-radius:50px;\n"
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
"}\n"
"#withdrawaccotype{\n"
"    border-radius:20px;\n"
"}\n"
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
"}")
        self.withdraw.setObjectName("withdraw")
        self.verticalLayout_5 = QVBoxLayout(self.withdraw)
        self.verticalLayout_5.setContentsMargins(13, 9, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.withdrawlabel = QLabel(self.withdraw)
        self.withdrawlabel.setMinimumSize(QSize(190, 40))
        self.withdrawlabel.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.withdrawlabel.setFont(font)
        self.withdrawlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.withdrawlabel.setScaledContents(True)
        self.withdrawlabel.setAlignment(Qt.AlignCenter)
        self.withdrawlabel.setObjectName("withdrawlabel")
        self.verticalLayout_5.addWidget(self.withdrawlabel)
        self.withdrawaccotype = QComboBox(self.withdraw)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.withdrawaccotype.sizePolicy().hasHeightForWidth())
        self.withdrawaccotype.setSizePolicy(sizePolicy)
        self.withdrawaccotype.setMinimumSize(QSize(190, 40))
        self.withdrawaccotype.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(14)
        self.withdrawaccotype.setFont(font)
        self.withdrawaccotype.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"\n"
"")
        self.withdrawaccotype.setInsertPolicy(QComboBox.InsertAtBottom)
        self.withdrawaccotype.setIconSize(QSize(40, 40))
        self.withdrawaccotype.setPlaceholderText("")
        self.withdrawaccotype.setObjectName("withdrawaccotype")
        self.verticalLayout_5.addWidget(self.withdrawaccotype)
        self.withdrawbalance = QLineEdit(self.withdraw)
        self.withdrawbalance.setMinimumSize(QSize(190, 40))
        self.withdrawbalance.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(10)
        self.withdrawbalance.setFont(font)
        self.withdrawbalance.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.withdrawbalance.setMaxLength(11)
        self.withdrawbalance.setClearButtonEnabled(False)
        self.withdrawbalance.setObjectName("withdrawbalance")
        self.verticalLayout_5.addWidget(self.withdrawbalance)
        self.withdrawbutton = QPushButton(self.withdraw)
        self.withdrawbutton.setMinimumSize(QSize(100, 40))
        self.withdrawbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.withdrawbutton.setFont(font)
        self.withdrawbutton.setStyleSheet("color:rgb(255, 255, 255);")
        self.withdrawbutton.setObjectName("withdrawbutton")
        self.verticalLayout_5.addWidget(self.withdrawbutton, 0, Qt.AlignHCenter)
        self.credit.raise_()
        self.deposit.raise_()
        self.takeout.raise_()
        self.newaccount.raise_()
        self.delaccount.raise_()
        self.withdraw.raise_()
        self.moneytransfer.raise_()
        self.verticalLayout_11.addWidget(self.alltransactions)
        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignHCenter)
        self.mainBody = QWidget(self.allframes)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(0, 600))
        self.mainBody.setMaximumSize(QSize(740, 600))
        self.mainBody.setStyleSheet("#mainBody{background-color: rgb(254, 254, 255);border-radius:20px;}")
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout_18 = QVBoxLayout(self.mainBody)
        self.verticalLayout_18.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.headerFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QSize(0, 0))
        self.headerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.headerFrame.setStyleSheet("border-radius:20px;")
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_4.setContentsMargins(3, 2, 0, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.trainbutton = QPushButton(self.headerFrame)
        self.trainbutton.setMinimumSize(QSize(55, 55))
        self.trainbutton.setMaximumSize(QSize(55, 55))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.trainbutton.setFont(font)
        self.trainbutton.setStyleSheet("")
        self.trainbutton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/Images/assets/icons/b2.png"), QIcon.Normal, QIcon.Off)
        self.trainbutton.setIcon(icon2)
        self.trainbutton.setIconSize(QSize(55, 55))
        self.trainbutton.setCheckable(True)
        self.trainbutton.setObjectName("trainbutton")
        self.horizontalLayout_4.addWidget(self.trainbutton)
        self.maintitle = QWidget(self.headerFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        self.profilebutton.setMinimumSize(QSize(60, 55))
        self.profilebutton.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.profilebutton.setFont(font)
        self.profilebutton.setStyleSheet("")
        self.profilebutton.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/Images/assets/icons/customer2.png"), QIcon.Normal, QIcon.Off)
        self.profilebutton.setIcon(icon3)
        self.profilebutton.setIconSize(QSize(60, 55))
        self.profilebutton.setCheckable(True)
        self.profilebutton.setObjectName("profilebutton")
        self.horizontalLayout_4.addWidget(self.profilebutton)
        self.verticalLayout_18.addWidget(self.headerFrame)
        self.statusFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusFrame.sizePolicy().hasHeightForWidth())
        self.statusFrame.setSizePolicy(sizePolicy)
        self.statusFrame.setMinimumSize(QSize(0, 110))
        self.statusFrame.setMaximumSize(QSize(16777215, 16777215))
        self.statusFrame.setObjectName("statusFrame")
        self.horizontalLayout_26 = QHBoxLayout(self.statusFrame)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.card1 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card1.sizePolicy().hasHeightForWidth())
        self.card1.setSizePolicy(sizePolicy)
        self.card1.setMinimumSize(QSize(160, 0))
        self.card1.setStyleSheet("#incomeshower{border-radius:20px;}")
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_19 = QVBoxLayout(self.card1)
        self.verticalLayout_19.setContentsMargins(-1, 4, -1, 9)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_19 = QFrame(self.card1)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        self.label_51.setMinimumSize(QSize(129, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_27.addWidget(self.label_51)
        self.incomeicon = QPushButton(self.frame_19)
        self.incomeicon.setMinimumSize(QSize(50, 50))
        self.incomeicon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.incomeicon.setFont(font)
        self.incomeicon.setStyleSheet("background:transparent;")
        self.incomeicon.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/Images/assets/icons/incomdene.png"), QIcon.Normal, QIcon.Off)
        self.incomeicon.setIcon(icon4)
        self.incomeicon.setIconSize(QSize(50, 50))
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
        self.incomeclient.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"border-radius:20px;\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.incomeclient.setText("")
        self.incomeclient.setCursorPosition(0)
        self.incomeclient.setReadOnly(True)
        self.incomeclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.incomeclient.setClearButtonEnabled(False)
        self.incomeclient.setObjectName("incomeclient")
        self.verticalLayout_19.addWidget(self.incomeclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card1)
        self.card2 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card2.sizePolicy().hasHeightForWidth())
        self.card2.setSizePolicy(sizePolicy)
        self.card2.setMinimumSize(QSize(160, 0))
        self.card2.setStyleSheet("#expenseshower{border-radius:20px;}")
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_20 = QVBoxLayout(self.card2)
        self.verticalLayout_20.setContentsMargins(-1, 4, -1, 9)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_20 = QFrame(self.card2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        self.label_54.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_28.addWidget(self.label_54)
        self.expenseicon = QPushButton(self.frame_20)
        self.expenseicon.setMinimumSize(QSize(50, 50))
        self.expenseicon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.expenseicon.setFont(font)
        self.expenseicon.setStyleSheet("background:transparent;")
        self.expenseicon.setText("")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/Images/assets/icons/expense.png"), QIcon.Normal, QIcon.Off)
        self.expenseicon.setIcon(icon5)
        self.expenseicon.setIconSize(QSize(50, 50))
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
        self.expenseclient.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"border-radius:20px;\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.expenseclient.setText("")
        self.expenseclient.setCursorPosition(0)
        self.expenseclient.setReadOnly(True)
        self.expenseclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.expenseclient.setClearButtonEnabled(False)
        self.expenseclient.setObjectName("expenseclient")
        self.verticalLayout_20.addWidget(self.expenseclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card2)
        self.card3 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card3.sizePolicy().hasHeightForWidth())
        self.card3.setSizePolicy(sizePolicy)
        self.card3.setMinimumSize(QSize(160, 0))
        self.card3.setStyleSheet("#profitshower{border-radius:20px;}\n"
"")
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_21 = QVBoxLayout(self.card3)
        self.verticalLayout_21.setContentsMargins(9, 4, -1, 9)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_21 = QFrame(self.card3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        self.label_57.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_29.addWidget(self.label_57)
        self.profiticon = QPushButton(self.frame_21)
        self.profiticon.setMinimumSize(QSize(50, 50))
        self.profiticon.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.profiticon.setFont(font)
        self.profiticon.setStyleSheet("background:transparent;")
        self.profiticon.setText("")
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/Images/assets/icons/profit.png"), QIcon.Normal, QIcon.Off)
        self.profiticon.setIcon(icon6)
        self.profiticon.setIconSize(QSize(50, 50))
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
        self.profitclient.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"border-radius:20px;\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.profitclient.setText("")
        self.profitclient.setCursorPosition(0)
        self.profitclient.setReadOnly(True)
        self.profitclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.profitclient.setClearButtonEnabled(False)
        self.profitclient.setObjectName("profitclient")
        self.verticalLayout_21.addWidget(self.profitclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card3)
        self.card4 = QFrame(self.statusFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card4.sizePolicy().hasHeightForWidth())
        self.card4.setSizePolicy(sizePolicy)
        self.card4.setMinimumSize(QSize(160, 0))
        self.card4.setStyleSheet("#totalbalanceshower{border-radius:20px;}")
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_22 = QVBoxLayout(self.card4)
        self.verticalLayout_22.setContentsMargins(-1, 4, -1, 9)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_22 = QFrame(self.card4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        self.label_60.setMinimumSize(QSize(130, 0))
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
        self.balanceicon.setStyleSheet("background:transparent;")
        self.balanceicon.setText("")
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(":/Images/assets/icons/total.png"), QIcon.Normal, QIcon.Off)
        self.balanceicon.setIcon(icon7)
        self.balanceicon.setIconSize(QSize(50, 50))
        self.balanceicon.setCheckable(True)
        self.balanceicon.setObjectName("balanceicon")
        self.horizontalLayout_30.addWidget(self.balanceicon)
        self.verticalLayout_22.addWidget(self.frame_22)
        self.totalclient = QLineEdit(self.card4)
        self.totalclient.setMinimumSize(QSize(160, 40))
        self.totalclient.setMaximumSize(QSize(160, 40))
        font = QFont()
        font.setPointSize(17)
        self.totalclient.setFont(font)
        self.totalclient.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"border-radius:20px;\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.totalclient.setText("")
        self.totalclient.setCursorPosition(0)
        self.totalclient.setReadOnly(True)
        self.totalclient.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.totalclient.setClearButtonEnabled(False)
        self.totalclient.setObjectName("totalclient")
        self.verticalLayout_22.addWidget(self.totalclient, 0, Qt.AlignHCenter)
        self.horizontalLayout_26.addWidget(self.card4)
        self.verticalLayout_18.addWidget(self.statusFrame)
        self.mainFrame = QWidget(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QSize(0, 0))
        self.mainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.statements = QFrame(self.mainFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statements.sizePolicy().hasHeightForWidth())
        self.statements.setSizePolicy(sizePolicy)
        self.statements.setMinimumSize(QSize(660, 200))
        self.statements.setMaximumSize(QSize(660, 200))
        self.statements.setStyleSheet("#statements{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
"    border-radius:20px;\n"
"    border: 2px solid rgb(37, 150, 190);\n"
"\n"
"}\n"
"#currencytype{\n"
"    border-radius:20px;\n"
"}")
        self.statements.setFrameShape(QFrame.StyledPanel)
        self.statements.setFrameShadow(QFrame.Raised)
        self.statements.setObjectName("statements")
        self.gridLayout_3 = QGridLayout(self.statements)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 5)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.editing = QFrame(self.statements)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editing.sizePolicy().hasHeightForWidth())
        self.editing.setSizePolicy(sizePolicy)
        self.editing.setStyleSheet("")
        self.editing.setFrameShape(QFrame.StyledPanel)
        self.editing.setFrameShadow(QFrame.Raised)
        self.editing.setObjectName("editing")
        self.gridLayout_4 = QGridLayout(self.editing)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.statementtable = QTableWidget(self.editing)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statementtable.sizePolicy().hasHeightForWidth())
        self.statementtable.setSizePolicy(sizePolicy)
        self.statementtable.setMinimumSize(QSize(633, 125))
        self.statementtable.setMaximumSize(QSize(633, 125))
        font = QFont()
        font.setPointSize(10)
        self.statementtable.setFont(font)
        self.statementtable.setStyleSheet("QWidget {\n"
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
"")
        self.statementtable.setFrameShadow(QFrame.Sunken)
        self.statementtable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.statementtable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.statementtable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.statementtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.statementtable.setGridStyle(Qt.CustomDashLine)
        self.statementtable.setWordWrap(True)
        self.statementtable.setCornerButtonEnabled(False)
        self.statementtable.setRowCount(5)
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
        self.statementtable.horizontalHeader().setDefaultSectionSize(85)
        self.statementtable.horizontalHeader().setMinimumSectionSize(85)
        self.statementtable.verticalHeader().setDefaultSectionSize(30)
        self.statementtable.verticalHeader().setHighlightSections(True)
        self.statementtable.verticalHeader().setMinimumSectionSize(30)
        self.statementtable.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_4.addWidget(self.statementtable, 1, 0, 1, 1, Qt.AlignHCenter)
        self.frame_3 = QFrame(self.editing)
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.statementicon = QPushButton(self.frame_3)
        self.statementicon.setMinimumSize(QSize(50, 50))
        self.statementicon.setMaximumSize(QSize(50, 50))
        self.statementicon.setText("")
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/Images/assets/icons/statements.png"), QIcon.Normal, QIcon.Off)
        self.statementicon.setIcon(icon8)
        self.statementicon.setIconSize(QSize(50, 50))
        self.statementicon.setObjectName("statementicon")
        self.horizontalLayout_5.addWidget(self.statementicon)
        self.label_76 = QLabel(self.frame_3)
        self.label_76.setMinimumSize(QSize(205, 40))
        self.label_76.setMaximumSize(QSize(205, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_76.setObjectName("label_76")
        self.horizontalLayout_5.addWidget(self.label_76)
        self.addmorestate = QPushButton(self.frame_3)
        self.addmorestate.setMinimumSize(QSize(100, 40))
        self.addmorestate.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addmorestate.setFont(font)
        self.addmorestate.setStyleSheet("QPushButton{\n"
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
"}")
        self.addmorestate.setObjectName("addmorestate")
        self.horizontalLayout_5.addWidget(self.addmorestate)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignTop)
        self.gridLayout_3.addWidget(self.editing, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.statements, 0, Qt.AlignHCenter)
        self.creditsFrame = QWidget(self.mainFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creditsFrame.sizePolicy().hasHeightForWidth())
        self.creditsFrame.setSizePolicy(sizePolicy)
        self.creditsFrame.setMinimumSize(QSize(724, 0))
        self.creditsFrame.setMaximumSize(QSize(724, 16777215))
        self.creditsFrame.setStyleSheet("#selectrowstatus{\n"
"    border-radius:20px;\n"
"}\n"
"#creditsFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
"    border-radius:20px;\n"
"    border: 2px solid rgb(37, 150, 190);\n"
"\n"
"}")
        self.creditsFrame.setObjectName("creditsFrame")
        self.verticalLayout = QVBoxLayout(self.creditsFrame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_23 = QFrame(self.creditsFrame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QSize(0, 50))
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setStyleSheet("#addmorestate{\n"
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
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_33 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_33.setContentsMargins(2, 0, 6, 0)
        self.horizontalLayout_33.setSpacing(9)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem = QSpacerItem(27, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem)
        self.creditstitles = QFrame(self.frame_23)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creditstitles.sizePolicy().hasHeightForWidth())
        self.creditstitles.setSizePolicy(sizePolicy)
        self.creditstitles.setMinimumSize(QSize(260, 50))
        self.creditstitles.setMaximumSize(QSize(260, 50))
        self.creditstitles.setFrameShape(QFrame.StyledPanel)
        self.creditstitles.setFrameShadow(QFrame.Raised)
        self.creditstitles.setObjectName("creditstitles")
        self.horizontalLayout_12 = QHBoxLayout(self.creditstitles)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.creditsicon = QPushButton(self.creditstitles)
        self.creditsicon.setMinimumSize(QSize(50, 50))
        self.creditsicon.setMaximumSize(QSize(50, 50))
        self.creditsicon.setText("")
        icon9 = QIcon()
        icon9.addPixmap(QPixmap(":/Images/assets/icons/credit.png"), QIcon.Normal, QIcon.Off)
        self.creditsicon.setIcon(icon9)
        self.creditsicon.setIconSize(QSize(50, 50))
        self.creditsicon.setObjectName("creditsicon")
        self.horizontalLayout_12.addWidget(self.creditsicon, 0, Qt.AlignHCenter)
        self.creditstitle = QLabel(self.creditstitles)
        self.creditstitle.setMinimumSize(QSize(180, 30))
        self.creditstitle.setMaximumSize(QSize(180, 30))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.creditstitle.setFont(font)
        self.creditstitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.creditstitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.creditstitle.setObjectName("creditstitle")
        self.horizontalLayout_12.addWidget(self.creditstitle, 0, Qt.AlignHCenter)
        self.horizontalLayout_33.addWidget(self.creditstitles)
        spacerItem1 = QSpacerItem(27, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_23)
        self.frame_2 = QFrame(self.creditsFrame)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.creditstable = QTableWidget(self.frame_2)
        self.creditstable.setMinimumSize(QSize(697, 125))
        self.creditstable.setMaximumSize(QSize(697, 125))
        font = QFont()
        font.setPointSize(10)
        self.creditstable.setFont(font)
        self.creditstable.setStyleSheet("QWidget {\n"
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
"")
        self.creditstable.setFrameShadow(QFrame.Sunken)
        self.creditstable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.creditstable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.creditstable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.creditstable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.creditstable.setTabKeyNavigation(False)
        self.creditstable.setProperty("showDropIndicator", False)
        self.creditstable.setDragDropOverwriteMode(False)
        self.creditstable.setTextElideMode(Qt.ElideLeft)
        self.creditstable.setGridStyle(Qt.CustomDashLine)
        self.creditstable.setWordWrap(True)
        self.creditstable.setCornerButtonEnabled(False)
        self.creditstable.setRowCount(11)
        self.creditstable.setColumnCount(8)
        self.creditstable.setObjectName("creditstable")
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.creditstable.setHorizontalHeaderItem(7, item)
        self.creditstable.horizontalHeader().setDefaultSectionSize(82)
        self.creditstable.horizontalHeader().setMinimumSectionSize(82)
        self.creditstable.verticalHeader().setDefaultSectionSize(30)
        self.creditstable.verticalHeader().setHighlightSections(True)
        self.creditstable.verticalHeader().setMinimumSectionSize(30)
        self.creditstable.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_7.addWidget(self.creditstable)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.creditsFrame, 0, Qt.AlignHCenter)
        self.verticalLayout_18.addWidget(self.mainFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.mainBody, 0, Qt.AlignHCenter)
        self.rightMenu = QWidget(self.allframes)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightMenu.sizePolicy().hasHeightForWidth())
        self.rightMenu.setSizePolicy(sizePolicy)
        self.rightMenu.setMinimumSize(QSize(0, 600))
        self.rightMenu.setMaximumSize(QSize(0, 600))
        self.rightMenu.setStyleSheet("#rightMenu{background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));border-top-right-radius:20px;border-bottom-right-radius:20px;}\n"
"#username{border-radius:20px;}")
        self.rightMenu.setObjectName("rightMenu")
        self.verticalLayout_27 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_27.setContentsMargins(5, 0, 5, 10)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.profileframe = QFrame(self.rightMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileframe.sizePolicy().hasHeightForWidth())
        self.profileframe.setSizePolicy(sizePolicy)
        self.profileframe.setMinimumSize(QSize(210, 240))
        self.profileframe.setMaximumSize(QSize(210, 240))
        self.profileframe.setFrameShape(QFrame.StyledPanel)
        self.profileframe.setFrameShadow(QFrame.Raised)
        self.profileframe.setObjectName("profileframe")
        self.verticalLayout_28 = QVBoxLayout(self.profileframe)
        self.verticalLayout_28.setContentsMargins(1, 5, 1, 14)
        self.verticalLayout_28.setSpacing(12)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.username = QLineEdit(self.profileframe)
        self.username.setMinimumSize(QSize(210, 40))
        self.username.setMaximumSize(QSize(210, 40))
        font = QFont()
        font.setPointSize(13)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.username.setText("")
        self.username.setMaxLength(50)
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setPlaceholderText("")
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.verticalLayout_28.addWidget(self.username)
        self.coolguy = QPushButton(self.profileframe)
        self.coolguy.setMinimumSize(QSize(100, 100))
        self.coolguy.setMaximumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.coolguy.setFont(font)
        self.coolguy.setStyleSheet("")
        self.coolguy.setText("")
        icon10 = QIcon()
        icon10.addPixmap(QPixmap(":/Images/assets/icons/customer.png"), QIcon.Normal, QIcon.Off)
        self.coolguy.setIcon(icon10)
        self.coolguy.setIconSize(QSize(100, 100))
        self.coolguy.setCheckable(True)
        self.coolguy.setObjectName("coolguy")
        self.verticalLayout_28.addWidget(self.coolguy, 0, Qt.AlignHCenter)
        self.myProfile = QPushButton(self.profileframe)
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.myProfile.setFont(font)
        self.myProfile.setStyleSheet("color: rgb(255, 255, 255);")
        self.myProfile.setIcon(icon3)
        self.myProfile.setIconSize(QSize(24, 24))
        self.myProfile.setObjectName("myProfile")
        self.verticalLayout_28.addWidget(self.myProfile)
        self.logout = QPushButton(self.profileframe)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logout.setFont(font)
        self.logout.setStyleSheet("color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addPixmap(QPixmap(":/Images/assets/icons/1053210.png"), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon11)
        self.logout.setIconSize(QSize(24, 24))
        self.logout.setObjectName("logout")
        self.verticalLayout_28.addWidget(self.logout)
        self.verticalLayout_27.addWidget(self.profileframe, 0, Qt.AlignHCenter|Qt.AlignTop)
        self._4customeraddinfo = QWidget(self.rightMenu)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._4customeraddinfo.sizePolicy().hasHeightForWidth())
        self._4customeraddinfo.setSizePolicy(sizePolicy)
        self._4customeraddinfo.setMinimumSize(QSize(0, 0))
        self._4customeraddinfo.setMaximumSize(QSize(0, 330))
        self._4customeraddinfo.setStyleSheet("#_4customeraddinfo{    \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(227, 76, 219, 226), stop:1 rgba(37, 183, 196, 219));\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QLineEdit,QTextEdit{\n"
"    border-radius:20px;\n"
"}\n"
"")
        self._4customeraddinfo.setObjectName("_4customeraddinfo")
        self.verticalLayout_8 = QVBoxLayout(self._4customeraddinfo)
        self.verticalLayout_8.setContentsMargins(9, 5, -1, 2)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
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
        self.verticalLayout_8.addWidget(self.registerlabelrep, 0, Qt.AlignHCenter)
        self.name_surnamecus = QLineEdit(self._4customeraddinfo)
        self.name_surnamecus.setMinimumSize(QSize(190, 40))
        self.name_surnamecus.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(13)
        self.name_surnamecus.setFont(font)
        self.name_surnamecus.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.name_surnamecus.setText("")
        self.name_surnamecus.setCursorPosition(0)
        self.name_surnamecus.setReadOnly(True)
        self.name_surnamecus.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.name_surnamecus.setClearButtonEnabled(False)
        self.name_surnamecus.setObjectName("name_surnamecus")
        self.verticalLayout_8.addWidget(self.name_surnamecus, 0, Qt.AlignHCenter)
        self.telephonecus = QLineEdit(self._4customeraddinfo)
        self.telephonecus.setMinimumSize(QSize(190, 40))
        self.telephonecus.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(13)
        self.telephonecus.setFont(font)
        self.telephonecus.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.telephonecus.setText("")
        self.telephonecus.setMaxLength(15)
        self.telephonecus.setClearButtonEnabled(False)
        self.telephonecus.setObjectName("telephonecus")
        self.verticalLayout_8.addWidget(self.telephonecus, 0, Qt.AlignHCenter)
        self.citizencus = QLineEdit(self._4customeraddinfo)
        self.citizencus.setMinimumSize(QSize(190, 40))
        self.citizencus.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(13)
        self.citizencus.setFont(font)
        self.citizencus.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.citizencus.setMaxLength(15)
        self.citizencus.setReadOnly(True)
        self.citizencus.setClearButtonEnabled(False)
        self.citizencus.setObjectName("citizencus")
        self.verticalLayout_8.addWidget(self.citizencus, 0, Qt.AlignHCenter)
        self.addresscus = QLineEdit(self._4customeraddinfo)
        self.addresscus.setMinimumSize(QSize(190, 70))
        self.addresscus.setMaximumSize(QSize(190, 70))
        font = QFont()
        font.setPointSize(13)
        self.addresscus.setFont(font)
        self.addresscus.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:40px;")
        self.addresscus.setText("")
        self.addresscus.setCursorPosition(0)
        self.addresscus.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.addresscus.setClearButtonEnabled(False)
        self.addresscus.setObjectName("addresscus")
        self.verticalLayout_8.addWidget(self.addresscus, 0, Qt.AlignHCenter)
        self.emailcus = QLineEdit(self._4customeraddinfo)
        self.emailcus.setMinimumSize(QSize(190, 40))
        self.emailcus.setMaximumSize(QSize(190, 40))
        font = QFont()
        font.setPointSize(13)
        self.emailcus.setFont(font)
        self.emailcus.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 183, 196, 219), stop:1 rgba(37, 196, 129, 226));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-left:5px;\n"
"padding-bottom:7px;")
        self.emailcus.setEchoMode(QLineEdit.Normal)
        self.emailcus.setObjectName("emailcus")
        self.verticalLayout_8.addWidget(self.emailcus, 0, Qt.AlignHCenter)
        self.cusbutton = QPushButton(self._4customeraddinfo)
        self.cusbutton.setMinimumSize(QSize(100, 40))
        self.cusbutton.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cusbutton.setFont(font)
        self.cusbutton.setStyleSheet("QPushButton{\n"
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
"}")
        self.cusbutton.setObjectName("cusbutton")
        self.verticalLayout_8.addWidget(self.cusbutton, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.verticalLayout_27.addWidget(self._4customeraddinfo, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.rightMenu, 0, Qt.AlignHCenter)
        self.mainBody.raise_()
        self.rightMenu.raise_()
        self.leftMenu.raise_()
        Customer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Customer)
        self.transfertype.setCurrentIndex(0)
        self.creditaccotype.setCurrentIndex(-1)
        self.paymenttype.setCurrentIndex(0)
        self.depositaccotype.setCurrentIndex(-1)
        self.takeouttype.setCurrentIndex(0)
        self.takeoutmonths.setCurrentIndex(-1)
        self.accounttype.setCurrentIndex(0)
        self.currencytype.setCurrentIndex(-1)
        self.accountstype.setCurrentIndex(-1)
        self.traaccotype.setCurrentIndex(-1)
        self.withdrawaccotype.setCurrentIndex(-1)
        QMetaObject.connectSlotsByName(Customer)

    def retranslateUi(self, Customer):
        _translate = QCoreApplication.translate
        Customer.setWindowTitle(_translate("Customer", "SeaBank"))
        self.label_56.setText(_translate("Customer", "Transactions"))
        self.transfertype.setItemText(0, _translate("Customer", "Withdraw"))
        self.transfertype.setItemText(1, _translate("Customer", "Deposit"))
        self.transfertype.setItemText(2, _translate("Customer", "Transfer"))
        self.transfertype.setItemText(3, _translate("Customer", "Take-Out Credit"))
        self.transfertype.setItemText(4, _translate("Customer", "Credit Payment"))
        self.transfertype.setItemText(5, _translate("Customer", "New Account"))
        self.transfertype.setItemText(6, _translate("Customer", "Delete Account"))
        self.transbutton.setText(_translate("Customer", "Submit"))
        self.creditlabel.setText(_translate("Customer", "Credit"))
        self.paymenttype.setItemText(0, _translate("Customer", "Current Month"))
        self.paymenttype.setItemText(1, _translate("Customer", "All Debt"))
        self.creditnecessary.setPlaceholderText(_translate("Customer", "  Necessary Amount"))
        self.creditbalance.setPlaceholderText(_translate("Customer", "  Balance"))
        self.creditbutton.setText(_translate("Customer", "Pay"))
        self.depositlabel.setText(_translate("Customer", "Deposit"))
        self.depositbalance.setPlaceholderText(_translate("Customer", "  Balance"))
        self.depositbutton.setText(_translate("Customer", "Deposit"))
        self.takeoutlabel.setText(_translate("Customer", "Take-Out Credit"))
        self.takeouttype.setItemText(0, _translate("Customer", "Personal Finance"))
        self.takeouttype.setItemText(1, _translate("Customer", "Housing Loan"))
        self.takeouttype.setItemText(2, _translate("Customer", "Transport Credit"))
        self.takeoutbalance.setPlaceholderText(_translate("Customer", "  Balance"))
        self.takeoutbutton.setText(_translate("Customer", "Demand"))
        self.newaccotitle.setText(_translate("Customer", "New Account"))
        self.accounttype.setItemText(0, _translate("Customer", "Savings Account"))
        self.accounttype.setItemText(1, _translate("Customer", "Checking Account"))
        self.accounttype.setItemText(2, _translate("Customer", "Money Market Account"))
        self.accounttype.setItemText(3, _translate("Customer", "Certificates of Deposit"))
        self.accounttype.setItemText(4, _translate("Customer", "Retirement Account"))
        self.accoopenbutton.setText(_translate("Customer", "Open"))
        self.label_59.setText(_translate("Customer", "Account Deletion"))
        self.delbutton.setText(_translate("Customer", "Delete"))
        self.transferlabel.setText(_translate("Customer", "Transfer"))
        self.transfernamesurname.setPlaceholderText(_translate("Customer", "  First and Last Name"))
        self.transferaccountno.setToolTip(_translate("Customer", "<html><head/><body><p>Başında Sıfır olmadan giriniz.</p></body></html>"))
        self.transferaccountno.setPlaceholderText(_translate("Customer", "  Account No"))
        self.transferbalance.setPlaceholderText(_translate("Customer", "  Balance"))
        self.explanation.setPlaceholderText(_translate("Customer", " Explanation"))
        self.transferdate.setDisplayFormat(_translate("Customer", "dd.MM.yyyy"))
        self.transferbutton.setText(_translate("Customer", "Tranfer"))
        self.withdrawlabel.setText(_translate("Customer", "Withdraw"))
        self.withdrawbalance.setPlaceholderText(_translate("Customer", "  Balance"))
        self.withdrawbutton.setText(_translate("Customer", "Withdraw"))
        self.appHeader.setText(_translate("Customer", "Welcome to SeaBank"))
        self.label_51.setText(_translate("Customer", "Income"))
        self.incomeclient.setPlaceholderText(_translate("Customer", "    Income"))
        self.label_54.setText(_translate("Customer", "Expense"))
        self.expenseclient.setPlaceholderText(_translate("Customer", "    Expense"))
        self.label_57.setText(_translate("Customer", "Profit"))
        self.profitclient.setPlaceholderText(_translate("Customer", "    Profit   "))
        self.label_60.setText(_translate("Customer", "Balance"))
        self.totalclient.setPlaceholderText(_translate("Customer", "    Balance"))
        self.statementtable.setSortingEnabled(False)
        item = self.statementtable.horizontalHeaderItem(0)
        item.setText(_translate("Customer", "Source No"))
        item = self.statementtable.horizontalHeaderItem(1)
        item.setText(_translate("Customer", "Target No"))
        item = self.statementtable.horizontalHeaderItem(2)
        item.setText(_translate("Customer", "Type"))
        item = self.statementtable.horizontalHeaderItem(3)
        item.setText(_translate("Customer", "Balance"))
        item = self.statementtable.horizontalHeaderItem(4)
        item.setText(_translate("Customer", "S_Balance"))
        item = self.statementtable.horizontalHeaderItem(5)
        item.setText(_translate("Customer", "T_Balance"))
        item = self.statementtable.horizontalHeaderItem(6)
        item.setText(_translate("Customer", "Date"))
        self.label_76.setText(_translate("Customer", "Monthly Statements"))
        self.addmorestate.setText(_translate("Customer", "Add More"))
        self.creditstitle.setText(_translate("Customer", "Credit Payments"))
        self.creditstable.setSortingEnabled(False)
        item = self.creditstable.horizontalHeaderItem(0)
        item.setText(_translate("Customer", "Instalment"))
        item = self.creditstable.horizontalHeaderItem(1)
        item.setText(_translate("Customer", "Principal"))
        item = self.creditstable.horizontalHeaderItem(2)
        item.setText(_translate("Customer", "Interest"))
        item = self.creditstable.horizontalHeaderItem(3)
        item.setText(_translate("Customer", "Debt "))
        item = self.creditstable.horizontalHeaderItem(4)
        item.setText(_translate("Customer", "Status"))
        item = self.creditstable.horizontalHeaderItem(5)
        item.setText(_translate("Customer", "Pay Date"))
        item = self.creditstable.horizontalHeaderItem(6)
        item.setText(_translate("Customer", "Due Date"))
        item = self.creditstable.horizontalHeaderItem(7)
        item.setText(_translate("Customer", "Late_Interest"))
        self.myProfile.setText(_translate("Customer", "My profile"))
        self.logout.setText(_translate("Customer", "Log Out"))
        self.registerlabelrep.setText(_translate("Customer", "Information"))
        self.name_surnamecus.setPlaceholderText(_translate("Customer", "  First and Last Name"))
        self.telephonecus.setToolTip(_translate("Customer", "<html><head/><body><p>Başında Sıfır olmadan giriniz.</p></body></html>"))
        self.telephonecus.setPlaceholderText(_translate("Customer", "  Telephone No"))
        self.citizencus.setPlaceholderText(_translate("Customer", "  Citizenship No"))
        self.addresscus.setPlaceholderText(_translate("Customer", " Address"))
        self.emailcus.setPlaceholderText(_translate("Customer", "  E-mail Address"))
        self.cusbutton.setText(_translate("Customer", "Save"))
import res_rc_rc
