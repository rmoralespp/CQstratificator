__author__ = 'jessicaPC'

from Lexer import Lexer
from Parser import Parser
from Cheker import Cheker
from Keywords import *
from SymbolsTable import *
from MyEncoder import *
from Visualizacion import *


class Controller(QObject):

    def __init__(self,vp,code):
        QObject.__init__(self)
        self.vp=vp
        self.code=code
        self.st=SymbolsTable()
        self.parser=Parser()
        self.cheker=Cheker()
        self.lexer=Lexer(self.st)
        #self.encoder=MyEncoder()
        self.rerrores=[]




    def analisisLex(self):
        self.parser.tokensReconocidos=[]
        self.parser.errores=[]
        self.cheker.errores=[]
        if self.code!="":
             st=SymbolsTable()
             self.parser.input=Lexer(st)
             self.parser.input.texto=self.code
             self.parser.input.caracter=str(self.code[0])
             self.parser.tokenActual=self.parser.input.nextToken()
             erroresL=self.parser.input.errores
             astPrograma=self.parser.programa()
             self.vp.cargarTokens(self.parser.tokensReconocidos)
             self.vp.cargarErrors(erroresL,[],[])




    def analisisPars(self):
        self.parser.tokensReconocidos=[]
        self.parser.errores=[]
        self.cheker.errores=[]
        if self.code!="":
             st=SymbolsTable()
             self.parser.input=Lexer(st)
             self.parser.input.texto=self.code
             self.parser.input.caracter=str(self.code[0])
             self.parser.tokenActual=self.parser.input.nextToken()
             erroresL=self.parser.input.errores
             erroresP=self.parser.errores
             astPrograma=self.parser.programa()
             self.vp.cargarTokens(self.parser.tokensReconocidos)
             self.vp.cargarErrors(erroresL,erroresP,[])




    def analisisChek(self):
        self.parser.tokensReconocidos=[]
        self.parser.errores=[]
        self.cheker.errores=[]
        if self.code!="":
             st=SymbolsTable()
             self.parser.input=Lexer(st)
             self.parser.input.texto=self.code
             self.parser.input.caracter=str(self.code[0])
             self.parser.tokenActual=self.parser.input.nextToken()
             erroresL=self.parser.input.errores
             erroresP=self.parser.errores
             erroresC=self.cheker.errores
             astPrograma=self.parser.programa()

             self.cheker.st=self.parser.input.symbolsTable
             self.cheker.visitPrograma(astPrograma)
             self.vp.cargarTokens(self.parser.tokensReconocidos)
             self.vp.cargarErrors(erroresL,erroresP,erroresC)


    def run(self):

        self.parser.tokensReconocidos=[]
        self.parser.errores=[]
        self.cheker.errores=[]
        self.rerrores=[]
        if self.code!="":
             st=SymbolsTable()
             self.parser.input=Lexer(st)
             self.parser.input.texto=self.code
             self.parser.input.caracter=str(self.code[0])
             self.parser.tokenActual=self.parser.input.nextToken()
             erroresL=self.parser.input.errores
             erroresP=self.parser.errores
             erroresC=self.cheker.errores
             astPrograma=self.parser.programa()

             self.cheker.st=self.parser.input.symbolsTable
             self.cheker.visitPrograma(astPrograma)
             self.vp.cargarTokens(self.parser.tokensReconocidos)
             self.vp.cargarErrors(erroresL,erroresP,erroresC)

             if len(erroresL+erroresP+erroresC)==0:
                 encoder=MyEncoder()
                 encoder.st=self.cheker.st
                 encoder.visitPrograma(astPrograma)
                 nlayer="%s"%encoder.nlayer
                 total=[]
                 control=True

                 thread=Visualizacion(encoder.estratos,nlayer,self)
                 self.connect(thread,self.vp.signal,self.vp.adicionarCapa)
                 self.connect(thread,self.vp.signalE,self.vp.cargarRErrors)
                 thread.run()


