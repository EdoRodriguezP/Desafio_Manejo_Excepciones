# Define una excepción personalizada que hereda de Exception
class DimensionError(Exception):  
    def __init__(self, mensaje, dimension=None, maximo=None):
        # Llama al constructor de la clase base Exception con el mensaje
        super().__init__(mensaje)      
        self.mensaje = mensaje         
        self.dimension = dimension     
        self.maximo = maximo           

    def __str__(self):
        # Si solo se ingresó el mensaje, retorna el __str__ de la clase base
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        # Comienza el mensaje con el texto principal
        msg = self.mensaje  
        # Si se proporcionó dimension, la agrega al mensaje
        if self.dimension is not None:
            msg += f" (valor ingresado: {self.dimension})"
        # Si se proporcionó maximo, la agrega al mensaje
        if self.maximo is not None:
            msg += f" (máximo permitido: {self.maximo})"
        return msg 