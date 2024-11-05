class CalculosPromedio:
    def calcular_promedio(self, conjunto):
        """Calcula el promedio de una lista de números enteros"""
        if not conjunto:
            return None
        return sum(conjunto) / len(conjunto)
