import pandas as pd 
import dbconnector
import config
import mysql.connector
import pymysql.cursors

class data_getter:
    df = pd.read_csv('massdata.csv',index_col=0)
    text = ''
    massdf = df.T
    # mysql connection initialize
    def __init__(self) :
        self.mysql =  dbconnector.MySQL(config.config)
        self.connection = pymysql.connect(host = config.host,
                                        user = config.user,
                                        password = config.password,
                                        db = config.db)

#  get df of 'Sequnce'
# sql 'select * from 
    def get_sequnce(self):
        u'''
        return result execution of sql
        '''
        sql =  'select * from uniprot_filtered' 

        return pd.read_sql(sql,mysql.conn)['Sequence']
    
    def create_eil_table(self):
        df = pd.read_table('uniprot_fragment.tsv')
        connection = pymysql.connect(host = config.host,
                                        user = config.user,
                                        password = config.password,
                                        db = config.db)
        for seri in df.iterrows():
            sql_1 = ('INSERT INTO EIL (Entry,Isoform,length) VALUES (%s,%s,%s)')
            connection.cursor().execute(sql_1,(seri[1]['Entry'],seri[1]['Entry name'],seri[1]['Length']))
            print('insert')
        connection.commit()
    
    def peptide_text_cut_process_by_tryp(self,text):
        split_by_KandR_list = [text.replace(' ','').replace('\n','').replace('KR',';'). 
        replace('K','K:').replace('R','R:').replace(';','KR').split(':')]
        return split_by_KandR_list

    def get_mass(self,text):
     
        result = 0
        i=0
        # print (text)
        while (i<=len(text)):
            try :
       # print(self.massdf[self.text[i:i+2]])
                result = result+self.massdf[text[i:i+2]][0]
                i=i+2
            except KeyError as e:
      #  sqlist = sq_series.values()  
     #   print(e)
                #print(self.massdf[self.text[i]])
                if(i!=len(text)):
                    try :
                        result = result+self.massdf[text[i]][0]
                    except KeyError as e:
                        print(e)
                i=i+1
    #print(result)
        return result


    def create_split_seq_table(self):
        df = pd.read_table('uniprot_fragment.tsv')
        dg = data_getter()
        for seri in df.iterrows():
            sq_f_list = dg.peptide_text_cut_process_by_tryp(seri[1]['Sequence'])
            s_pos = 0
            g_pos=  0
            no = 1
            for sq_f in sq_f_list:
                sql = ('INSERT INTO uniprot_slice_sequence (Isoform,no,seq,s_pos,g_pos,mass) Values (%d,%d,%s,%d,%d,%d)')
                self.connection.cursor().execute(sql,[seri[1]['Entry name'],no,sq_f,s_pos,g_pos,dg.get_mass(sq_f)])
                s_pos = g_pos
                no = no+1
        self.connection.commit()
        print('insert')
                


if __name__ == '__main__':
    cont = data_getter()
    cont.create_split_seq_table()