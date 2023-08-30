FROM python:3.8.10

ENV PYTHONUNBUFFERED=1

WORKDIR /core
COPY . /core

RUN pip install -r requirments.txt

EXPOSE 8000

CMD ["bash","/core/docker-entrypoint.sh"]

