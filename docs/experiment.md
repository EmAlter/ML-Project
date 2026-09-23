!!! info "Permessi e Ruoli"
    * **Gestisce (crea, modifica, elimina):** :material-account-hard-hat: Progettista
    * **Visualizza:** :material-account-hard-hat: Progettista

Nel progetto concettuale una sperimentazione rappresenta <u>l'obiettivo dello studio</u> ed ha diverse relazioni con altri elementi del progetto:

* <span class="term">**Composizione** <span class="tip"><strong>Composizione</strong><br>
In UML è una relazione strutturale di tipo "tutto-parte" molto forte, in cui la classe contenitore possiede e controlla totalmente il ciclo di vita degli oggetti contenuti.<br>
</span> </span> 
:material-arrow-right-thin: una sperimentazione è composta [corsi](course.md)
* <span class="term">**Aggregazione** <span class="tip"><strong>Aggregazione</strong><br>
In UML è una relazione strutturale di tipo "tutto-parte" debole, in cui la classe contenitore fa riferimento agli oggetti contenuti, ma non ne controlla il ciclo di vita, i quali possono esistere in modo indipendente.<br>
</span> </span> 
:material-arrow-right-thin: una sperimentazione può avere una o più [valutazioni](evaluation.md) associate
* <span class="term">**Associazione** <span class="tip"><strong>Associazione</strong><br>
In UML è una relazione strutturale di tipo "peer-to-peer", in cui le classi coinvolte comunicano e collaborano tra loro, ma non esiste alcun vincolo gerarchico o di ciclo di vita tra gli oggetti, i quali rimangono totalmente indipendenti.<br>
</span> </span>  :material-arrow-right-thin: una sperimentazione ha associate una o più [classi](class.md) di utenti

<p align="center">
  <img src="../assets/images/experiment.svg" alt="Sperimentazione">
</p>

Ogni sperimentazione ha diversi attributi che la identificano:

* **Nome** :material-arrow-right-thin: rappresenta il nome della sperimentazione, che deve essere univoco all'interno del progetto
* **Anonimità** :material-arrow-right-thin: rappresenta se la sperimentazione è anonima o meno, ovvero se i dati raccolti saranno associati all'identità del testato o meno

## Moodle
In Moodle non esiste un concetto di Sperimentazione, l'elemento che più si avvicina è il Corso.

> [!ATTENZIONE]
> Il **Corso** di Moodle non è equivalente al **Corso** del progetto concettuale!

Come definito precedentemente nel progetto concettuale, una sperimentazione dovrebbe poter essere anonima oppure no, purtroppo in Moodle non è possible definire un corso come anonimo.

### Creare una nuova categoria di corso
Prima di poter creare una nuova sperimentazione, è importante definire un elemento che non è previsto nel progetto concettuale, ma che è necessario in Moodle, cioè la **Categoria di corso**. Essa serve a raggruppare più corsi, ma nel nostro caso potrà essere utilizzata soprattutto in due modi:

* Creando una categoria di corso "generale" nella quale inserire tutte le sperimentazioni, oppure
* Creando una categoria di corso che raggruppa le sperimentazioni in base a un criterio specifico (es. anno, tipologia di test, ecc.)

> [!TIP]
> Si possono anche creare sotto-categorie di corso innestate una dentro l'altra.

I passi da seguire per creare una nuova categoria di corso sono:

1. Accedere a **I miei corsi** nel menù centrale
1. In alto a destra cliccare sul pulsante **Gestisci corsi**, apparirà la lista delle categorie di corso e delle sperimentazioni contenute in esse
1. Cliccare sul pulsante **Crea categoria** e compilare i campi obbligatori:

    * **Categoria di appartenenza** :material-arrow-right-thin: rappresenta la categoria di corso alla quale apparterrà la nuova categoria di corso
    * **Nome categoria** :material-arrow-right-thin: rappresenta il nome della nuova categoria di corso, che deve essere univoco all'interno del progetto

1. Cliccare sul pulsante **Crea categoria** per salvare le impostazioni.

> [!ESEMPIO]
> In questo esempio verrà creatà una possibile categoria di corso per raggruppare le sperimentazioni in base all'anno di creazione:
>   * **Categoria di appartenenza** :material-arrow-right-thin: Primo Livello (per essere a livello di sistema)
    * **Nome categoria** :material-arrow-right-thin: Sperimentazioni 2026

### Eliminare una categoria di corso
I passi da seguire per eliminare una categoria di corso sono:

1. Accedere a **I miei corsi** nel menù centrale
1. In alto a destra cliccare sul pulsante **Gestisci corsi**, apparirà la lista delle categorie di corso e delle sperimentazioni contenute in esse
1. Cliccare sul simbolo **<img src="../assets/icons/dots-vertical.svg" alt="Menù Verticale" width="20">** a destra della categoria di corso che si vuole eliminare e cliccare su **<img src="../assets/icons/delete.svg" alt="Elimina" width="20"> Elimina**
1. Si aprirà una finestra di conferma nella quale sarà necessario compilare il campo **Cosa fare** che ha due opzioni:
    
    * **Sposta i corsi in un'altra categoria** :material-arrow-right-thin: permette di spostare le sperimentazioni contenute nella categoria che si vuole eliminare in un'altra categoria di corso (in questo caso nel campo sottostanse scelto la categoria di corso nella quale si vogliono spostare le sperimentazioni)

        > [!ATTENZIONE]
        > Se si sceglie questa opzione, deve esistere almeno un'altra categoria di corso nella quale spostare le sperimentazioni.
    
    * **Elimina tutto - non sarà possibile tornare indietro** :material-arrow-right-thin: permette di eliminare la categoria di corso e tutte le sperimentazioni contenute in essa

1. Cliccare sul pulsante **Elimina** per confermare l'eliminazione.


### Creare una nuova sperimentazione
I passi da seguire per creare una nuova sperimentazione sono:

1. Accedere alla Home di Moodle
1. In alto a destra cliccare sul pulsante **Modalità modifica**, appariranno diverse nuove "zone" modificabili all'interno della pagina
1. Cliccare sul pulsante **Aggiungi corso** e compilare i campi:

    > [!ATTENZIONE]
    > In fase di creazione della sperimentazione, i campi che Moodle propone sono molti di più di quelli che verranno elencati qui sotto, tuttavia per il progetto concettuale bastano soltanto quelli descritti.<br>
    > Gli altri campi possono essere lasciati (anche se obbligatori) con le impostazioni di default oppure adattarli ad eventuali eccezioni che il progettista ritiene necessarie per la sperimentazione stessa.

    * **Generale**
        - **`Titolo del corso`** :material-arrow-right-thin: rappresenta il nome della sperimentazione
        - **`Titolo abbreviato`** :material-arrow-right-thin: rappresenta il nome breve della sperimentazione, che deve essere univoco all'interno del progetto
        - **`Categoria di corsi`** :material-arrow-right-thin: rappresenta la categoria di corso alla quale appartiene la sperimentazione
    * **Gruppi**
        - **`Modalità gruppo`** :material-arrow-right-thin: rappresenta se la sperimentazione deve essere gestita in modalità gruppo o meno, ovvero se i testati devono essere divisi in gruppi oppure no
        - **`Forza modalità gruppo`** :material-arrow-right-thin: obbliga la divisione in gruppi per ogni modulo Moodle 

1. Cliccare sul pulsante **Salva e visualizza** per salvare le impostazioni della sperimentazione e passare alla pagina di visualizzazione della sperimentazione stessa.

> [!ESEMPIO]
> In questo esempio, verrà mostrato come compilare i campi di un eventuale sperimentazione per rimanere in linea con le richieste del progetto concettuale:
>
>    * **Generale**
>        - **`Titolo del corso`** :material-arrow-right-thin: Sperimentazione n°9
>        - **`Titolo abbreviato`** :material-arrow-right-thin: sperimentazione9
>        - **`Categoria di corsi`** :material-arrow-right-thin: Sperimentazioni 2026
>    * **Gruppi**
>        - **`Modalità gruppo`** :material-arrow-right-thin: Gruppi separati, ogni testato appartiene al gruppo assegnatogli e non può vedere i contenuti degli altri gruppi
>        - **`Forza modalità gruppo`** :material-arrow-right-thin:

            * No, se si prevede di creare, oltre ai test, moduli Moodle (es. Feedback) che saranno compilati da tutti indipendentemente dal gruppo di appartenenza
            * Sì, se si prevede di mantenere la suddivisione in gruppi per qualsiasi altro modulo Moodle che verrà creato all'interno della sperimentazione

### Modificare una sperimentazione
I passi da seguire sono:

1. Accedere a **I miei corsi** nel menù centrale e selezionare la sperimentazione che si vuole modificare
1. Nel menù centrale cliccare su **Impostazioni** e modificare i campi che si vogliono cambiare
1. Cliccare sul pulsante **Salva e visualizza** per salvare le modifiche effettuate.

### Eliminare una sperimentazione
I passi da seguire sono:

1. Accedere a **I miei corsi** nel menù centrale
1. Cliccare sul pulsante **Gestisci corsi** in alto a destra
1. Nella pagina che si aprirà, ci saranno due sezioni: a sinistra la lista delle categorie di corso e a sinistra la lista delle sperimentazioni contenute nella categoria selezionata.<br> 
Cliccare la categoria alla quale appartiene la sperimentazione che si vuole eliminare e poi cliccare sul simbolo **<img src="../assets/icons/delete.svg" alt="Elimina" width="20"> Elimina**
1. Confermare l'eliminazione della sperimentazione nella finestra di conferma cliccando su **Elimina**.

