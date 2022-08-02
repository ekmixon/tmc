from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts

# Get list of all tools available in the database.
def get_tools(tool=''):
    db = get_db()
    db.row_factory = make_dicts
    try:
        if not tool:
            return db.execute(
                'SELECT id as \'db_id\', tool_id as ID, tool_name as Tool, tool_description as Description, tool_identifiers as Identifiers FROM tools ORDER BY tool_name'
            ).fetchall()

    except TypeError:
        #embed()
        return False #Change this for something more meaningful -- warning/alert 