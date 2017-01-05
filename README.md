# CQstratificator
CQstratificator es un plugin para el Sistema de Información Geográfica QGIS que permite representar estratos o grupos de territorios a través de un simple lenguaje de código. La aplicación se apoya sobre la arquitectura de un compilador, específicamente en las fases de análisis léxico, análisis sintáctico y análisis semántico.
La aplicación es capaz de seleccionar capas de tipo polígono y multipolígono, cargadas por QGIS, y a partir de estas crear grupos de características. Cada una de estas se maneja por su identificador correspondiente, y a cada grupo creado se le permite asignar un color en formato RGB. Los resultados pueden se exportados como imagen.
Requerimientos: QGIS, Python 2.7.X, PyQt.
