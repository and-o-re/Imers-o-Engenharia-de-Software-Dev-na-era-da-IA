/**
 * Desafio 03: Lista de Tarefas (To-Do List) com Interface Visual Cyberpunk 2077
 * Manipulação de DOM com JavaScript Puro (Vanilla JS) + Persistência em localStorage
 */

const STORAGE_KEY = "cyberpunk_2077_todo_contracts_v2";

// Contratos iniciais temáticos caso seja o primeiro acesso do usuário
const CONTRATOS_INICIAIS = [
  {
    id: "gig-2077-1",
    texto: "Calibrar implantes ópticos Kiroshi para o Patch 2.2",
    prioridade: "ALTA",
    concluida: true,
  },
  {
    id: "gig-2077-2",
    texto: "Encontrar Lucy e Falco no Afterlife (Homenagem Temporada 2)",
    prioridade: "ALTA",
    concluida: false,
  },
  {
    id: "gig-2077-3",
    texto: "Executar suíte de testes unitários no Cyberdeck Arasaka",
    prioridade: "MEDIA",
    concluida: false,
  },
];

// Estado da aplicação
let tarefas = carregarTarefas();
let filtroAtual = "all";

// Seletores de elementos do DOM
const formElement = document.getElementById("todo-form");
const inputElement = document.getElementById("todo-input");
const prioritySelect = document.getElementById("todo-priority");
const listElement = document.getElementById("todo-list");
const emptyStateElement = document.getElementById("empty-state");
const countTotalElement = document.getElementById("count-total");
const countPendingElement = document.getElementById("count-pending");
const countCompletedElement = document.getElementById("count-completed");
const filterButtons = document.querySelectorAll(".filter-btn");

/**
 * Carrega a lista de tarefas do localStorage ou retorna os contratos iniciais.
 */
function carregarTarefas() {
  try {
    const dadosSalvos = localStorage.getItem(STORAGE_KEY);
    if (dadosSalvos) {
      return JSON.parse(dadosSalvos);
    }
  } catch (erro) {
    console.warn("Não foi possível acessar o localStorage:", erro);
  }
  return [...CONTRATOS_INICIAIS];
}

/**
 * Salva o estado atual das tarefas no localStorage.
 */
function salvarTarefas() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tarefas));
  } catch (erro) {
    console.warn("Não foi possível salvar no localStorage:", erro);
  }
}

/**
 * Adiciona uma nova tarefa à lista e atualiza o DOM.
 */
function adicionarTarefa(texto, prioridade = "MEDIA") {
  const textoLimpo = texto.trim();
  if (!textoLimpo) return;

  const novaTarefa = {
    id: `gig-${Date.now()}-${Math.random().toString(36).substring(2, 7)}`,
    texto: textoLimpo,
    prioridade,
    concluida: false,
  };

  tarefas.unshift(novaTarefa);
  salvarTarefas();
  renderizarTarefas();
}

/**
 * Alterna o estado de conclusão (concluída <-> pendente) de uma tarefa pelo ID.
 */
function alternarConclusaoTarefa(id) {
  tarefas = tarefas.map((tarefa) =>
    tarefa.id === id ? { ...tarefa, concluida: !tarefa.concluida } : tarefa
  );
  salvarTarefas();
  renderizarTarefas();
}

/**
 * Remove uma tarefa existente pelo ID.
 */
function removerTarefa(id) {
  tarefas = tarefas.filter((tarefa) => tarefa.id !== id);
  salvarTarefas();
  renderizarTarefas();
}

/**
 * Atualiza os contadores numéricos do painel de telemetria no topo da página.
 */
function atualizarContadores() {
  const total = tarefas.length;
  const concluidas = tarefas.filter((t) => t.concluida).length;
  const pendentes = total - concluidas;

  countTotalElement.textContent = total;
  countPendingElement.textContent = pendentes;
  countCompletedElement.textContent = concluidas;
}

/**
 * Constrói e atualiza os elementos HTML da lista de tarefas no DOM.
 */
function renderizarTarefas() {
  atualizarContadores();

  const tarefasFiltradas = tarefas.filter((tarefa) => {
    if (filtroAtual === "pending") return !tarefa.concluida;
    if (filtroAtual === "completed") return tarefa.concluida;
    return true;
  });

  // Limpa a lista antes de reconstruir os nós do DOM
  listElement.innerHTML = "";

  if (tarefasFiltradas.length === 0) {
    emptyStateElement.hidden = false;
    return;
  }

  emptyStateElement.hidden = true;

  tarefasFiltradas.forEach((tarefa) => {
    const li = document.createElement("li");
    li.className = `todo-item ${tarefa.concluida ? "completed" : ""}`;
    li.dataset.id = tarefa.id;

    // Área clicável à esquerda (checkbox + metadados + texto)
    const leftDiv = document.createElement("div");
    leftDiv.className = "todo-left";
    leftDiv.title = "Clique para marcar/desmarcar este contrato";
    leftDiv.addEventListener("click", () => alternarConclusaoTarefa(tarefa.id));

    const checkboxSpan = document.createElement("span");
    checkboxSpan.className = "cyber-checkbox";
    checkboxSpan.setAttribute("role", "checkbox");
    checkboxSpan.setAttribute("aria-checked", String(tarefa.concluida));
    checkboxSpan.textContent = tarefa.concluida ? "✓" : "";

    const contentDiv = document.createElement("div");
    contentDiv.className = "todo-content";

    const metaDiv = document.createElement("div");
    metaDiv.className = "todo-meta";

    const prioritySpan = document.createElement("span");
    prioritySpan.className = `priority-tag priority-${tarefa.prioridade}`;
    prioritySpan.textContent = `AMEAÇA: ${tarefa.prioridade}`;

    const statusSpan = document.createElement("span");
    statusSpan.className = "status-tag";
    statusSpan.textContent = tarefa.concluida
      ? "// STATUS: CONTRATO FINALIZADO"
      : "// STATUS: EM ABERTO";

    metaDiv.appendChild(prioritySpan);
    metaDiv.appendChild(statusSpan);

    const textSpan = document.createElement("span");
    textSpan.className = "todo-text";
    textSpan.textContent = tarefa.texto;

    contentDiv.appendChild(metaDiv);
    contentDiv.appendChild(textSpan);

    leftDiv.appendChild(checkboxSpan);
    leftDiv.appendChild(contentDiv);

    // Botões de ação à direita (Concluir/Reabrir e Remover)
    const actionsDiv = document.createElement("div");
    actionsDiv.className = "todo-actions";

    const toggleBtn = document.createElement("button");
    toggleBtn.type = "button";
    toggleBtn.className = "toggle-btn";
    toggleBtn.textContent = tarefa.concluida ? "REABRIR" : "CONCLUIR";
    toggleBtn.addEventListener("click", () => alternarConclusaoTarefa(tarefa.id));

    const deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.className = "delete-btn";
    deleteBtn.setAttribute("aria-label", `Remover tarefa: ${tarefa.texto}`);
    deleteBtn.textContent = "EXPURGAR [X]";
    deleteBtn.addEventListener("click", () => removerTarefa(tarefa.id));

    actionsDiv.appendChild(toggleBtn);
    actionsDiv.appendChild(deleteBtn);

    li.appendChild(leftDiv);
    li.appendChild(actionsDiv);

    listElement.appendChild(li);
  });
}

// Evento de submissão do formulário para criar nova tarefa
formElement.addEventListener("submit", (evento) => {
  evento.preventDefault();
  adicionarTarefa(inputElement.value, prioritySelect.value);
  inputElement.value = "";
  inputElement.focus();
});

// Eventos dos botões de filtro (Todos / Ativos / Finalizados)
filterButtons.forEach((botao) => {
  botao.addEventListener("click", () => {
    filterButtons.forEach((b) => b.classList.remove("active"));
    botao.classList.add("active");
    filtroAtual = botao.dataset.filter;
    renderizarTarefas();
  });
});

// Inicializa a interface ao carregar o script
renderizarTarefas();
