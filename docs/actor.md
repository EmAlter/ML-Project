Un attore è una persona o un'entità che interagisce con il sistema per raggiungere un obiettivo specifico.

Nel contesto del progetto, gli attori principali sono:

* **Progettista** :material-account-hard-hat:: è l'attore che ha il compito di gestire le sperimentazioni, i corsi e le attività, oltre a occuparsi della gestione degli utenti e dei loro ruoli. Il progettista ha accesso a tutte le funzionalità del sistema.
* **Moderatore** :material-shield-account:: è l'attore che ha il compito di moderare i test dettando il tempo e leggendo le consegne delle attività, oltre a gestire eventuali dati dei testati.
* **Testato** :material-account:: è l'attore che partecipa ai test.
* **Esperto** :material-account-tie:: è l'attore che ha il compito di presentare un'intervento tra un test e l'altro, fornendo spiegazioni o chiarimenti sulle attività svolte.

## Differenza tra utente, ruolo e attore
Un **utente** rappresenta l'identità digitale (l'account) che accede e interagisce materialmente con il sistema, mentre un **ruolo** definisce l'insieme di permessi, competenze e limiti operativi associati a quell'utente.

Un **attore** è invece un'astrazione concettuale, utilizzata nella fase di analisi e progettazione dello Unified Process, per mappare le interazioni esterne con i casi d'uso e stabilire "chi fa cosa". Non esiste come entità a sé stante nell'applicativo, ma prende vita nel momento in cui una persona fisica viene dotata delle autorizzazioni necessarie per operare.

Nel contesto del progetto (come formalizzato nel modello di dominio), è obbligatorio che ogni utente sia associato a un ruolo. Di conseguenza, al momento della creazione di un nuovo profilo in Moodle, sarà vincolante assegnargli una qualifica specifica (Progettista, Moderatore, Esperto o Testato). Questa assegnazione traduce nella pratica l'attore teorico definito in fase di analisi.

Per semplicità possiamo dire che:<br>
[Utente](user.md) + [Ruolo](role.md) = Attore