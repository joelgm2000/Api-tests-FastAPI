FROM python:3.10.7-slim

COPY ./main /app/install

WORKDIR /app

RUN pip install requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "host=0.0.0.0", "--reload"]