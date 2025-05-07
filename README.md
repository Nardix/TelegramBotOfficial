# Bot-Telegram

- [Bot-Telegram](#bot-telegram)
  - [Modo d'uso](#modo-duso)
  - [Prima di iniziare](#prima-di-iniziare)
  - [Docker](#docker)
  - [Python](#python)
    - [Requirements per python](#requirements-per-python)

Bot personale di telegram per contare "punteggi" (es. ogni volta che si beve acqua, ogni volta che si va in bagno ecc...) nei gruppi telegram

il bot funziona tranquillamente su diversi gruppi e per ognuno crea una classifica mensile (si resetta ogni mese) o totale (senza reset)
visualizzabili tramite gli appositi comandi (vedere - [Modo d'uso](#modo-duso))

## Modo d'uso

ci sono diversi comandi:

| Comando | Utilizzo |
| :---: | :---: |
| /start | usato da ogni utente per registrarsi |
| /profilo | per vedere i propri dati |
| /classifica | per vedere la classifica mensile |
| /classifica_totale | per vedere la classifica sul totale dei punteggi |
| /record | per vedere la classifica dei record massimi raggiunti |

## Prima di iniziare

Genera un token per il bot tramite BotFather (https://telegram.me/BotFather) 

Creare un istanza in neo4j (e' gratis e dura per sempre)

Rinomina il file .env.dummy in .env

Inserisci i dati (URI,username e password di Neo4j e Token di telegram) nel file .env

## Docker

lancia il comando: 
- `docker-compose up`

## Python

lancia il comando:
- `python bot.py`

### Requirements per python

- `python-telegram-bot==20.7`
- `python-telegram-bot[job-queue]==20.7`
- `py2neo`
- `python-dotenv`