# El problema de la mochila es un problema de optimización en el que se tienen una serie de objetos con un valor y un peso específicos 
# y se busca seleccionar un conjunto de estos objetos para obtener el máximo valor posible dentro de un límite de peso establecido.

#generador de variables random
import random

# Función evaluar calcula el valor total de los objetos seleccionados y compara si el peso total de estos no supera el peso total máximo
def evaluate(items, knapsack_weight, solution):
    total_value = 0 #inicializamo el valor
    total_weight = 0 #inicializamos peso
    for i in range(len(items)): #seleccion de los objetos
        if solution[i] == 1:
            total_value += items[i][0] 
            total_weight += items[i][1]
    if total_weight > knapsack_weight: #comparativa del peso total contra el peso de la mochila
        return [0, total_weight] 
    else:
        return (total_value, total_weight)
        

# Función vecino: genera una solución vecina a la sol actual,
def generate_neighbor(solution):
    neighbor = solution[:]
    i = random.randint(0, len(solution)-1)
    neighbor[i] = 1 - neighbor[i]
    return neighbor

# Inicializar la solución: inicializa la solucion al azar
def initialize_solution(n):
    return [random.randint(0,1) for i in range(n)] # N NUMERO DE ITERACIONES

#Algoritmo de Hill climbing: genera soluciones vecinas, evaluza las puntiaciones y act la sol actual si encuentra una sol vecina mejor.
def hill_climbing(items, knapsack_weight, n_iter): #RECIBE DATOS LOS ITEMS EL PESO Y LAS ITERACIONES PARAMETROS
    current_solution = initialize_solution(len(items))# N TAMAÑO DE LOS ITEMS LEN CUENTO LA LONGITUD DEL ARREGLO
    current_value, total_weight = evaluate(items, knapsack_weight, current_solution) #FUNCIONES EVALUETE obtener la knapsack_weight con cada iteración y la mejor solución presente
    PesoFinal = total_weight
    print("El valor actual es: " + str(current_value) +" con peso un peso de: "+str(total_weight))
    for i in range (n_iter): 
        neighbor = generate_neighbor(current_solution)
        neighbor_value, total_weight = evaluate(items, knapsack_weight, neighbor)
        if neighbor_value > current_value:  #DESCARTA LA PEOR SOLUCION
            current_value = neighbor_value
            current_solution = neighbor
            PesoFinal = total_weight
            print("En la iteracion: " + str(i) + " se escogio: "+ str(current_solution) +" con el valor de: "+ str(current_value)+" con un peso de: "+str(total_weight))
    return current_solution, current_value, PesoFinal


#Uso con items definidos y peso definido
items = [[4,12],[2,1],[2,2],[1,1],[10,4]]  #LISTA DE ITEMS
knapsack_weight = 15  #PESO DE LA MOCHILA
solution, value, pesoFinal = hill_climbing(items, knapsack_weight,10) #10 NUMERO DE ITARACIONES, ASIGANAR VALORES HILL_CLIMBING
print("Items seleccionados:", [items[i] for i in range(len(items)) if solution[i] == 1])
print("Valor total:", value) #solucion peso y valor
print("El peso final es: ", pesoFinal)