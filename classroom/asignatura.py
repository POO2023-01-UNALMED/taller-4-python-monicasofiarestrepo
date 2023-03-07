class Asignatura:

    def __init__(self, nombre, salon):
        self._nombre = nombre
        self._salon = salon
        nombre = ""
        salon = "remoto"

    def __str__(self):
        linea = ("Grupo de estudiantes" +self._grupo)
        return linea