# ⚡ Desafio 03: Lista de Tarefas (To-Do List) com Interface Visual Cyberpunk 2077

Bem-vindo à documentação do **Desafio 03**, uma aplicação web de gerenciamento de tarefas (**Fixer Contracts & Missions HUD**) construída com **HTML5, CSS3 e JavaScript puro (Vanilla JS)**, trazendo a estética icônica de **Cyberpunk 2077** em homenagem à 2ª Temporada do anime e à nova atualização do jogo.

---

## 📁 1. Estrutura dos Arquivos

| Arquivo | Responsabilidade Arquitetural |
| :--- | :--- |
| [`index.html`](./index.html) | Define a estrutura semântica da página (`<header>`, `<main>`, `<section>`, `<form>`, `<nav>`, `<ul>`, `<footer>`), acessibilidade (`aria-live`, `aria-checked`, `label`) e importação das fontes *Orbitron*, *Rajdhani* e *Share Tech Mono*. |
| [`style.css`](./style.css) | Implementa a direção de arte **Cyberpunk 2077**: paleta oficial Amarelo Neon (`#fcee0a`), Ciano Kiroshi (`#00f0ff`), Vermelho Glitch (`#ff003c`) e Verde Matrix (`#00ff9d`), recortes angulares com `clip-path: polygon(...)`, efeito de *scanlines* e diferenciação visual clara para tarefas concluídas (texto tachado com `text-decoration: line-through`, borda verde neon e tag `CONTRATO FINALIZADO`). |
| [`script.js`](./script.js) | Gerencia o estado da aplicação, sincroniza os dados com `localStorage` e realiza toda a **manipulação dinâmica do DOM** em resposta aos eventos do usuário. |

---

## ⚡ 2. Como o JavaScript Manipula o DOM

A aplicação segue o padrão **Estado → Renderização (State-Driven UI)**:

### 🔹 1. Captura de Referências do DOM
Ao iniciar, o `script.js` armazena referências para os elementos estáticos principais usando `document.getElementById` e `document.querySelectorAll`:
- `#todo-form`, `#todo-input`, `#todo-priority`: captura da entrada do usuário.
- `#todo-list` (`<ul>`): contêiner onde os itens `<li>` são injetados dinamicamente.
- `#count-total`, `#count-pending`, `#count-completed`: contadores de telemetria no cabeçalho.

### 🔹 2. Adição de Novas Tarefas (`submit` do Formulário)
1. O listener `formElement.addEventListener("submit", ...)` intercepta o envio padrão da página com `evento.preventDefault()`.
2. A função `adicionarTarefa()` valida se o texto não está vazio (`.trim()`), cria um objeto representando a tarefa (`{ id, texto, prioridade, concluida: false }`) e o insere no início do array `tarefas`.
3. Em seguida, chama `renderizarTarefas()`, que reconstrói a lista visual e limpa o campo de entrada (`inputElement.value = ""`).

### 🔹 3. Marcar e Desmarcar Tarefas como Concluídas (`click`)
1. Cada item renderizado possui listeners de clique tanto na área esquerda da tarefa (`leftDiv`) quanto no botão `CONCLUIR / REABRIR`.
2. Ao clicar, a função `alternarConclusaoTarefa(id)` inverte a propriedade booleana `concluida` (`!tarefa.concluida`) daquele item específico usando `Array.prototype.map()`.
3. Na re-renderização, os itens com `concluida === true` recebem a classe CSS `.completed`:
   ```javascript
   li.className = `todo-item ${tarefa.concluida ? "completed" : ""}`;
   ```
4. O CSS aplica automaticamente o **texto tachado** (`text-decoration: line-through`), altera a cor da borda esquerda para **Verde Neon** (`#00ff9d`), preenche o checkbox customizado com `✓` e muda o status para `// STATUS: CONTRATO FINALIZADO`.

### 🔹 4. Remoção de Tarefas Existentes (`click` em `EXPURGAR [X]`)
1. O botão `.delete-btn` de cada item dispara `removerTarefa(tarefa.id)`.
2. A função utiliza `Array.prototype.filter()` para manter apenas as tarefas cujo `id` seja diferente do item excluído.
3. A função `renderizarTarefas()` atualiza imediatamente a `<ul id="todo-list">` e recalcula os contadores do topo (`atualizarContadores()`).

### 🔹 5. Segurança contra XSS na Criação de Elementos
Em vez de concatenar strings do usuário diretamente com `innerHTML`, o texto da tarefa é inserido via `textSpan.textContent = tarefa.texto` após criar os nós com `document.createElement()`. Isso impede que qualquer código HTML ou script digitado no campo de texto seja executado pelo navegador.

---

## ▶️ Como Executar

Abra o arquivo `index.html` diretamente no navegador ou execute um servidor local:

```bash
python3 -m http.server 8080
```
Depois, acesse `http://localhost:8080` no navegador.
