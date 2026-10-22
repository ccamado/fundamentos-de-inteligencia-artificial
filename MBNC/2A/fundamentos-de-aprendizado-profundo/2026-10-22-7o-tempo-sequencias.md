# MBNC · 2º A · Fundamentos de Aprendizado Profundo
## Aula de 22/10/2026 · 7º tempo — Dados sequenciais e previsão
**Material de estudo — professor Claudio Amado**  
**Situação:** material preparado, não confirmado como ministrado. A aula prevista para 21/10 sobre LSTM/GRU exige verificação de execução.

### Dados sequenciais
Em uma sequência, **a ordem é importante**: temperatura por hora, palavras em frase ou consumo por dia. Redes recorrentes (**RNN**) combinam o dado atual com informação de passos anteriores. Redes **LSTM** e **GRU** incluem mecanismos de memória e portas, úteis para aprender dependências mais longas.

### Janela de entrada e alvo
Série fictícia: 10, 12, 14, 16, 18.
- Entrada [10, 12, 14] → próximo valor observado (alvo): **16**.
- Entrada [12, 14, 16] → alvo: **18**.

A hipótese de próximo valor **20** é uma extrapolação manual da progressão, **não** uma previsão obtida de uma rede neural treinada. Dados reais podem mudar de padrão.

### Prática guiada
**Série A:** 4, 6, 8, 10, 12, 14. Forme duas janelas de três termos com seus alvos. Qual valor viria depois se o padrão continuasse?

**Série B:** 7, 7, 8, 9, 11, 14. Forme duas janelas de três termos com alvos. Por que uma regra simples pode falhar?

Explique: o que é entrada? O que é alvo? Por que respeitar a ordem temporal? Que risco existe em prever valores futuros?

### Código Python curto (sem bibliotecas externas)
Arquivo: [janelas_temporais.py](janelas_temporais.py). Esse código apenas **prepara exemplos de treino**; não treina uma rede neural.

<details><summary>Gabarito de conferência</summary>
A: [4, 6, 8]→10; [6, 8, 10]→12. Se a progressão continuar, valor seguinte 16, sem garantia. B: [7, 7, 8]→9; [7, 8, 9]→11. As diferenças variam; extrapolações simples podem falhar. É importante separar dados de treino e teste respeitando o tempo.
</details>

**Plano completo do professor:** https://docs.google.com/document/d/1o2kWIPziUQnG4evyVwY-MRuyNCSH-TnX3DXbJ-Wu1Jg/edit
