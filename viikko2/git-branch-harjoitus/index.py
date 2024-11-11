# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaanpas tästä")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") # muutos mainissa
print(f"{x} - {y} = {erotus(x, y)}") # muutos mainissa

logger("lopetetaan")
print("goodbye")
