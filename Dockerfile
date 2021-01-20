FROM python:3.9.1-alpine

RUN adduser -D admin

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install gunicorn

COPY app.py app.py
COPY config.py config.py
COPY errors.py errors.py
COPY db db
COPY api api

RUN chown -R admin:admin ./
USER admin

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
