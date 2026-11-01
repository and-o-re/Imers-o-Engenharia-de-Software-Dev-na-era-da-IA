# ⚡ Desafio 01: Calculadora Básica em Python (`Cyberdeck CLI v1.0`)

Bem-vindo à documentação didática da **Calculadora Básica em Python**, estilizada com a identidade visual de terminal **Cyberpunk 2077** em homenagem à 2ª Temporada do anime e à nova atualização do jogo.

---

## 🧩 1. Principais Componentes do Código

O arquivo [`calculadora.py`](./calculadora.py) foi construído aplicando o princípio de **Responsabilidade Única** (cada função resolve um problema específico):

### 🔹 Funções Matemáticas Puras
Separamos os cálculos puros da interface de terminal. Isso torna o código limpo, legível e fácil de reaproveitar:
- `somar(a, b)`: Retorna `a + b`.
- `subtrair(a, b)`: Retorna `a - b`.
- `multiplicar(a, b)`: Retorna `a * b`.
- `dividir(a, b)`: Verifica se `b == 0` antes de dividir. Caso seja zero, lança uma exceção `ValueError` para impedir que o programa quebre com `ZeroDivisionError` sem tratamento amigável.

### 🔹 Estruturas de Repetição (`while True`)
O projeto utiliza dois loops `while True` estratégicos:
1. **Loop Principal (`executar_calculadora`)**: Mantém o terminal ligado continuamente para que o usuário possa realizar várias operações seguidas até digitar `0` (comando `break`).
2. **Loop de Validação (`ler_numero`)**: Garante que, se o usuário digitar letras ou símbolos inválidos (ex.: `"abc"`), o programa não trave; ele captura o `ValueError` com `try/except` e pede o número novamente.

### 🔹 Estruturas Condicionais (`if`, `not in`, `try/except`)
- `if opcao == "0"`: Encerra a aplicação de forma segura.
- `if opcao not in operacoes`: Intercepta opções inválidas no menu e usa `continue` para reiniciar o ciclo do menu.
- `if b == 0`: Protege a operação de divisão contra divisão por zero.

---

## 🎛️ 2. Recebimento de Entradas e Identificação da Operação

1. **Menu de Seleção**: A função `exibir_painel()` apresenta as opções numeradas de `1` a `4` (e `0` para sair).
2. **Leitura da Opção**: Usamos `input().strip()` para remover espaços extras acidentais antes ou depois da digitação.
3. **Mapeamento por Dicionário (`operacoes`)**:
   Em vez de uma longa cadeia de `if/elif/elif`, utilizamos um dicionário que associa o código digitado a uma tupla contendo `(simbolo, funcao, nome_operacao)`:
   ```python
   operacoes = {
       "1": ("+", somar, "ADIÇÃO"),
       "2": ("-", subtrair, "SUBTRAÇÃO"),
       "3": ("*", multiplicar, "MULTIPLICAÇÃO"),
       "4": ("/", dividir, "DIVISÃO"),
   }
   ```
4. **Conversão Segura dos Operandos**: A função `ler_numero()` aceita tanto ponto (`.`) quanto vírgula (`,`) como separador decimal (`.replace(",", ".")`) e converte a string para `float`.

---

## ⚙️ 3. Execução dos Cálculos e Exibição dos Resultados

1. Após validar a opção escolhida, desempacotamos a função correspondente:
   ```python
   simbolo, funcao, nome_operacao = operacoes[opcao]
   ```
2. Coletamos `num1` e `num2` através de `ler_numero()`.
3. Executamos `resultado = funcao(num1, num2)` dentro de um bloco `try/except ValueError`.
4. **Caso de Sucesso**: O resultado é formatado com `:g` (que remove zeros decimais desnecessários, exibindo `10` em vez de `10.0`, mas mantendo casas decimais quando existem, como `2.5`) e impresso em **Verde Matrix** no terminal.
5. **Caso de Divisão por Zero**: O bloco `except ValueError` captura o erro lançado por `dividir()` e exibe um alerta em **Vermelho Glitch**, retornando ao menu principal sem interromper a execução do programa.

---

## ▶️ Como Executar

```bash
python3 calculadora.py
```
