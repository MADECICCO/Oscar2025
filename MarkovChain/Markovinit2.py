# Refinamento do Modelo

# Refinement of the model

 #   Real data to estimate objections:
#        Use databases such as the IMDb, Academy Awards, and social networks to tweak P(Si-> Si+1) .
#    The Impact of Trends:
#        Incorporate social networks using sentiment and trend analysis (e.g., Twitter, Google Trends).
#    Assessment based on Competitor:
#        Analyze competitiveness in specific years.
#        Estimate weights based on the involvement of big studios like Netflix, Amazon, or A24.

        
import numpy as np

# Definir a matriz de transição baseada em probabilidades estimadas
transition_matrix = np.array([
    [0.7, 0.3, 0.0, 0.0, 0.0, 0.0],  # S0: Atriz não associada a filme
    [0.0, 0.6, 0.4, 0.0, 0.0, 0.0],  # S1: Filme submetido ao Oscar
    [0.0, 0.0, 0.7, 0.3, 0.0, 0.0],  # S2: Filme pré-selecionado
    [0.0, 0.0, 0.0, 0.8, 0.2, 0.0],  # S3: Filme indicado ao Oscar
    [0.0, 0.0, 0.0, 0.0, 0.9, 0.1],  # S4: Atriz indicada
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]   # S5: Atriz vencedora
])

# Probabilidade inicial (estado S0)
initial_state = np.array([1, 0, 0, 0, 0, 0])  # Inicia no estado S0

# Simular até a convergência
current_state = initial_state
steps = 10
for _ in range(steps):
    current_state = np.dot(current_state, transition_matrix)

# Probabilidade final de Fernanda Torres ganhar o Oscar
final_probability = current_state[-1]  # Estado S5
print(f"Probabilidade de Fernanda Torres ganhar o Oscar: {final_probability:.4f}")
