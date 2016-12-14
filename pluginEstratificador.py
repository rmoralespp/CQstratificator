from PyQt4.QtCore import *
from PyQt4.QtGui import *

from VistaCompilador import *

import recursos7

class pluginEstratificador:
 def __init__(self, iface):

#Guardar la referencia para la interfaz de QGIS-------------------------------------------------------------------------
       self.iface = iface
       self.canvas = iface.mapCanvas()



 def initGui(self):
     icon18 = QIcon()
     icon18.addPixmap(QPixmap(":/newPrefix/logo.png"), QIcon.Normal, QIcon.Off)
     self.action = QAction(icon18,"CQEstratificator", self.iface.mainWindow())
     self.action.setWhatsThis("CQEstratificator")
     QObject.connect(self.action, SIGNAL("activated()"), self.run)
     self.iface.addToolBarIcon(self.action)
     self.iface.addPluginToMenu("&CQEstratificator", self.action)

 def unload(self):
       self.iface.removePluginMenu("&CQEstratificator",self.action)
       self.iface.removeToolBarIcon(self.action)

 def run(self):
     flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
     self.principal=VistaCompilador()
     self.principal.show()


if __name__ == "__main__":
    pass
