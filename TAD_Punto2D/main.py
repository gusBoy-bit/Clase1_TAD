from punto2d import Punto2D
def main():
    p1=Punto2D(2,3); p2=Punto2D(6,6)
    print("TAD PUNTO2D")
    print("p1:",p1,"| p2:",p2)
    print("X de p1:",p1.coordenada_x())
    print("Y de p1:",p1.coordenada_y())
    print("Distancia:",p1.distancia(p2))
    trasladado=p1.trasladar(3,2)
    print("Punto trasladado:",trasladado)
    print("Punto original:",p1)
if __name__=="__main__": main()
