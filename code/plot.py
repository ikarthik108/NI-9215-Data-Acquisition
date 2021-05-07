# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:28:51 2021

@author: Karthik
"""

#Importing the wrapper for the daqmx configured
import nidaqmx as nqmx 

import statistics

import matplotlib.pyplot as plt
plt.ion() # For real time plotting
import csv 
import datetime as dt

# libraries for Configuring the timing properties of the nidaqmx.task class
from nidaqmx.constants import LineGrouping
from nidaqmx.constants import Edge
from nidaqmx.constants import AcquisitionType

import time

#drawnow to make figures
from drawnow import *  

#To Check if the File Exists
import os.path




def voltage_acquisition_figure():
 
    
    plt.xticks(rotation=90)
    
    """ Takes the set of voltages inputs and plots it in real time"""
    
    plt.title('Voltage at 10kHz Sampling Rate Over a Period of Time')
    plt.xlabel('Time Interval(In Seconds)')
    plt.ylabel('Voltage Values')
    plt.plot(x,voltages,'r-')
    

    




# Column names for the csv file 
headerList = ['Interval', 'Voltage Value at 10Khz sampling Rate']

colours=['r-','b-','g-','y-','o-','v-']
print(type(colours[0]))


#if (os.path.isfile("./9215-A-VoltageReadings.csv")):
    

no_of_experiments=2



#Creating n Different Voltage Lists for n corresponding Experiments

for i in range (no_of_experiments):
   
    globals()[f'voltage_{i}'] = [i]
    globals()[f'time_{i}'] = [i]
    

    

# =============================================================================
# clear=input("Do you Want To Clear Previous Readings and Start Afresh? Type 'Yes' or 'No' :")
# clear=clear.lower()
# if (clear=='yes' or clear =='y'):
#     file.truncate()
# 
# =============================================================================


for i in range(no_of_experiments):
    
    
    with open("9215-A-VoltageReadings.csv",'a') as file: 
       
        writer = csv.DictWriter(file, fieldnames=headerList)  #Creating a DictWriter  
        writer.writeheader()
    
    
        with nqmx.Task() as task:
         
            #Adding the voltage channel from the device configured(name=Dev2-9215A,channel=ai0)
            task.ai_channels.add_ai_voltage_chan("Dev2-9215A/ai1") 
            
            #Converting 10khz=10000 cycles/second
            task.timing.cfg_samp_clk_timing(rate=10000,samps_per_chan=10) #rate specifies the sampling rate(samples per channel per second).
            
            
            start_time = time.time()
            timeout = 10   # [seconds]
            
            while time.time()< start_time + timeout:
                current_time = time.time()
                elapsed_time = current_time - start_time
# =============================================================================
#                 
#                 if elapsed_time <= timeout:
# =============================================================================
                    
                data=task.read() #Collecting the voltage from the NI 9215A simulator          
           
                #Appending the value to a list for plotting
                vol_list_name=globals()[f'voltage_{i}']
                vol_list_name.append(data)
                time_list_name= globals()[f'time_{i}']
                time_list_name.append(elapsed_time)
            
                #Writing the values on a real time to the csv file
                writer.writerow({'Interval':elapsed_time,'Voltage Value at 10Khz sampling Rate':data}) 
            
                #Calling the drawnow Function to plot values in Real Time           
                #drawnow(voltage_acquisition_figure,show_once=True) 
                
                plt.clf()
                plt.plot(time_list_name,vol_list_name,colours[i])
                plt.xticks(rotation=45, ha='right')
                plt.subplots_adjust(bottom=0.30)
                plt.title('Voltage over Time')
                plt.ylabel('Voltage Values')
                plt.show()
                
                    
# =============================================================================
#                 else :
#                     plt.clf()
#                     break
# =============================================================================
    plt.close()
       
                
#else:
    
    

    

       

        