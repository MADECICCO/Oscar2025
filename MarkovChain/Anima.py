import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Definição das atrizes e matrizes de transição
atrizes = ["Fernanda Torres", "Demi Moore", "Mikey Madison", "Karla Sofía Gascón", "Cynthia Erivo"]

matrizes_transicao = {
    "Fernanda Torres": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],  
        [0.0, 0.0, 0.4, 0.6, 0.0, 0.0],  
        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0],  
        [0.0, 0.0, 0.0, 0.0, 0.2, 0.8],  
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],  
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]   
    ]),
    "Demi Moore": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.5, 0.5, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.3, 0.7], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ]),
    "Mikey Madison": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.3, 0.7, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.25, 0.75], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ]),
    "Karla Sofía Gascón": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.55, 0.45, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.4, 0.6, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.35, 0.65], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ]),
    "Cynthia Erivo": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.6, 0.4, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.55, 0.45, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.4, 0.6], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ])
}

# Estado inicial (todas começam não indicadas)
estado_inicial = np.array([1, 0, 0, 0, 0, 0])

# Evolução das probabilidades ao longo das iterações
num_iteracoes = 50
historico_probabilidades = {atriz: [] for atriz in atrizes}

for atriz, matriz in matrizes_transicao.items():
    estado_atual = estado_inicial.copy()
    for _ in range(num_iteracoes):
        estado_atual = matriz @ estado_atual
        historico_probabilidades[atriz].append(estado_atual[4])  # Estado S4 (vitória)

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
cores = ["red", "blue", "green", "purple", "orange"]
linhas = {atriz: ax.plot([], [], label=atriz, color=cor)[0] for atriz, cor in zip(atrizes, cores)}

ax.set_xlim(0, num_iteracoes)
ax.set_ylim(0, 1)
ax.set_xlabel("Iterações")
ax.set_ylabel("Probabilidade de Vitória")
ax.set_title("Evolução da Probabilidade de Vitória (Oscars 2025)")
ax.legend()

# Função de atualização da animação
def update(frame):
    for atriz, linha in linhas.items():
        linha.set_data(range(frame), historico_probabilidades[atriz][:frame])

# Criar a animação
ani = animation.FuncAnimation(fig, update, frames=num_iteracoes, interval=100)

# Mostrar animação
plt.show()
