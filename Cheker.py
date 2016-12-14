__author__ = 'Rolando.Morales'

from Parser import *
from AST import *
from SymbolsTable import *

class Cheker(Visitor):

    def __init__(self):
        Visitor.__init__(self)
        self.errores=[]
        self.parser=Parser()
        self.st=None



#METODO PARA RECORRER TODAS LAS INSTRUCCIONES---------------------------------------------------------------------------
    def visitPrograma(self,programa):
      if programa!=None:
        for i in range(0,len(programa.lista)):
           if programa.lista[i]!=None:
             programa.lista[i].visit(self)
        return None


#METODO PARA VISITAR LOS IDENTIFICADORES DE UNA DECLARACION-------------------------------------------------------------
    def visitDeclaracion(self,astDeclaracion):
       if astDeclaracion!=None:
          ids=astDeclaracion.ids
          for id in ids:
           if id!=None:
            id.visit(self)
            info=self.st.entry(id.entry)
            info.type=astDeclaracion.tipo
          return

#METODO PARA COMPROBAR SI EL IDENTIFICADOR DE UNA ASIGNACION ES DEL MISMO TIPO DE DATO QUE EL DEL VALOR K LE FUE ASIGNADO
    def visitAsignacion(self,astAsignacion):
      if astAsignacion.valor!=None and astAsignacion.id!=None :
        t1=self.visitIdentifierReference(astAsignacion.id)
        t2=None
        if astAsignacion.valor.tipo=="id":
            t2=self.visitIdentifierValue(astAsignacion.valor)

        elif astAsignacion.valor.tipo=="int":
            t2=self.visitIntValue(astAsignacion.valor)

        elif astAsignacion.valor.tipo=="cadena":
            t2=self.visitCadenaValue(astAsignacion.valor)

        elif astAsignacion.valor.tipo=="color":
            t2=self.visitColorValue(astAsignacion.valor)

        elif astAsignacion.valor.tipo=="list":
            t2=self.visitListValue(astAsignacion.valor)

        elif astAsignacion.valor.tipo=="estrato":
            t2=self.visitEstratoValue(astAsignacion.valor)
        if t1!=t2:
            self.errores.append((astAsignacion.line,"Semantic error: Assignment of incompatible types"))
            return "None"
        else:

            return t1

#METODO PARA RETORNAR EL TIPO DE DATO DE UN LITERAL CADENA--------------------------------------------------------------
    def visitCadenaValue(self,astCadenaValue):
        return "qstring"


#METODO PARA RETORNAR EL TIPO DE DATO DE UN LITERAL ENTERO--------------------------------------------------------------
    def visitIntValue(self,astIntValue):
        return "qinteger"



#METODO PARA COMPROBAR SI TODOS LOS ELEMENTOS DE UNA LISTA SON DEL TIPO DE DATO CORRECTO Y PARA RETORNAR EL TIPO DE DATO CORRESPONDIENTE
    def visitListValue(self,astListValue):
      control=False
      tipo="None"
      if astListValue.lista!=None:
        for item in astListValue.lista:
         if item!=None:
          if item.tipo=="id":
            tipo=self.visitIdentifierValue(item)
          else:
            tipo=self.visitIntValue(item)
          if tipo!="qinteger":
              self.errores.append((astListValue.line,"Semantic error: Assignment of incompatible types"))
              control=True
        if control==False:
         tipo= "qlist"
      return tipo

#METODO PARA COMPROBAR SI TODOS LOS ELEMENTOS DE UN ESTRATO SON DEL TIPO DE DATO CORRECTO Y PARA RETORNAR EL TIPO DE DATO CORRESPONDIENTE
    def visitEstratoValue(self,astEstrato):
        control=False
        tipo="None"
        if astEstrato!=None:
            if astEstrato.nombre.tipo=="cadena":
                self.visitCadenaValue(astEstrato.nombre)
            else:
                tipo=self.visitIdentifierValue(astEstrato.nombre)
                if tipo!="qstring":
                      control=True
            if astEstrato.color.tipo=="id":
                 tipo=self.visitIdentifierValue(astEstrato.color)
            else:
                 tipo=self.visitColorValue(astEstrato.color)
                 if tipo!="qcolor":
                      control=True

            if astEstrato.territorios.tipo=="list":
                tipo=self.visitListValue(astEstrato.territorios)
            else:
                tipo=self.visitIdentifierValue(astEstrato.territorios)

                if tipo!="qlist":
                      control=True
            if control==False:
                tipo= "qstrata"
        return tipo


#METODO PARA COMPROBAR SI TODOS LOS ELEMENTOS DE UN COLOR SON DEL TIPO DE DATO CORRECTO Y PARA RETORNAR EL TIPO DE DATO CORRESPONDIENTE
    def visitColorValue(self,astcolor):
      control=False
      tipo="None"
      if astcolor.color!=None:
        for item in astcolor.color:
         if item!=None:
          if item.tipo=="id":
            tipo=self.visitIdentifierValue(item)
          else:
            tipo=self.visitIntValue(item)
          if tipo!="qinteger":
              self.errores.append((astcolor.line,"Semantic error: Assignment of incompatible types"))
              control=True
        if control==False:
         tipo= "qcolor"
      return tipo


#METODO PARA VERIFICAR SI UN IDENTIFICARDOR INICIAIZADO FUE DELCARADO---------------------------------------------------
    def visitIdentifierReference(self,identifierReference):
      if identifierReference!=None:
        info=self.st.entry(identifierReference.entry)
        if info.declared==True:
          info.init=True
          return info.type
        else:
         self.errores.append((identifierReference.line,"Semantic error: Using the variable %s not be declared"%info.lexeme))
         return "None"


#METODO PARA VERIFICAR SI UN IDENTIFICADOR DECLARADO NO HA SIDO DECLARADO ANTERIORMENTE---------------------------------
    def visitIdentifierDeclaration(self,identifierDeclaration):
       if identifierDeclaration!=None:
        info=self.st.entry(identifierDeclaration.entry)
        if info.declared==True:
            self.errores.append((identifierDeclaration.line,"Semantic error: The Variable %s already been declared"%info.lexeme))
        else:
         info.declared=True
        return


#METODO PARA VERIFICAR SI UN IDENTIFICADOR QUE ESTA SIENDO UTILIZADO COMO VALOR FUE DECLARO E INICILAIZADO--------------
    def visitIdentifierValue(self,astIdentifierValue):
      if astIdentifierValue!=None:
        info=self.st.entry(astIdentifierValue.entry)
        tipodatos=info.type
        if info.declared==False:
            tipodatos="None"
            self.errores.append((astIdentifierValue.line,"Semantic error: The Variable %s has not been declared"%info.lexeme))
        if  info.init==False:
            self.errores.append((astIdentifierValue.line,"Semantic error: Using Variable %s not be initialized"%info.lexeme))
        return tipodatos



#METODO PARA COMPROBAR SI TODOS LOS ELEMENTOS A REPRESENTAR SON ESTRATOS------------------------------------------------
    def visitImpresion(self,astImpresion):
        if astImpresion!=None:
          if astImpresion.estratos!=None:
            for item in astImpresion.estratos:
                if item.tipo=="id":
                    tipo=self.visitIdentifierValue(item)
                    if tipo!="qstrata":
                            self.errores.append((astImpresion.line,"Semantic error: Assignment of incompatible types"))
                else:
                    tipo=self.visitEstratoValue(item)
                    if tipo!="qstrata":
                            self.errores.append((astImpresion.line,"Semantic error: Assignment of incompatible types"))


