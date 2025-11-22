from proceso import Proceso

def lifo(procesos, mostrar_tabla=True):
    """
    Algoritmo Last-In First-Out (LIFO)
    """
    clk = 0  # Reloj
    procesados = 0
    completados = [False] * len(procesos)
    resultados = [Proceso(p.id, p.ti, p.t) for p in procesos]
    
    while procesados < len(procesos):
        idx = -1
        
        # Buscar el último proceso disponible (LIFO)
        for i in range(len(procesos)-1, -1, -1):
            if not completados[i] and procesos[i].ti <= clk:
                idx = i
                break
        
        if idx == -1:
            # Avanzar al siguiente tiempo de llegada
            siguiente_ti = float('inf')
            for i in range(len(procesos)):
                if not completados[i] and procesos[i].ti > clk:
                    siguiente_ti = min(siguiente_ti, procesos[i].ti)
            clk = siguiente_ti
            continue
        
        # Procesar el proceso seleccionado
        completados[idx] = True
        resultados[idx].tf = clk + procesos[idx].t
        resultados[idx].T = resultados[idx].tf - procesos[idx].ti
        resultados[idx].E = resultados[idx].T - procesos[idx].t
        resultados[idx].I = procesos[idx].t / resultados[idx].T if resultados[idx].T > 0 else 0
        
        clk = resultados[idx].tf
        procesados += 1
    
    if mostrar_tabla:
        mostrar_tabla_procesos(resultados, "LIFO")
    
    # Calcular promedios
    total_T = sum(p.T for p in resultados)
    total_E = sum(p.E for p in resultados)
    total_I = sum(p.I for p in resultados)
    
    print(f"\nLIFO - PROMEDIOS:")
    print(f"   Tiempo Total (T): {total_T/len(procesos):.2f}")
    print(f"   Tiempo Espera (E): {total_E/len(procesos):.2f}")
    print(f"   Indice Servicio (I): {total_I/len(procesos):.4f}")
    
    return resultados, 0  # No medimos tiempo aquí

def mostrar_tabla_procesos(procesos, algoritmo):
    """Mostrar tabla de resultados con diseño mejorado"""
    print(f"\n{'=' * 85}")
    print(f"{algoritmo:^85}")
    print(f"{'=' * 85}")
    
    # Encabezado que COINCIDE EXACTAMENTE con el formato de los datos
    print("| Proceso  | ti |  t  |  tf  |  T   |  E   |    I    |")
    print(f"{'-' * 85}")
    
    for proceso in procesos:
        print(proceso)
    
    print(f"{'=' * 85}")