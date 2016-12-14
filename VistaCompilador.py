__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Lexer import Lexer
from Parser import Parser
from Cheker import Cheker
from Keywords import *
from SymbolsTable import *
from compiler4 import Ui_MainWindow
from MyEncoder import *
from Visualizacion import *
import os
from VistaAbout import VistaAbout
from qgis.utils import iface
import qgis.core
from qgis.core import *
from qgis.gui import *
from Controller import Controller
import os
from Keywords import *


class VistaCompilador(QMainWindow,Ui_MainWindow):

     def __init__(self):
        super(VistaCompilador,self).__init__()
        self.setupUi(self)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        st=SymbolsTable()
        self.lexer=Lexer(st)
        self.parser=Parser()
        self.cheker=Cheker()
        self.autoCompletamiento=QShortcut(self)
        self.autoCompletamiento.setKey("Ctrl+Space")
        self.signal=SIGNAL("paint")
        self.signalE=SIGNAL("error")
        self.control=True
        self.texto=None
        self.controller=Controller(self,self.texto)
        self.fichero=None
        self.format=self.textEdit.currentCharFormat()



#lista para el autocompletamiento de codigo-----------------------------------------------------------------------------
        self.listaPosibles=QListWidget(self.textEdit)
        self.listaPosibles.setHidden(True)
        self.listaPosibles.setFixedWidth(120)
        self.listaPosibles.setFixedHeight(120)
        self.listaPosibles.setStyleSheet("background:rgb(240, 248, 255)")
        self.listaPosibles.setStyle(QStyleFactory.create('Cleanlooks'))

#Crear el Map Canvas----------------------------------------------------------------------------------------------------
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(QColor(250,250,250))
        self.canvas.enableAntiAliasing(True)
        self.canvas.useImageToRender(False)
        self.canvas.show()

#Agregar el Map canvas al tab1, dentro del marco del tabWidget----------------------------------------------------------
        self.layout = QVBoxLayout(self.frame)
        self.layout.addWidget(self.canvas)

#Create the map tools---------------------------------------------------------------------------------------------------
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionHold)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(self.actionZoom_in)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(self.actionZoom_out)
        self.pan()

#Toolbar Sections-------------------------------------------------------------------------------------------------------
        self.toolBar.addActions([self.actionNew,self.actionOpen,self.actionSave])
        self.toolBar_2.addActions([self.actionUndo_Insert_Action,self.action_Rehacer,self.actionCut,self.actionCopy,self.actionPaste,self.actionDelete])
        self.toolBar_3.addActions([self.actionRun,self.actionLexer,self.actionParser,self.actionCheker])
        self.toolBar_4.addActions([self.actionZoom_in,self.actionZoom_out,self.actionHold])
        self.toolBar_5.addAction(self.actionAbout_CompilerQGisEstratitifcation)



#Signals-----------------------------------------------------------------------------------------------------------------
        self.textEdit.cursorPositionChanged.connect(self.verify)
        self.actionUndo_Insert_Action.triggered.connect(self.undo)
        self.action_Rehacer.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionDelete.triggered.connect(self.delete)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSelect_All.triggered.connect(self.textEdit.selectAll)
        self.actionNew.triggered.connect(self.limipiar)
        self.actionClose.triggered.connect(self.cerrar)
        self.actionQuit.triggered.connect(self.close)
        self.actionLexer.triggered.connect(self.lex)
        self.actionParser.triggered.connect(self.pars)
        self.actionCheker.triggered.connect(self.chek)
        self.actionSave_image.triggered.connect(self.guardarImagen)
        self.actionAbout_language.triggered.connect(self.openALanguage)
        self.actionSave_as.triggered.connect(self.guardarCodeAs)
        self.actionSave.triggered.connect(self.guardar)
        self.listaPosibles.itemActivated.connect(self.capturarSennal)
        self.actionZoom_in.triggered.connect(self.zoomIn)
        self.actionZoom_out.triggered.connect(self.zoomOut)
        self.actionHold.triggered.connect(self.pan)
        self.actionRun.triggered.connect(self.run)
        self.autoCompletamiento.activated.connect(self.autocompletar)
        self.actionAbout_CompilerQGisEstratitifcation.triggered.connect(self.mabout)

#short cut--------------------------------------------------------------------------------------------------------------
        self.actionSelect_All.setShortcut('Ctrl+a')
        self.actionOpen.setShortcut('Ctrl+o')
        self.action_Rehacer.setShortcut('Ctrl+y')
        self.actionSave_as.setShortcut('Ctrl+g')
        self.actionUndo_Insert_Action.setShortcut('Ctrl+z')
        self.actionRun.setShortcut('Ctrl+r')
        self.actionLexer.setShortcut('Ctrl+l')
        self.actionParser.setShortcut('Ctrl+p')
        self.actionCheker.setShortcut('Ctrl+k')
        self.actionSave.setShortcut('Ctrl+s')
        self.actionAbout_language.setShortcut('f2')
        self.actionAbout_CompilerQGisEstratitifcation.setShortcut('f1')
        self.actionNew.setShortcut('Ctrl+n')
        self.actionClose.setShortcut('Ctrl+e')

#tokens Sections--------------------------------------------------------------------------------------------------------
        hlTokens=["No","Kind","Lexeme"]
        headerTokens=QTreeWidgetItem(hlTokens)
        self.treeWidget_2.setHeaderItem(headerTokens)
        self.rootTokens = self.treeWidget_2.invisibleRootItem()
        self.listaTokens=[]

#Errors Sections--------------------------------------------------------------------------------------------------------
        hlErrors=["No","Line number","Kind","Description"]
        headerErrors=QTreeWidgetItem(hlErrors)
        self.treeWidget.setHeaderItem(headerErrors)
        self.rootErrors = self.treeWidget.invisibleRootItem()
        self.errorsL=[]
        self.errorsP=[]
        self.errorsC=[]

     def mabout(self):
         self.va=VistaAbout()
         self.va.show()
     def guardarCodeAs(self):
       file=""
       if str(self.textEdit.toPlainText())!="":
         text = self.textEdit
         file=QFileDialog.getSaveFileName(self, "Save your code into file", "", ".txt")
         if file!="":
            file= open(file, 'w')
            file.write(str(text.toPlainText()))
            file.close()
       if file!="":
           return True
       else:
           return False

     def guardar(self):
        if self.fichero!=None:
          fname = open(self.fichero,'r')
          lines=fname.readlines()
          for line in lines:
              lines.remove(line)
          fname.close()

          fname= open(self.fichero, 'w')
          fname.write(str(self.textEdit.toPlainText()))
          fname.close()

     def openALanguage(self):
         #ruta="C:/Users/Rolando.Morales/.qgis2/python/plugins/compiler/Language.pdf"
         #ruta=":/manuales/AboutLanguage.pdf"
         #os.startfile(ruta)
         pass


     def lex(self):
         texto=self.textEdit.toPlainText()
         if texto!="":
             self.controller.code=texto
             self.controller.analisisLex()

     def pars(self):
         texto=self.textEdit.toPlainText()
         if texto!="":
             self.controller.code=texto
             self.controller.analisisPars()

     def chek(self):
         texto=self.textEdit.toPlainText()
         if texto!="":
             self.controller.code=texto
             self.controller.analisisChek()

     def run(self):
         self.canvas.setLayerSet([])
         texto=self.textEdit.toPlainText()
         if texto!="":
             self.controller.code=texto
             self.controller.run()

     def zoomIn(self):
      self.canvas.setMapTool(self.toolZoomIn)

     def zoomOut(self):
      self.canvas.setMapTool(self.toolZoomOut)

     def pan(self):
      self.canvas.setMapTool(self.toolPan)

     def openFile(self):
         if str(self.textEdit.toPlainText())!="":
          reply = QMessageBox.question(self, 'Confirm open file',"Do you want to save the code?",QMessageBox.Save |QMessageBox.No |QMessageBox.Discard)
          if reply == QMessageBox.Save:
           if self.fichero==None:
              control=self.guardarCodeAs()
              if control==False:
                  return
           else:
            self.guardar()
          elif reply == QMessageBox.Discard:
            return
         filename=""
         filename = QFileDialog.getOpenFileName(self, 'Open File','')
         if filename!="":
          fname = open(filename)
          data = fname.read()
          self.textEdit.setText(data)
          self.fichero=filename
          self.treeWidget.clear()
          self.treeWidget_2.clear()
          self.canvas.setLayerSet([])

     def cargarTokens(self,tokensReconocidos):
         self.treeWidget_2.clear()
         self.listaTokens=[]
         for i in range(0,len(tokensReconocidos)):
            raiz= QTreeWidgetItem(self.rootTokens, [str(i+1),tokensReconocidos[i].kind,tokensReconocidos[i].lexema])
            raiz.setTextColor(2,QColor("Green"))
            raiz.setTextColor(1,QColor("Green"))

     def cargarErrors(self,errorsL,errorsP,errorsC):
         self.treeWidget.clear()
         for i in range(0,len(errorsL)):
            raiz= QTreeWidgetItem(self.rootErrors, [str(i+1),str(errorsL[i][0]),errorsL[i][1].split(":",-1)[0],errorsL[i][1].split(":",-1)[-1]])
            raiz.setTextColor(3,QColor("Red"))
            raiz.setTextColor(2,QColor("Red"))
            raiz.setTextColor(1,QColor("Green"))
         for i in range(0,len(errorsP)):
            raiz= QTreeWidgetItem(self.rootErrors, [str(i+1),str(errorsP[i][0]),errorsP[i][1].split(":",-1)[0],errorsP[i][1].split(":",-1)[-1]])
            raiz.setTextColor(3,QColor("Red"))
            raiz.setTextColor(2,QColor("Red"))
            raiz.setTextColor(1,QColor("Green"))
         for i in range(0,len(errorsC)):
            raiz= QTreeWidgetItem(self.rootErrors, [str(i+1),str(errorsC[i][0]),errorsC[i][1].split(":",-1)[0],errorsC[i][-1].split(":",-1)[-1]])
            raiz.setTextColor(3,QColor("Red"))
            raiz.setTextColor(2,QColor("Red"))
            raiz.setTextColor(1,QColor("Green"))

     def cargarRErrors(self,errors):
         self.treeWidget.clear()
         for i in range(0,len(errors)):
            raiz= QTreeWidgetItem(self.rootErrors, [str(i+1),str(errors[i][0]),errors[i][1].split(":",-1)[0],errors[i][1].split(":",-1)[-1]])
            raiz.setTextColor(3,QColor("Red"))
            raiz.setTextColor(2,QColor("Red"))
            raiz.setTextColor(1,QColor("Green"))
         self.controller.rerrores=[]


     def undo(self):
       self.textEdit.undo()

     def redo(self):
        self.textEdit.redo()

     def cut(self):
         self.textEdit.cut()

     def copy(self):
         self.textEdit.copy()

     def paste(self):
         self.textEdit.paste()

     def delete(self):
         self.textEdit.textCursor().removeSelectedText()

     def cerrar(self):
          if str(self.textEdit.toPlainText())!="":
           reply1 = QMessageBox.question(self, 'Confirm',"Do you want to save the code?",QMessageBox.Save |QMessageBox.No |QMessageBox.Discard)
           if reply1 == QMessageBox.Save:
            if self.fichero==None:
              control=self.guardarCodeAs()
              if control==True:
               self.close()
              else:
                  return
            else:
              self.guardar()
              self.close()
           elif  reply1 == QMessageBox.Discard:
               return
           else:
               self.close()
          else:
              self.close()


     def limipiar(self):
       if str(self.textEdit.toPlainText())!="":
        reply = QMessageBox.question(self, 'Confirm new file',"Do you want to save the code?",QMessageBox.Save |QMessageBox.No |QMessageBox.Discard)
        if reply == QMessageBox.Save:
          if self.fichero==None:
              control=self.guardarCodeAs()
              if control==False:
                  return
          else:
            self.guardar()
        if reply == QMessageBox.Discard:
            return
       self.textEdit.clear()
       self.treeWidget.clear()
       self.treeWidget_2.clear()
       self.canvas.setLayerSet([])
       self.fichero=None

     def adicionarCapa(self,par):
        layerTerritorios=par[0]
        layer=par[1]

        # Agregar el layer al registro
        layerTerritorios.rendererV2().symbol().setColor(QColor(255,255,255))
        QgsMapLayerRegistry.instance().addMapLayer(layer)

        # Fijar el extent al extent del primer layer cargado
        if self.canvas.layerCount() == 0:
            self.canvas.setExtent(layer.extent())
        # Fijar el conjunto de capas (LayerSet) para el map canvas
        layers=[]
        layers.insert(0, QgsMapCanvasLayer(layer))
        layers.insert(1, QgsMapCanvasLayer(layerTerritorios))
        self.canvas.setLayerSet(layers)

     def guardarImagen(self):
        rutaGuardar=""
        rutaguardar=QFileDialog.getSaveFileName(self, "Save map image", "", ".jpg")
        if rutaguardar!="":
         mapRenderer = self.canvas.mapRenderer()
         c = QgsComposition(mapRenderer)
         c.setPlotStyle(QgsComposition.Print)
         dpi = c.printResolution()
         dpmm = (dpi / 25.4)
         width = int(dpmm * c.paperWidth())
         height = int(dpmm * c.paperHeight())
         x, y = 0, 0
         w, h = c.paperWidth(), c.paperHeight()
         composerMap = QgsComposerMap(c, x,y,w,h)
         composerMap.hasFrame() # Does not work with QGIS 1.9-Master. Use hasFrame() instead.
         c.addItem(composerMap)
         # Create output image and initialize it
         image = QImage(QSize(width, height), QImage.Format_ARGB32)
         image.setDotsPerMeterX(dpmm * 1000)
         image.setDotsPerMeterY(dpmm * 1000)
         image.fill(0)
         # Render composition
         imagePainter = QPainter(image)
         sourceArea = QRectF(0, 0, c.paperWidth(), c.paperHeight())
         targetArea = QRectF(0, 0, width, height)
         c.render(imagePainter, targetArea, sourceArea)
         imagePainter.end()
         image.save(rutaguardar)

     def verify(self):
        self.listaPosibles.hide()
        self.textEdit.clearFocus()
        self.textEdit.setFocus(Qt.ActiveWindowFocusReason)
        aux=False
        self.CursorPosition()
        if self.control==True:
         posStart=0
         posEnd=0
         lexema=""
         texto=str(self.textEdit.toPlainText())
         i=0
         while i < len(texto):
            if      texto[i]!='#' and texto[i]!='\n' and texto[i]!=',' \
                    and texto[i]!='=' and texto[i]!='}' \
                    and texto[i]!='{' and texto[i]!=')' \
                    and texto[i]!='(' and texto[i]!=';' \
                    and texto[i]!='[' and texto[i]!=']' \
                    and texto[i]!=':' and not texto[i].isspace():
              posEnd=i
              lexema+=texto[i]
              if kw.__contains__(lexema):
                 self.pintar(posStart,"blue")
              elif td.__contains__(lexema):
                self.pintar(posStart,"red")
              elif lexema.__contains__('"'):

                self.pintarC(posStart,posEnd,lexema)
              else:
                self.pintar(posStart,"negro")

            elif  texto[i]=='#':
                i=self.pintarCom(posStart)
            else:
                 posStart=i+1
                 lexema=""
            i=i+1

     def pintar(self,s,color):
       cursor = self.textEdit.textCursor()
       format = QTextCharFormat()

       cursor.setPosition(int(s))
       if color=="blue":
         format.setForeground(QBrush(QColor("blue")))
       elif color=="red":
         format.setForeground(QBrush(QColor("red")))
       else:
         format.setForeground(QBrush(QColor(0,0,0)))
       self.control=False
       cursor.movePosition(QTextCursor.EndOfWord, 1)
       cursor.mergeCharFormat(format)
       self.textEdit.setCurrentCharFormat(self.format)
       self.control=True

     def pintarC(self,s,e,l):
       cursor = self.textEdit.textCursor()
       format = QTextCharFormat()
       cursor.setPosition(int(s))
       format.setForeground(QBrush(QColor("green")))
       x=int(s)
       while x<=int(e):
         self.control=False
         cursor.movePosition(QTextCursor.NextCharacter, 1)
         cursor.mergeCharFormat(format)
         x=x+1
       self.textEdit.setCurrentCharFormat(self.format)
       self.control=True
       return x

     def pintarCom(self,s):
       cursor = self.textEdit.textCursor()
       format = QTextCharFormat()
       format.setFontItalic(True)
       format.setForeground(QBrush(QColor(176,176,176)))
       cursor.setPosition(int(s))
       x=int(s)
       cursor.setPosition(x)
       self.control=False
       cursor.movePosition(QTextCursor.EndOfLine,1)
       cursor.mergeCharFormat(format)
       self.textEdit.setCurrentCharFormat(self.format)
       self.control=True
       return int(cursor.position())-1

     def CursorPosition(self):
        cursor = self.textEdit.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

     def autocompletar(self):
         self.control=False
         self.listaPosibles.clear()
         posE=self.textEdit.textCursor().position()
         self.textEdit.moveCursor(QTextCursor.StartOfWord,1)
         posS=self.textEdit.textCursor().position()
         word=str(self.textEdit.toPlainText())[posS:posE]
         self.textEdit.moveCursor(QTextCursor.EndOfWord,1)
         posibles=[]
         todo=td+kw
         for posible in todo:
             if posible.__contains__(word):
               posibles.append(posible)
         if len(posibles)>0:
          rect=self.textEdit.cursorRect(self.textEdit.textCursor())
          x=rect.x()
          y=rect.y()
          if self.textEdit.textCursor().position>20:
             x=x-10
          self.listaPosibles.move(x,y+20)
          for posible in posibles:
             item=QListWidgetItem(posible)
             icon =QIcon()
             icon.addPixmap(QPixmap(":/newPrefix/3.png"), QIcon.Normal, QIcon.Off)
             item.setIcon(icon)
             self.listaPosibles.addItem(item)
          self.listaPosibles.setHidden(False)
          posibles=[]
          self.listaPosibles.setFocus()
          self.listaPosibles.show()

     def capturarSennal(self,item):
         self.listaPosibles.hide()
         self.textEdit.clearFocus()
         self.textEdit.setFocus(Qt.ActiveWindowFocusReason)
         self.textEdit.moveCursor(QTextCursor.StartOfWord,1)
         self.textEdit.textCursor().removeSelectedText()
         self.control=True
         self.textEdit.textCursor().insertText(item.text())
         self.textEdit.moveCursor(QTextCursor.EndOfWord,1)




if __name__ == '__main__':
        import sys
        app = QApplication(sys.argv)
        NuclearMotionWidget = VistaCompilador()
        NuclearMotionWidget.showMaximized()
        sys.exit(app.exec_())
