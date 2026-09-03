!!! info "Permessi e Ruoli"
    * **Gestisce (crea, modifica, elimina):** :material-account-hard-hat: Progettista
    * **Gestisce (solo modifica):** :material-shield-account: Moderatore
    * **Visualizza:** :material-account-hard-hat: Progettista, :material-shield-account: Moderatore

Nel progetto concettuale, un **Utente** rappresenta una persona con determinati attributi:

* **Username** :material-arrow-right-thin: rappresenta il token che l'utente utilizzerà per accedere al sistema
* **Nome** :material-arrow-right-thin: rappresenta il nome dell'utente
* **Cognome** :material-arrow-right-thin: rappresenta il cognome dell'utente
* **Data di nascita** :material-arrow-right-thin: rappresenta la data di nascita dell'utente

Il **Progettista:material-account-hard-hat:** si occupa di creare/modificare/eliminare gli **Utenti**, mentre il **Moderatore:material-shield-account:** può visualizzarli ed eventualmente aggiornare i loro dati anagrafici e certificazioni.

Dal punto di vista concettuale, l'utente è un "guscio vuoto" che non ha alcun significato senza un ruolo associato, per questo motivo a ognuno di essi viene associato un [Ruolo](role.md) che ne definisce le azioni che può compiere all'interno del sistema.


## Moodle
In Moodle, il concetto di Utente è uguale a quello del progetto concettuale.

> [!ATTENZIONE]
> Alcuni campi per la creazione di un utente sono obbligatori, come ad esempio l'email o la password, ma non sono presenti nel progetto concettuale, perché non sono necessari per il corretto funzionamento del sistema, per questo motivo il **Progettista:material-account-hard-hat:** dovrà eventualmente inserire un valore fittizio per questi campi. 

> [!ATTENZIONE]
>Alcuni campi non esistono perché Moodle non li prevede, come ad esempio la data di nascita, per questo motivo il **Progettista:material-account-hard-hat:** dovrà eventualmente creare un campo personalizzato per l'utente.

### Creare un campo personalizzato per l'utente
Un campo personalizzato permette di aggiungere ulteriori informazioni per l'utente che Moodle non prevede, ma che sono necessarie o previste dal progetto concettuale.

I passi sono:

1. Accedere alla Home page di Moodle
1. Cliccare su **Utenti** nel menù centrale
1. Nella sezione **Profili** cliccare su **Campi personalizzati**
1. Cliccare nel menù a tendina "Crea un campo personalizzato" e selezionare il tipo di campo da creare (es. Data e ora, Testo, ecc.)
1. Nella pagina che si apre popolare i seguenti campi obbligatori:

    * **Nome** :material-arrow-right-thin: rappresenta il nome del campo che sarà visibile agli utenti
    * **Nome abbreviato** :material-arrow-right-thin: rappresenta l'identificativo del campo

1. (Opzionale) Mettere la spunta in **Compilazione obbigatoria** se si vuole che il campo sia obbligatorio per tutti gli utenti
1. Mettere la spunta in **Da compilare nella pagina di creazione account** se si vuole che il campo sia compilabile in fase di creazione dell'utente
1. Cliccare su **Salva modifiche** per terminare la creazione.

A questo punto, i campi personalizzati creati saranno visibili nella pagina di creazione dell'utente sotto la categoria "Altri campi".

> [!ESEMPIO]
> Un esempio di campo personalizzato potrebbe essere "Data di nascita", che permette di registrare la data di nascita degli utenti.
> Il campo **Nome** sarà "Data di nascita" con **Nome abbreviato** "datanascita".<br>
> Questo tipo di campo (Data e Ora) richiede una anno minimo e massimo da impostare.

### Creare un nuovo utente
I passi sono:

1. Accedere alla Home page di Moodle
1. Cliccare su **Utenti** nel menù centrale
1. Nella sezione **Profili** cliccare su **Nuovo utente**
1. Inserire i seguenti campi di default obbligatori:
    
    * **Username** :material-arrow-right-thin: rappresenta il **token univoco** che l'utente utilizzerà per accedere al sistema
    * **Password** :material-arrow-right-thin: rappresenta la password assegnata all'utente (non sarà usata, vedi il plugin [Login](plugin.md#login))
    * **Nome** :material-arrow-right-thin: rappresenta il nome dell'utente
    * **Cognome** :material-arrow-right-thin: rappresenta il cognome dell'utente
    * **Indirizzo email** :material-arrow-right-thin: rappresenta l'indirizzo email dell'utente (dovrà essere un email fittizia)

1. Inserire eventuali campi personalizzati creati in precedenza (vedi [Creare un campo personalizzato per l'utente](#creare-un-campo-personalizzato-per-lutente))
1. Cliccare sul pulsante **Crea utente** in fondo alla pagina per terminare la creazione del nuovo utente.

> [!IMPORTANTE]
> Una volta creato il nuovo utente, il **Progettista:material-account-hard-hat:** dovrà assegnargli un [Ruolo](role.md) per permettergli di svolgere le azioni previste dal progetto concettuale (vedi [Assegnare o rimuovere un ruolo a un utente in Moodle](role.md#assegnare-o-rimuovere-un-ruolo-a-un-utente-in-moodle)).

### Creare un nuovo utente tramite CSV file
Per semplificare la creazione di più utenti, Moodle permette di creare un nuovo utente tramite un file CSV contenente un elenco degli utenti da creare.

> [!TIP]
> Creare nuovi utenti tramite CSV è preferibile perché permette di assegnare direttamente un ruolo senza passi aggiuntivi, opzione non possibile nella creazione singola dell'utente.

#### Impostare il file CSV
Per prima cosa bisogna preparare un file CSV con i dati degli utenti da creare.<br>
La prima riga del file CSV deve contenere le seguenti colonne obbligatorie di default:

```csv
username,firstname,lastname,email,password
```

Poichè nel progetto abbiamo previsto anche la data di nascita, dovrà esserci anche la colonna relativa al campo personalizzato creato in precedenza (vedi [Creare un campo personalizzato per l'utente](#creare-un-campo-personalizzato-per-lutente)), che sarà formata dal termine `profile_field_` seguita dal nome abbreviato del campo, quindi in questo caso `profile_field_datanascita`:<br>

```csv
username,firstname,lastname,email,password,profile_field_datanascita
```

Per ogni utente è previsto anche un ruolo, **sebbene non sia possibile assegnare un ruolo in fase di creazione singola dell'utente**, è possibile farlo tramite CSV inserendo la colonna `sysrole1` (vedi **Nome abbreviato** in [Ruolo](role.md)):<br>

```csv
username,firstname,lastname,email,password,profile_field_datanascita,sysrole1
```

Riassumendo, le colonne sono:

* `username` :material-arrow-right-thin: rappresenta il **token univoco** che l'utente utilizzerà per accedere al sistema
* `firstname` :material-arrow-right-thin: rappresenta il nome dell'utente
* `lastname` :material-arrow-right-thin: rappresenta il cognome dell'utente
* `email` :material-arrow-right-thin: rappresenta l'indirizzo email dell'utente (dovrà essere un email fittizia)
* `password` :material-arrow-right-thin: rappresenta la password assegnata all'utente (non sarà usata, vedi il plugin [Login](plugin.md#login))
* `profile_field_datanascita` :material-arrow-right-thin: rappresenta la data di nascita dell'utente
* `sysrole1` :material-arrow-right-thin: rappresenta il ruolo che l'utente dovrà avere all'interno del sistema, (vedi **Nome abbreviato** in [Ruolo](role.md))

> [!ESEMPIO]
> ```csv
> username,firstname,lastname,email,password,profile_field_datanascita,sysrole1
> TokenMR,Mario,Rossi,emailfittizia.mariorossi@email.it,mr1998,1998-01-01,testato
> TokenAP,Artù,Pendragon,emailfittizia.artupendragon@email.it,ap1999,1999-02-02,moderatore
> ```

> [!ATTENZIONE]
> Il campo `profile_field_datanascita`, essendo un campo di tipo Data e Ora, deve rispettare il formato `YYYY-MM-DD` (anno-mese-giorno), altrimenti Moodle non riuscirà a interpretarlo correttamente.

#### Inserire gli utenti
1. Accedere alla Home page di Moodle
1. Cliccare su **Utenti** nel menù centrale
1. Nella sezione **Profili** cliccare su **Importazione utenti**
1. Trascinare il file CSV nella sezione apposita e selezionare il tipo di separatore utilizzato (in questo caso la virgola `,`)
1. Cliccare su **Importazione utenti**
1. Nella pagina che si apre è importante comprendere cosa fa il campo "Modalità importazione":

    * **Crea solamente i nuovi utenti, ignora gli utenti già esistenti:** Crea account solo per gli username che non sono ancora presenti nel database di Moodle. Se il file CSV contiene un username già registrato, quella specifica riga viene ignorata senza alterare i dati preesistenti.
    * **Crea tutti gli utenti, aggiungendo un numero agli username ove necessario:** Forza la creazione di un nuovo account per ogni riga del CSV. Se rileva un username in conflitto con uno già a sistema (es. `mario.rossi`), crea un nuovo utente generando una variante numerata (es. `mario.rossi2`).
    * **Crea i nuovi utenti ed aggiorna gli utenti già esistenti:** Inserisce gli account inediti e, per gli username già riconosciuti dal sistema, sovrascrive o popola i campi del profilo (inclusi ruoli o campi custom) con i nuovi valori forniti nel file.
    * **Aggiorna solamente gli utenti già esistenti:** Non genera alcun nuovo profilo. Cerca nel database gli username indicati nel file e ne modifica esclusivamente i dati.


1. Poichè le password sono definite nel file CSV, scegliere dal menù a tendina **Il campo è presente nel file**
1. Infine cliccare su **Importazione utenti** per terminare.

### Modificare un utente