from flask import ( g, redirect, url_for )
from tmc.db import get_db

# Isert into db for any table
def insert_into_events(event_name, event_description, event_url):

    author_id = g.user['id']

    g.db = get_db()

    query = 'INSERT INTO events (author_id, event_name, event_description, event_url) VALUES (?, ?, ?, ?)'


    result = g.db.execute(query, (author_id, event_name, event_description, event_url))
    g.db.commit()
    return result.lastrowid