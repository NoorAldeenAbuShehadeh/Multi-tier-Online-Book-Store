FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask flask_cors requests

RUN pip install gunicorn

EXPOSE 5001

CMD ["gunicorn", "main:app", "-w", "1", "--bind", "0.0.0.0:5001"]
