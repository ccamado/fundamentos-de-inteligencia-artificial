# MBNC — 2º A — Fundamentos de Aprendizado Profundo
# Exemplo didático: transformar uma sequência em pares entrada/alvo.
# Este programa NAO treina uma rede neural.

serie = [10, 12, 14, 16, 18]  # dados fictícios em ordem temporal
janela = 3  # número de valores conhecidos em cada entrada

for i in range(len(serie) - janela):  # percorre janelas válidas
    entrada = serie[i:i + janela]  # valores que o modelo receberia
    alvo = serie[i + janela]  # próximo valor realmente observado
    print(f"Entrada: {entrada} -> Alvo: {alvo}")

# Saída esperada:
# Entrada: [10, 12, 14] -> Alvo: 16
# Entrada: [12, 14, 16] -> Alvo: 18
