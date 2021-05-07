
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

import os
import os.path as path

folder_creation_path=  path.abspath(path.join(__file__ ,"../"))
print(type(folder_creation_path))


import glob #For accessing files inside a directory

import re

df_list = []

day_no=input("Enter the day no for which you want to view the experiment results: ")
day_no=str(day_no);

try : os.chdir(f"{folder_creation_path}/Day_{day_no}")
except: print("Day Does not Exist,Please Run some experiments for the specified day in 'real_time_plots.py'")
    

#os.chdir(f"{folder_creation_path}/Day_1")

for i,each_file in enumerate(glob.glob('*.{}'.format('csv'))):
    #print(each_file)
    new=each_file.replace("_VoltageReadings.csv","")
    df=pd.read_csv(each_file)
    
    #Extracting The Experiment Number from the corresponding FileName
    re_ex=re.compile(r'\d+')
    exp_grp=re_ex.search(each_file)
    exp_no=int(exp_grp.group())
    #print(exp_no)
    
    #Retrieving the Proper Readings by passing it the Extracted Experiment Number
       
    df=df[['Interval',f'Voltage at 10Khz S.R (AI1) (Exp {exp_no})']]
    
    if i==0:
        ax = df.plot(x ='Interval', y=f'Voltage at 10Khz S.R (AI1) (Exp {exp_no})', kind = 'line') 
        ax.set_title('{}'.format('Previous Signals'), 
             fontsize = 14)
        ax.legend(bbox_to_anchor=(0.5,1),loc='best')
               
    else:
        df.plot(x ='Interval', y=f'Voltage at 10Khz S.R (AI1) (Exp {exp_no})', 
                kind = 'line',linestyle='dashed',ax=ax)
        ax.set_title('{}'.format('Previous Signals'), fontsize = 14)
        ax.legend(bbox_to_anchor=( 0.5,1),loc='best')
        
       
        
  
    df_list.append(new)
plt.show()
    
    
        
        
# =============================================================================
#         
#         globals()[f'{name}'] =pd.read_csv(each_file)
#         df_list.append([globals()[f'{name}'])
# =============================================================================
                        
        
        
                                         
 
print(df_list)