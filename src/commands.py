import click
from flask.cli import with_appcontext
from src.ext import db
from src.models import User


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Create database tables"""
    db.drop_all()
    db.create_all()
    click.echo('Database initialized.')


@click.command('populate-db')
@with_appcontext
def populate_db_command():
    """Populate database with an admin user"""
    admin_user = User(username='admin', password='admin123')
    db.session.add(admin_user)
    db.session.commit()
    click.echo('Database populated with admin user')


def register_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)