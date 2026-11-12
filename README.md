# IPPy 2026/27 – Resolução das Fichas Práticas

Introdução à Programação em Python – TeSP Análise de Dados

Uma pasta por ficha, um ficheiro por exercício (`exNN_descricao.py`). A Ficha 3 segue a
numeração das secções (`ex3_1_05_...` = secção 3.1, exercício 5).

| Pasta | Matéria | Notas |
|---|---|---|
| `Ficha2` | Algoritmos | Pseudocódigo + fluxogramas (Mermaid) em `Ficha2_Algoritmos.md` |
| `Ficha3` | Tipos de dados | Ainda sem `if`, ciclos nem funções |
| `Ficha4` | `if` | Sem ciclos nem funções |
| `Ficha5` | `for` / `while` | Sem funções |
| `Ficha6` | `def` | Ex 7 f) usa **dois ficheiros**: `ex07f_modulo_circulo.py` (módulo) e `ex07f_programa.py` (executar este) |
| `Ficha7` | Strings | Ex 1–3 iguais à Ficha 3 (secção 3.3) |
| `Ficha8` | Tuplos | Só tuplos (sem listas nem dicionários) |
| `Ficha9` | Listas | |
| `Ficha10` | Dicionários | |
| `Ficha11` | Ficheiros | Executar o `ex01` antes do `ex02` (cria `texto3.txt`). Os ficheiros são criados na pasta de trabalho |
| `Ficha12` | Gráficos | `matplotlib` + `numpy` |
| `Extra_ExercicioGrupo_Atletas` | Exercício de grupo (Testes/exercicio_grupo.txt) | Só tuplos |

A Ficha 1 (ambiente informático) não tem exercícios de programação.

## Regras da UC respeitadas (cap. 00 – boas práticas)

Não se usa: `break`, `continue`, `else` em ciclos, `while True`, `global`, `match`,
`try/except`, `def main()`, `if __name__ == "__main__":`, nem funções dentro de funções.
Estrutura de cada ficheiro: imports → funções → programa. Valores passados por parâmetro e
devolvidos com `return`.

## Resoluções que vieram do ficheiro Colab (e o que foi ajustado)

- **F3.3 Ex 3**, **F4 Ex 4, 10, 14, 17, 20**, **F5 Ex 3, 5, 6, 8**, **F6 Ex 5–8**,
  **F7 Ex 4, 6**, **F8 Ex 1, 3, 4**, **F9 Ex 1–3** e o exercício de grupo dos atletas.
- Correções feitas:
  - F4 Ex 3 alternativo: o número de jogos usa `(n_equipas - 1) * 2` em vez de `18 * 2 - 2`.
  - F4 Ex 10: acrescentado o caso do número negativo.
  - F4 Ex 14: `angle % 360` e caso "sobre um eixo" (90, 180, ...).
  - F4 Ex 20: acrescentado o caso sem infração e a inibição/proibição de conduzir.
  - F5 Ex 14: um Enter vazio terminava o ciclo (`"" in ".!?"` é `True`).
  - F5 Ex 18: reescrito **sem `break`**; corrigido o "Perdeu" que aparecia ao acertar na 5.ª tentativa.
  - F6 Ex 6: faltava o `print`; lista dos meses passou a tuplo (listas só na Ficha 9).
  - F7 Ex 4: o `return False` dentro do ciclo passou a variável de controlo.
  - F8 Ex 1 b): "pares da forma (n, n²)" são pares ordenados para todos os n (não só os n pares); e) não tinha `return t`.
  - F8 Ex 4: divisão por zero numa palavra sem vogais.
  - F9 Ex 1 b): os *n* primeiros múltiplos de 6 (coerente com a F8 Ex 1 a)).
  - Atletas: a média dividia por todos os atletas (incluindo tempos inválidos);
    validação da opção do menu e do dorsal (pedida no enunciado).

## Pressupostos assumidos

- **Avaliação de Programação** (F3 Ex 9, F4 Ex 13, F9 Ex 10, F12 Ex 7): PE1 30% + PE2 30% +
  Trabalho 40%, aprovação a partir de 9.5 (constante `NOTA_MINIMA` no topo dos ficheiros).
- F4 Ex 19: os intervalos que a tabela não cobre (]35, 36[ e ]37.5, 37.8[) têm classificação própria.
- F4 Ex 22: IRS simplificado (taxa normal sobre todo o rendimento, sem parcela a abater).
- F10 Ex 6: a fórmula do metabolismo basal (Harris-Benedict) está em unidades imperiais;
  a altura e o peso são convertidos para polegadas e libras.
