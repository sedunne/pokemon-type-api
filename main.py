from fastapi import FastAPI

from funcs import *

## default to use Gen 8 typing
APP_DEFAULT_GEN: int = 8

app = FastAPI()

## routes
@app.get("/")
async def get_root():
    """Root path."""
    return {"message": "gotta catch 'em all"}


@app.get("/pokemon/{pokemon_name}")
async def get_weakness_by_pokemon(pokemon_name: str):
    """This path returns the move-type effectiveness for attacks against the given Pokemon."""
    lookup_types = get_pokemon_types(pokemon_name.capitalize())
    if type:
        types = get_type_weaknesses(type=lookup_types[0].capitalize())
        return {pokemon_name.capitalize() : types}
    else:
        return {"message" : "could not find type for %s" % pokemon_name}


@app.get("/{type_name}")
async def get_type_chart(type_name: str, generation: int = APP_DEFAULT_GEN):
    """This path returns the effectiveness of moves with type {type_name} against other types in a given generation. In other words, a JSON move-type chart."""
    if not is_valid_type(type_name.capitalize(), generation=generation):
        return {"error": "%s is not a valid type for generation %s" % (type_name, generation)}

    typechart = build_type_dict_from_row(get_type_row_by_gen(type_name.capitalize(), generation))
    typechart["generation"] = generation
    return typechart


@app.get("/{type_name}/weakness")
async def get_weakness_chart(type_name: str, generation: int = APP_DEFAULT_GEN):
    """This path returns the weaknesses of pokemon with type {type_name}."""
    if not is_valid_type(type_name.capitalize(), generation=generation):
        return {"error": "%s is not a valid type for generation %s" % (type_name, generation)}

    return get_type_weaknesses(type=type_name.capitalize(), gen=generation)


@app.get("/{attacking}/{defending}")
async def get_type_path(attacking: str, defending: str, generation: int = APP_DEFAULT_GEN):
    """This path returns the effectiveness of a move of type {attacking} against a defending Pokemon of type {defending}."""
    if not is_valid_type(attacking.capitalize(), generation=generation):
        return {"error": "%s is not a valid type for generation %s" % (attacking, generation)}

    if not is_valid_type(defending.capitalize(), generation=generation):
        return {"error": "%s is not a valid type for generation %s" % (defending, generation)}

    return get_type_effectiveness(attacking.capitalize(), defending.capitalize(), generation)

