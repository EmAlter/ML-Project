Gli attori sono entità che interagiscono con il sistema per raggiungere un obiettivo specifico.

Nel contesto del progetto, gli attori principali sono:

* **Progettista**: è l'attore che ha il compito di gestire le sperimentazioni, i corsi e le attività, oltre a occuparsi della gestione degli utenti e dei loro ruoli. Il progettista ha accesso a tutte le funzionalità del sistema.
* **Moderatore**: è l'attore che ha il compito di moderare i test dettando il tempo e leggendo le consegne delle attività, oltre a gestire eventuali dati dei testati.
* **Testato**: è l'attore che partecipa ai test.
* **Esperto**: è l'attore che ha il compito di presentare un'intervento tra un test e l'altro, fornendo spiegazioni o chiarimenti sulle attività svolte.

## Gli attori in Moodle
In Moodle, attori differenti vengono riconosciuti tramite il concetto di ==Ruolo==, che definisce le azioni che un utente può compiere all'interno del sistema.
Per questo motivo per ogni utente deve essere definito un ruolo corrispondente in Moodle, con le relative autorizzazioni.

> [!IMPORTANTE]
> Il **Progettista** in Moodle è rappresentato dal ruolo di **Amministratore**, che viene generato e assegnato automaticamente al momento dell'installazione del sistema, quindi non è necessario creare un nuovo ruolo per esso.

### Creare un nuovo ruolo in Moodle
Per creare un nuovo ruolo in Moodle è necessario rispettare alcune precondizioni:

* L'utente deve avere il ruolo di **Progettista (Amministratore)**, in quanto solo i progettisti hanno accesso alla gestione dei ruoli.
* Nel sistema devono esistere una serie di autorizzazioni assegnabili (in Moodle sono definite come **Permessi**), che rappresentano le azioni che un utente può compiere all'interno del sistema. Queste autorizzazioni sono già presenti in Moodle, quindi non è necessario crearne di nuove.

Di seguito i passi per creare un nuovo ruolo in Moodle:

1. Accedere alla Home page di Moodle
1. Cliccare su "Amministrazione del sito" nel menù centrale
1. Nel menù orizzontale scegliere "Utenti" > "Autorizzazioni" > "Gestione Ruoli"
1. Cliccare su "Aggiungi un ruolo"
1. Inserire gli attributi che identificano il ruolo:

    * **Nome abbreviato** :material-arrow-right-thin: es. "moderatore" rappresenta l'identificativo del ruolo
    * **Nome personalizzato** :material-arrow-right-thin: es. "Moderatore" rappresenta il nome del ruolo che sarà visibile agli utenti
    * **Descrizione personalizzata** :material-arrow-right-thin: es. "Ruolo che permette di moderare i test" rappresenta la descrizione del ruolo che sarà visibile agli utenti
    * **Ruolo archetipo (opzionale)** :material-arrow-right-thin: es. "Docente (non editor)" un archetipo rappresenta un ruolo predefinito che può essere utilizzato come modello per quello nuovo, in questo caso il ruolo di Docente (non editor) è il più simile a quello di Moderatore
    * **Contesti dove questo ruolo può essere assegnato** :material-arrow-right-thin: es. "Sistema" rappresenta il contesto in cui il ruolo può essere assegnato, in questo caso il contesto di Sistema permette di assegnare il ruolo a livello globale, quindi indipendentemente dalla Sperimentazione e/o dal Corso selezionato.

1. Una volta inseriti gli attributi, si devono assegnare le autorizzazioni (permessi) al ruolo spuntando "consenti" sulle quelle desiderate.
1. Per terminare la creazione del ruolo, scorrere in fondo alla pagina e cliccare su "Salva modifiche".

### Modificare o eliminare un ruolo in Moodle
Per modificare o eliminare un ruolo in Moodle il procedimento è molto semplice, in entrambi i casi è necessario accedere alla pagina di gestione dei ruoli:

1. Accedere alla Home page di Moodle
1. Cliccare su "Amministrazione del sito" nel menù centrale
1. Nel menù orizzontale scegliere "Utenti" > "Autorizzazioni" > "Gestione Ruoli"

A questo punto:

* **MODIFICARE**: Cliccare sull'icona della matita <img src="../assets/icons/edit.svg" alt="Modifica" width="10"> a fianco a ruolo desiderato, modificare gli attributi e/o le autorizzazioni e cliccare su "Salva modifiche"
* **ELIMINARE**: Cliccare sull'icona del cestino <img src="../assets/icons/delete.svg" alt="Elimina" width="10"> a fianco a ruolo desiderato e confermare l'eliminazione del ruolo.