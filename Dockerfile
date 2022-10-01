FROM python:3.7

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN
COPY . app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

