from pulp import LpMinimize, LpProblem, LpStatus, LpVariable, lpSum, value

# Definición de datos
origen = ['A', 'B', 'C']
destino = ['1', '2', '3', '4']

oferta = {'A': 1500, 'B': 1500, 'C': 1500}
demanda = {'1': 1000, '2': 1200, '3': 1500, '4': 1000}

costo_envio = {
    'A': {'1': 80, '2': 100, '3': 85, '4': 90},
    'B': {'1': 95, '2': 85, '3': 80, '4': 100},
    'C': {'1': 90, '2': 80, '3': 95, '4': 90}
}

# Crear el problema de optimización
prob = LpProblem('Transporte', LpMinimize)

# Definir rutas y variables de decisión
rutas = [(i, j) for i in origen for j in destino]
cantidad = LpVariable.dicts('Cantidad_de_Envio', (origen, destino), 0)

# Definir la función objetivo
prob += lpSum(cantidad[i][j] * costo_envio[i][j] for (i, j) in rutas), "Costo_Total"

# Agregar restricciones de demanda
for j in destino:
    prob += lpSum(cantidad[i][j] for i in origen) == demanda[j], f"Demanda_{j}"

# Agregar restricciones de oferta
for i in origen:
    prob += lpSum(cantidad[i][j] for j in destino) <= oferta[i], f"Oferta_{i}"

# Resolver el problema
prob.solve()

# Imprimir el estado del problema
print("Estado:", LpStatus[prob.status])

# Imprimir la solución
if LpStatus[prob.status] == 'Optimal':
    for i in origen:
        for j in destino:
            if cantidad[i][j].varValue > 0:
                print(f"Enviar {cantidad[i][j].varValue} unidades desde {i} a {j}")

    # Imprimir el costo total mínimo
    print('El costo mínimo es:', value(prob.objective))
else:
    print("No se encontró una solución óptima.")