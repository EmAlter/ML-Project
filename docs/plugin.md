Per adattare alcune funzionalità di Moodle alle esigenze del progetto sono state apportare alcune modifiche tramite l'utilizzo di plugin e injections di codice nel layout del sistema.

## Modifiche al layout
I cambiamenti fatti hanno agito soprattutto sul layout mostrato all'utente durante i test, in particolare per quanto riguarda la visualizzazione delle domande e delle risposte.

Poichè i test sono di natura percettiva, è molto importante che le domande e le risposte siano visualizzate in maniera chiara e leggibile, senza elementi di disturbo o di confusione.
Una soluzione adottata è stata quella di agire sul CSS, andando a creare due colonne verticali, una a sinistra per le domande e una a destra per le risposte, in modo che l'utente possa avere sempre visione di eventuali immagini o richieste nella domanda, senza dover scorrere la pagina verso l'alto o verso il basso ogni volta.

> [!IMPORTANTE]
> Il layout a due colonne funziona solo nei moduli di tipo **Test** di Moodle e solo se una delle due domande è di tipo **Descrizione**.

### HTML
Il seguente codice va inserito nell'header html delle pagine di Moodle, 
il percorso da seguire è: **Amministrazione del sito > Aspetto > Tema > HTML aggiuntivo**, inserire poi il codice nel campo **All'interno del tag HEAD**.

```html
--8<-- "docs/assets/files/HTML_head.txt"
```

### CSS
A questo punto è importante adattare il CSS per rendere le due colonne visibili e allineate al tema, il percorso da seguire è: **Amministrazione del sito > Aspetto > Temi**, cliccare sul simbolo
<img src="../assets/icons/setting.svg" alt="Impostazioni" width="10"> del tema attivo, dal menù muoversi in **Impostazioni avanzate** e incollare il seguente codice nel campo **SCSS raw**.

```css
--8<-- "docs/assets/files/SCSS_raw.txt"
```
Oltre ad adattare le domande al layout a due colonne, il CSS rimuove eventuali elementi di disturbo, come ad esempio il menù laterale, che non è necessario durante lo svolgimento dei test.

---
## Plugin obbligatori
Di seguito sono elencati i plugin (obbligatori) installati e configurati per il progetto, con una breve descrizione delle loro funzionalità.

> [!DOWNLOAD]
> I plugin aggiuntivi scaricati devono essere della stessa versione di Moodle

> [!INSTALLAZIONE]
> Nel caso in cui i plugin non siano già installati, è possibile scaricarli e installarli manualmente, andando nella sezione **Amministrazione del sito > Plugin > Installazione plugin** e caricando il file zip del plugin nel campo **Installa plugin da file ZIP**.

### Login
Una prerogativa importante del progetto è la gestione dell'accesso degli utenti al sistema.
Nella sezione del progetto che descrive i vari attori ([Vai alla sezione](actor.md)), è stato specificato che non tutti hanno le stesse autorizzazioni, per esempio un testato può solo partecipare ai test, mentre un progettista può gestire le sperimentazioni e i corsi. Sebbene i permessi siano gestiti tramite i ruoli, è importante che l'utente acceda al sistema con le proprie credenziali, in modo da essere riconosciuto e quindi avere accesso alle funzionalità a lui consentite.

In un contesto di test, in cui gli utenti sono tanti, è importante che l'accesso al sistema sia semplice e veloce, per questo motivo è stato creato il plugin **Token Login** che permette agli utenti di accedere tramite un **TOKEN** unico che viene fornito dal progettista, senza dover inserire username e password.

Il funzionamento è molto semplice, il Progettista:material-account-hard-hat: in fase di creazione del test, genera un token per ogni Testato:material-account: che parteciperà al test, il token verrà poi fornito al Testato:material-account: che, il giorno del test, potrà accedere al sistema tramite esso, senza dover inserire username e password.

[:material-download: Scarica il plugin](assets/files/tokenlogin.zip){: .md-button .md-button--primary }

### Moove
Il plugin **Moove** è un tema per Moodle che permette di personalizzare l'aspetto del sistema, rendendolo più moderno e intuitivo.

Il link per scaricare il plugin è il seguente: <https://moodle.org/plugins/theme_moove>

### FilterCodes
Il plugin **FilterCodes** è uno strumento molto potente che permette di iniettare codice html in qualsiasi punto del sistema (domande, pagine, corsi, ecc.), permettendo di personalizzare l'aspetto e le funzionalità del sistema in base alle esigenze del progetto.

> [!ESEMPIO]
> Nel contesto del progetto, l'attore **Moderatore:material-shield-account:** oltre a dover moderare i test, ha anche il compito di fornire spiegazioni o chiarimenti sulle attività che i testati svolgeranno, 
> perciò ha la necessità di poter visualizzare informazioni aggiuntive sulle domande.
>
> Senza rischiare di dovere scrivere una copia di ogni test visualizzabile solo dal moderatore, **FilterCodes** permette di far visualizzare del contenuto solo agli utenti che hanno un determinato ruolo, in questo caso il ruolo di **Moderatore:material-shield-account:**, utilizzando la seguente sintassi:
> ```
> {ifcustomrole moderatore}
>
> Testo visibile solo al ruolo di Moderatore
>
> {/ifcustomrole}
> ```
> È importante notare che il nome del ruolo deve essere quello che in Moodle è definito **Nome abbreviato**, in questo caso **moderatore**, per visualizzare il contenuto solo agli utenti con quel ruolo.

Il link per scaricare il plugin è il seguente: <https://moodle.org/plugins/filter_filtercodes>

Per altre informazioni sul plugin è possibile consultare la documentazione ufficiale: <https://github.com/michael-milette/moodle-filter_filtercodes>

---
## Plugin opzionali
Di seguito sono elencati i plugin (opzionali) installati e configurati per il progetto, con una breve descrizione delle loro funzionalità.

### C4L
Il plugin **C4L (Components for Learning)** permette di inserire componenti grafici aggiuntivi all'interno dei campi **TinyMCE** di Moodle, come ad esempio immagini, quotes, tips, advices ecc., per rendere eventualmente più informativa e accattivante la visualizzazione dei contenuti.

Il link per scaricare il plugin è il seguente: <https://marketplace.moodle.com/plugins/2695>

### WidgetHub
Il plugin **WidgetHub** permette di inserire widget all'interno dei campi **TinyMCE** di Moodle, come ad esempio grafici, mappe, video ecc., per rendere eventualmente più interattiva la visualizzazione dei contenuti.

Il link per scaricare il plugin è il seguente: <https://marketplace.moodle.com/plugins/3123>
