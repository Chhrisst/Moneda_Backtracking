# Moneda_Backtracking
print("---------------------------Algoritmo de Backtracking---------------------------")
def cambio_monedas_retroceso(monedas, monto):
   
    def retroceso(inicio, restante, camino, resultados):
        if restante == 0:
            resultados.append(list(camino))
            return
        if restante < 0:
            return

        for i in range(inicio, len(monedas)):
            camino.append(monedas[i])
            retroceso(i, restante - monedas[i], camino, resultados)
            camino.pop()

    resultados = []
    retroceso(0, monto, [], resultados)

   
    if resultados:
        return min(resultados, key=len)
    else:
        return None


def obtener_entradas():

    monedas = input("Introduzca el valor de cada moneda, debe de colocarlas separadas por espacios(Ejemplo: 10 20 30): ").split()
  
    monedas = [int(moneda) for moneda in monedas]
    monto = int(input("Introduzca el monto especifico(Ejemplo 200): "))
    return monedas, monto

def principal():
    monedas, monto = obtener_entradas()
    solucion = cambio_monedas_retroceso(monedas, monto)
    if solucion:
        print("La solución mas optima con la menor cantidad de monedas es:", solucion)
    else:
        print("No es posible dar el cambio con las denominaciones proporcionadas.")

if __name__ == "__main__":
    principal()
print("-------------------------------------------------------------------------------")
