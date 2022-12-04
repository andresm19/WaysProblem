
import datetime
import numpy.random as random

t = datetime.datetime(year=2022, month=12, day=1, hour=0, minute=0, second=0, microsecond=0)
delta = datetime.timedelta(0, 0, 0, 0, 0, 1, 0)
fin = datetime.datetime(2022, 12, 2, 0, 0, 0, 0)
prolluvia = 0.3

random.seed(1)

class Via():
    def __init__(self, nombre, km, carriles, semaforos):
        self.nombre = nombre
        self.km = km
        self.carriles = carriles
        self.semaforos = semaforos
        self.plluvia, self.ptrafico, self.paccidente = (0, 0, 0)
        self.lluvia, self.trafico, self.accidente = (False, False, False)
        self.probabilidades = dict()

    def start(self, p_lluvia, p_trafico, p_accidente):
        self.plluvia = p_lluvia
        self.ptrafico = p_trafico
        self.paccidente = p_accidente

    def evaluate(self):
        global prolluvia, t

        if t.hour % 24 < 5:
            self.plluvia = (self.plluvia + 0.8) / 2
        elif t.hour < 14 and t.hour > 11:
            self.plluvia = (self.plluvia + 1) / 2
        elif t.hour > 20 and t.hour < 25:
            self.plluvia = (self.plluvia + 0.9) / 2
        else:
            self.plluvia = prolluvia 

        self.plluvia = round(self.plluvia, 2)

        x = random.choice(2, 1, p=[1-self.plluvia, self.plluvia])
        if  x == [1]:
            self.lluvia = True
        else:
            self.lluvia = False
        
        print("Ciudad " + self.nombre + "  |   Lluvia =", self.lluvia, "con probabilidad de lluvia de", self.plluvia)
        
    
    def update(self):
        if self.lluvia: self.plluvia = 0.7
        self.evaluate()

class Ciudad():
    def __init__(self, vias):
        self.vias = vias

    def update(self):
        global t, delta
        print(t.strftime('%d / %m / %Y   son las   %H:%M'))
        for via in self.vias:
            via.update()

