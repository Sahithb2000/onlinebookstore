
from flask import g #type:ignore
import sqlite3

from app import app
def connect_db():
    return sqlite3.connect(app.config.DATABASE)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config.DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = list(cur.fetchall())
    print(f"Query Result : {rv}")
    if rv is None or len(rv) == 0:
        return None 
    if one:
        d = {}
        rv = rv[0]
        for idx,col in enumerate(cur.description):
            d[col[0]] = rv[idx]
        cur.close()
        return d
    else:
        cur.close()
        return rv

def update_db(query, args=()):
    get_db().execute(query, args)
    get_db().commit()
    return True
