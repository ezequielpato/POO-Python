"""
    Ejercicio 4:
        Modelar la clase Alien con las siguientes caracteristicas:
            - Un alien posee una energia que va en el rango de 0 a 5.
            - Un alien puede:
                # estaVivo: retorna verdadero solo si su energia es mayor a 0.
                # recibirDisparo: decrementa la energia del alien en 1.
                # reponerse: aumenta la energia del alien en dos unidades.

    Realizar los test necesarios que validen
    el comportamiento del alien, ademas verifique que cuando el robot realice un
    disparo al alien decremente la energia del mismo.
"""

class Alien(object):
    """
    Clase Alien

    Métodos:
            # estaVivo: retorna verdadero solo si su energia es mayor a 0.
            # recibirDisparo: decrementa la energia del alien en 1.
            # reponerse: aumenta la energia del alien en dos unidades.
    """
    def __init__(self) -> None:
        self.__ENERGIA_MAXIMA = 5
        self.__energia = self.__ENERGIA_MAXIMA

    @property
    def energia(self): return self.__energia


    def estaVivo(self) -> bool:
        """ Metodo que devuelve TRUE si el Alien está vivo. """
        return self.energia > 0

    def recibirDisparo(self) -> None:
        """ Decrementa la energía del Alien en 1"""
        self.__energia -= 1

    def reponerse(self) -> None:
        """ Aumenta la energia del Alien en dos unidades """
        if self.energia + 2 <= self.__ENERGIA_MAXIMA:
            self.__energia += 2
        else:
            self.__energia = self.__ENERGIA_MAXIMA


if __name__ == "__main__":
    # pass
    alien = Alien()
    alien.recibirDisparo()
    print(alien.estaVivo())
    print(alien.energia)
    alien.reponerse()
    print(alien.energia)