from flask import Flask
from flask.ext.restful import Api, Resource
from sqlalchemy import Table, Column, Integer, DateTime, String, ForeignKey, MetaData
from datetime import datetime

# OK this is a total naming fail, I admit it :)
class Database:
    def initialize(self):
        metadata = MetaData()

        tracked_items = Table('tracked_items', metadata,
                              Column('tracked_item_id', Integer(), primary_key=True, autoincrement=True),
                              Column('tracked_item_description', String(50), index=True),
                              )

        entries = Table('entries', metadata,
                        Column('entry_ts', DateTime, default=datetime.datetime.utcnow),
                        Column('entry_type', ForeignKey('tracked_items.tracked_item_id')),
                        )

class Container:
    def initialize(self):
        app = Flask(__name__)
        api = Api(app)

        # This may be the wrong place for this?
        api.add_resource(EntryAPI, '/clicker/api/v1.0/entries/<int:id>', endpoint = 'entry')



class EntryAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


