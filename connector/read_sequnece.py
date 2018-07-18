import pandas as pd 
import dbconnetor 
import config

def class data_gatter:

    # mysql connection initialize
    def __init__(self) :
        self.mysql =  MySQL(config.config)

#  get df of 'Sequnce'
# sql 'select * from 
    def get_sequnce(self):
        u'''
        return result execution of sql
        '''
        sql =  'select * from uniprot_filtered' 

        return pd.read_sql(sql,mysql.conn)['Sequence']