from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts

# Get list of all techniques available in the database.
def get_tactics(tactic=''):
    db = get_db()
    db.row_factory = make_dicts
    try:
        return (
            db.execute(
                'SELECT * FROM tactics WHERE id is ?', (tactic,)
            ).fetchone()
            if tactic
            else db.execute(
                'SELECT id as \'db_id\', tactic_id as ID, tactic_name as Tactic, tactic_description as Description FROM tactics ORDER BY tactic_name ASC'
            ).fetchall()
        )

    except TypeError:
        return False #Change this for something more meaningful -- warning/alert 