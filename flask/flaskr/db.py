import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# g = {}

# class sqlite3:
#     def connect(self, a,b):
          # connect database 
#         return self
    # def close(self):
    #     # shut the database connection
    # def executescript(self, text):
    #     # let database execute the script

# g = {
#     'db': sqlite3_instance
# }

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        file_content = f.read().decode('utf8')
        db.executescript(file_content)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)