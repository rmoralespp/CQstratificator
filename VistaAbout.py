__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from about import *

class VistaAbout(QDialog,Ui_Dialog):
      def __init__(self):
        super(VistaAbout,self).__init__()
        self.setupUi(self)
        self.setFixedHeight(532)
        self.setFixedWidth(458)



