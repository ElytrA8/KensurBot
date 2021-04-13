FROM kenhv/kensurbot:debian

RUN set -ex \
    && git clone -b master https://github.com/just6chill/KensurBot /root/userbot \
    && chmod 777 /root/userbot 
    apt-get install gcc

WORKDIR /root/userbot/

CMD ["python3", "-m", "userbot"]
