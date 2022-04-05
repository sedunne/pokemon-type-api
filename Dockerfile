FROM python:3.10-slim
WORKDIR /usr/src/app

LABEL org.opencontainers.image.authors="Stephen Dunne"
LABEL org.opencontainers.image.url="https://hub.docker.com/repository/docker/sedunne/pokemon-type-api"
LABEL org.opencontainers.image.source="https://github.com/sedunne/pokemon-type-api"
LABEL org.opencontainers.image.title="pokemon-type-api"
LABEL org.opencontainers.image.version="1.1.0"

## ran into issues with buildkit cache mount in github actions, so just do it the old way for now
RUN apt-get update && apt-get --no-install-recommends install -y curl sqlite3

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN /bin/bash initdb.sh

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["--host=0.0.0.0", "main:app"]
