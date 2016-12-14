__author__ = 'jess'


from qgis.utils import iface
import qgis.core
from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import qgis
import math


class Visualizacion(QObject):

    def __init__(self,estratos,nombrelayerBase,c):
        QObject.__init__(self)
        self.c=c
        self.estratos=estratos
        self.nombrelayerBase=nombrelayerBase
        self.layerBase=None
        self.errores=self.c.rerrores
        self.validarCapa()
        self.validarTerritorios()
        self.validarColores()
        self.territoriosMultipoligono=[]
        self.categoriasCapa={}


#Metodo para crear la capa----------------------------------------------------------------------------------------------
    def crearCapa(self):

     mem_layer = qgis.core.QgsVectorLayer("Polygon?crs=epsg:4326&field=Id:integer""&field=Estrato&index=yes","CQESTRATIFICATOR","memory")
     mem_layer.startEditing()
     cont=0
     for estrato in self.estratos:
      for territorio in estrato["territorios"]:
        points=self.getGeometria(int(territorio))
        if len(points)>0:
         feature = qgis.core.QgsFeature()
         if self.territoriosMultipoligono.__contains__(int(territorio)):
           feature.setGeometry(qgis.core.QgsGeometry.fromMultiPolygon(points))
         else:
          feature.setGeometry(qgis.core.QgsGeometry.fromPolygon(points))
         feature.setAttributes([territorio,estrato["nombre"]])
         mem_layer.addFeature(feature, True)
      cont+=1

      #stop editing and save changes
     mem_layer.commitChanges()
     return mem_layer

#Metodo para obtener la lista de puntos de un territorio(poligono)------------------------------------------------------
    def getGeometria(self,id):
        featuresAux=""
        geom=[]
        territorios = self.layerBase.getFeatures()
        for feature in territorios:

            if id==feature.id():

             featuresAux=feature

        if featuresAux!="":
         if  featuresAux.geometry().isMultipart():
                 self.territoriosMultipoligono.append(id)
                 geom = featuresAux.geometry().asMultiPolygon()
         elif featuresAux.geometry().type() == QGis.Polygon:
                geom = featuresAux.geometry().asPolygon()  #Lista QgsPoint(x,y)
         return geom
        return []

#Metodo para dibujar cada uno de los territorios(poligonos) en base al color de sus estratos----------------------------
    def run(self):
       if self.errores==[]:
        capa=self.crearCapa()
        categories = []
        for i in range(len(self.estratos)):
          for territorio in self.estratos[i]["territorios"]:
            symbol = QgsSymbolV2.defaultSymbol(capa.geometryType())
            symbol.setColor(QColor(self.validarColor(self.estratos[i]["color"])))
            category = QgsRendererCategoryV2(territorio, symbol,"%s" %territorio)
            categories.append(category)
            self.categoriasCapa[territorio]=category

        expression = 'id'
        renderer = QgsCategorizedSymbolRendererV2(expression, categories)
        capa.setRendererV2(renderer)
        self.emit(self.c.vp.signal,(self.layerBase,capa))

       else:
          errores=self.errores
          self.errores=[]
          self.c.rerrores=errores
          self.emit(self.c.vp.signalE,errores)


#METODOS PARA VALIDAR SI LA CAPA, LOS TERRITORIOS Y LOS COLORES ESTABLECIDOS SON CORRECTOS------------------------------

    def validarColor(self,colorI):
        control=True
        if int(colorI[0])<0 or int(colorI[0])>255:
            control=False
        if int(colorI[1])<0 or int(colorI[1])>255:
            control=False
        if int(colorI[2])<0 or int(colorI[2])>255:
            control=False
        if control==True:
         colorO=QColor(int(colorI[0]),int(colorI[1]),int(colorI[2]))
         return colorO
        else:
          return None

    def validarTerritorios(self):
        total=[]

        if self.errores==[]:
           control=True
           for estrato in self.estratos:
             for  t in estrato["territorios"]:
              if self.contains(t)==False:
                  control=False
                  break
              else:
                if total.__contains__(int(t)):
                    control=False

                    break
                else:
                    total.append(int(t))
           if control==False:
               self.errores.append((-1,"Runtime error: Invalid territories"))

    def validarColores(self):
         if self.errores==[]:
           control=True
           for estrato in self.estratos:
              if self.validarColor(estrato["color"])==None:
                  control=False
                  break
           if control==False:
               self.errores.append((-1,"Runtime error: Invalid color"))

    def validarCapa(self):
       control=False
       capa=None
       layerArray =[]
       for layer in iface.mapCanvas().layers():
          if layer.wkbType()==QGis.WKBPolygon or layer.wkbType()==QGis.WKBMultiPolygon:
             layerArray.append(layer)

       for layer in layerArray:
           if self.nombrelayerBase==layer.name():
               control=True
               capa=layer
               break
       if control==True:
           self.layerBase=capa
       else:
           self.errores.append((-1,"Runtime error: Invalid name layer"))

    def contains(self,id):
           control=False

           for idF in self.layerBase.getFeatures():
                 if int(id)==int(idF.id()):
                     control=True
                     break

           if control==True:
               return True
           else:
               return False


















