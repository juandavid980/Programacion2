class SueldoInvalidoException(Exception):
    pass
class CargoInvalidoException(Exception):
    pass


class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Sueldo: {self.sueldo} Bs")
        print("-" * 30)


class Empresa:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.empleados = [None] * cantidad

    def registrar_empleados(self):
        for i in range(len(self.empleados)):
            print(f"\nEmpleado {i+1}")

            nombre = input("Nombre: ")

            while True:
                try:
                    cargo = input("Cargo: ")

                    for caracter in cargo:
                        if caracter.isdigit():
                            raise CargoInvalidoException(
                                "El cargo no puede contener números."
                            )

                    break

                except CargoInvalidoException as e:
                    print("Error:", e)
                    print("Ingrese nuevamente el cargo.")

            try:
                sueldo = float(input("Sueldo: "))

                if sueldo < 2500:
                    raise SueldoInvalidoException(
                        "El sueldo es menor al Salario Mínimo Nacional."
                    )

            except SueldoInvalidoException as e:
                print("Error:", e)
                print("Se asignará automáticamente 2500 Bs.")
                sueldo = 2500

            self.empleados[i] = Empleado(nombre, cargo, sueldo)

    def mostrar_empleados(self):
        print(f"\nEMPRESA: {self.nombre}")
        print("=" * 30)

        for i in range(len(self.empleados)):
            self.empleados[i].mostrar()

nombre_empresa = input("Nombre de la empresa: ")
n = int(input("Cantidad de empleados: "))

empresa = Empresa(nombre_empresa, n)

empresa.registrar_empleados()
empresa.mostrar_empleados()