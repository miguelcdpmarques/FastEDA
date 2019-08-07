import click

from sqlalchemy_utils import database_exists, create_database

from fasteda.app import create_app, db
from fasteda.models import User

# Create an app context for the database connection.
app = create_app()
db.app = app


@click.group()
def cli():
    """ Run PostgreSQL related tasks. """
    pass


@click.command()
def init():
    """Initialize the database."""
    db.drop_all()
    db.create_all()
    DB_URI = app.config['SQLALCHEMY_DATABASE_URI']

    if not database_exists(db_uri):
        create_database(db_uri)

    return None


@click.command()
def seed():
    """
    Seed the database with an initial user.

    :return: User instance
    """
    if User.find_by_identity(app.config['SEED_ADMIN_EMAIL']) is not None:
        return None

    params = {
        'role': 'admin',
        'email': app.config['SEED_ADMIN_EMAIL'],
        'password': app.config['SEED_ADMIN_PASSWORD']
    }

    return User(**params).save()


@click.command()
@click.pass_context
def reset(ctx):
    """Init and seed automatically"""
    ctx.invoke(init)
    ctx.invoke(seed)

    return None


cli.add_command(init)
cli.add_command(seed)
cli.add_command(reset)
