__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-

class SymbolInfo:

    def __init__(self,lexema,kind):

        self.lexeme = lexema
        self.kind = kind
        self.declared = False
        self.type = None
        self.address = -1
        self.init=False

