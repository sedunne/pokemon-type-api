from fastapi import FastAPI

from funcs import *


app = FastAPI()

## routes
@app.get("/")
async def get_root():
    """Root path."""
    return {"message": "gotta catch 'em all"}


@app.get("/{type_name}")
async def get_type_chart(type_name: str, generation: int = 8):
    """This path returns the effectiveness of moves with type {type_name} against other types in a given generation. In other words, a JSON move-type chart."""
    typechart = build_type_dict_from_row(get_type_row_by_gen(type_name.capitalize(), generation))
    typechart["generation"] = generation
    return typechart


@app.get("/{type_name}/weakness")
async def get_weakness_chart(type_name: str, generation: int = 8):
    """This path returns the weaknesses of pokemon with type {type_name}."""
    return get_type_weaknesses(type=type_name.capitalize(), gen=generation)


@app.get("/{attacking}/{defending}")
async def get_type_path(attacking: str, defending: str, generation: int = 8):
    """This path returns the effectiveness of a move of type {attacking} against a defending Pokemon of type {defending}."""
    return get_type_effectiveness(attacking.capitalize(), defending.capitalize(), generation)
