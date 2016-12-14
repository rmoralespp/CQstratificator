# -*- coding: utf-8 -*-

class Token:

    def __init__(self,s,e,kind,lexema, position,entry):
      self.kind=kind
      self.lexema=lexema
      self.entry=entry
      self.line=position
      self.start=s
      self.end=e



