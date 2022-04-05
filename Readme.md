# Pokemon Type API
This is a simple API that mimics the behavior of a typical move type chart.

Note, that currently dual-typing/4x effectiveness is ignored and values will only be pulled based on what's set as the Pokemon's "Type1" value in the pokemonData CSV. This will be supported in a future update.

## Setup
### Manual
Install the required Python modules:
```
pip install -r requirements.txt
```

The sqlite3 database needs to be initialized, and can be done so with the helper script:
```
./initdb.sh
```

Run the app with `Uvicorn` to start the service on the default address of `127.0.0.1:8000`:
```
uvicorn main:app
```

### Docker
Releases are automatically built for x86 and arm64 and pushed to [DockerHub](https://hub.docker.com/r/sedunne/pokemon-type-api). The image can be ran with something like:
```
docker run -dp 8000:8000 --name pokemon-type-api sedunne/pokeon-type-api:latest
```

## Paths
As the project is built on [FastAPI](https://github.com/tiangolo/fastapi), apidocs are available on the `/docs` and `redoc` paths. The main paths are also summarized below:

### `/{type_name}`
This path takes a Pokemon type (e.g. Ghost), and with no additional options will display it's effectiveness against all other types in the current generation (8). Generation can be manually specified with the `generation` (int) query parameter.

Optionally, a `defending` query parameter can be passed containing another Pokemon type (e.g. Bug), which will only return the effectiveness of the first type against this provided defending type.

### `/{type_name}/weakness`
Inverse of the `/{type_name}` path, this path will show the weaknesses or defending efficacy against all other types in a given generation. Generation can be manually specified with the `generation` (int) query parameter.

### `/{attacking_type}/{defending_type}`
Similar to the `/{type_name}` path, except filters the output to one specific defending type. Generation can be manually specified with the `generation` (int) query parameter.

### `/pokemon/{pokemon_name}`
Similar to the `/{type_name}/weakness` path, but returns the weakness/efficacy list of move types against a specific Pokemon, without needing to specify its type. Currently locked to Gen8 typing, as this is all that the pokemonData source currently provides.

## Sources
The type CSV files are created by me, based on the type charts provided by [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Type/Type_chart). Additionally, I source the data for the `pokemon` table from the [pokemonData project](https://github.com/lgreski/pokemonData) (currently unused, but for future features).
