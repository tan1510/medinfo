import pandas as pd 
from connection_setting import MySQL
import config

if __name__ == '__main__'
'''
mysql = MySQL(config.config)

sql =  'select * from uniprot_filtered' 

df = pd.read_sql(sql,mysql.conn)

print(df['Sequence'])
'''
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

        return pd.read_sql(sql,mysql.conn)