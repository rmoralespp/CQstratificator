__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from Keywords import *
from Token import *
from SymbolsTable import *
import re


class Lexer:

    def __init__(self,st):
        self.texto=None
        self.numeroLinea=1
        self.caracter=None
        self.errores=[]
        self.symbolsTable=st
        self.posicion=0
        self.start=-2
        self.end=-2
        self.patron=re.compile('[a-zA-Z]*[0-9]*')


#METODO PARA PASAR AL SIGUENTE CARACTER---------------------------------------------------------------------------------
    def consume(self):
         if self.caracter=='\n':
            self.numeroLinea+=1
         self.posicion+=1
         if self.posicion<len(self.texto):
          self.caracter=str(self.texto[self.posicion])
         else:
          self.caracter='\0'




#METODO PARA DESCARCATAR CARACTERES, COMO ESPACIOS, CAMBIOS DE LINEA, ETC-----------------------------------------------
    def WS(self):
        while self.caracter==' ' or self.caracter=='\t' or self.caracter=='\n' or self.caracter=='\r':
            self.consume()

#METODO PARA COMPROBAR SI DE LOS CARACTERES ACTUALES SE PODRIA FORMAR UN NUMERO ENTERO----------------------------------
    def literalEntero(self):
        lexema=""
        while self.caracter.isdigit():
            lexema+=str(self.caracter)
            self.consume()
        token=Token("","","tk_literalEntero",lexema, self.numeroLinea,self.symbolsTable.add(lexema,"tk_literalEntero"))
        return token

#METODO PARA DESCARTAR UN COMENTARIO DE UNA LINEA-----------------------------------------------------------------------
    def literalComentario(self):
        while self.caracter!='\n' and self.caracter!='\0':
            self.consume()

#METODO PARA DESCARTAR UN COMENTARIO MULTILINEA-------------------------------------------------------------------------
    def literalMultiComentario(self):
        lexema=""
        self.consume()
        if self.caracter=='*':
         while self.caracter!='*' and self.caracter!='\0':
            lexema+=str(self.caracter)
            self.consume()

         if  self.caracter=='*':
             #self.consume()
             #if self.caracter=='/':
              return None
             #else:
               # self.errores.append((self.numeroLinea,"Error lexico: comentario no valido"))
               # token=Token("","","tk_error","comentario no valido %s"%lexema, self.numeroLinea,"")
               # return token
         else:
             self.errores.append((self.numeroLinea,"Error lexico: comentario no valido"))
             token=Token("","","tk_error","comentario no valido %s"%lexema, self.numeroLinea,"")
             return token
        else:
         self.errores.append((self.numeroLinea,"Error lexico: caracter no valido %s"%self.caracter))
         token=Token("","","tk_error","caracter no valido %s"%lexema, self.numeroLinea,"")
         self.consume()
         return token


#METODO PARA COMPROBAR SI DE LOS CARACTERES ACTUALES SE PODRIA FORMAR UNA CADENA DE TEXTO-------------------------------
    def literalCadena(self):
        lexema=""
        while  self.caracter!='"' and self.caracter!='\0'and self.caracter!='\n':
          lexema+=str(self.caracter)
          self.consume()
        if self.caracter!='\0' and self.caracter!='\n':
         self.consume()
         if self.patron.match(lexema):
          token=Token("","","tk_literalCadena",lexema, self.numeroLinea,self.symbolsTable.add(lexema,"tk_literalCadena"))
          return  token
         else:
          token=Token("","","tk_error","cadena no valida", self.numeroLinea,-1)
          self.errores.append((self.numeroLinea,"Lexical error: Invalid qstring %s"%lexema))
          return  token
        else:
          token=Token("","","tk_error","cadena no valida", self.numeroLinea,-1)
          self.errores.append((self.numeroLinea,"Lexical error: Invalid qstring %s"%lexema))
          return token




#METODO PARA COMPROBAR SI EL CONJUNTO DE CARACTERES ACTUALES ES UNA PALABRA RESERVADA O UN IDENTIFICADOR----------------
    def ID(self):
        lexema=""
        while  self.caracter.isdigit() or self.caracter.isalpha() or self.caracter=='_':
            lexema+=str(self.caracter)
            self.consume()
        if keywordsTable.keys().__contains__(lexema):
            kind=keywordsTable[lexema]
            token=Token("","",kind,lexema, self.numeroLinea,self.symbolsTable.add(lexema,kind))
        else:
            token=Token("","","tk_identificador",lexema, self.numeroLinea,self.symbolsTable.add(lexema,"tk_identificador"))
        return token


#METODO PRINCIPAL DE LA CLASE PARA BUSCAR EL PROXIMO TOKEN Y RETORNARLO-------------------------------------------------
    def nextToken(self):

       while  self.caracter != '\0' :
         if self.caracter==' ' or self.caracter=='\t' or self.caracter=='\n' or  self.caracter=='\r':
             self.WS()

         elif self.caracter=="(":
           self.consume()
           token=Token("","","tk_lparent","(", self.numeroLinea,-1)
           return token


         elif self.caracter==")":
           self.consume()
           token=Token("","","tk_rparent",")", self.numeroLinea,-1)
           return token

         elif self.caracter=="{":
           self.consume()
           token=Token("","","tk_lkey","{", self.numeroLinea,-1)
           return token


         elif self.caracter=="}":
           self.consume()
           token=Token("","","tk_rkey","}", self.numeroLinea,-1)
           return token

         elif self.caracter=="[":
           self.consume()
           token=Token("","","tk_lcorchete","}", self.numeroLinea,-1)
           return token

         elif self.caracter=="]":
           self.consume()
           token=Token("","","tk_rcorchete","}", self.numeroLinea,-1)
           return token

         elif self.caracter==";":
           self.consume()
           token=Token("","","tk_puntoComa",";", self.numeroLinea,-1)
           return token

         elif self.caracter==",":
           self.consume()
           token=Token("","","tk_coma",",", self.numeroLinea,-1)
           return token


         elif self.caracter==":":
           self.consume()
           token=Token("","","tk_dosPuntos",":", self.numeroLinea,-1)
           return token

         elif self.caracter=="=":
           self.consume()
           token=Token("","","tk_asignacion","=", self.numeroLinea,-1)
           return token

         elif self.isLetter():
             return self.ID()

         elif self.isDigit():
             return self.literalEntero()

         elif self.caracter=='#':
              self.literalComentario()

         elif self.caracter=='/':
               control=self.literalMultiComentario()
               if control!=None:
                   return control

         elif self.caracter=='"':
             self.consume()
             return self.literalCadena()

         elif self.caracter=='\0':
             break

         else:
            token=Token("","","tk_error",self.caracter, self.numeroLinea,-1)
            self.errores.append((self.numeroLinea,"Lexical error: Character %s not expected "%self.caracter))
            self.consume()
            return token
       return  Token("","","tk_eot","\0", self.numeroLinea,-1)



#METODO PARA COMPROBAR SI EL CARACTER ACTUAL ES UNA LETRA---------------------------------------------------------------
    def isLetter(self):
        return self.caracter.isalpha() or self.caracter == '_'

#METODO PARA COMPROBAR SI EL CARACTER ACTUAL ES UN DIGITO---------------------------------------------------------------
    def isDigit(self):
        return self.caracter.isdigit()














































