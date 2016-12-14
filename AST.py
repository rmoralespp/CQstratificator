__author__ = 'Rolando.Morales'


class AST:
    def __init__(self, line):
         self.line=line

    def visit(self,visitor):
        pass



class ASTPrograma(AST):
    def __init__(self,lista, line,nlayer):
         AST.__init__(self,line)
         self.lista=lista
         self.line=line
         self.nlayer=nlayer

    def visit(self,visitor):
        visitor.visitPrograma(self)



class ASTInstruccion(AST):
    def __init__(self,line):
         AST.__init__(self,line)
         self.line=line

    def visit(self,visitor):
        visitor.visit(self)



class ASTDeclaracion(ASTInstruccion):
    def __init__(self,line, tipo, ids):
        ASTInstruccion.__init__(self,line)
        self.ids=ids
        self.tipo=tipo
        self.line=line
        self.desp="declaracion"

    def visit(self,visitor):
        visitor.visitDeclaracion(self)


class ASTAsignacion(ASTInstruccion):
    def __init__(self, line, id, valor):
        ASTInstruccion.__init__(self,line)
        self.id=id
        self.valor=valor
        self.desp="asignacion"

    def visit(self,visitor):
        visitor.visitAsignacion(self)


class ASTImpresion(ASTInstruccion):
    def __init__(self, line, estratos):
        ASTInstruccion.__init__(self,line)
        self.estratos=estratos

    def visit(self,visitor):
        visitor.visitImpresion(self)




class ASTExpresion(AST):
    def __init__(self,line):
        AST.__init__(self,line)
        self.line=line


    def visit(self,visitor):
        visitor.visit(self)

class ASTSymbol(ASTExpresion):
      def __init__(self,entry, line):
        ASTExpresion.__init__(self,line)
        self.entry=entry

      def visit(self,visitor):
        visitor.visit(self)



class ASTIdentifier(ASTSymbol):
      def __init__(self,lexema, entry, line):
        ASTSymbol.__init__(self,entry, line)
        self.lexema=lexema

      def visit(self,visitor):
        visitor.visit(self)



class ASTIdentifierDeclaration(ASTIdentifier):
      def __init__(self,lexema, entry, line):
        ASTIdentifier.__init__(self,lexema, entry, line)

      def visit(self,visitor):
        visitor.visitIdentifierDeclaration(self)


class ASTIdentifierReference(ASTIdentifier):
     def __init__(self,lexema, entry, line):
          ASTIdentifier.__init__(self,lexema, entry, line)

     def visit(self,visitor):
        visitor.visitIdentifierReference(self)

class ASTIdentifierValue(ASTIdentifier):
     def __init__(self,lexema, entry, line):
        ASTIdentifier.__init__(self,lexema, entry, line)
        self.tipo="id"

     def visit(self,visitor):
        visitor.visitIdentifierValue(self)


class ASTIntValue(ASTSymbol):
     def __init__(self,lexema, entry, line):
        ASTSymbol.__init__(self, entry, line)
        self.lexema=lexema
        self.tipo="int"

     def visit(self,visitor):
        visitor.visitIntValue(self)



class ASTCadenaValue(ASTSymbol):
      def __init__(self,lexema, entry, line):
        ASTSymbol.__init__(self, entry, line)
        self.lexema=lexema
        self.tipo="cadena"

      def visit(self,visitor):
        visitor.visitCadenaValue(self)


class ASTEstratoValue(ASTSymbol):
     def __init__(self,nombre,color,territorios, entry, line):
        ASTSymbol.__init__(self, entry, line)
        self.nombre=nombre
        self.territorios=territorios
        self.color=color
        self.tipo="estrato"


     def visit(self,visitor):
        visitor.visit(self)


class ASTColorValue(ASTSymbol):
     def __init__(self,color, entry, line):
        ASTSymbol.__init__(self, entry, line)
        self.color=color
        self.tipo="color"


     def visit(self,visitor):
        visitor.visit(self)



class ASTListValue(ASTSymbol):
     def __init__(self,lista, entry, line):
        ASTSymbol.__init__(self, entry, line)
        self.lista=lista
        self.tipo="list"

     def visit(self,visitor):
        visitor.visit(self)



class Visitor:
    def __init__(self):
        pass




    def visit(self,aThis):
        pass

    def visitPrograma(self,programa):
        pass


    def visitDeclaracion(self,astDeclaracion):
          pass

    def visitAsignacion(self,astAsignacion):
        pass

    def visitCadenaValue(self,ast):
        pass

    def visitIntValue(self,ast):
        pass

    def visitIdentifierReference(self,identifierReference):
        pass


    def visitIdentifierDeclaration(self,identifierDeclaration):
        pass


    def visitIdentifierValue(self,astIdentifierValue):
        pass




