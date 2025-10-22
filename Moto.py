from  Vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float, cc: int):
        super().__init__(marca, modelo, precioBase)
        
        if cc <= 0:
            raise ValueError("El cilindraje debe ser mayor que 0.")
        
        self.__cc = cc
    
    def _impuesto(self) -> float:
        tasa: float = 0.05 if self.__cc <= 250 else 0.09
        return self.getPrecioBase() * tasa

    def ficha(self) -> str:
        return f"Moto | {super().ficha()} | {self.__cc} Cilindraje"

    