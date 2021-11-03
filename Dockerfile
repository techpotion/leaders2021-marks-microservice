FROM python:3.9-slim-bullseye

WORKDIR /app

COPY production_requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python3", "main.py"]