import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
#%matplotlib inline

class PopReader:
    def __init__(self, file:str, year_from:int):
        self.file = file
        self.year_from = year_from
        
    def read(self):
        data = pd.read_csv(self.file, encoding= 'cp1251',sep=';', comment='#')
        return data.astype({'YYYY':'int32',"Sq":"float32","Pop":"float32"})
    
    def filter(self):
        new_data = self.read()
        return new_data[new_data['YYYY']>=self.year_from]
    
    def crcs(self):
        data = self.filter()
        num = data.shape[0]
        t = np.arange(num)

        hst = data.plot.scatter(x='YYYY', 
                                y='Density', 
                                s = 70,
                                c = data['Pop'],
                                cmap='jet',
                                sharex=False
                               )
        hst.set_ylabel('Плотность')
        hst.set_xlabel('Год')
        return hst
    
    def md_plot(self):
        data = self.filter()
        hst = data.plot(x='YYYY', y='Pop', c = 'r')
        hst.set_ylabel('Население')
        hst.set_xlabel('Год')
        hst.legend('Население')
        return hst
       
data = PopReader(file = 'data/msc_data2.csv', year_from = 1900)#.filter(1900)

data.crcs()
data.md_plot()
