__author__ = 'jess'
# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""
from pluginEstratificador import pluginEstratificador


def name():
    return "CQESTRATIFICATOR"

def description():
    return "Plugin to represent stratas of territories"

def qgisMinimumVersion():
    return "1.0"

def version():
    return "0.1.0"

def author():
    return "Rolando Morales Perez"
def email():
    return "rolando.morales@mtss.cu"

def category():
  return "EST"

def classFactory(iface):
  return pluginEstratificador(iface)
