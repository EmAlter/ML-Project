# File CSV
Per semplificare la gestione di alcune funzionalità, Moodle permette di operare anche tramite file
<span class="term">**CSV** <span class="tip"><strong>File CSV</strong><br>
Un file CSV (Comma-Separated Values) è un file di testo semplice usato per memorizzare dati in formato tabellare, dividendo ogni valore con un separatore (es. virgola, punto e virgola, ecc.).<br>
</span> </span>.<br>
Questo tipo di file permette di operare su più dati, permettendo di creare o modificare più istanze contemporanamente.

## Introduzione
In Moodle, il file verrà utilizzato per:

* Gestire le classi (vedi [Classe](class.md)) a livello di sistema.
* Creare o aggiornare più utenti contemporaneamente, definendo tutti i loro attributi, ruoli e classi di appartenenza in un'unica operazione.

## Creare più classi contemporaneamente
### Impostare il file CSV
Per prima cosa bisogna preparare un file CSV con i dati delle classi da creare/aggiornare.<br>
La prima riga del file CSV dovrà contenere le seguente colonna obbligatoria di default:

```csv
name
```

---
Successivamente, per ogni classe è previsto anche un **codice identificativo**, che sarà utilizzato per assegnare gli utenti alla classe stessa tramite CSV file.<br>
Questa colonna sarà formata dal termine `idnumber`:

```csv
name,idnumber
```

> [!IMPORTANTE]
> Nonostante il nome, il campo `idnumber` accetta anche valori alfanumerici, quindi è possibile inserire sia lettere che numeri.<br>
> Una buona pratica è evitare di utilizzare spazi (usare `_` o `-` al loro posto) o caratteri speciali, in quanto potrebbero generare problemi in fase di importazione del file CSV.

>[!ATTENZIONE]
> Il codice identificativo deve essere univoco per ogni classe, in caso di codici uguali, Moodle segnalerà un errore in fase di importazione.

---
Infine, bisognerà permettere la visibilità della classe al **Progettista:material-account-hard-hat:** in modo che possa visualizzarla e gestirla, questo è possibile tramite la colonna `visible`.<br>
Questa colonna può assumere due valori: `0` (la classe non è visibile) oppure `1` (la classe è visibile):

```csv
name,idnumber,visible
```

---
Riassumendo, le colonne sono:

* `name` :material-arrow-right-thin: rappresenta il nome della classe che sarà visibile agli utenti
* `idnumber` :material-arrow-right-thin: rappresenta il codice identificativo della classe, che sarà utilizzato per assegnare gli utenti alla classe stessa tramite CSV file
* `visible` :material-arrow-right-thin: rappresenta la visibilità della classe

> [!ESEMPIO]
> ```csv
> name,idnumber,visible
> Classe 3A,classe_3a,1
> ```
## Creare o aggiornare più utenti contemporaneamente
### Impostare il file CSV
Per prima cosa bisogna preparare un file CSV con i dati degli utenti da creare/aggiornare.<br>
La prima riga del file CSV dovrà contenere le seguenti colonne obbligatorie di default:

```csv
username,firstname,lastname,email,password
```

---
Per ogni utente è previsto anche un ruolo, **sebbene non sia possibile assegnare un ruolo in fase di creazione singola dell'utente**, è possibile farlo tramite CSV inserendo la colonna `sysrole1` (vedi **Nome abbreviato** in [Ruolo](role.md)):<br>

```csv
username,firstname,lastname,email,password,sysrole1
```

---
Ogni utente, poi, deve far parte di un gruppo globale, cioè la classe di appartenenza (vedi [Classe](class.md)), questo è possibile tramite la colonna `cohort1`.<br>

> [!IMPORTANTE]
> Il campo `cohort1` deve contenere il **Codice identificativo gruppo globale** generato in fase di creazione della classe e non il nome del gruppo globale.

```csv
username,firstname,lastname,email,password,sysrole1,cohort1
```

---
Infine, poichè nel progetto sono previsti anche i campi personalizzati già definiti precedentemente (vedi [Creare un campo personalizzato per l'utente](user.md#creare-un-campo-personalizzato-per-lutente)), dovrà esserci anche la colonna relativa a ogni campo personalizzato. Questa colonna sarà formata dal termine `profile_field_` seguita dal nome abbreviato del campo, (es `profile_field_datanascita`):<br>

```csv
username,firstname,lastname,email,password,sysrole1,cohort1,profile_field_1, profile_field_2, profile_field_3, ...
```

---
Riassumendo, le colonne sono:

* `username` :material-arrow-right-thin: rappresenta il **token univoco** che l'utente utilizzerà per accedere al sistema
* `firstname` :material-arrow-right-thin: rappresenta il nome dell'utente
* `lastname` :material-arrow-right-thin: rappresenta il cognome dell'utente
* `email` :material-arrow-right-thin: rappresenta l'indirizzo email dell'utente (dovrà essere un email fittizia)
* `password` :material-arrow-right-thin: rappresenta la password assegnata all'utente (non sarà usata, vedi il plugin [Login](plugin.md#login))
* `sysrole1` :material-arrow-right-thin: rappresenta il ruolo che l'utente dovrà avere all'interno del sistema, (vedi **Nome abbreviato** in [Ruolo](role.md))
* `cohort1` :material-arrow-right-thin: rappresenta il gruppo globale (classe) a cui l'utente appartiene
* `profile_field_1`, `profile_field_2`, `profile_field_3`, ... :material-arrow-right-thin: rappresentano i campi personalizzati dell'utente
> [!ESEMPIO]
> ```csv
> username,firstname,lastname,email,password,sysrole1,cohort1,profile_field_datanascita
> TokenMR,Mario,Rossi,emailfittizia.mariorossi@email.it,mr1998,testato,classe_3a,1998-01-01
> TokenAP,Artù,Pendragon,emailfittizia.artupendragon@email.it,ap1999,moderatore,classe_2b,1999-02-02
> ```
> > [!ATTENZIONE]
> > Il campo `profile_field_datanascita`, essendo un campo di tipo Data e Ora, deve rispettare il formato `YYYY-MM-DD` (anno-mese-giorno), altrimenti Moodle non riuscirà a interpretarlo correttamente.




### Creare un nuovo utente o aggiornare quelli esistenti tramite CSV file
> [!TIP]
> Creare nuovi utenti tramite CSV è preferibile perché permette, per esempio, di assegnare direttamente un ruolo senza passi aggiuntivi, opzione non possibile nella creazione singola dell'utente.


1. Accedere alla Home page di Moodle
1. Cliccare su **Utenti** nel menù centrale
1. Nella sezione **Profili** cliccare su **Importazione utenti**
1. Trascinare il file CSV nella sezione apposita e selezionare il tipo di separatore utilizzato (es. `,`)
1. Cliccare su **Importazione utenti**
1. Nella pagina che si apre è importante comprendere cosa fa il campo **Modalità importazione**:

    * **Crea solamente i nuovi utenti, ignora gli utenti già esistenti:** Crea account solo per gli username che non sono ancora presenti nel database di Moodle. Se il file CSV contiene un username già registrato, quella specifica riga viene ignorata senza alterare i dati preesistenti.
    * **Crea tutti gli utenti, aggiungendo un numero agli username ove necessario:** Forza la creazione di un nuovo account per ogni riga del CSV. Se rileva un username in conflitto con uno già a sistema (es. `mario.rossi`), crea un nuovo utente generando una variante numerata (es. `mario.rossi2`).
    * **Crea i nuovi utenti ed aggiorna gli utenti già esistenti:** Inserisce gli account inediti e, per gli username già riconosciuti dal sistema, sovrascrive o popola i campi del profilo (inclusi ruoli o campi custom) con i nuovi valori forniti nel file.
    * **Aggiorna solamente gli utenti già esistenti:** Non genera alcun nuovo profilo. Cerca nel database gli username indicati nel file e ne modifica esclusivamente i dati.

    >[!ATTENZIONE]
    > L'aggiornamento dei dati di un utente già esistente nel sistema tramite CSV non si applica ai ruoli e i gruppi globali.

1. Poichè le password sono definite nel file CSV, scegliere dal menù a tendina **Il campo è presente nel file**
1. Infine cliccare su **Importazione utenti** per terminare.



