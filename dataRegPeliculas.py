import json

class peliculas:
    peMM = []
    def readRegPeliculas(self):
        with open('data/peliculas.json','r') as file:
            peMM = json.load(file)
            self.peMM = peMM['results']
    def getPelicula(self):
        regPeliculas = []
        for row in self.peMM:
            p = row['titulo']
            if p not in regPeliculas:
                regPeliculas.append(p)
        return regPeliculas