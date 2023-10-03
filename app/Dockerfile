FROM python:3.12-alpine

# Output logging faster
ENV PYTHONUNBUFFERED 1
# Don't write bytecode
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache \
    ffmpeg

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./* /app/
RUN /usr/bin/crontab ./crontab
RUN crontab -l

CMD ["/usr/sbin/crond", "-f", "-l", "0"]
