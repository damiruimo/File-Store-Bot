FROM python:3.10-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
 && apt install -y git \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /VJ-File-Store

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
