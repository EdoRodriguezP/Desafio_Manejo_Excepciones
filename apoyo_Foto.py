from error import DimensionError 

class Foto():
    # Constante de clase que define el valor máximo permitido para ancho y alto
    MAX = 2500  

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho  
        self.__alto = alto    
        ruta = ruta           

    # Devuelve el valor actual de ancho
    @property
    def ancho(self) -> int:
        return self.__ancho  

    @ancho.setter
    def ancho(self, ancho) -> None:
        # Valida que el nuevo ancho esté dentro del rango permitido
        if not (1 <= ancho <= self.MAX):
            # Si no está en el rango, lanza la excepción personalizada con detalles
            raise DimensionError(
                "El ancho debe estar entre 1 y el máximo permitido.",
                dimension=ancho,
                maximo=self.MAX
            )
        # Si es válido, asigna el nuevo valor a __ancho    
        self.__ancho = ancho  

    # Devuelve el valor actual de alto
    @property
    def alto(self) -> int:
        return self.__alto  

    @alto.setter
    def alto(self, alto) -> None:
        # Valida que el nuevo alto esté dentro del rango permitido
        if not (1 <= alto <= self.MAX):
            # Si no está en el rango, lanza la excepción personalizada con detalles
            raise DimensionError(
                "El alto debe estar entre 1 y el máximo permitido.",
                dimension=alto,
                maximo=self.MAX
            )
        # Si es válido, asigna el nuevo valor a __alto
        self.__alto = alto  