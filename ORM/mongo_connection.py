import mongoengine
from mongoengine import connect


class Connection:

    def __init__(self,database,host,port):
        self.host=host
        self.database=database
        self.port=port
        self.alias='default'
        self.client=None

    def connect(self):
        if self.client is None:
            self.client =mongoengine.connect(db=self.database,host=self.host,port=self.port)



