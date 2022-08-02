from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts

# Get list of all subtechniques available in the database.
def get_subtechniques(subtechnique=''):
    db = get_db()
    db.row_factory = make_dicts
    try:
        return (
            db.execute(
                'SELECT * FROM subtechniques WHERE id is ?', (subtechnique,)
            ).fetchone()
            if subtechnique
            else db.execute(
                'SELECT id as \'db_id\', subtechnique_id as ID, subtechnique_name as Subtechnique, subtechnique_description as Description FROM subtechniques ORDER BY subtechnique_name ASC'
            ).fetchall()
        )

    except TypeError:
        return False #Change this for something more meaningful -- warning/alert 