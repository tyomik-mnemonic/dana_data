import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import e as euler_num


class IntAndDif:
    
    """
    Задача. Для известной функии сигмоиды y = 1 / (1+e**(-x))
    найдем первую производную

    """
    def __init__(x,h,):
        x = self.x
        h = self.h
    
    @staticmethod
    def sig(xo:float):
        e = euler_num
        yo = 1 / (1 + e**(-xo))
        return yo
    
    @staticmethod
    def derivative(yo:float):
        yone = yo * (1-yo)
        return yone
        
        
    
IntAndDif.derivative(IntAndDif.sig(1))

        
    
