Nel progetto concettuale, i permessi rappresentano le regole che definiscono quali azioni un attore può compiere all'interno del sistema.

Queste regole sono fondamentali per garantire la sicurezza e l'integrità del sistema, assicurando che solo gli attori autorizzati possano accedere a determinate funzionalità.

<p align="center">
  <img src="../assets/images/permission.svg" alt="Permessi">
</p>

Ogni [ruolo](role.md) all'interno del sistema ha un insieme specifico di permessi associati. 

È importante notare che i permessi sono in una relazione di
<span class="term">**Aggregazione** <span class="tip"><strong>Aggregazione</strong><br>
In UML è una relazione strutturale di tipo "tutto-parte" debole, in cui la classe contenitore fa riferimento agli oggetti contenuti, ma non ne controlla il ciclo di vita, i quali possono esistere in modo indipendente.<br>
</span> </span>
con i ruoli, poichè esistono indipendentemente da essi, infatti eliminare un ruolo non comporta l'eliminazione dei permessi associati.

## Moodle
Moodle, essendo una piattaforma che gestisce un gran numero di utenti e ruoli, offre un sistema di permessi molto dettagliato e flessibile.

Dal punto di vista del progetto concettuale, non serve entrare nei dettagli di tutti i permessi disponibili in Moodle, ma è sufficiente capire cosa un attore può fare all'interno del sistema e quali azioni sono permesse o vietate in base al suo ruolo.

### Attore: Progettista:material-account-hard-hat:
Il Progettista:material-account-hard-hat: ha il permesso di creare e gestire tutti gli elementi del sistema, come sperimentazioni, corsi e test.<br>
In Moodle, un utente di questo tipo viene definito come **Amministratore** e ha accesso a tutte le funzionalità della piattaforma, inclusa la gestione stessa di ruoli e permessi.

### Attore: Moderatore:material-shield-account:
Il Moderatore:material-shield-account: ha il permesso di moderare i contenuti e gestire le interazioni tra gli utenti, ma non può creare o modificare elementi del sistema.
Perciò sarà limitato alla visualizzazione dei test senza doverli completare e alla gestione dei dati personali dei testati per aggiungere eventuali informazioni aggiuntive, come ad esempio certificazioni.

### Attore: Esperto:material-account-tie:
L'Esperto:material-account-tie: ha il permesso di visualizzare i test che dovrà presentare alla classe di testati, ma non può modificarli o gestirli. Perciò, potrà soltanto visualizzare i corsi e i test a cui è stato assegnato e completare le attività previste.

### Attore: Testato:material-account:
Il Testato:material-account: ha il permesso di partecipare ai test e completare le attività assegnate, ma non può modificare o gestire gli elementi del sistema. Perciò, potrà soltanto visualizzare i corsi e i test a cui è stato assegnato, completarne le attività e inviare le risposte.
