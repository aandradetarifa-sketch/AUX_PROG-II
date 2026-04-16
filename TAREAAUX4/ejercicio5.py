from abc import ABC, abstractmethod
import math

# a) clase abstracta
class Figura(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def obtenerArea(self) -> float:
        pass

# b) subclases con obtenerArea()
class Cuadrado(Figura):
    def __init__(self, color: str, lado: int):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self) -> float:
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado [color={self.color}, lado={self.lado}, área={self.obtenerArea():.2f}]"

class Triangulo(Figura):
    def __init__(self, color: str, lado1: int, lado2: int, lado3: int):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtenerArea(self) -> float:
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

    def __str__(self):
        return f"Triángulo [color={self.color}, lados=({self.lado1},{self.lado2},{self.lado3}), área={self.obtenerArea():.2f}]"

class Redondo(Figura):
    def __init__(self, color: str, radio: int):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self) -> float:
        return math.pi * (self.radio ** 2)

    def __str__(self):
        return f"Redondo (Círculo) [color={self.color}, radio={self.radio}, área={self.obtenerArea():.2f}]"

# c) instanciar 2 objetos de cada subclase
cuadrado1 = Cuadrado("rojo", 5)
cuadrado2 = Cuadrado("azul", 7)

triangulo1 = Triangulo("verde", 3, 4, 5)
triangulo2 = Triangulo("amarillo", 5, 5, 8)

redondo1 = Redondo("blanco", 4)
redondo2 = Redondo("negro", 6)

print("--- Cuadrados ---")
print(cuadrado1)
print(cuadrado2)

print("\n--- Triángulos ---")
print(triangulo1)
print(triangulo2)

print("\n--- Redondos ---")
print(redondo1)
print(redondo2)

# ""d) dado un Cuadrado y un Triángulo, mostrar el color del que tenga mayor área"""
print("\n--- Comparación Cuadrado vs Triángulo ---")
cuadrado_ejemplo = Cuadrado("morado", 8)
triangulo_ejemplo = Triangulo("naranja", 6, 8, 10)

area_cuad = cuadrado_ejemplo.obtenerArea()
area_tri = triangulo_ejemplo.obtenerArea()

print(cuadrado_ejemplo)
print(triangulo_ejemplo)

if area_cuad > area_tri:
    print(f"La figura con mayor área es el Cuadrado de color {cuadrado_ejemplo.color} (área {area_cuad:.2f})")
elif area_tri > area_cuad:
    print(f"La figura con mayor área es el Triángulo de color {triangulo_ejemplo.color} (área {area_tri:.2f})")
else:
    print("Ambas figuras tienen la misma área.")