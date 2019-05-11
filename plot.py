# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:47:14 2019

@author: 振振
"""
import scipy.io
import numpy as np
import pandas as pd
data2 = []
for i in range(1,16):
    data = scipy.io.loadmat('jingjing_20140629.mat')['jj_eeg%d'%i]
    data1 = data[0]
    data2.append(data1)


    
    























