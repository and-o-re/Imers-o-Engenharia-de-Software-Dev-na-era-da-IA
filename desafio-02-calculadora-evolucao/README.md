# ⚡ Desafio 02: Evolução da Calculadora com Porcentagem e Testes (`Cyberdeck CLI v2.1`)

Nesta segunda etapa, evoluímos a calculadora do **Desafio 01** simulando um ciclo real de engenharia de software: **adição de uma nova feature (porcentagem)** acompanhada de **testes automatizados** para garantir que nenhuma funcionalidade existente foi quebrada (*regressão zero*).

---

## 🔄 1. Alterações Realizadas em Relação à Primeira Versão

1. **Nova Função `calcular_porcentagem(valor_base, percentual)`**:
   Implementada em [`calculadora.py`](./calculadora.py) com a fórmula `(valor_base * percentual) / 100.0`, permitindo descobrir rapidamente quanto representa `X%` de um valor base (por exemplo, calcular a comissão de um Fixer em Night City!).
2. **Atualização do Dicionário de Operações e Menu HUD**:
   - Adicionada a opção `[5] 📊 Porcentagem (% de um valor)` no painel visual e no dicionário `operacoes`.
3. **Fluxo de Entrada Contextualizado**:
   - Quando o usuário escolhe a opção `5`, os prompts solicitam especificamente o **valor base** e a **porcentagem desejada**, exibindo uma saída semântica clara: `20% de 250 = 50`.
4. **Criação da Suíte de Testes (`test_calculadora.py`)**:
   - Criação do arquivo [`test_calculadora.py`](./test_calculadora.py) utilizando o módulo nativo `unittest` (100% compatível também com `pytest`), cobrindo:
     - `test_somar`: positivos, negativos e números decimais.
     - `test_subtrair`: resultados positivos, negativos e decimais.
     - `test_multiplicar`: inteiros, decimais, números negativos e multiplicação por zero.
     - `test_dividir_valores_validos`: divisões exatas, decimais e numerador zero.
     - `test_dividir_por_zero_lanca_excecao`: verificação com `assertRaises(ValueError)` garantindo proteção contra divisão por zero.
     - `test_calcular_porcentagem`: validação de percentuais inteiros, decimais, `0%` e `100%`.

---

## 🧪 2. Instruções para Rodar os Testes Automatizados

### Opção A: Usando `unittest` (Nativo do Python — Não requer instalação externa)
No terminal, dentro da pasta `desafio-02-calculadora-evolucao/`, execute:

```bash
python3 -m unittest test_calculadora.py -v
```

Saída esperada:
```text
test_calcular_porcentagem (test_calculadora.TestCalculadoraCyberdeck.test_calcular_porcentagem) ... ok
test_dividir_por_zero_lanca_excecao (test_calculadora.TestCalculadoraCyberdeck.test_dividir_por_zero_lanca_excecao) ... ok
test_dividir_valores_validos (test_calculadora.TestCalculadoraCyberdeck.test_dividir_valores_validos) ... ok
test_multiplicar (test_calculadora.TestCalculadoraCyberdeck.test_multiplicar) ... ok
test_somar (test_calculadora.TestCalculadoraCyberdeck.test_somar) ... ok
test_subtrair (test_calculadora.TestCalculadoraCyberdeck.test_subtrair) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### Opção B: Usando `pytest` (Caso esteja instalado no ambiente)
```bash
pytest -v
```

---

## ▶️ Como Executar a Calculadora Interativa

```bash
python3 calculadora.py
```
