__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-
from SymbolInfo import *

class SymbolsTable:

    def __init__(self):
        self.items=[]


    def add(self,lexema,tipo):
        item=SymbolInfo(lexema,tipo)
        control=False
        x=None
        for i in range(0,len(self.items)):
            if self.items[i].lexeme==lexema:
                control=True
                x=i
                break
        if control==False:
           self.items.append(item)
           return len(self.items)-1
        else:
            return x


    def entry(self,index):
        return self.items[index]


    def count(self):
        return len(self.items)
