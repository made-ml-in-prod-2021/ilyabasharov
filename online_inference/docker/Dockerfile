FROM python:3.8-slim

MAINTAINER Ilya Basharov <ilya.basharov.98@mail.ru>

WORKDIR /home

COPY . .

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir --upgrade setuptools && \
    python3 -m pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3", "src/app.py", "--host", "0.0.0.0", "--port",  "8000"]
