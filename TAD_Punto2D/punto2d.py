from math import sqrt
class Punto2D:
    def __init__(self,x,y):
        self.__x=x; self.__y=y
    def coordenada_x(self): return self.__x
    def coordenada_y(self): return self.__y
    def distancia(self,otro):
        return sqrt((otro.__x-self.__x)**2+(otro.__y-self.__y)**2)
    def trasladar(self,dx,dy):
        return Punto2D(self.__x+dx,self.__y+dy)
    def __str__(self): return f"({self.__x}, {self.__y})"
