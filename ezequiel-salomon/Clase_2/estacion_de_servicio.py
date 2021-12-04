from surtidor import Surtidor
from functools import reduce

class Estacion():
    """
        Estacion:
            ✅ Tienen un conjunto de surtidores
            ✅ Al instanciarse no tendrá surtidores
            ✅ Podrá agregar un surtidor
            ✅ Saber cuantos surtidores tiene
            ✅ Saber cuantos surtidores vacios tiene
            ✅ Saber cuáles son su surtidores vacios
            ✅ Sumar total de litros que faltan para
                completar su capacidad total
            ✅ Obtener el costo total para completar
                la carga faltante dado un precio por litro
    """

    def __init__(self) -> None:
        self.__surtidores = []

    @property
    def surtidores(self) -> list[Surtidor] : return self.__surtidores

    def agregarSurtidor(self, un_surtidor:Surtidor) -> None:
        """ Agrega un surtidor a la colección """
        self.__surtidores.append(un_surtidor)

    def cantidadDeSurtidores(self) -> int:
        """ Cuenta la cantidad de surtidores añadidos """
        return len(self.surtidores)

    def surtidoresVacios(self) -> list[Surtidor] :
        """ Retorna la lista de surtidores vacios """
        return list(filter(Surtidor.estaVacio, self.surtidores))

    def cantidadSurtidoresVacios(self) -> int:
        """ Retorna la cantidad de surtidores vacios de la estación """
        return len(self.surtidoresVacios())

    def litrosFaltantes(self) -> int:
        """ Devuelve los litros faltantes """
        result = lambda cont, surtidor: cont + surtidor.cargaFaltante()
        return reduce(result, self.surtidores, 0)

    def costoDeCarga(self, precio_por_litros: int) -> int:
        """ Devuelve el costo de carga para completar la estacion """
        if self.litrosFaltantes() > 0:
           return precio_por_litros * self.litrosFaltantes()
        else:
            print("Error")

if __name__ == "__main__":
    estacion = Estacion()
    sur = Surtidor(100)

