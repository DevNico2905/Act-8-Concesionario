from abc import ABC, abstractmethod
from typing import final

class Vehiculo(ABC):
    
    def __init__(self, marca: str, modelo: str, precioBase: float):
        if precioBase <= 0:
            raise ValueError("El precio base debe ser mayor a 0.")
        
        self.__marca = marca
        self.__modelo = modelo
        self.__precioBase = precioBase
    
    @final
    def getMarca(self) -> str:
        return self.__marca
    
    @final
    def getModelo(self) -> str:
        return self.__modelo
    
    @final
    def getPrecioBase(self) -> float:
        return self.__precioBase
    
    @abstractmethod
    def _impuesto( self) -> float:
        pass
    
    def precioFinal(self) -> float:
        return self.__precioBase + self._impuesto()
        
    def ficha(self) -> str:
        return f"{self.getMarca()} {self.getModelo()} (${self.getPrecioBase():.2f})"

    def __str__(self) -> str:
        return f"{self.ficha()} | Final: ${self.precioFinal():.2f}"

        