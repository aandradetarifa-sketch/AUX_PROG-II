class Persona:
    def __init__(self, nombre: str, carnet: int, edad: int):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carnet}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre: str, carnet: int, edad: int, matricula: int, carrera: str):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print(f"Matrícula: {self.matricula}, Carrera: {self.carrera}")

    def misma_carrera(self, otro_estudiante):
        return self.carrera == otro_estudiante.carrera


class Docente(Persona):
    def __init__(self, nombre: str, carnet: int, edad: int, antiguedad: int, sueldo: float):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print(f"Antigüedad: {self.antiguedad} años, Sueldo: {self.sueldo}")

# b) instancias
estudiante1 = Estudiante("Ana López", 2024001, 20, 12345, "Ingeniería Informática")
estudiante2 = Estudiante("Carlos Pérez", 2024002, 22, 12346, "Matemáticas")
docente1 = Docente("Dra. Marta Ríos", 998877, 45, 12, 3500.0)

# Mostrar datos
print("--- Estudiante 1 ---")
estudiante1.mostrar()
print("\n--- Estudiante 2 ---")
estudiante2.mostrar()
print("\n--- Docente ---")
docente1.mostrar()

# c) verif si tienen la misma edad
if estudiante1.edad == docente1.edad:
    print(f"\n{estudiante1.nombre} tiene la misma edad que {docente1.nombre}.")
elif estudiante2.edad == docente1.edad:
    print(f"\n{estudiante2.nombre} tiene la misma edad que {docente1.nombre}.")
else:
    print("\nNingún estudiante tiene la misma edad que el docente.")

# d) verif si tienen la misma carrera
if estudiante1.misma_carrera(estudiante2):
    print(f"{estudiante1.nombre} y {estudiante2.nombre} están en la misma carrera.")
else:
    print(f"{estudiante1.nombre} y {estudiante2.nombre} están en carreras diferentes.")