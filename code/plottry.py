# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:14:07 2021

@author: Karthik
"""

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


def voltage_acquisition_figure_multiple_analog_inputs():
    fig, axs = plt.subplots(2)

    plt.xticks(rotation=90)
    
    """ Takes the set of voltages inputs and plots it in real time"""
    
   
    axs[0].plot(x_ai1,voltages_ai1,'r-')
    axs[0].set_title('Voltage at 10kHz Sampling Rate (Analog Input 1)')
    plt.xlabel('Time Interval(In Seconds)')
    plt.ylabel('Voltage Values(Analog Input 1)')
    
    axs[1].plot(x_ai1,voltages_ai2,'b-')
    #axs[1].set_title('Voltage at 10kHz Sampling Rate (Analog Input 2)')
    plt.xlabel('Time Interval(In Seconds)')
    plt.ylabel('Voltage Values(Analog Input 2)')

    


x_ai1=[] 
voltages_ai1=[]
voltages_ai2=[]

# Column names for the csv file 
headerList = ['Interval', 
              'Voltage Value at 10Khz sampling Rate(AI1)',
              'Voltage Values(AI2)']



#Csv file Creation along with plotting values in real time simultaneously


def real_time_plotting():
    no_of_experiments=int(input("How Many Times Do you Want to Run the Experiment?:"))


    for i in range(no_of_experiments):
    
        with open("9215-A-VoltageReadings.csv",'a') as file: 
            #file.truncate(0)
            writer = csv.DictWriter(file, fieldnames=headerList)  #Creating a DictWriter  
            writer.writeheader()
        
        
            with nqmx.Task() as task:
             
                #Adding the voltage channel from the device configured(name=Dev2-9215A,channel=ai1,ai2)
                task.ai_channels.add_ai_voltage_chan("Dev2-9215A/ai1:2") 
                
                #Converting 10khz=10000 cycles/second
                task.timing.cfg_samp_clk_timing(rate=10000) #rate specifies the sampling rate(samples per channel per second).
                
                
                start_time = time.time()
                timeout = 10   # [seconds]
                
                while True:
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    
                    if elapsed_time <= timeout:
                        
                        data=task.read() #Collecting the voltage from the NI 9215A simulator          
                   
                        #Appending the value to a list for plotting
                        voltages_ai1.append(data[0])
                        voltages_ai2.append(data[1])
                        
                      
                        x_ai1.append(elapsed_time)
                        
                        
                    
                        #Writing the values on a real time to the csv file
                        writer.writerow({'Interval':elapsed_time,
                                         'Voltage Value at 10Khz sampling Rate(AI1)':data[0],
                                         "Voltage Values(AI2)":data[1]
                                         }) 
                    
                        #Calling the drawnow Function to plot values in Real Time           
                        drawnow(voltage_acquisition_figure_multiple_analog_inputs) 
                        
                        
                        
                    else :
                        break
                    
                    
                        
    print("CSV FILE CREATION COMPLETE!")
       

        