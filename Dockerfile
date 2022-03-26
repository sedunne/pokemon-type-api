FROM python:3.10-slim
WORKDIR /usr/src/app

LABEL org.opencontainers.image.authors="Stephen Dunne"
LABEL org.opencontainers.image.url="https://hub.docker.com/repository/docker/sedunne/pokemon-type-api"
LABEL org.opencontainers.image.source="https://github.com/sedunne/pokemon-type-api"
LABEL org.opencontainers.image.title="pokemon-type-api"
LABEL org.opencontainers.image.version="0.1.0"

RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
  apt update && apt-get --no-install-recommends install -y sqlite3

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN /bin/bash initdb.sh

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["--host=0.0.0.0", "main:app"]