# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:11:20 2021

@author: Karthik
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import glob #For accessing files inside a directory

VoltageMean={} #To Store the Avg Values
VoltageStd={}  ##To Store the Std Values

xs=[] #List to Sotre the Experiment Numbers
colors = list("rgbcmyk")

for i,each_file in enumerate(glob.glob('*.{}'.format('csv'))):
    new=each_file.replace("_VoltageReadings.csv","")
    df=pd.read_csv(each_file)
    
    #Extracting The Experiment Number from the corresponding FileName
    re_ex=re.compile(r'\d+')
    exp_grp=re_ex.search(each_file)
    exp_no=int(exp_grp.group())
    #print(exp_no)
    
    #Retrieving the Proper Readings by passing it the Extracted Experiment Number
    newdf=df[f'Voltage at 10Khz S.R (AI1) (Exp {exp_no})']
    VoltageMean[exp_no]=np.mean(newdf)
    VoltageStd[exp_no]=np.std(newdf)
    xs.append(exp_no)
    
    


        
#x=sorted(VoltageMean.items())
#print(x)
plt.scatter(x =VoltageMean.keys(),y=VoltageMean.values(),color=colors.pop())


#plt.xticks(np.arange(0, max(), 2))
plt.xticks(rotation=90)
plt.xticks(np.arange(1,len(xs)+1, 1))
plt.xlabel("Experiment Number")
plt.ylabel("Average Voltage")
plt.title("Average Voltage Values")
plt.show()

plt.errorbar(x=VoltageMean.keys(), y=VoltageMean.values(),yerr = VoltageStd.values(), linestyle='None', marker='^')
plt.title("Error Bar Chart")
plt.show()

    

print(VoltageMean)
print(VoltageStd)
    
    