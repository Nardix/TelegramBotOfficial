# Usa un'immagine di Python ufficiale da Docker Hub
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

# Copia il tuo script Python nella directory di lavoro del container
COPY query.py /app/query.py
COPY bot.py /app/bot.py
COPY .env /app/.env
COPY Audio/ /app/res/

# Imposta la directory di lavoro
WORKDIR /app

# Installa le dipendenze del tuo script, se necessario
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# it_IT.UTF-8 UTF-8/it_IT.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG it_IT.UTF-8
ENV LC_ALL it_IT.UTF-8
ENV LC_NUMERIC it_IT.UTF-8

# Comando predefinito che verrà eseguito quando il container viene avviato
CMD ["python", "bot.py"]