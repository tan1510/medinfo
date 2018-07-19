import pandas as pd 
from dbconnector import MySQL
from config import config
class data_getter:
    # mysql connection initialize
    def __init__(self) :
        self.mysql =  MySQL(config)
#  get df of 'Sequnce'
# sql 'select * from 
    def get_sequence(self):
        u'''
        return result execution of sql
        '''
        sql =  'select * from uniprot_filtered' 

        return pd.read_sql(sql,self.mysql.conn)[['Entry','Sequence']]
        