!!! info "Permessi e Ruoli"
    * **Gestisce (crea, modifica, elimina):** :material-account-hard-hat: Progettista
    * **Visualizza:** :material-account-hard-hat: Progettista, :material-shield-account: Moderatore, :material-account: Testato, :material-account-tie: Esperto

## Concetto
Nel progetto concettuale un'attività ha diversi attributi che la identificano:

* Nome :material-arrow-right-thin: rappresenta il nome dell'attività, che deve essere univoco all'interno del progetto
* Istruzioni :material-arrow-right-thin: rappresentano le istruzioni che il testato deve seguire per completare l'attività
* Tipo :material-arrow-right-thin: rappresenta la tipologia di appartenenza dell'attività (es. Riconoscere un modello tipico, Stile cognitivo ecc.)

Un <span class="term">obiettivo formativo<span class="tip"><strong>Obiettivo formativo</strong><br>Descrizione qui.</span></span> collegato a...

Ed è costituta da una o più [Domande](questions_and_responses.md) che rappresentano il contenuto dell'attività stessa, poi ogni domanda a sua volta sarà costituita da una o più [Risposte](questions_and_responses.md) che rappresentano le possibili scelte, secondo il seguente schema:

<p align="center">
  <img src="../assets/images/activities.svg" alt="Attività">
</p>

> [!ESEMPIO]
> **Nome**: Questionario sulle teorie dell'intelligenza
>
> **Istruzioni**: Leggi ogni frase riportata qui sotto e poi fai una crocetta solo nel quadratino che indica quanto sei d'accordo con l'affermazione.
>
> **Domanda 1**: La tua intelligenza è qualcosa di te che non puoi cambiare.
>
> **Risposte**:
> * [ ] 1a. D'accordo
> * [ ] 1b. Un po' d'accordo
> * [ ] 1c. Un po' contrario
> * [x] 1d. Contrario
>
> **Domanda 2**: Puoi imparare cose nuove, ma non puoi cambiare la tua intelligenza.
>
> **Risposte**:
> * [ ] 2a. D'accordo
> * [x] 2b. Un po' d'accordo
> * [ ] 2c. Un po' contrario
> * [ ] 2d. Contrario

***

## Moodle
In Moodle, non esiste un concetto di Attività nella quale è possibile inserire una o più domande, tuttavia è possibile avere una rappresentazione molto simile attraverso le ==Categorie== gestibili nel [Deposito delle domande](activity-collection.md), che permettono di raggruppare serie di domande.

Il meccanismo è molto semplice, il progettista per ogni attività che ha definito nel progetto, crea una categoria nel [Deposito delle domande](activity-collection.md) di Moodle, e all'interno di questa categoria inserisce tutte le domande che fanno parte dell'attività stessa.

### Creare una nuova attività
Per creare una nuova attività è importante che l'utente sia all'interno di un [Deposito delle domande](activity-collection.md) esistente.
A questo punto i passi sono:

1. Nel menù a tendina in alto a sinistra scegliere "Categorie"
1. Cliccare sul pulsante "Aggiungi categoria" e compilare i campi:

    * **Categoria genitore** :material-arrow-right-thin: es. "Primo livello di sistema" rappresenta a quale categoria si vuole inserire quella nuova
    * **Nome** :material-arrow-right-thin: es. "Questionario sulle teorie dell'intelligenza" rappresenta il nome della nuova categoria
    * **Informazioni categoria (opzionale)** :material-arrow-right-thin: es. "Categoria che contiene le domande del questionario sulle teorie dell'intelligenza" rappresenta la descrizione della nuova categoria

> [!TIP]
> Per una migliore organizzazione delle attività si consiglia di creare una categoria padre contenente tutte le attività concettualmente simili (stesso tipo) e al suo interno sotto-categorie per ogni attività, in questo modo sarà più semplice la loro ricerca.

### Modificare un'attività
Per modificare un'attività è importante che l'utente sia all'interno di un [Deposito delle domande](activity-collection.md) esistente.

1. Nel menù a tendina in alto a sinistra scegliere "Categorie"
1. Scorrere la lista delle categorie fino a trovare quella che si vuole modificare e premere il menù a tre puntini
1. All'interno del menù selezionare "Impostazioni <img src="../assets/icons/edit.svg" alt="Modifica" width="10">" e modificare i campi desiderati.

### Eliminare un'attività
Per eliminare un'attività è importante che l'utente sia all'interno di un [Deposito delle domande](activity-collection.md) esistente.

1. Nel menù a tendina in alto a sinistra scegliere "Categorie"
1. Scorrere la lista delle categorie fino a trovare quella che si vuole eliminare e premere il menù a tre puntini
1. All'interno del menù selezionare "Elimina <img src="../assets/icons/delete.svg" alt="Elimina" width="10">" e confermare l'eliminazione della categoria.
