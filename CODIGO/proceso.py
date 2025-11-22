class Proceso:
    def __init__(self, id_proceso, ti, t):
        self.id = id_proceso
        self.ti = ti
        self.t = t
        self.tf = 0
        self.T = 0
        self.E = 0
        self.I = 0.0
        self.tiempo_restante = t
    
    def __str__(self):
        return "| {:^8} | {:^3} | {:^3} | {:^4} | {:^4} | {:^4} | {:^8.4f} |".format(
            self.id, self.ti, self.t, self.tf, self.T, self.E, self.I)