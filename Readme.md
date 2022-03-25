# Pokemon Type API
This is a simple API that mimics the behavior of a typical move type chart.

## Setup
Install the required Python modules:
```
pip install -r requirements.txt
```

The sqlite3 database needs to be initialized, and can be done so with the helper script:
```
./initdb.sh
```

## Paths
As the project is built on [FastAPI](https://github.com/tiangolo/fastapi), apidocs are available on the `/docs` and `redoc` paths. The main paths are also summarized below:

### `/type/{type_name}`
This path takes a Pokemon type (e.g. Ghost), and with no additional options will display it's effectiveness against all other types in the current generation (8). Generation can be manually specified with the `generation` (int) query parameter.

Optionally, a `defending` query parameter can be passed containing another Pokemon type (e.g. Bug), which will only return the effectiveness of the first type against this provided defending type.

## Sources
The type CSV files are created by me, based on the type charts provided by [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Type/Type_chart). Additionally, I source the data for the `pokemon` table from the [pokemonData project](https://github.com/lgreski/pokemonData) (currently unused, but for future features).