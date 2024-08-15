FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && apt-get clean

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3"]

CMD ["server.py"]
