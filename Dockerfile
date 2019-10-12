FROM python:3

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./app
COPY docker/run.sh .
COPY nbdime/original.ipynb template.ipynb

RUN pip install tf-nightly-2.0-preview

ENV NBDIME_URL "http://localhost:81/d/"
ENV PAGES_PATH "app/pages"

CMD ["sh", "run.sh"]