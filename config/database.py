from peewee import MySQLDatabase

# Conexão com o banco de dados MySQL
database = MySQLDatabase(
    'matemarcia',
    user='root',
    host='127.0.0.1',
    port=3306,
)


def startup_db():
    if database.is_closed():
        database.connect()

    from models.termos import TermoDB

    database.create_tables(
        [
            TermoDB

        ]
    )


def shutdown_db():
    if not database.is_closed():
        database.close()
