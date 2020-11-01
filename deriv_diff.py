import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import e as euler_num


class IntAndDer:
    
    """
    - Для известной функии сигмоиды y = 1 / (1+e**(-x)) #функцмя sig
    найдем первую производную #функция sig_derivative;
    - Элементарная экспоненциальная функция manual_exp;
    - Производная экспоненциальной функции man_exp_derivative;
    - неопределенный интеграл экспоненциальной функции 
      с заданной константой и множителем x man_exp_integ
    """
    
    def __init__(self, x):
        self.x = x
 
    def sig(self):
        e = euler_num
        yo = 1 / (1 + e**(-self.x))
        return yo
    
    def sig_derivative(self):
        fun_result = self.sig()
        yone = fun_result * (1-fun_result)
        return yone
    
    def manual_exp(self):
        e = euler_num
        print(f" значение экспоненциальной функции при x = {self.x} равно: {e**self.x} ")
        return e**self.x
    
    def man_exp_derivative(self):
        return (f"производная экспоненты при x = {self.x} равна: {self.manual_exp()}")
    
    def man_exp_integ(self, multiplier, c:float):
        if multiplier <= 1:
            print(f"неопределеннй интеграл функции e^x = e^x + c= {self.manual_exp()+c}")
            return self.manual_exp()+c
        if multiplier > 1:
            e = euler_num
            integ = ((1/multiplier)*e**(multiplier*self.x)) + c
            print(f"неопределеннй интеграл функции e^ax ((1/a)*e^(a*x)) + c= {integ}")
            return integ

        
"Запуски методов экземпляра класса -закомментированны"

MathAn = IntAndDer

#MathAn(2).sig()
#MathAn(2).sig_derivative()
        
#MathAn(1).man_exp_integ(1,2)
#MathAn(2).man_exp_integ(2,2)
#MathAn(2).manual_exp()
#MathAn(2).man_exp_derivative()
