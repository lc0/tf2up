FROM python:3

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./app
COPY docker/run.sh .

ENV NBDIME_URL "http://localhost:81/d/"

CMD ["sh", "run.sh"]