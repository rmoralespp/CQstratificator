__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-
from Lexer import Lexer
from AST import *



class Parser:
    def __init__(self):
        self.input=None
        self.errores=[]
        self.tokenActual=None
        self.tokensReconocidos=[]


#METODO PARA PASAR AL SIGUIENTE TOKEN-----------------------------------------------------------------------------------
    def consume(self):
        self.tokenActual = self.input.nextToken()

#METODO PARA COMPROBAR SI EL TOKEN ACTUAL ES EL CORRECTO----------------------------------------------------------------
    def  match(self,tk_expected):
        if tk_expected == self.tokenActual.kind:
            self.tokensReconocidos.append(self.tokenActual)
            self.consume()
        else:
          self.errores.append((self.tokenActual.line, "Sintax error: It was excepted the token %s and was found the token %s"%(tk_expected,self.tokenActual.kind)))

#METODO PARA PASAR DE TOKEN  SI EL TOKEN ACTUAL NO ES EL CORRECTO-------------------------------------------------------
    def recuperate(self,tk_expected):
        while self.tokenActual.kind != tk_expected and  self.tokenActual.kind != "tk_eot":
            self.consume()
        self.consume()


#METODOS PARA  COMPROBAR SI ES CORRECTO EL CODIGO ENTRADO POR EL USUARIO A PARTIR DE LA GRAMATICA DEL LENGUAJE----------

#<program>->tk_main tk_lparent tk_rparent tk_twoPoints tk_layer tk_ twoPoints tk_literalString tk_semiColon <instructions>
    def  programa(self):
        self.match("tk_main")
        self.match("tk_lparent")
        self.match("tk_rparent")
        self.match("tk_dosPuntos")
        self.match("tk_layer")
        self.match("tk_dosPuntos")
        tk_layer=self.tokenActual
        self.match("tk_literalCadena")
        self.match("tk_puntoComa")
        lista = self.instrucciones()
        return  ASTPrograma (lista, self.tokenActual.line,tk_layer)

#<instructions> -> <instruction> tk_ semiColon <moreInstruction>--------------------------------------------------------
    def instrucciones(self):
        lista=[]
        instrucion = self.instruccion()
        self.match("tk_puntoComa")
        lista.append(instrucion)
        lista=lista+self.Mas_Instruction()
        return lista

#<instruction> -> <asignation> | <declaration> | <impresion>------------------------------------------------------------
    def instruccion(self):
        aux=None
        if self.tokenActual.kind=="tk_qcolor" or self.tokenActual.kind=="tk_qlist" or self.tokenActual.kind=="tk_qinteger" or self.tokenActual.kind=="tk_qstrata" or self.tokenActual.kind=="tk_qstring":
           aux=self.declaracion()
        elif self.tokenActual.kind=="tk_identificador":
            aux=self.asignacion()
        elif self.tokenActual.kind=="tk_paint":
            aux=self.impresion()
        return aux

#<moreInstruction> -> e|<instructions>----------------------------------------------------------------------------------
    def Mas_Instruction(self):
      lista=[]
      if self.tokenActual.kind!="tk_eot" and self.tokenActual.kind!="tk_qcolor" and self.tokenActual.kind!="tk_qlist" and self.tokenActual.kind!="tk_qinteger" and self.tokenActual.kind!="tk_qstrata" and self.tokenActual.kind!="tk_qstring" and self.tokenActual.kind!="tk_paint" and self.tokenActual.kind!="tk_identificador":
         self.errores.append((self.tokenActual.line, "Sintax error: Ilegal instruction"))
         self.recuperate("tk_puntoComa")
      while self.tokenActual.kind!="tk_eot":
            lista.append(self.instruccion())
            self.match("tk_puntoComa")
            lista=lista+(self.Mas_Instruction())
      return lista

#<declaration> -> <kind><ids>-------------------------------------------------------------------------------------------
#<kind> -> tk_qstring |tk_qinteger |tk_qlist|tk_qcolor|tk_qstrata
    def declaracion(self):
        tipo = "None"
        if self.tokenActual.kind=="tk_qstring":
            tipo = "qstring"
            self.match("tk_qstring")
        elif self.tokenActual.kind=="tk_qcolor":
            tipo = "qcolor"
            self.match("tk_qcolor")
        elif self.tokenActual.kind=="tk_qstrata":
            tipo = "qstrata"
            self.match("tk_qstrata")
        elif self.tokenActual.kind=="tk_qlist":
            tipo = "qlist"
            self.match("tk_qlist")
        elif self.tokenActual.kind=="tk_qinteger":
            tipo = "qinteger"
            self.match("tk_qinteger")
        ids=self.ids()
        return  ASTDeclaracion(self.tokenActual.line,tipo, ids)

#<ids> -> tk_identificator <moreId>-------------------------------------------------------------------------------------
    def ids(self):
        if self.tokenActual.kind=="tk_identificador":
            id = ASTIdentifierDeclaration(self.tokenActual.lexema,self.tokenActual.entry, self.tokenActual.line)
            self.match("tk_identificador")
            return self.masIds(id)
        else :
            self.errores.append((self.tokenActual.line, "Sintax error: He expected an identifier "))
            return []

#<moreId> -> tk_colon <ids> | e-----------------------------------------------------------------------------------------
    def masIds(self,id):
        ides=[]
        ides.append(id)
        if (self.tokenActual.kind == "tk_coma"):
            self.match("tk_coma")
            ides=ides+self.ids()
            return ides
        else:
            return ides


#<asignation> -> tk_identificator tk_asignation <value>-----------------------------------------------------------------
    def asignacion(self):
        id =  ASTIdentifierReference(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
        self.match("tk_identificador")
        self.match("tk_asignacion")
        valor = self.operando()
        return  ASTAsignacion(self.tokenActual.line, id, valor)


#<value> -> tk_identificator | tk_literalInteger| tk_literalString |<color> |<strata> |<list>---------------------------
    def operando(self):
        term=None
        if self.tokenActual.kind=="tk_identificador":
           term=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
           self.match("tk_identificador")
        elif self.tokenActual.kind=="tk_literalEntero":
           term=ASTIntValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
           self.match("tk_literalEntero")
        elif self.tokenActual.kind=="tk_literalCadena":
           term=ASTCadenaValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
           self.match("tk_literalCadena")
        elif self.tokenActual.kind=="tk_lcorchete":
           self.match("tk_lcorchete")
           lista=self.valuesLista()
           term=ASTListValue(lista,self.tokenActual.entry,self.tokenActual.line)
           self.match("tk_rcorchete")
        elif self.tokenActual.kind=="tk_lparent":
           term=self.color()
        elif self.tokenActual.kind=="tk_lkey":
           term=self.estrato()
        else:
            self.errores.append((self.tokenActual.line, "Sintax error: Invalid assignment"))
            self.recuperate("tk_puntoComa")
        return term


#<color> -> tk_lparent <valueList> tk_colon <valueList> tk_colon <valueList> tk_rparent---------------------------------
    def color(self):
            r=None
            g=None
            b=None
            self.match("tk_lparent")
            if self.tokenActual.kind=="tk_literalEntero":
             r=ASTIntValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_literalEntero")
            elif self.tokenActual.kind=="tk_identificador":
             r=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_identificador")
            else:
             self.errores.append((self.tokenActual.line, "Sintax error: He expected an qinteger"))
             self.recuperate("tk_puntoComa")
            self.match("tk_coma")


            if self.tokenActual.kind=="tk_literalEntero":
             g=ASTIntValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_literalEntero")
            elif self.tokenActual.kind=="tk_identificador":
             g=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_identificador")
            else:
             self.errores.append((self.tokenActual.line, "Sintax error: He expected an qinteger"))
             self.recuperate("tk_puntoComa")
            self.match("tk_coma")


            if self.tokenActual.kind=="tk_literalEntero":
             b=ASTIntValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_literalEntero")
            elif self.tokenActual.kind=="tk_identificador":
             b=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_identificador")
            else:
             self.errores.append((self.tokenActual.line, "Sintax error: He expected an qinteger"))
             self.recuperate("tk_puntoComa")
            self.match("tk_rparent")
            if r!=None and g!=None and b!=None:
             return ASTColorValue((r,g,b),self.tokenActual.entry,self.tokenActual.line)
            else:
             return None

#<strata> -> tk_lkey tk_e_name tk_ twoPoints <valueName> tk_ colon tk_e_color tk_twoPoints <valueColor> tk_colon tk_e_territories tk_ twoPoints <valueT> tk_rkey
#<valueName> -> tk_identificator| tk_LiteralString
#<valueColor> -> <color>| tk_identificator
#<valueT> -> <list>| tk_identificator
    def estrato(self):
            nombre=None
            color=None
            territorios=None
            self.match("tk_lkey")
            self.match("tk_e_name")
            self.match("tk_dosPuntos")

            if self.tokenActual.kind=="tk_literalCadena":
             nombre=ASTCadenaValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_literalCadena")
            elif self.tokenActual.kind=="tk_identificador":
             nombre=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_identificador")
            else:
             self.errores.append((self.tokenActual.line, "Sintax error: He expected an qstring"))
             self.recuperate("tk_puntoComa")

            self.match("tk_coma")
            self.match("tk_e_color")
            self.match("tk_dosPuntos")

            if self.tokenActual.kind=="tk_identificador":
             color=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_identificador")
            elif self.tokenActual.kind=="tk_lparent":
             color=self.color()
            else:
             self.match("tk_lparent")

            self.match("tk_coma")
            self.match("tk_e_territories")
            self.match("tk_dosPuntos")

            if self.tokenActual.kind=="tk_identificador":
             territorios=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
             self.match("tk_identificador")
            elif self.tokenActual.kind=="tk_lcorchete":
              self.match("tk_lcorchete")
              lista=self.valuesLista()
              territorios=ASTListValue(lista,self.tokenActual.entry,self.tokenActual.line)
              self.match("tk_rcorchete")
            self.match("tk_rkey")
            if nombre!=None and color!=None and territorios!=None:
             return ASTEstratoValue(nombre,color,territorios,self.tokenActual.entry,self.tokenActual.line)
            else:
             return None


#<moreValueList > -> tk_colon <list>|e----------------------------------------------------------------------------------
    def MasvalueLista(self,value):
        values=[]
        values.append(value)
        if self.tokenActual.kind == "tk_coma":
            self.match("tk_coma")
            values=values+self.valuesLista()
            return values
        else:
            return values


#<list> -> <valueList> <moreValueList>----------------------------------------------------------------------------------
#<valueList> -> tk_identificator|tk_literalInteger
    def valuesLista(self):
        if self.tokenActual.kind=="tk_literalEntero":
           value=ASTIntValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
           self.match("tk_literalEntero")
           return self.MasvalueLista(value)

        elif self.tokenActual.kind=="tk_identificador":
            value=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
            self.match("tk_identificador")
            return self.MasvalueLista(value)
        else :
            self.errores.append((self.tokenActual.line, "Sintax error: He expected an qinteger"))
            return []

#<impresion> -> tk_paint tk_lparent <valuesImpresion> tk_rparent--------------------------------------------------------
    def impresion(self):
        self.match("tk_paint")
        self.match("tk_lparent")
        values=self.valuesImpresion()
        return ASTImpresion(self.tokenActual.line,values)

#<valuesImpresion> -> <valueImpresion> <moreValueImpresion>-------------------------------------------------------------
    def valuesImpresion(self):
        if self.tokenActual.kind=="tk_identificador":
           id=ASTIdentifierValue(self.tokenActual.lexema,self.tokenActual.entry,self.tokenActual.line)
           self.match("tk_identificador")
           return self.MasValueImpresion(id)

        elif self.tokenActual.kind=="tk_lkey":
            return self.MasValueImpresion(self.estrato())

        else :
            self.errores.append((self.tokenActual.line, "Sintax error: Ilegal expresion"))
            self.recuperate("tk_puntoComa")
            return []

# <moreValueImpresion> -> tk_ colon <valuesImpresion>|e-----------------------------------------------------------------
# <valueImpresion> -> tk_identificator| <strata>
    def MasValueImpresion(self,id):
        ids=[]
        ids.append(id)

        if self.tokenActual.kind == "tk_coma":
            self.match("tk_coma")
            res=self.valuesImpresion()
            if res!=None:
             ids=ids+res
            return ids
        elif self.tokenActual.kind == "tk_rparent":
            self.match("tk_rparent")
            return ids
