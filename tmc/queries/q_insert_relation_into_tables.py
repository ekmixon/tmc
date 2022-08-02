from flask import ( g, redirect, url_for )
from tmc.db import get_db

# Isert relation into db from any table
def insert_relation_into_tables(table, relation_name, element_name, related_id, element_id):

    author_id = g.user['id']

    g.db = get_db()
    query = f'INSERT INTO {table} (author_id, {relation_name}, {element_name}) VALUES (?, ?, ?)'


    result = g.db.execute(query, (author_id, related_id, element_id))
    g.db.commit()
    element_id = result.lastrowid

    return element_id