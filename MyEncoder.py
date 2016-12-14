__author__ = 'Rolando.Morales'
from AST import Visitor

class MyEncoder(Visitor):
    def __init__(self):
        Visitor.__init__(self)
        self.store={}
        self.st=None
        self.estratos=[]
        self.errores=[]
        self.nlayer=None


#METODO PARA VISITAR TODAS LAS INSTRUCCIONES----------------------------------------------------------------------------
    def visitPrograma(self,programa):
        self.nlayer=programa.nlayer.lexema
        for i in range(0,len(programa.lista)):
             programa.lista[i].visit(self)



#METODO PARA VISITAR LOS VARIABLES DE UNA DELCARACION-------------------------------------------------------------
    def visitDeclaracion(self,astDeclaracion):
          ids=astDeclaracion.ids
          for id in ids:
            id.visit(self)

#METODO PARA REGISTRAR O ACTUALIZAR EN EL STORE EL VALOR DE UNA VARIABLE------------------------------------------------
    def visitAsignacion(self,astAsignacion):
        key=self.visitIdentifierReference(astAsignacion.id)
        key="%s"%key

        if astAsignacion.valor.tipo=="id":
            valor=self.visitIdentifierValue(astAsignacion.valor)
            self.store[key]=valor

        elif astAsignacion.valor.tipo=="int":
            valor=self.visitIntValue(astAsignacion.valor)
            self.store[key]=valor

        elif astAsignacion.valor.tipo=="cadena":
            valor=self.visitCadenaValue(astAsignacion.valor)
            self.store[key]=valor

        elif astAsignacion.valor.tipo=="color":
            valor=self.visitColorValue(astAsignacion.valor)
            self.store[key]=valor


        elif astAsignacion.valor.tipo=="list":
            valor=self.visitListValue(astAsignacion.valor)
            self.store[key]=valor

        elif astAsignacion.valor.tipo=="estrato":
            valor=self.visitEstratoValue(astAsignacion.valor)
            self.store[key]=valor





#METODO PARA RETORNAR EL VALOR DE UN LITERAL CADENA---------------------------------------------------------------------
    def visitCadenaValue(self,astCadenaValue):
        info=self.st.entry(astCadenaValue.entry)
        return info.lexeme


#METODO PRA RETORNAR EL VALOR DE UN LITERAL ENTERO----------------------------------------------------------------------
    def visitIntValue(self,astIntValue):
        info=self.st.entry(astIntValue.entry)
        return info.lexeme




#METODO PARA VISITAR TODOS LOS ELEMENTOS DE UNA LISTA Y RETORNAR LOS VALORES DE LA MISMA--------------------------------
    def visitListValue(self,astListValue):
        valores=[]
        for item in astListValue.lista:
          if item.tipo=="id":
            valor=self.visitIdentifierValue(item)
            valores.append(valor)
          else:
            valor=self.visitIntValue(item)
            valores.append(valor)
        return valores


#METODO PARA VISITAR TODOS LOS ELEMENTOS DE UN ESTRATO Y RETORNAR LOS VALORES DE LEL MISMO------------------------------
    def visitEstratoValue(self,astEstrato):
            valores={}
            if astEstrato.nombre.tipo=="cadena":
                valor=self.visitCadenaValue(astEstrato.nombre)
                valores["nombre"]=valor
            else:
                valor=self.visitIdentifierValue(astEstrato.nombre)
                valores["nombre"]=valor

            if astEstrato.color.tipo=="id":
                 valor=self.visitIdentifierValue(astEstrato.color)
                 valores["color"]=valor
            else:
                valor=self.visitColorValue(astEstrato.color)
                valores["color"]=valor

            if astEstrato.territorios.tipo=="list":

                valor=self.visitListValue(astEstrato.territorios)
                valores["territorios"]=valor
            else:
               valor=self.visitIdentifierValue(astEstrato.territorios)
               valores["territorios"]=valor
            return valores

#METODO PARA VISITAR TODOS LOS ELEMENTOS DE UN COLOR Y RETORNAR LOS VALORES DEL MISMO-----------------------------------
    def visitColorValue(self,astcolor):
        valores=[]
        for item in astcolor.color:
          if item.tipo=="id":
            valor=self.visitIdentifierValue(item)
            valores.append(valor)
          else:
            valor=self.visitIntValue(item)
            valores.append(valor)
        return valores


#METODO PARA RETORNAR LA VARIABLE DE UNA ASIGNACION---------------------------------------------------------------------
    def visitIdentifierReference(self,identifierReference):
        info=self.st.entry(identifierReference.entry)
        return info.lexeme


#METODO PARA ADICIONAR AL STORE UNA NUEVA VARIABLE----------------------------------------------------------------------
    def visitIdentifierDeclaration(self,identifierDeclaration):
        info=self.st.entry(identifierDeclaration.entry)
        self.store["%s"%info.lexeme]=None


#METODO PARA RETORNAR EL VALOR DE UNA VARIABLE ALMACENADA EN EL STORE---------------------------------------------------
    def visitIdentifierValue(self,astIdentifierValue):
        info=self.st.entry(astIdentifierValue.entry)
        return self.store["%s"%info.lexeme]


#METODO PARA VISITAR CADA UNO DE LOS ESTRATOS A REPRESENTAR Y ADICIONARLOS A LA LISTA DE ESTRATOS-----------------------
    def visitImpresion(self,astImpresion):
        for item in astImpresion.estratos:
            if item.tipo=="id":
                valor=self.visitIdentifierValue(item)
                self.estratos.append(valor)
            else:
                valor=self.visitEstratoValue(item)
                self.estratos.append(valor)





