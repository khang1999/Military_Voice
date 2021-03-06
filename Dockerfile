FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

copy ./requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt

RUN apk del .tmp

RUN mkdir /Military_Voice
COPY ./Military_Voice /Military_Voice

WORKDIR /Military_Voice
COPY ./scripts /scripts

RUN chmod +x /scripts/*
RUN mkdir -p /media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol

RUN chmod -R 777 .

RUN chmod -R 777 /vol/web
USER user

CMD ["entrypoint.sh"]