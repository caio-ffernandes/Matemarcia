from peewee import AutoField, CharField, Model
from config.database import database

class TermoDB(Model):
    id_termo = AutoField()
    termo_nome = CharField()
    termo_conteudo = CharField()

    class Meta:
        database = database
        table_name = 'termos'