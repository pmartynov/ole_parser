FROM python:3.7-slim

WORKDIR .

COPY ./init/envs.py .
COPY ./init/main.py .

RUN apt-get update

RUN pip3 install --upgrade awscli

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./init/requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN chmod u+x main.py

ENTRYPOINT [ "python3" , "main.py"]
CMD ['']