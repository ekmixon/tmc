from flask import ( g, redirect, url_for )
from tmc.db import get_db

# Insert relation adversary per tool
def insert_adversary_x_tool(adversary_id, tool_id):
    author_id = g.user['id']

    g.db = get_db()
    query = 'INSERT INTO adversaries_x_tools (author_id, adversary_id, tool_id) VALUES (?, ?, ?)'


    result = g.db.execute(query, (author_id, adversary_id, tool_id))
    g.db.commit()
    return result.lastrowid