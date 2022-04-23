import mongoengine
from mongoengine import *

from ORM.mongo_connection import Connection


class MutualFund(Document):
    code=StringField()
    name=StringField()
    payout_growth=StringField()
    reinvesetment=StringField()
    nav=StringField()
    repurchase_price=StringField()
    sale_price=StringField()
    date=StringField(required=True)
