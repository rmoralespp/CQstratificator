# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compiler4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import recursos7
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(591, 576)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.textEdit = QtGui.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        #font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.treeWidget_2 = QtGui.QTreeWidget(self.tab_3)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        self.treeWidget_2.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_5.addWidget(self.treeWidget_2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.tab_2)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(MainWindow)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QtGui.QToolBar(MainWindow)
        self.toolBar_4.setObjectName(_fromUtf8("toolBar_4"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        self.toolBar_5 = QtGui.QToolBar(MainWindow)
        self.toolBar_5.setObjectName(_fromUtf8("toolBar_5"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_5)
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/234.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/6.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/7.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon2)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/8.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_image = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/567.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_image.setIcon(icon4)
        self.actionSave_image.setObjectName(_fromUtf8("actionSave_image"))
        self.actionClose = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/11.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon5)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionUndo_Insert_Action = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo_Insert_Action.setIcon(icon6)
        self.actionUndo_Insert_Action.setObjectName(_fromUtf8("actionUndo_Insert_Action"))
        self.action_Rehacer = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Rehacer.setIcon(icon7)
        self.action_Rehacer.setObjectName(_fromUtf8("action_Rehacer"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon8)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/67.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon9)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/46.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon10)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/76.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon11)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))
        self.actionLexer = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/18.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLexer.setIcon(icon12)
        self.actionLexer.setObjectName(_fromUtf8("actionLexer"))
        self.actionParser = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/13.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionParser.setIcon(icon13)
        self.actionParser.setObjectName(_fromUtf8("actionParser"))
        self.actionCheker = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/15.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheker.setIcon(icon14)
        self.actionCheker.setObjectName(_fromUtf8("actionCheker"))
        self.actionRun = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon15)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionAbout_CompilerQGisEstratitifcation = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/12.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_CompilerQGisEstratitifcation.setIcon(icon16)
        self.actionAbout_CompilerQGisEstratitifcation.setObjectName(_fromUtf8("actionAbout_CompilerQGisEstratitifcation"))
        self.actionHelp_Manual = QtGui.QAction(MainWindow)
        self.actionHelp_Manual.setObjectName(_fromUtf8("actionHelp_Manual"))
        self.actionAbout_language = QtGui.QAction(MainWindow)
        self.actionAbout_language.setObjectName(_fromUtf8("actionAbout_language"))
        self.actionZoom_in = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/zi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon17)
        self.actionZoom_in.setObjectName(_fromUtf8("actionZoom_in"))
        self.actionZoom_out = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/zo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon18)
        self.actionZoom_out.setObjectName(_fromUtf8("actionZoom_out"))
        self.actionHold = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/mano.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHold.setIcon(icon19)
        self.actionHold.setObjectName(_fromUtf8("actionHold"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuOptions.addAction(self.actionRun)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionLexer)
        self.menuOptions.addAction(self.actionParser)
        self.menuOptions.addAction(self.actionCheker)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionZoom_in)
        self.menuOptions.addAction(self.actionZoom_out)
        self.menuOptions.addAction(self.actionHold)
        self.menuOptions.addSeparator()
        self.menuHelp.addAction(self.actionAbout_CompilerQGisEstratitifcation)
        self.menuHelp.addAction(self.actionHelp_Manual)
        self.menuHelp.addAction(self.actionAbout_language)
        self.menuEdit.addAction(self.actionUndo_Insert_Action)
        self.menuEdit.addAction(self.action_Rehacer)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CQestratifcator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tokens", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Errors", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3", None))
        self.toolBar_4.setWindowTitle(_translate("MainWindow", "toolBar_4", None))
        self.toolBar_5.setWindowTitle(_translate("MainWindow", "toolBar_5", None))
        self.actionNew.setText(_translate("MainWindow", "New...", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_image.setText(_translate("MainWindow", "Save Image...", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionUndo_Insert_Action.setText(_translate("MainWindow", "Undo ", None))
        self.action_Rehacer.setText(_translate("MainWindow", "Redo", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All", None))
        self.actionLexer.setText(_translate("MainWindow", "Lexer", None))
        self.actionParser.setText(_translate("MainWindow", "Parser", None))
        self.actionCheker.setText(_translate("MainWindow", "Cheker", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionAbout_CompilerQGisEstratitifcation.setText(_translate("MainWindow", "About CQestratifcator", None))
        self.actionHelp_Manual.setText(_translate("MainWindow", "Help Manual", None))
        self.actionAbout_language.setText(_translate("MainWindow", "About language", None))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in...", None))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out...", None))
        self.actionHold.setText(_translate("MainWindow", "Hold", None))


