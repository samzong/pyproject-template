FROM python:3.11-slim

LABEL maintainer="samzong.lu@gmail.com"

WORKDIR /app

COPY ./* $WORKDIR

RUN cd $WORKDIR
RUN poetry install --no-dev

EXPOSE 5000

CMD ["uvicorn", "main:app" ,"--host", "0.0.0.0", "--port", "5000"]