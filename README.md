# INSTALLAZIONE FREE KIOSK

## Sommario

- [Requisiti](#requisiti)
- [Download risorse](#download-risorse)
- [Preparazione tablet](#preparazione-tablet)
- [Installazione](#installazione)
- [Configurazione](#configurazione)
- [Informazioni aggiuntive](#informazioni-aggiuntive)    

---
### Requisiti

- Tablet Android (versione 8.0 o superiore)
- PC con accesso a internet (Windows, Mac o Linux)
- Cavo USB per collegare il tablet al PC

---
### Download risorse
1. Scaricare l’ultima versione di Free Kiosk dal sito ufficiale: [Free Kiosk](https://github.com/RushB-fr/freekiosk)
2. Scaricare il pacchetto ADB (Android Debug Bridge) dal sito ufficiale: [ADB](https://developer.android.com/studio/releases/platform-tools)

---
### Preparazione tablet
1. Ripristinare il dispositivo ai dati di fabbrica evitando di fare login con qualsiasi tipo di account al primo avvio
2. Una volta ripristinato, accedere alle impostazioni, cercare tra le info la versione di build e premere 7 volte su di essa per sbloccare le opzioni sviluppatore
3. Entrare nel menù delle opzioni sviluppatore e scorrere fino a trovare e attivare Debug USB

---
### Installazione
1. Estrarre la cartella platorm-tools dal pacchetto ADB scaricato in precedenza
2. Inserire il file apk dell'app Free Kiosk nella cartella platform-tools
3. Aprire il terminale (o prompt dei comandi) e navigare nella cartella platform-tools
4. Collegare il tablet al PC tramite cavo USB e verificare che sia connesso con opzione trasferimento file (MTP)
5. Digitare il comando `.\adb devices` per verificare che il tablet sia riconosciuto dal PC, a questo punto dovrebbe comparire un messaggio sul tablet per autorizzare il debug USB, accettare.
Una volta accettato, digitare nuovamente il comando `.\adb devices`, il terminale dovrebbe mostrare il numero di serie del tablet con la dicitura "device"
> Se invece di "device" dovesse uscire la dicitura "unauthorized", vuol dire che non è stato accettato il messaggio sul tablet durante la connessione.
> In tal caso scollegare e ricollegare il tablet al PC, accettare nuovamente il messaggio sul tablet e ripetere il comando `.\adb devices` fino a quando non compare la dicitura "device"
6. Digitare il comando `.\adb install nomefile.apk` sostituendo "nomefile.apk" con il nome del file apk di Free Kiosk, per installare l'app sul tablet
7. Una volta completata l'installazione, NON APRIRE L'APP, ma digitare il comando `.\adb shell dpm set-device-owner com.freekiosk/.DeviceAdminReceiver` per impostare Free Kiosk come amministratore del dispositivo
8. Scollegare il tablet dal PC e riavviare il dispositivo, a questo punto Free Kiosk sarà impostato come app predefinita

---
### Configurazione
Una volta riavviato il tablet, Free Kiosk si avvierà automaticamente chiedendo di impostare un PIN, ecco alcune impostazioni da configurare per il corretto funzionamento dell'app:
| Menù        | Opzione     | Cosa fare      | 
| ----------- | ----------- | ------------- |
| General     | URL to Display | Inserire l'URL del sito web da visualizzare |
| General     | Auto Reload    | Abilitare Reload on Error |
| Display     | Keep Screen On | Abilitare |
| Security    | Enable Lock Mode | Attivare e abilitare Block Power Menu |
| Security    | Launch on Boot | Abilitare impostando anche i permessi nelle impostazioni del tablet |
| Security    | Set FreeKiosk as default launcher | Abilitare |
| Security    | Enable Lock Screen Controls | Abilitare e disattivare tutto tranne Brightness control on lock screen |

Alla fine della configurazione, scorrere in fondo al menù e premere il pulsante "Save", a questo punto Free Kiosk mostrerà la pagina web inserita.

---
### Informazioni aggiuntive
Per uscire dalla modalità kiosk, l'app è impostata di default premendo 5 volte in qualsiasi punto dello schermo e inserendo la password inserita al primo avvio. La password uò essere modificata in Settings > General > Password

Per rimuovere l'amministrazione del dispositivo da parte di Free Kiosk, è necessario andare in Settings > Advanced > Remove Device Owner.

Per spegnere il tablet, poiché il tasto di accensione è bloccato, è necessario andare in Settings > Advanced > Exit Kiosk Mode, una volta seguiti i passaggi sarà possibile spegnere il tablet normalmente.
