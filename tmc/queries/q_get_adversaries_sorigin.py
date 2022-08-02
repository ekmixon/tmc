from flask import ( g, redirect, url_for )
from tmc.db import get_db, make_dicts

# Get list of all adversaries available in the database.
def get_adversaries_sorigin():

    db = get_db()
    try:
        db.row_factory = make_dicts
        return db.execute(
            'SELECT adversary_sorigin as \'Suspected Origin\', GROUP_CONCAT(adversary_name) as Adversary \
            FROM adversaries \
            where adversary_sorigin is not null \
            GROUP BY adversary_sorigin;'
        ).fetchall()

    except TypeError:
        #embed()
        return False #Change this for something more meaningful -- warning/alert 