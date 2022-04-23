import pandas as pd

from ORM.mongo_connection import Connection
from ORM.mutualfund_orm import MutualFund


from utils.utils import getFileNamePart


def csvParser():

    dataframe=pd.read_csv('/Users/karanprinja/Documents/sample'+getFileNamePart()+'.txt',header=0)
    for lines in dataframe.values:
        filtered_value=str(lines).replace('[','').replace(']','')
        if 'Open Ended Schemes' in filtered_value:
            start_index=filtered_value.index('(')
            end_index=filtered_value.index(')')
            if '-' in filtered_value:
                scheme_type,scheme_subtype=(filtered_value[start_index+1:end_index].split("-"))

            else:
                scheme_type= filtered_value[start_index+1:end_index]
        else:
            insertInDb(filtered_value)

def insertInDb(filtered_value):
    conn = Connection(host='0.0.0.0', port=27017, database='dummy')
    conn.connect()
    if ";" in filtered_value:
        data = filtered_value.split(";")
        print(data)
        mf_db_data = MutualFund()
        *name, payout_growth, reinvestment = data[1].split(" ")
        mf_db_data.code = data[0]
        mf_db_data.name = " ".join(name)
        mf_db_data.payout_growth = payout_growth
        mf_db_data.reinvesetment = reinvestment
        mf_db_data.nav = data[4]
        mf_db_data.repurchase_price = data[5]
        mf_db_data.sale_price = data[6]
        mf_db_data.date = data[7]
        mf_db_data.save()

'''
0 = {str} '\'139619'
1 = {str} 'Taurus Investor Education Pool - Unclaimed Dividend - Growth'
2 = {str} ''
3 = {str} ''
4 = {str} '10.0000'
5 = {str} ''
6 = {str} ''
7 = {str} '21-Apr-2022\''
'''

