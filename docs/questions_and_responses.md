!!! info "Permessi e Ruoli"
    * **Gestisce (crea, modifica, elimina):** :material-account-hard-hat: Progettista
    * **Visualizza:** :material-account-hard-hat: Progettista, :material-shield-account: Moderatore, :material-account: Testato, :material-account-tie: Esperto

Nel modello di dominio, una **Domanda** è un'entità che dipende strettamente da un'[attività](activity.md) (<u>non può esistere in modo indipendente</u>) ed è a sua volta composta da una o più **Risposte**.<br>
Concettualmente, questi due elementi presentano i seguenti attributi:

* **Domanda - Testo** :material-arrow-right-thin: rappresenta il quesito vero e proprio formulato al Testato:material-account:.
* **Domanda - Tipo** :material-arrow-right-thin: definisce il formato strutturale del quesito (es. a scelta multipla, risposta aperta, vero/falso).
* **Risposta - Testo** :material-arrow-right-thin: rappresenta il contenuto dell'opzione di risposta associata alla domanda.

<p align="center">
  <img src="../assets/images/questions_responses.svg" alt="Domande e Risposte">
</p>

> [!IMPORTANTE]
> Una domanda ha un rapporto di <span class="term">composizione <span class="tip"><strong>Composizione</strong><br>
> In UML è una relazione strutturale di tipo "tutto-parte" molto forte, in cui la classe contenitore possiede e controlla totalmente il ciclo di vita degli oggetti contenuti.<br>
> </span> </span> 
> con le risposte, questo significa che se essa viene eliminata, anche tutte le risposte di cui è composta verrano eliminate.


## Moodle
In Moodle, i concetti di **Domanda** e **Risposta** non sono entità separate.<br>
Vengono gestiti congiuntamente all'interno del [deposito delle domande](activity_collection.md) e si fondono in un unico elemento di configurazione basato sulla tipologia scelta.

> [!ESEMPIO]
> Per esempio, creando una domanda di tipo **Scelta multipla**, la pagina di configurazione incorporerà direttamente i campi per definire le varie risposte associate.

In fase di creazione, una domanda, con le sue risposte, sarà inserita nella categoria corrispondente all'[attività](activity.md) a cui appartiene.
<!-- 
<span class="term">Modulo
<span class="tip"><strong>Modulo</strong><br>
È un componente di Moodle che viene aggiunto a un corso per compiere determinate azioni.<br>
Tra i più utilizzati ci sono: Quiz, Questionario, Glossario, Pagina ecc.
</span>
</span>
-->


### Creare una nuova domanda e le sue risposte
Da definizione una **Domanda** non può esistere senza un'**Attività** in cui essere inserita, per questo motivo è necessario che nel sistema siano già registrate delle attività in cui verrano inserite le domande.

#### Prima parte - Domanda
Una volta che le attività sono state create, i passi per creare una nuova domanda sono:

1. Accedere alla Home page di Moodle
1. Cliccare su **Deposito delle domande** nel menù centrale
1. Nel menù a tendina in alto a sinistra scegliere **Domande**
1. Cliccare su **Crea una nuova domana** e scegliere il **Tipo** di domanda da generare (es. Scelta multipla, Vero/Falso, Risposta breve ecc.)
1. Nella pagina che si apre, compilare questi campi:

    * **Categoria** :material-arrow-right-thin: rappresenta l'attività in cui si vuole inserire la domanda
    * **Nome della domanda** :material-arrow-right-thin: rappresenta il nome della domanda (utile per la ricerca all'interno del Deposito delle domande)
    * **Testo della domanda** :material-arrow-right-thin: rappresenta il quesito o la richiesta vera e propria formulata al Testato:material-account:
    * **Punteggio** :material-arrow-right-thin: rappresenta il punteggio massimo che si può ottenere con la domanda (obbligatorio per default di Moodle, ma non utile ai fini del progetto, quindi va bene anche un valore fittizio)

> [!TIP]
> Nel **Testo della domanda** è utile inserire anche le eventuali informazioni aggiuntive visibili solo al Moderatore:material-shield-account:, come ad esempio il tempo totale per rispondere all'attività o eventuali note di approfondimento (vedi il plugin [FilterCodes](plugin.md#filtercodes)).


#### Seconda parte - Risposte
Una volta compilata la prima parte della pagina che definisce la domanda, si dovrà compilare la seconda parte che definisce, invece, le risposte associate ad essa e che dipende strettamente dal tipo di domanda scelto.

> [!IMPORTANTE]
> **Sebbene il punteggio non verrà mai utilizzato ai fini del progetto**, è necessario però adattare quello (fittizio) definito precedentemente nella domanda, in modo che la somma dei punteggi di tutte le risposte sia uguale al punteggio massimo della domanda stessa, per evitare che Moodle generi un errore.

### Modificare una domanda e le sue risposte
Modificare una domanda e le sue risposte è molto simile al processo di creazione, i passi sono:

1. Accedere alla Home page di Moodle
1. Cliccare su **Deposito delle domande** nel menù centrale
1. Muoversi nella categoria corrispondente all'[attività](activity.md) in cui è inserita la domanda da modificare
1. Scorrere la lista delle domande fino a trovare quella che si vuole modificare e premere **Modifica** nella colonna **Azioni**
1. Nel menù a tendina selezionare **<img src="../assets/icons/edit.svg" alt="Modifica" width="15"> Modifica domanda**
1. Modificare i campi desiderati (sia per la domanda che per le risposte) e cliccare su **Salva modifiche** per terminare l'operazione.

### Eliminare una domanda e le sue risposte
ELiminare una domanda e le sue risposte è molto simile al processo di modifica, i passi sono:

1. Accedere alla Home page di Moodle
1. Cliccare su **Deposito delle domande** nel menù centrale
1. Muoversi nella categoria corrispondente all'[attività](activity.md) in cui è inserita la domanda da modificare
1. Scorrere la lista delle domande fino a trovare quella che si vuole modificare e premere **Modifica** nella colonna **Azioni**
1. Nel menù a tendina selezionare **<img src="../assets/icons/delete.svg" alt="Elimina" width="15"> Elimina**
1. Nella finestra di conferma che si apre, cliccare su **Elimina** per terminare l'operazione.