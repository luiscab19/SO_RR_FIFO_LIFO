import csv
import time
from FIFO import fifo
from LIFO import lifo
from RR import round_robin
from proceso import Proceso

def load_data(filename):
    """Cargar datos desde archivo CSV"""
    procesos = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for fila in reader:
                if len(fila) >= 3:
                    id_proceso = fila[0].strip()
                    ti = int(fila[1])
                    t = int(fila[2])
                    procesos.append(Proceso(id_proceso, ti, t))
        
        print(f"[OK] Se cargaron {len(procesos)} procesos desde {filename}")
        return procesos
    
    except FileNotFoundError:
        print(f"[ERROR] No se pudo abrir el archivo {filename}")
        return None
    except Exception as e:
        print(f"[ERROR] Error al leer el archivo CSV: {e}")
        return None

def calcular_promedios(resultados):
    """Calcular promedios de T, E e I"""
    total_T = sum(p.T for p in resultados)
    total_E = sum(p.E for p in resultados)
    total_I = sum(p.I for p in resultados)
    n = len(resultados)
    return total_T/n, total_E/n, total_I/n

def mostrar_encabezado(titulo):
    """Mostrar un encabezado con diseño limpio"""
    print("\n" + "=" * 70)
    print(f"{titulo:^70}")
    print("=" * 70)

def mostrar_recomendaciones(algoritmos):
    """Mostrar recomendaciones"""
    print("\n" + "-" * 70)
    print("RECOMENDACION FINAL")
    print("-" * 70)
    
    # Encontrar el mejor en cada categoría
    mejor_T = min(algoritmos, key=lambda x: x[1][0])
    mejor_E = min(algoritmos, key=lambda x: x[1][1])
    mejor_I = max(algoritmos, key=lambda x: x[1][2])
    
    print("\nMEJORES ALGORITMOS POR CATEGORIA:")
    print(f"  * Menor Tiempo Total: {mejor_T[0]} (T = {mejor_T[1][0]:.2f})")
    print(f"  * Menor Tiempo Espera: {mejor_E[0]} (E = {mejor_E[1][1]:.2f})")
    print(f"  * Mayor Indice Servicio: {mejor_I[0]} (I = {mejor_I[1][2]:.4f})")
    
    # Recomendación general (priorizando Tiempo Total)
    recomendacion_general = mejor_T[0]
    
    print(f"\nRECOMENDACION GENERAL:")
    print(f"  {recomendacion_general}")
    print(f"  (Basado en el menor Tiempo Total promedio: {mejor_T[1][0]:.2f})")

def mostrar_resumen_final(algoritmos, tiempos):
    """Mostrar tabla comparativa final"""
    print("\n" + "-" * 70)
    print("COMPARACION FINAL DE ALGORITMOS")
    print("-" * 70)
    
    print("\nAlgoritmo        | Avg T    | Avg E    | Avg I     | Tiempo (µs)")
    print("-----------------|----------|----------|-----------|-------------")
    
    for i, (nombre, metricas) in enumerate(algoritmos):
        print(f"{nombre:15} | {metricas[0]:8.2f} | {metricas[1]:8.2f} | {metricas[2]:9.4f} | {tiempos[i]:11.2f}")

def main():
    procesos = []
    
    # Mostrar banner de inicio
    print("\n" + "=" * 70)
    print("SIMULADOR DE ALGORITMOS DE PLANIFICACION DE PROCESOS")
    print("=" * 70)
    
    # Cargar datos desde el archivo CSV
    procesos = load_data("CODIGO\\data_so.csv")
    
    if not procesos:
        print("No se pudieron cargar los procesos. Saliendo...")
        return
    
    # Preguntar si mostrar tablas completas
    opcion = input("\n¿Desea ver las tablas completas de procesos? (s/n): ")
    mostrar_tablas = (opcion.lower() == 's')
    
    # Quantum fijo en 4
    quantum = 4
    print(f"\n[INFO] Quantum establecido en: {quantum}")
    
    resultados_rr, resultados_fifo, resultados_lifo = None, None, None
    tiempo_rr, tiempo_fifo, tiempo_lifo = 0, 0, 0
    promedios_rr, promedios_fifo, promedios_lifo = None, None, None
    
    # EJECUCIÓN SECUENCIAL: RR -> FIFO -> LIFO
    
    mostrar_encabezado("EJECUTANDO ALGORITMO ROUND ROBIN")
    
    inicio_rr = time.perf_counter()
    resultados_rr, _ = round_robin(procesos, quantum, mostrar_tablas)
    fin_rr = time.perf_counter()
    tiempo_rr = (fin_rr - inicio_rr) * 1_000_000
    promedios_rr = calcular_promedios(resultados_rr)
    print(f"Tiempo de ejecucion: {tiempo_rr:.2f} microsegundos")
    
    mostrar_encabezado("EJECUTANDO ALGORITMO FIFO")
    
    inicio_fifo = time.perf_counter()
    resultados_fifo, _ = fifo(procesos, mostrar_tablas)
    fin_fifo = time.perf_counter()
    tiempo_fifo = (fin_fifo - inicio_fifo) * 1_000_000
    promedios_fifo = calcular_promedios(resultados_fifo)
    print(f"Tiempo de ejecucion: {tiempo_fifo:.2f} microsegundos")
    
    mostrar_encabezado("EJECUTANDO ALGORITMO LIFO")
    
    inicio_lifo = time.perf_counter()
    resultados_lifo, _ = lifo(procesos, mostrar_tablas)
    fin_lifo = time.perf_counter()
    tiempo_lifo = (fin_lifo - inicio_lifo) * 1_000_000
    promedios_lifo = calcular_promedios(resultados_lifo)
    print(f"Tiempo de ejecucion: {tiempo_lifo:.2f} microsegundos")
    
    # Preparar datos para comparación
    algoritmos = [
        ("Round Robin", promedios_rr),
        ("FIFO", promedios_fifo),
        ("LIFO", promedios_lifo)
    ]
    tiempos = [tiempo_rr, tiempo_fifo, tiempo_lifo]
    
    # Mostrar resumen final
    mostrar_resumen_final(algoritmos, tiempos)
    
    # Mostrar recomendaciones
    mostrar_recomendaciones(algoritmos)
    
    print("\n" + "=" * 70)
    print("SIMULACION COMPLETADA")
    print("=" * 70)

if __name__ == "__main__":
    main()