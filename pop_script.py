import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
%matplotlib inline
import itertools
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class PopReader:
    def __init__(self, file:str, year_from:int):
        self.file = file
        self.year_from = year_from
    
    #читаем данные
    def read(self):
        data = pd.read_csv(self.file, encoding= 'cp1251',sep=';', comment='#')
        return data.astype({'YYYY':'int32',"Sq":"float32","Pop":"float32"})
    
    #фильтруем данные
    def filt(self):
        new_data = self.read()
        return new_data[new_data['YYYY']>=self.year_from]
    
    #визуализация с помощью пузырьковой диаграммы без прогноза
    def crcs(self):
        data = self.filt()
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
    
    #визуализация с помощью линейной диаграммы без прогноза
    def md_plot(self):
        data = self.future()       
        hst = data.plot(x='YYYY', y='Pop', c = 'r')
        hst.set_ylabel('Население')
        hst.set_xlabel('Год')
        hst.legend('Население')
        return hst
    
    #метод предсказания на основе линейной регрессии (предикторы: год, площадь, плотность)
    def future(self):
        
        def avge(lst):
            return sum(lst)/len(lst)
        
        #линейная регрессия
        def prediction(df, pred_bound:int):
            x = df[['YYYY','Sq','Density']]
            y = df[['Pop']]

            X_train = x[:pred_bound]
            X_test = x[pred_bound:]

            Y_train = y[:pred_bound]
            Y_test = y[pred_bound:]

            regr = LinearRegression()

            regr.fit(X_train, Y_train)

            pred = regr.predict(X_test)

            return pred[0][0]
        
        #увеличение предикторов на основе среднего прироста
        def growth(column):
            l = []
            for i in range (1, len(column)):
                    l.append(column[i] - column[i-1])
            return avge(l)
        
        s = growth(self.read()['Sq'])
        p = growth(self.read()['Pop'])
        d = growth(self.read()['Density'])
        
        df = self.filt().append({'YYYY': 2050,
                                     'Sq':self.read()['Sq'].iloc[-1] + abs(s), 
                                     'Pop':0, 
                                     'Density': self.read()['Density'].iloc[-1] + abs(d)}, 
                                    ignore_index=True)
        
        #присвоение предсказываемого значения популяции в набор данных
        df.loc[df['Pop'] == 0, 'Pop'] = prediction(df, 14)
        return df
        
        
    def hist_future(self):
        self.future()
        return self.md_plot()
    
    def scat_future(self):
        self.future()
        return self.crcs()
    
data = PopReader(file = '/home/toemik/msc_data2.csv', year_from = 1900)

data.scat_future()
data.hist_future()
data.future()[['YYYY','Sq','Pop','Density']]
