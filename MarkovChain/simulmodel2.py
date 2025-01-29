import numpy as np

# Dados das candidatas
candidatas = {
    "Fernanda Torres": {"globo": 1, "sag": 0, "bafta": 0, "engajamento": 0.6, "campanha": 0.7},
    "Demi Moore": {"globo": 1, "sag": 1, "bafta": 1, "engajamento": 0.9, "campanha": 0.9},
    "Cynthia Erivo": {"globo": 0, "sag": 1, "bafta": 1, "engajamento": 0.8, "campanha": 0.7},
    "Karla Sofía Gascón": {"globo": 0, "sag": 0, "bafta": 0, "engajamento": 0.6, "campanha": 0.8},
    "Mikey Madison": {"globo": 0, "sag": 1, "bafta": 1, "engajamento": 0.7, "campanha": 0.7},
}

# Pesos dos fatores
pesos = {
    "premiacoes": 0.4,  # Globo, SAG, BAFTA
    "engajamento": 0.3,  # Volume e sentimentos nas redes sociais
    "campanha": 0.2,     # Estratégias de marketing
    "historico": 0.1,    # Dados históricos (ajustado para candidatas estrangeiras)
}

# Função para calcular a probabilidade
def calcular_probabilidade(candidata):
    # Pontuação das premiações
    premio_score = (candidata["globo"] + candidata["sag"] + candidata["bafta"]) / 3
    
    # Pontuação total
    score = (
        premio_score * pesos["premiacoes"]
        + candidata["engajamento"] * pesos["engajamento"]
        + candidata["campanha"] * pesos["campanha"]
        - 0.1 * pesos["historico"]  # Penalização para candidatas estrangeiras
    )
    return score

# Cálculo das probabilidades
probabilidades = {}
for nome, dados in candidatas.items():
    probabilidades[nome] = calcular_probabilidade(dados)

# Normalização para somar 100%
total = sum(probabilidades.values())
for nome in probabilidades:
    probabilidades[nome] = (probabilidades[nome] / total) * 100

# Exibição dos resultados
print("Probabilidades de Vitória no Oscar de Melhor Atriz em 2025:")
for nome, prob in probabilidades.items():
    print(f"{nome}: {prob:.2f}%")