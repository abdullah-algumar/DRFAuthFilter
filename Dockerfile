FROM python:3.8.10

ENV PYTHONUNBUFFERED=1

WORKDIR /core
COPY . /core

RUN pip install -r requirements.txt
CMD ["bash","/IstanbulBorsa/docker-entrypoint.sh"]