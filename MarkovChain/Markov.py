
#Markov's chain, incorporating historical data and specific information from each actress and their respective films.
#  The candidates considered are:

 #   Demi Moore for "The Substance"
 #   Karla Sofía Gascón for "Emilia Pérez"
#    Fernanda Torres for "I'm Still Here"
 #   Cynthia Erivo for "The Brutalist"
 #   Actress And for "Film E"



import numpy as np

import pandas as pd


matrizes = {

    "Demi Moore": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.8, 0.2, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.7, 0.3, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.9, 0.1], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Karla Sofía Gascón": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.7, 0.3, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.85, 0.15], 

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

        [0.0, 0.0, 0.75, 0.25, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.65, 0.35, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.9, 0.1], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Atriz E": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.65, 0.35, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.85, 0.15], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ])

}


# Estado inicial (100% no estado S0)

estado_inicial = np.array([1, 0, 0, 0, 0, 0])



# Calcular a probabilidade final (no estado vencedor S5) para cada atriz

resultados = {}

for atriz, matriz in matrizes.items():

    probabilidade_final = np.linalg.matrix_power(matriz, 1000) @ estado_inicial

    resultados[atriz] = probabilidade_final[-1]  # Probabilidade de S5



# Criar uma tabela com os resultados

tabela_resultados = pd.DataFrame({

    "Atriz": list(resultados.keys()),

    "Probabilidade de vencer (%)": [p * 100 for p in resultados.values()]

})



tabela_resultados.sort_values(by="Probabilidade de vencer (%)", ascending=False, inplace=True)

tabela_resultados.reset_index(drop=True, inplace=True)

tabela_resultados
