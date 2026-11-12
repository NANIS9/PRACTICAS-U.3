import pandas as pd

datos = {
    "estudiante": [
        "Ana", "Luis", "Maria", "Carlos", "Sofia", "Pedro", "Elena", "Jorge",
    ],
    "horas_estudio": [8, 3, 10, 5, 6, 2, 7, 4],
    "asistencia": [95, 60, 90, 75, 85, 50, 90, 80],
    "actividades_entregadas": [100, 50, 100, 90, 90, 40, 80, 70],
    "calificacion": [92, 50, 90, 72, 85, 58, 80, 65],
}

df = pd.DataFrame(datos)

print("Tabla:")
print(df[["estudiante", "horas_estudio"]])