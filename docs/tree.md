<style>
  .tech-tree-container { 
    display: flex; flex-direction: column; gap: 40px; 
    font-family: var(--md-text-font-family, sans-serif); 
    margin-top: 20px;
  }
  .setup-level { 
    display: flex; flex-direction: column; gap: 20px; 
  }
  
  .level-header {
    display: flex; align-items: center; gap: 15px;
  }
  .level-label {
    font-weight: 700; font-size: 0.85em; text-transform: uppercase;
    letter-spacing: 2px; color: var(--md-primary-fg-color);
    white-space: nowrap;
  }
  .level-line {
    flex-grow: 1; height: 1px;
    background: linear-gradient(90deg, var(--md-primary-fg-color) 0%, transparent 100%);
    opacity: 0.4;
  }
  
  .level-nodes {
    display: flex; gap: 25px; flex-wrap: wrap; padding-left: 15px;
  }
  
  .node { 
    border: 1px solid var(--md-default-fg-color--light); 
    border-radius: 2px; padding: 12px 20px; 
    background: var(--md-default-bg-color);
    transition: all 0.2s ease-in-out;
    display: flex; align-items: center; gap: 12px;
    min-width: 240px;
  }
  .node.locked { 
    opacity: 0.4; border-style: dashed; filter: grayscale(100%); 
    pointer-events: none; 
  }
  .node.completed { 
    border-color: var(--md-primary-fg-color);
    /* Indicatore laterale in stile HUD */
    box-shadow: inset 4px 0 0 var(--md-primary-fg-color);
    background: rgba(100, 100, 100, 0.05); 
  }
  
  .node label { 
    cursor: pointer; font-weight: 600; font-size: 0.9em; 
    user-select: none; flex-grow: 1;
  }
  .node input { 
    cursor: pointer; transform: scale(1.2); 
    accent-color: var(--md-primary-fg-color); 
    margin: 0;
  }

  .node-link {
    text-decoration: none;
    color: var(--md-primary-fg-color);
    font-weight: bold;
    padding: 4px 8px;
    border-radius: 4px;
    transition: background 0.2s;
  }
  .node-link:hover {
    background: rgba(128, 128, 128, 0.2);
  }

  .node.locked .node-link {
    opacity: 0.3;
    pointer-events: none; 
  }
</style>

<div class="tech-tree-container">
  <!-- Livello 1 -->
  <div class="setup-level">
    <div class="level-header">
      <span class="level-label">Livello 1</span>
      <div class="level-line"></div>
    </div>
    <div class="level-nodes">
      <div class="node" id="ui-raccolta">
        <input type="checkbox" id="chk-raccolta" class="node-chk">
        <label for="chk-raccolta">Creare una Raccolta Attività</label>
        <a href="../activity_collection/" class="node-link" title="Vai alla guida">↗</a>
      </div>
      <div class="node" id="ui-ruolo">
        <input type="checkbox" id="chk-ruolo" class="node-chk">
        <label for="chk-ruolo">Creare un Ruolo</label>
        <a href="../role/" class="node-link" title="Vai alla guida">↗</a>
      </div>
        <div class="node" id="ui-classe">
        <input type="checkbox" id="chk-classe" class="node-chk">
        <label for="chk-classe">Creare una Classe</label>
        <a href="../class/" class="node-link" title="Vai alla guida">↗</a>
      </div>
    </div>
  </div>
  
  <!-- Livello 2 -->
  <div class="setup-level">
    <div class="level-header">
      <span class="level-label">Livello 2</span>
      <div class="level-line"></div>
    </div>
    <div class="level-nodes">
      <div class="node locked" id="ui-attivita">
        <input type="checkbox" id="chk-attivita" class="node-chk" disabled>
        <label for="chk-attivita">Crea Attività</label>
        <a href="../activity/" class="node-link" title="Vai alla guida">↗</a>
      </div>
    </div>
  </div>

  <!-- Livello 3 -->
  <div class="setup-level">
    <div class="level-header">
      <span class="level-label">Livello 3</span>
      <div class="level-line"></div>
    </div>
    <div class="level-nodes">
      <div class="node locked" id="ui-utente">
        <input type="checkbox" id="chk-utente" class="node-chk" disabled>
        <label for="chk-utente">Crea Utente</label>
        <a href="../user/" class="node-link" title="Vai alla guida">↗</a>
      </div>
    </div>
  </div>
  
  <!-- Livello 4 -->
  <div class="setup-level">
    <div class="level-header">
      <span class="level-label">Livello 4</span>
      <div class="level-line"></div>
    </div>
    <div class="level-nodes">
      <div class="node locked" id="ui-classe">
        <input type="checkbox" id="chk-classe" class="node-chk" disabled>
        <label for="chk-classe">Assegna a Classe/Corso</label>
        <a href="../class/" class="node-link" title="Vai alla guida">↗</a>
      </div>
    </div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {
  // Dizionario delle dipendenze: "id-nodo": ["array", "di", "prerequisiti"]
  const dependencies = {
    "chk-raccolta": [],
    "chk-ruolo": [],
    "chk-classe": [] 
    "chk-attivita": ["chk-raccolta"], 
    "chk-utente": ["chk-attivita", "chk-ruolo"], 
    
  };

  const nodeIds = Object.keys(dependencies);
  const progressKey = "moodleSetupPath";
  
  // Ripristino stato dal localStorage
  const savedProgress = JSON.parse(localStorage.getItem(progressKey)) || {};
  nodeIds.forEach(id => {
    const chk = document.getElementById(id);
    if (chk) chk.checked = savedProgress[id] || false;
  });

  // Valutatore logico dell'albero
  function updateTree() {
    const currentProgress = {};

    nodeIds.forEach(id => {
      const chk = document.getElementById(id);
      const nodeDiv = chk.closest('.node');
      const deps = dependencies[id];
      
      // Verifica logica AND sui prerequisiti
      const isUnlocked = deps.every(depId => document.getElementById(depId).checked);
      
      if (isUnlocked) {
        nodeDiv.classList.remove("locked");
        chk.disabled = false;
      } else {
        nodeDiv.classList.add("locked");
        chk.disabled = true;
        chk.checked = false; 
      }

      // Applica lo stile visivo se completato
      if (chk.checked) {
        nodeDiv.classList.add("completed");
      } else {
        nodeDiv.classList.remove("completed");
      }

      currentProgress[id] = chk.checked;
    });

    localStorage.setItem(progressKey, JSON.stringify(currentProgress));
  }

  // Registrazione eventi
  document.querySelectorAll(".node-chk").forEach(chk => {
    chk.addEventListener("change", updateTree);
  });

  // Prima computazione
  updateTree();
});
</script>