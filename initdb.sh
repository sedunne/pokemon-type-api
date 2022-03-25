#!/bin/sh

curl -L -o data/Pokemon.csv https://raw.githubusercontent.com/lgreski/pokemonData/master/Pokemon.csv
sqlite3 db/pokemon-type-api.db < data/import.sql