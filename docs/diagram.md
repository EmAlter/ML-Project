<style>
/* CSS per l'interattività dell'SVG */
.uml-class { cursor: pointer; transition: all 0.3s ease; pointer-events: all; }
.uml-link { transition: all 0.3s ease; stroke-width: 2px; }

.dimmed { opacity: 0.15 !important; }
.highlighted { stroke: #007acc !important; stroke-width: 4px !important; }
.highlighted-linked { opacity: 1 !important; stroke: #4caf50 !important; }

/* Stile della Legenda */
.diagram-legend {
    position: absolute; 
    top: 15px; 
    right: 15px;
    background: rgba(255, 255, 255, 0.95); 
    border: 1px solid #ccc;
    padding: 15px; 
    border-radius: 8px; 
    z-index: 10;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
</style>

<div style="position: relative; border: 1px solid #ccc; height: 600px; overflow: hidden; background: #fafafa; border-radius: 8px;">
    
    <div class="diagram-legend">
        <h4 style="margin-top: 0;">Legenda Interattiva</h4>
        <div style="margin-bottom: 5px;"><span style="color: #007acc; font-size: 1.2rem;">■</span> Classe selezionata</div>
        <div style="margin-bottom: 15px;"><span style="color: #4caf50; font-size: 1.2rem;">■</span> Entità collegate</div>
        <button id="reset-diagram" class="md-button md-button--primary">Reset Vista</button>
    </div>

    <!-- Iniezione diretta dell'SVG tramite Snippet MkDocs -->
    <div id="svg-container" style="width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;">
        --8<-- "docs/assets/files/diagram.svg"
    </div>
</div>

<script src="https://unpkg.com/@panzoom/panzoom/dist/panzoom.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById('svg-container');
    const svgElement = container.querySelector('svg');
    
    if (!svgElement) return;

    // Adatta l'SVG al container
    svgElement.style.width = '100%';
    svgElement.style.height = '100%';

    // Inizializza Panzoom
    const panzoom = Panzoom(svgElement, { maxScale: 10, minScale: 1, contain: 'outside' });
    container.parentElement.addEventListener('wheel', panzoom.zoomWithWheel);

    // Logica di interazione
    const classes = svgElement.querySelectorAll('.uml-class');
    const links = svgElement.querySelectorAll('.uml-link');

    classes.forEach(cls => {
        cls.addEventListener('click', function(e) {
            e.stopPropagation(); 
            const clickedId = this.id;
            
            // Applica il dimming generale
            classes.forEach(c => c.classList.add('dimmed'));
            links.forEach(l => l.classList.add('dimmed'));
            
            // Evidenzia l'entità cliccata
            this.classList.remove('dimmed');
            this.classList.add('highlighted');
            
            // Cerca le relazioni
            links.forEach(link => {
                const connects = link.getAttribute('data-connects') || "";
                if (connects.includes(clickedId)) {
                    link.classList.remove('dimmed');
                    link.classList.add('highlighted');
                    
                    // Evidenzia i nodi di destinazione
                    const connectedIds = connects.split(' ');
                    connectedIds.forEach(connId => {
                        const connectedNode = svgElement.querySelector(`#${connId}`);
                        if(connectedNode) {
                            connectedNode.classList.remove('dimmed');
                            connectedNode.classList.add('highlighted-linked');
                        }
                    });
                }
            });
        });
    });

    // Reset vista
    document.getElementById('reset-diagram').addEventListener('click', () => {
        svgElement.querySelectorAll('.dimmed, .highlighted, .highlighted-linked').forEach(el => {
            el.classList.remove('dimmed', 'highlighted', 'highlighted-linked');
        });
    });
});
</script>