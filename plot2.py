# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:14:45 2021

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


import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
            voltage=calculate_voltage()
        
            # Add x and y to lists
            xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
            ys.append(voltage)
        
            # Limit x and y lists to 20 items
            xs = xs[-20:]
            ys = ys[-20:]
        
            # Draw x and y lists
            ax.clear()
            ax.plot(xs, ys)
        
            # Format plot
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            plt.title('Voltage over Time')
            plt.ylabel('Voltage Values')
            

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()

def calculate_voltage():
    with nqmx.Task() as task:
         
            #Adding the voltage channel from the device configured(name=Dev2-9215A,channel=ai0)
            task.ai_channels.add_ai_voltage_chan("Dev2-9215A/ai1") 
            
            #Converting 10khz=10000 cycles/second
            task.timing.cfg_samp_clk_timing(rate=10000,samps_per_chan=10)
            
            data=task.read()
            return data
    