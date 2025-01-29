
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

import pandas as pd


# Each matrix will be modified to include more progressive transition chances to S5

matrizes_ajustadas = {

    "Demi Moore": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], # S0 -> S1

        [0.0, 0.0, 0.7, 0.3, 0.0, 0.0], # S1 -> S2, S3

        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], # S2 -> S3, S4

        [0.0, 0.0, 0.0, 0.0, 0.7, 0.3], # S3 -> S4, S5

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], # S4 -> S5

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0] # S5 (estado absorvente)

    ]),

    "Karla Sofía Gascón": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.65, 0.35, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.55, 0.45, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.75, 0.25], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Fernanda Torres": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.6, 0.4, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.8, 0.2], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Cynthia Erivo": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.7, 0.3, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.65, 0.35, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.85, 0.15], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Atriz E": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.65, 0.35, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.75, 0.25], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ])

}


# Estado inicial (100% no estado S0)

estado_inicial = np.array([1, 0, 0, 0, 0, 0])




# Recalcular as probabilidades finais

resultados_ajustados = {}

for atriz, matriz in matrizes_ajustadas.items():

    probabilidade_final = np.linalg.matrix_power(matriz, 1000) @ estado_inicial

    resultados_ajustados[atriz] = probabilidade_final[-1]  # Probabilidade de S5



# Criar uma nova tabela com os resultados ajustados

tabela_resultados_ajustados = pd.DataFrame({

    "Atriz": list(resultados_ajustados.keys()),

    "Probabilidade de vencer (%)": [p * 100 for p in resultados_ajustados.values()]

})



tabela_resultados_ajustados.sort_values(by="Probabilidade de vencer (%)", ascending=False, inplace=True)

tabela_resultados_ajustados.reset_index(drop=True, inplace=True)

print(tabela_resultados_ajustados)