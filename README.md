# Bot Telegram

## 📋 Indice

- [Bot Telegram](#bot-telegram)
  - [📋 Indice](#-indice)
  - [✨ Caratteristiche](#-caratteristiche)
  - [🔧 Prerequisiti](#-prerequisiti)
  - [🚀 Installazione](#-installazione)
  - [⚙️ Configurazione](#️-configurazione)
  - [🎮 Utilizzo](#-utilizzo)
    - [Avvio del Bot](#avvio-del-bot)
    - [Utilizzo con Docker (opzionale)](#utilizzo-con-docker-opzionale)
  - [📝 Comandi Disponibili](#-comandi-disponibili)
  - [🔍 Funzionalità Avanzate](#-funzionalità-avanzate)
    - [Neo4j](#neo4j)
  - [🤝 Contribuire](#-contribuire)
  - [🐛 Segnalazione Bug](#-segnalazione-bug)
  - [📄 Licenza](#-licenza)
  - [🔗 Link Utili](#-link-utili)
  - [🏆 Crediti](#-crediti)
  - [📊 Badge](#-badge)

## ✨ Caratteristiche

Bot di telegram per contare "punteggi" (es. ogni volta che si beve acqua, ogni volta che si va in bagno ecc...) nei gruppi telegram

il bot funziona tranquillamente su diversi gruppi e per ognuno crea una classifica mensile (si resetta ogni mese) e totale (senza reset)
visualizzabili tramite gli appositi comandi

## 🔧 Prerequisiti

- Python 3.8 o superiore
- Docker (opzionale)
- Neo4j
- Account Telegram
- Token del bot ottenuto da [@BotFather](https://t.me/botfather)

## 🚀 Installazione

1. **Clona il repository**
   ```bash
   git clone https://github.com/Nardix/Bot-Telegram.git
   cd Bot-Telegram
   ```

2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configurazione

1. **Ottieni il token del bot**
   - Vai su [@BotFather](https://t.me/botfather) su Telegram
   - Usa il comando `/newbot` e segui le istruzioni
   - Copia il token fornito

2. **Configura le variabili d'ambiente**
   
   Crea un file `.env` nella root del progetto e sostituisci i ??? con i tuoi dati:
   ```env
   NEO4J_URI=???
   NEO4J_USERNAME=???
   NEO4J_PASSWORD=???
   TOKEN_ORIGINAL=???
   TOKEN_TEST=???
   CHAT_ID=???
   ```

## 🎮 Utilizzo

### Avvio del Bot

```bash
python bot.py
```

### Utilizzo con Docker (opzionale)

```bash
docker-compose up
```

## 📝 Comandi Disponibili

| Comando | Descrizione |
|---------|-------------|
| `/start` | Ti registra per iniziare i conteggi | 
| `/help` | Mostra la lista completa dei comandi | 
| `/profilo` | Permette di visualizzare i propri dati | 
| `/classifica` | Visualizza la classifica mensile | 
| `/classifica_totale` | Visualizza la classifica sul totale dei punteggi |
| `/record` | Mostra la classifica dei record massimi raggiunti |

## 🔍 Funzionalità Avanzate

### Neo4j

Bisogna avviare un istanza di Neo4j (gratuita)

## 🤝 Contribuire

I contributi sono sempre benvenuti! Ecco come puoi aiutare:

1. **Fork** il progetto
2. **Crea** un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. **Push** al branch (`git push origin feature/AmazingFeature`)
5. **Apri** una Pull Request

## 🐛 Segnalazione Bug

Se trovi un bug, per favore:

1. Controlla se è già stato segnalato nelle [Issues](https://github.com/Nardix/Bot-Telegram/issues)
2. Se non esiste, crea una nuova issue con:
   - Descrizione dettagliata del problema
   - Steps per riprodurre il bug
   - Environment (OS, Python version, etc.)
   - Log dell'errore (se disponibile)

## 📄 Licenza

Questo progetto è rilasciato sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per i dettagli.

## 🔗 Link Utili

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [BotFather](https://t.me/botfather)

## 🏆 Crediti

Creato con ❤️ da [Nardix](https://github.com/Nardix)

---

⭐ Se questo progetto ti è stato utile, considera di mettere una stella!

## 📊 Badge

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
