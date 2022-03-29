import sqlite3

def db_connect():
    """This function returns a connection object for the sqlite db."""
    try:
        db = sqlite3.connect('db/pokemon-type-api.db')
        return db
    except:
        raise sqlite3.Error


def map_gen_to_table(generation: int):
    """This function returns the correct type table for a given generation, as multiple generations will share a type table."""
    if generation == 1:
        return 'gen1'
    elif 2 <= generation < 6:
        return 'gen2'
    else:
        return 'gen6'


def build_type_dict_from_row(row: sqlite3.Row):
    """This function takes a row from a sqlite3 query, and returns a dict of damage modifers by type."""
    type_dict = {'type': row[0], "effectiveness": {}}
    for i in range(len(row.keys())):
        if i == 0:
            continue
        else:
            type_dict['effectiveness'][row.keys()[i]] = row[i]
    return type_dict


def get_type_row_by_gen(type: str, gen: int = 8):
    """This function returns all the damage modifiers for a given type, based on generation."""
    gentable = map_gen_to_table(gen)
    try:
        db = db_connect()
        db.row_factory = sqlite3.Row
        cur = db.cursor()
        ## this sucks, but you can't use query params for table names, and since the data doesn't (directly) come from a user, should be "safe" from injection attacks.
        cur.execute("SELECT * FROM %s WHERE TYPE = ?" % gentable, [type])
        return cur.fetchone()
    except:
        raise
    finally:
        db.close()


## maybe there's a better way to do a "column select" than this
def get_type_weaknesses(type: str, gen: int = 8):
    """This function returns a dict of defending damage modifiers (weaknesses) based on a given type."""
    gentable = map_gen_to_table(gen)
    types = []
    modifiers = []
    try:
        db = db_connect()
        cur = db.cursor()
        cur.execute("SELECT %s FROM %s" % (type, gentable))
        modifiers = cur.fetchall()
        cur.execute("SELECT Type FROM %s" % gentable)
        types = cur.fetchall()
    except:
        raise
    finally:
        db.close()

    weaknesses = {"type": type, "weaknesses": {}, "generation": gen}
    for i in range(len(types)):
        weaknesses['weaknesses'][types[i][0]] = modifiers[i][0]

    return weaknesses

def get_type_effectiveness(attacking: str, defending: str, generation: int = 8):
    """This function gets the effectiveness of an attacking move type against a defending pokemon type."""
    type_row = get_type_row_by_gen(type=attacking, gen=generation)
    return {"attacking" : attacking, "defending" : defending, "effectiveness": type_row[defending], "generation": generation}

