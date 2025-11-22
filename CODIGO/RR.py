from proceso import Proceso

def round_robin(procesos, quantum, mostrar_tabla=True):
    """
    Algoritmo Round Robin
    """
    clk = 0
    procesos_terminados = 0
    resultados = [Proceso(p.id, p.ti, p.t) for p in procesos]
    tiempos_restantes = [p.t for p in procesos]
    
    while procesos_terminados < len(procesos):
        proceso_ejecutado = False
        
        for i in range(len(procesos)):
            if procesos[i].ti <= clk and tiempos_restantes[i] > 0:
                tiempo_ejecutado = min(quantum, tiempos_restantes[i])
                tiempos_restantes[i] -= tiempo_ejecutado
                clk += tiempo_ejecutado
                proceso_ejecutado = True
                
                if tiempos_restantes[i] == 0:
                    resultados[i].tf = clk
                    resultados[i].T = resultados[i].tf - procesos[i].ti
                    resultados[i].E = resultados[i].T - procesos[i].t
                    resultados[i].I = procesos[i].t / resultados[i].T
                    procesos_terminados += 1
        
        if not proceso_ejecutado:
            # Avanzar al siguiente tiempo de llegada
            siguiente_ti = float('inf')
            for i in range(len(procesos)):
                if tiempos_restantes[i] > 0:
                    siguiente_ti = min(siguiente_ti, procesos[i].ti)
            clk = max(clk, siguiente_ti)
    
    if mostrar_tabla:
        mostrar_tabla_procesos(resultados, "Round Robin")
    
    # Calcular promedios
    total_T = sum(p.T for p in resultados)
    total_E = sum(p.E for p in resultados)
    total_I = sum(p.I for p in resultados)
    
    print(f"\nRound Robin - PROMEDIOS:")
    print(f"   Tiempo Total (T): {total_T/len(procesos):.2f}")
    print(f"   Tiempo Espera (E): {total_E/len(procesos):.2f}")
    print(f"   Indice Servicio (I): {total_I/len(procesos):.4f}")
    
    return resultados, 0  # No medimos tiempo aquí

def mostrar_tabla_procesos(procesos, algoritmo):
    """Mostrar tabla de resultados con diseño mejorado"""
    print(f"\n{'=' * 85}")
    print(f"{algoritmo:^85}")
    print(f"{'=' * 85}")
    
    print("| Proceso  | ti |  t  |  tf  |  T   |  E   |    I    |")
    print(f"{'-' * 85}")
    
    for proceso in procesos:
        print(proceso)
    
    print(f"{'=' * 85}")