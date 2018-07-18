import pandas as pd
import sys
class sequence_mass_calc :
    df = pd.read_csv('massdata.csv',index_col=0)
    text = ''
    massdf = df.T

    #setting searchword
    def __init__(self,text):
        self.text = text

    #calc mass and  output
    def get_mass(self):
        
        result = 0
        i=0
        list_mass = self.df.values.tolist()
        #print(list_mass)
        while (i<=len(self.text)):
            try :
               # print(self.massdf[self.text[i:i+2]])
                result = result+self.massdf[self.text[i:i+2]][0]
                i=i+2
            except KeyError as e:
                
      #  sqlist = sq_series.values()  
     #   print(e)
                #print(self.massdf[self.text[i]])
                if(i!=len(self.text)):
                    try :
                        result = result+self.massdf[self.text[i]][0]
                        i=i+1
                    except KeyError as e:
                        print(e)
                        i=i+1
                    
        print (result)
        return result