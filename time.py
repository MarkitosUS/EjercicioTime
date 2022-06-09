import time
from datetime import datetime


HORA_DE_SALIDA = 19

tiempo_actual = time.localtime()

if tiempo_actual.tm_hour > HORA_DE_SALIDA:
    print("Es hora de ir a casa")
else:
    hora_de_salida = datetime.now().replace(hour=HORA_DE_SALIDA, minute=0)
    diff = hora_de_salida - datetime.now() 
    print(f"Para ir a casa quedan: {diff.seconds//3600} horas {(diff.seconds//60)%60} minutos")