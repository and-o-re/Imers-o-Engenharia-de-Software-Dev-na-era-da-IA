# ⚡ CYBERDECK DEV LAB // Desafios Práticos de Programação (Edição Cyberpunk 2077)

> *"Wake the f*ck up, Samurai... temos código para refatorar e testes para rodar."*
> Homenagem especial à **2ª Temporada no universo Cyberpunk** e à **Nova Atualização de Cyberpunk 2077**.

Bem-vindo ao repositório central dos **3 Desafios Práticos de Engenharia de Software**. Este projeto foi estruturado de forma modular para demonstrar a evolução gradual de habilidades fundamentais de desenvolvimento: lógica de programação em Python, evolução arquitetural com testes automatizados e desenvolvimento Front-End interativo com manipulação de DOM.

---

## 🗺️ Estrutura do Repositório

```text
meu-repositorio/
├── .gitignore
├── README.md
├── desafio-01-calculadora-basica/
│   ├── calculadora.py
│   └── README.md
├── desafio-02-calculadora-evolucao/
│   ├── calculadora.py
│   ├── test_calculadora.py
│   └── README.md
└── desafio-03-todo-list/
    ├── index.html
    ├── style.css
    ├── script.js
    └── README.md
```

---

## 🎯 Objetivo dos 3 Desafios

| Desafio | Pasta | Tecnologias | Objetivo Principal |
| :--- | :--- | :--- | :--- |
| **Desafio 01** | [`desafio-01-calculadora-basica/`](./desafio-01-calculadora-basica/) | Python 3 (CLI ANSI) | Construir uma calculadora interativa no terminal com as 4 operações básicas, validação de entradas e tratamento de divisão por zero, estilizada como um terminal **NetWatch / Militech**. |
| **Desafio 02** | [`desafio-02-calculadora-evolucao/`](./desafio-02-calculadora-evolucao/) | Python 3 + `unittest` | Evoluir a base da calculadora adicionando cálculos de **porcentagem** e garantindo a confiabilidade do código por meio de uma suíte de **testes unitários automatizados**. |
| **Desafio 03** | [`desafio-03-todo-list/`](./desafio-03-todo-list/) | HTML5, CSS3, JS Vanilla | Desenvolver uma **Lista de Tarefas (Fixer Contracts / Cyberdeck To-Do)** com interface visual inspirada no HUD de *Cyberpunk 2077*, permitindo adicionar, concluir/desmarcar e remover missões em tempo real. |

---

## 🚀 Como Navegar e Executar os Projetos

### 1️⃣ Desafio 01: Calculadora Básica (Cyberdeck CLI v1.0)
```bash
cd desafio-01-calculadora-basica
python3 calculadora.py
```
📖 Consulte o [README do Desafio 01](./desafio-01-calculadora-basica/README.md) para entender o funcionamento das funções, loops e condicionais.

---

### 2️⃣ Desafio 02: Calculadora Evoluída + Testes (Cyberdeck CLI v2.1)
Para usar a calculadora interativa:
```bash
cd desafio-02-calculadora-evolucao
python3 calculadora.py
```
Para executar a suíte de testes automatizados:
```bash
cd desafio-02-calculadora-evolucao
python3 -m unittest test_calculadora.py -v
```
📖 Consulte o [README do Desafio 02](./desafio-02-calculadora-evolucao/README.md) para detalhes sobre a refatoração e os testes.

---

### 3️⃣ Desafio 03: To-Do List Cyberpunk 2077 (Night City HUD)
Basta abrir o arquivo `desafio-03-todo-list/index.html` diretamente no seu navegador ou iniciar um servidor HTTP local:
```bash
cd desafio-03-todo-list
python3 -m http.server 8080
# Acesse http://localhost:8080 no navegador
```
📖 Consulte o [README do Desafio 03](./desafio-03-todo-list/README.md) para entender a arquitetura HTML/CSS/JS e a manipulação do DOM.

---

## 🛠️ Histórico de Commits Semânticos

O repositório segue o padrão **Conventional Commits**:
- `feat(desafio-1): implementacao da calculadora basica em python`
- `feat(desafio-2): evolucao da calculadora com porcentagem e testes automatizados`
- `feat(desafio-3): criacao da aplicacao to-do list com interface visual`
