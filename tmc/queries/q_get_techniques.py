from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts

# Get list of all techniques available in the database.
def get_techniques(technique=''):
    db = get_db()
    db.row_factory = make_dicts
    try:
        return (
            db.execute(
                'SELECT * FROM techniques WHERE id is ?', (technique,)
            ).fetchone()
            if technique
            else db.execute(
                'SELECT id as \'db_id\', technique_id as ID, technique_name as Technique, technique_description as Description FROM techniques ORDER BY technique_name ASC'
            ).fetchall()
        )

    except TypeError:
        return False #Change this for something more meaningful -- warning/alert 