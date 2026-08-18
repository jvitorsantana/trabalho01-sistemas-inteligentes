def add_visitado(l, c, visitados):
    visitados.append((l, c))

def limpar(matriz, l, c, linhas, colunas, visitados):
  if(l < 0 or l >= linhas or c < 0 or c >= colunas):
    return
  if(matriz[l][c] == 1):
    return
  if(matriz[l][c] == 2):
    print(f"Sujeira limpa ({l}, {c})")
    matriz[l][c] = 0

  if (l, c) in visitados:
    return
  
  add_visitado(l, c)
  
  limpar(matriz,l - 1, c, linhas, colunas)
  limpar(matriz,l + 1, c, linhas, colunas)
  limpar(matriz,l, c - 1, linhas, colunas)
  limpar(matriz,l, c + 1, linhas, colunas)