class ImposibleDividirPorCero(Exception):
  """ Exepción al intentar dividir por cero """
  pass

if __name__ == "__main__":
    try:
        raise ImposibleDividirPorCero({"mensaje":"Imposible dividir por cero"})
    except ImposibleDividirPorCero as error:
        mensaje  = error.args[0]
        print(mensaje["mensaje"])