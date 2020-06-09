FROM python:3.7-buster

WORKDIR /app

COPY .env /app
COPY requirements.txt /app
COPY voice_channel.py /app

RUN apt update && \
  apt install -y libffi-dev libnacl-dev ffmpeg && \
  pip install -r requirements.txt

ENTRYPOINT ["python",  "voice_channel.py"]
