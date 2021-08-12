FROM python:3

LABEL maintainer="vollborn <oliver.vollborn@gmail.com>"
LABEL version="1.0"
LABEL description="A bot to track file changes on my school platform"

WORKDIR /app

ENV MOODLE_USERNAME=""
ENV MOODLE_PASSWORD=""
ENV DISCORD_WEBHOOK_URL=""

COPY src/ ./src
COPY requirements.txt ./
COPY bse-file-bot.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./bse-file-bot.py" ]
