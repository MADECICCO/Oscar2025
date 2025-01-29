import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from textblob import TextBlob

# Função para analisar sentimento (simulado)
def analyze_sentiment(nominee):
    sample_tweets = [
        f"{nominee} gave an incredible performance! Oscar-worthy!",
        f"I'm not sure if {nominee} will win, but she deserves the nomination.",
        f"{nominee} is totally overrated. Others did better this year."
    ]
    scores = [TextBlob(tweet).sentiment.polarity for tweet in sample_tweets]
    return np.mean(scores)

# Simulação de dados
atrizes = ["Fernanda Torres", "Demi Moore", "Mikey Madison", "Karla Sofía Gascón", "Cynthia Erivo"]
google_trends = {"Fernanda Torres": 0.45, "Demi Moore": 0.80, "Mikey Madison": 0.60, "Karla Sofía Gascón": 0.75, "Cynthia Erivo": 0.85}
prediction_market_odds = {"Fernanda Torres": 0.10, "Demi Moore": 0.35, "Mikey Madison": 0.15, "Karla Sofía Gascón": 0.25, "Cynthia Erivo": 0.40}

# Pesos
WEIGHT_SENTIMENT = 0.40
WEIGHT_TRENDS = 0.30
WEIGHT_MARKETS = 0.30

# Histórico das probabilidades
num_iteracoes = 50
historico_probabilidades = {atriz: [] for atriz in atrizes}

for _ in range(num_iteracoes):
    sentiment_scores = {nominee: analyze_sentiment(nominee) for nominee in atrizes}
    final_probabilities = {
        nominee: (
            WEIGHT_SENTIMENT * sentiment_scores[nominee] +
            WEIGHT_TRENDS * google_trends[nominee] +
            WEIGHT_MARKETS * prediction_market_odds[nominee]
        )
        for nominee in atrizes
    }
    for atriz in atrizes:
        historico_probabilidades[atriz].append(final_probabilities[atriz] * 100)  # Convertendo para %

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
cores = ["red", "blue", "green", "purple", "orange"]
linhas = {atriz: ax.plot([], [], label=atriz, color=cor)[0] for atriz, cor in zip(atrizes, cores)}

ax.set_xlim(0, num_iteracoes)
ax.set_ylim(0, max([max(probs) for probs in historico_probabilidades.values()]) + 5)
ax.set_xlabel("Iterações")
ax.set_ylabel("Probabilidade de Vitória (%)")
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
