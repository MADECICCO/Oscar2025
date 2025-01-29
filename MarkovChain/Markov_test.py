
# To calculate the odds of winning each Oscar contender, the same model of Markov Chains can be used, 
# adjusting the initial conditions and transition probabilities based on the historical data 
# and factors specific to each candidate, such as:

  #  Global recognition and previous awards.
   # Engagement on social networks and popularity of performance.
   # Factors related to the film, such as studio, direction, script, etc.
   # Historical tendencies of the Academy to reward certain genres or profiles.

#Adjusted Transition Matrix

# Each actress will have a personalized transition matrix based on the factors cited.
#  For example, the probability of transition between states may vary depending on:

#     Award history: Previously awarded actresses are more likely to advance to the victory state.
#     Films with greater engagement tend to take their actresses further in the process.
 #   Geographic distribution: Non-American actresses may be less likely to win, depending on the history.
#
#

import numpy as np

# Matrizes de transição para cada candidata
P_fernanda = np.array([
    [0.7, 0.3, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.6, 0.4, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.7, 0.3, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.8, 0.2, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.9, 0.1],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
])

P_atriz_a = np.array([
    [0.5, 0.5, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.7, 0.3, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.6, 0.4, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.9, 0.1, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.95, 0.05],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
])

# Lista de todas as matrizes de transição
matrizes = [P_fernanda, P_atriz_a]  # Adicione as outras atrizes aqui

# Estado inicial (todas começam no estado S0)
estado_inicial = np.array([1, 0, 0, 0, 0, 0])

# Iterações (10 passos)
n = 10
probabilidades = []

for P in matrizes:
    estado_atual = estado_inicial
    for _ in range(n):
        estado_atual = np.dot(estado_atual, P)
    probabilidades.append(estado_atual[-1])  # P(S5): Probabilidade de vitória

# Exibir resultados
candidatas = ["Fernanda Torres", "Atriz A"]
for i, prob in enumerate(probabilidades):
    print(f"Probabilidade de {candidatas[i]} vencer o Oscar: {prob:.4f}")
