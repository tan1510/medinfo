import pandas as pd 
from config import config
from dbconnector import MySQL
from read_sequence import data_getter
from config import config
import sequence_mass_calc
import numpy as np
import csv
#peputidonosirturyou wo keisan si kaesu
def calc_seq_mass(df):

    result = 0
    i=0
    list_mass = df.values.tolist()
    print(list_mass)

# process cut by 'K' or 'P'
# but sequence             tryp cannt cut  KR 
def cut_process_by_tryp(sq_list):
    u'''
    arg list : sequence list
    return   list :
    '''
    listT = sq_list.T
    split_by_KandR_list = [sq.replace(' ','').replace('\n','').replace('KR',';'). 
    replace('K','K:').replace('R','R:').replace(';','KR').split(':')
    for sq in listT[1]]
    return split_by_KandR_list


def calc_dif_mass(list,search_word_mass):
    masslist  = [abs(get_mass(seq)-search_word_mass) for seq in list]
    return masslist

df = pd.read_csv('massdata.csv',index_col=0)
text = ''
massdf = df.T
list_mass = df.values.tolist()


def get_mass(text):
    result = 0
    i=0
    #print(list_mass)
    print (text)
    while (i<=len(text)):
        try :
       # print(self.massdf[self.text[i:i+2]])
            result = result+massdf[text[i:i+2]][0]
            i=i+2
        except KeyError as e:
      #  sqlist = sq_series.values()  
     #   print(e)
                #print(self.massdf[self.text[i]])
            if(i!=len(text)):
                result = result+massdf[text[i]][0]
            i=i+1
    print(result)
    return result

def pick_min_mass_index(list):
   
    return np.asarray(list).argmin()

if __name__ == '__main__':
#kekka
    result = []
    sqs =[]
    search_word = ('TQVCGLR')
    search_word_mass =get_mass(search_word)
    sq_list = data_getter().get_sequence().values
    cut_sqs=cut_process_by_tryp(sq_list)

    print ('end cut')
    min_index_list = [pick_min_mass_index(calc_dif_mass(sq_split,search_word_mass)) for sq_split in cut_sqs]

    min_positon_list = [cut_sqs[index] for index in min_index_list]
    writecsv = csv.writer(file(output.csv,'w'),lineterminator='n')   
    writecsv.writerow([cut_sqs[i][min_index_list] for i in range(len(cut_sqs))])