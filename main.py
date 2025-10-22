from Moto import Moto
from Automovil import Automovil

def main():
    inventario = [
        Automovil("Citroen", "C3", 20000, 5),
        Moto("KTM", "Duke 200", 15000, 200),
        Automovil("Ford", "Mustang", 50000, 4),
        Moto("Kawasaki", "ER6n", 19000, 650)
    ]

    total = 0

    for vehiculo in inventario:
        print(vehiculo)  # Esto llama a vehiculo.__str__()
        total += vehiculo.precioFinal()

    print(f"Valor total del inventario: ${total:.2f}")

if __name__ == "__main__":
    main()