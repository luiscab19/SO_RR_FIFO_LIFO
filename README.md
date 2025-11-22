## Descripción

Este proyecto implementa un simulador de tres algoritmos fundamentales de planificación de procesos en sistemas operativos: **Round Robin (RR)**, **First-In-First-Out (FIFO)** y **Last-In-First-Out (LIFO)**. Desarrollado en Python, permite analizar y comparar el rendimiento de cada algoritmo mediante métricas clave de desempeño.

## Características

- **Implementación completa** de tres algoritmos de planificación
- **Carga automática** de procesos desde archivo CSV
- **Cálculo de métricas** para cada proceso:
  - Tiempo Final (tf)
  - Tiempo Total (T = tf - ti)
  - Tiempo de Espera (E = T - t)
  - Índice de Servicio (I = t/T)
- **Medición de tiempos** de ejecución por algoritmo
- **Comparación automática** entre métodos
- **Generación de reportes** detallados con promedios
- **Interfaz de consola** intuitiva

## 🛠️ Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- Archivo `data_so.csv` con los datos de procesos

### Ejecución
```bash
# Clonar el repositorio
git clone https://github.com/luiscab19/SO_RR_FIFO_LIFO.git
cd SO_RR_FIFO_LIFO

# Ejecutar el programa principal
python main.py
```

### Estructura del Archivo CSV
El archivo `data_so.csv` debe contener los procesos con el formato:
```
Proceso;ti;t
A;2;17
B;9;47
C;8;14
...
```

## Algoritmos Implementados

### Round Robin (RR)
- **Tipo**: Apropiativo
- **Quantum**: Configurable (por defecto: 4)
- **Ventajas**: Equitativo, evita inanición, buen tiempo de respuesta
- **Desventajas**: Overhead por cambios de contexto

### First-In-First-Out (FIFO)
- **Tipo**: No apropiativo
- **Ventajas**: Simple, bajo overhead
- **Desventajas**: Efecto convoy, pobre tiempo de respuesta

### Last-In-First-Out (LIFO)
- **Tipo**: No apropiativo
- **Ventajas**: Útil para procesos recientes urgentes
- **Desventajas**: Alto riesgo de inanición

## Métricas Calculadas

Para cada proceso y algoritmo, el sistema calcula:

- **Tiempo Final (tf)**: Cuando termina el proceso
- **Tiempo Total (T)**: tf - ti (tiempo en el sistema)
- **Tiempo de Espera (E)**: T - t (tiempo en cola de listos)
- **Índice de Servicio (I)**: t/T (eficiencia)

## Resultados y Análisis

El programa genera:
- Tablas detalladas por algoritmo
- Promedios de todas las métricas
- Tiempos de ejecución de cada algoritmo
- Recomendación del mejor método según métricas
- Comparación final entre los tres algoritmos

## Estructura del Proyecto

```
SO_RR_FIFO_LIFO/
├── main.py              # Programa principal
├── RR.py               # Algoritmo Round Robin
├── FIFO.py             # Algoritmo FIFO
├── LIFO.py             # Algoritmo LIFO
├── proceso.py          # Clase Proceso
├── data_so.csv         # Datos de procesos
└── README.md           # Este archivo
```

## Autor

- **Luis Álvarez** 

## Contexto Académico

Desarrollado para la cátedra de Sistemas Operativos en la Universidad Rafael Urdaneta, bajo la guia del profesor Mario Gonzalez.
