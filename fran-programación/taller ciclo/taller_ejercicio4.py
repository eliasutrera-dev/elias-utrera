# Ejercicio 4 - Notas de estudiantes

notas_estudiantes = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

calificaciones_estudiantes = {}

for estudiante in notas_estudiantes:

    nota = notas_estudiantes[estudiante]

    if nota >= 91:
        calificacion = "Sobresaliente"
    elif nota >= 81:
        calificacion = "Supera las expectativas"
    elif nota >= 71:
        calificacion = "Aceptable"
    else:
        calificacion = "Reprobado"

    calificaciones_estudiantes[estudiante] = calificacion

print("Calificaciones de los estudiantes:")

for estudiante in calificaciones_estudiantes:
    print(estudiante, ":", calificaciones_estudiantes[estudiante])