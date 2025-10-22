from  Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float, puertas: int):
        super().__init__(marca, modelo, precioBase)
        
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que 0.")
        
        self.__puertas = puertas
    
    def _impuesto(self) -> float:
        imp: float = self.getPrecioBase() * 0.08
        desc: float = self.getPrecioBase() * 0.01 if self.__puertas == 5 else 0
        return imp - desc

    def ficha(self) -> str:
        return f"Automovil | {super().ficha()} | {self.__puertas} puertas"

