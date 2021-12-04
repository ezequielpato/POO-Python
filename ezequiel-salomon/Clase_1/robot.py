"""
    Ejercicio 3:
        Modelar la clase Robot con las siguientes caracteristicas:
            - Un robot posee una bateria en la cual almacena su energia.
            La carga de la bateria de encuentra en el rango de 0 a 100.
            - Un robot puede:
                # caminar(metros): le consume 1 unidad cada 10 metros.
                # cargarBateria(una_carga): le agrega una determinada cantidad
                de unidades, pero no puede superar las 100 unidades de la bateria.
                # disparar(un_objetivo): le consume el 10% de la bateria que posea.

    Realizar los test necesarios que validen
    el comportamiento.
"""

from alien import Alien


class Robot(object):
    """ pass """


    def __init__(self, bateria: int) -> None:
        self.__CARGA_MAX = 100
        self.__bateria = bateria


    @property
    def bateria(self): return self.__bateria



    def caminar(self, distancia: int) -> None:
        """ Consume 1 unidad de bateria cada 10mts recorridos """

        # Convierte parametro recibido en positivo si es negativo
        # if distancia < 0: distancia *= -1

        # abs() -> Funcion valor absoluto

        unidades = abs(distancia) / 10

        if self.bateria >= unidades:
            self.__bateria -= unidades
        else:
            raise ValueError('no hay bateria suficiente')


    def cargarBateria(self, unidades: int):
        """ pass """
        if self.bateria + unidades <= self.__CARGA_MAX:
            self.__bateria += unidades
        else:
            self.__bateria = self.__CARGA_MAX


    def dispararAUnObjetivo(self, un_objetivo):
        """ pass """
        self.__bateria -= self.bateria *0.1
        un_objetivo.recibirDisparo()


if __name__ == '__main__':


    alien = Alien()
    robot = Robot(100)

    robot.caminar(-100)
    # robot.cargarBateria(10)
    # robot.dispararAUnObjetivo(alien)
    print(robot.bateria)




