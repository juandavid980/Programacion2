class Televisor:

    def __init__(self, marca=None, resolucion=None, tipo=None):
        if marca is None and resolucion is None and tipo is None:

            self._marca = "Sin marca"
            self._resolucion = 0
            self._tipo = "Desconocido"
        else:

            self._marca = marca
            self._resolucion = resolucion
            self._tipo = tipo

    def toString(self) -> str:
        return f"Televisor [marca={self._marca}, resolucion={self._resolucion}, tipo={self._tipo}]"

tv1 = Televisor("Samsung", 4, "OLED")

tv2 = Televisor("Samsung",6,"OLED")

print(tv1.toString())
print(tv2.toString())
    