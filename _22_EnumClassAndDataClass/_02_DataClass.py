from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

p1 = Product("Laptop", 1200)

print(p1)