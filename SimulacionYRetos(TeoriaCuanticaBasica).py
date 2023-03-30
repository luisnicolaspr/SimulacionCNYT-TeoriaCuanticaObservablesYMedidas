import numpy as np

'''Simulación del sistema cuántico descrito en la sección 4.1'''

n = 5  # Número de posiciones
psi = np.random.rand(n) + 1j * np.random.rand(n)
psi /= np.linalg.norm(psi)  # Normalizamos el vector

pos = 2  # Posición de interés
prob = np.abs(psi[pos])**2
print(f"La probabilidad de encontrar la partícula en la posición {pos} es {prob:.4f}")

phi = np.random.rand(n) + 1j * np.random.rand(n)  # Nuevo vector ket
phi /= np.linalg.norm(phi)
amp = np.vdot(phi, psi)  # Amplitud de transición
prob = np.abs(amp)**2
print(f"La probabilidad de transitar de psi a phi es {prob:.4f}")




'''Retos de programación del capítulo 4'''

#----------Programming Drill 4.1.1----------

#Amplitud de transición
#Dado dos vectores ket, podemos calcular la amplitud detransición como el producto interno conjugado de los dos vectores:

import numpy as np

def transition_amplitude(psi_1, psi_2):
    """Calcula la amplitud de transición entre dos vectores."""
    return np.dot(np.conj(psi_2), psi_1)

  
    
#----------Programming Drill 4.2.1----------

#Media y varianza de un observable
#Dado un observable representado por una matriz hermitiana A y un vector ket psi, podemos calcular la media y varianza del observable en el estado dado:

import numpy as np

def observable_mean_variance(obs, state):
    # Revisar si la matriz es hermitiana
    if not np.allclose(obs, np.conj(obs).T):
        return "La matriz no es hermitiana"

    # Calcular la media
    mean = np.dot(np.conj(state).T, np.dot(obs, state)).real

    # Calcular la varianza
    var = np.dot(np.conj(state).T, np.dot(obs**2, state)).real - mean**2

    return mean, var


#----------Programming Drill 4.3.1----------

#El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

def observable_eigenstates(obs):
    # Revisar si la matriz es hermitiana
    if not np.allclose(obs, np.conj(obs).T):
        return "La matriz no es hermitiana"

    # Calcular los valores propios y vectores propios
    eigvals, eigvecs = np.linalg.eig(obs)

    # Calcular la probabilidad de transitar a los vectores propios
    probs = np.abs(np.dot(np.conj(eigvecs).T, np.array([1, 0])))**2

    return eigvals, eigvecs, probs

#----------Programming Drill 4.4.1----------

#Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

def evolve(initial_state, U):
    final_state = initial_state
    for i in range(len(U)):
        final_state = np.dot(U[i], final_state)
    return final_state







'''Ejemplos de problemas:'''

#4.3.1: Simular la operación de la compuerta de Hadamard en un qubit en el estado |0>.

# Estado inicial
initial_state = np.array([1, 0])

# Matriz de Hadamard
H = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
              [1/np.sqrt(2), -1/np.sqrt(2)]])

# Aplicar la compuerta de Hadamard
final_state = np.dot(H, initial_state)

# Probabilidades de obtener 0 y 1
p0 = np.abs(final_state[0])**2
p1 = np.abs(final_state[1])**2

print(f"Estado final: {final_state}")
print(f"Probabilidad de obtener 0: {p0}")
print(f"Probabilidad de obtener 1: {p1}")



#4.3.2: Simular la operación de la compuerta CNOT en un sistema de dos qubits en el estado |00>.

import numpy as np

# Definir los estados
state_initial = np.array([1, 0, 0, 1]) / np.sqrt(2)
state_final = np.array([0, 1, 1, 0]) / np.sqrt(2)

# Construir el operador de Hadamard tensorizado con la matriz identidad
hadamard = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
operator = np.kron(hadamard, np.identity(2))

# Evolucionar el estado inicial
state_evolved = operator @ state_initial

# Calcular la probabilidad de obtener el estado final
prob = np.abs(state_final @ state_evolved)**2

print("La probabilidad de obtener el estado final es:", prob)


#4.4.1: Supongamos que tenemos un sistema cuántico de 3 qubits y un observable A que se puede representar mediante la siguiente matriz hermitiana,Además, consideremos el siguiente estado inicial:    |ψ> = 1/2 |000> + 1/2 |011> + 1/2 |110> + 1/2 |101> Usando nuestra librería de computación cuántica, podemos calcular la media y varianza de A en el estado |ψ>:

import numpy as np
from quantum_computing import *

# Definir matriz A y vector ket psi
A = np.array([[2, 1, 1, 1],
              [1, 0, 0, -1j],
              [1, 0, 0, 1j],
              [1, -1j, 1j, 0]])
psi = np.array([1/2, 0, 0, 1/2, 0, 0, 1/2, 0])

# Verificar si A es hermitiana
if is_hermitian(A):
    # Calcular media y varianza de A en el estado psi
    mean_A = np.real(expectation_value(A, psi))
    var_A = np.real(variance(A, psi))
    print("Media de A en el estado |ψ>: ", mean_A)
    print("Varianza de A en el estado |ψ>: ", var_A)
else:
    print("La matriz A no es hermitiana.")

#4.4.2 Ahora queremos calcular los valores propios de A y la probabilidad de transitar a cada uno de los vectores propios después de la observación.Usando nuestra librería de computación cuántica, podemos hacer lo siguiente:

import numpy as np
from quantum_computing import *

# Definir matriz A
A = np.array([[2, 1, 1, 1],
              [1, 0, 0, -1j],
              [1, 0, 0, 1j],
              [1, -1j, 1j, 0]])

# Calcular valores propios y vectores propios de A
eigvals, eigvecs = np.linalg.eig(A)

# Calcular probabilidad de transitar a cada vector propio después de la observación
psi = np.array([1/2, 0, 0, 1/2, 0, 0, 1/2, 0])
prob_eigvals = []
for i in range(len(eigvecs)):

    psi = np.array([1/2, 0, 0, 1/2, 0, 0, 1/2, 0])
    prob_eigvals = []
    for i in range(len(eigvals)):
    P = projection_operator(eigvecs[:, i])
    prob_eigvals.append(quantum_prob(P @ psi))

print("Valores propios:", eigvals)
print("Probabilidades de transitar a cada vector propio después de la observación:", prob_eigvals)
               
