#!/usr/bin/env python


class Figuras():

    def getArea_1(self,figura, param1):
        if figura == "square":
            return self.areaCuadrado(param1)
        elif figura == "circle":
            return self.areaCirculo(param1)

    def getArea_2(self,figura, param1, param2):
        if figura == "rectangle":
            return self.areaRectangulo(param1,param2)
        elif figura == "triangle":
            return self.areaTriangulo(param1,param2)
        elif figura == "rhombus":
            return self.areaRombo(param1,param2)
        

    def areaCuadrado(self, side):
        area = side**2
        return area

    def areaTriangulo(self, base, altura):
        area = (base * altura) / 2
        return area

    def areaCirculo(self, radio):
        area = (3.1416) * (radio**2)
        return area

    def areaRectangulo(self, base, altura):
        area = base * altura
        return area

    def areaRombo(self, diagonal1, diagonal2):
        area = (diagonal1 * diagonal2) / 2
        return area



