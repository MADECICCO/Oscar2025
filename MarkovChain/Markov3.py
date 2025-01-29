

import numpy as np

import pandas as pd


# Each matrix will be modified to include more progressive transition chances to S5

matrizes_corrigidas = {

    "Demi Moore": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.6, 0.4, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.6, 0.4], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Karla Sofía Gascón": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.55, 0.45, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.4, 0.6, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.5, 0.5], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Fernanda Torres": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.5, 0.5, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.4, 0.6, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.3, 0.7], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Cynthia Erivo": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.65, 0.35, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.55, 0.45, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.4, 0.6], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ]),

    "Atriz E": np.array([

        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 

        [0.0, 0.0, 0.6, 0.4, 0.0, 0.0], 

        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0], 

        [0.0, 0.0, 0.0, 0.0, 0.4, 0.6], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 

        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

    ])

}






# Estado inicial (100% no estado S0)

estado_inicial = np.array([1, 0, 0, 0, 0, 0])


# Recalcular novamente as probabilidades finais



for atriz in matrizes_corrigidas:

    matriz = matrizes_corrigidas[atriz]

    matriz[3, 4] = 0.7  # Ajuste na transição para S4 -> S5 (decisiva)

    matriz[3, 5] = 0.3  # Ajuste na transição para S4 -> S6

    matriz[4, 5] = 1.0  # S5 sendo absorvente

    matrizes_corrigidas[atriz] = matriz

resultados_corrigidos = {}

for atriz, matriz in matrizes_corrigidas.items():

    probabilidade_final = np.linalg.matrix_power(matriz, 1000) @ estado_inicial

    resultados_corrigidos[atriz] = probabilidade_final[-1]  # Probabilidade de S5



# Criar a nova tabela com os resultados corrigidos

tabela_resultados_corrigidos = pd.DataFrame({

    "Atriz": list(resultados_corrigidos.keys()),

    "Probabilidade de vencer (%)": [p * 100 for p in resultados_corrigidos.values()]

})



tabela_resultados_corrigidos.sort_values(by="Probabilidade de vencer (%)", ascending=False, inplace=True)

tabela_resultados_corrigidos.reset_index(drop=True, inplace=True)

print(tabela_resultados_corrigidos)