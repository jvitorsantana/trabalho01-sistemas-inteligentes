import random
random.seed(98)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

def plotar_ambiente(M, N):
  porcentagem_obstaculos = 0.20
  porcentagem_sujeiras = 0.10
  LIVRE, OBSTACULO, SUJEIRA, ROBO = 0, 1, 2, 3
  CORES = ["#fcfcfb", "#0f0f0f", "#cde2fb"]
  FUNDO = "#f0efec"

  matriz = np.zeros((M, N), dtype=int)

  total_posicoes = M*N
  total_obstaculos = round(total_posicoes * porcentagem_obstaculos)
  total_sujeiras = round(total_posicoes * porcentagem_sujeiras)

  posicoes = [(linha, coluna)
              for linha in range(M)
              for coluna in range(N)]
  
  posicoes_obstaculos = random.sample(posicoes, total_obstaculos)
  for linha, coluna in posicoes_obstaculos:
      matriz[linha, coluna] = OBSTACULO

  posicoes_livres = [(linha, coluna)
                    for linha in range(M)
                    for coluna in range(N)
                    if matriz[linha, coluna] == LIVRE]

  posicoes_sujeiras = random.sample(posicoes_livres, total_sujeiras)

  for linha, coluna in posicoes_sujeiras:
      matriz[linha, coluna] = SUJEIRA

  linha_robo, coluna_robo = random.choice(posicoes_livres)
  matriz[linha_robo, coluna_robo] = ROBO


  fig, ax = plt.subplots(figsize=(0.7 * N, 0.7 * M))
  fig.patch.set_facecolor(FUNDO)
  ax.imshow(matriz, cmap=ListedColormap(CORES), vmin=LIVRE, vmax=SUJEIRA)

  for linha, coluna in posicoes_sujeiras:
      ax.text(coluna, linha, "•", fontsize=12,
              ha="center", va="center")
  ax.text(coluna_robo, linha_robo, "🧹", fontname='Segoe UI Emoji', fontsize=12,
          ha="center", va="center")

  ax.set_xticks(range(N))
  ax.set_yticks(range(M))
  ax.xaxis.set_ticks_position("top")
  ax.set_xticks([x - 0.5 for x in range(N + 1)], minor=True)
  ax.set_yticks([y - 0.5 for y in range(M + 1)], minor=True)
  ax.grid(which="minor", color="#000000", linewidth=1)
  ax.tick_params(which="both", length=0, colors="#898781")

  plt.show()