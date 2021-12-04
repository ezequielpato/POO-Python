class ImposibleRealizarUnaCarga(Exception):
    """ Excepción para definir una carga que no puede realizarse. """
    pass

if __name__ == "__main__":
    try:
        raise ImposibleRealizarUnaCarga({"mensaje":"Carga no realizada"})
    except ImposibleRealizarUnaCarga as error:
        mensaje  = error.args[0]
        print(mensaje["mensaje"])

    try:
        raise ImposibleRealizarUnaCarga("Carga no realizada")
    except ImposibleRealizarUnaCarga as error:
        print(error)