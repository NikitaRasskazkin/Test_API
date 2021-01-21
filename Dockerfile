FROM python:3.9.1-alpine

RUN adduser -D admin

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --no-cache-dir gunicorn

COPY . .

RUN chown -R admin:admin ./
USER admin

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
