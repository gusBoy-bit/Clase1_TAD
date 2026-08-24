from math import gcd
class Fraccion:
    def __init__(self,numerador,denominador):
        if denominador==0: raise ValueError("El denominador no puede ser igual a cero.")
        self.__numerador=numerador; self.__denominador=denominador
    def numerador(self): return self.__numerador
    def denominador(self): return self.__denominador
    def sumar(self,otra):
        return Fraccion(self.__numerador*otra.__denominador+otra.__numerador*self.__denominador,self.__denominador*otra.__denominador)
    def simplificar(self):
        d=gcd(abs(self.__numerador),abs(self.__denominador))
        n=self.__numerador//d; den=self.__denominador//d
        if den<0: n=-n; den=-den
        return Fraccion(n,den)
    def restar(self,otra):
        return Fraccion(self.__numerador*otra.__denominador-otra.__numerador*self.__denominador,self.__denominador*otra.__denominador)
    def multiplicar(self,otra):
        return Fraccion(self.__numerador*otra.__numerador,self.__denominador*otra.__denominador)
    def son_iguales(self,otra):
        return self.__numerador*otra.__denominador==otra.__numerador*self.__denominador
    def __str__(self): return f"{self.__numerador}/{self.__denominador}"
