#%% 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


x = []
y = []

with open ('COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(str(row[1]))
plt.plot (x, y, marker = 'o')

plt.title ('Data for COVID-19 Cases in NYC')

plt.xlabel('Date')
plt.ylabel('Confirmed Cases')

plt.show()



# %%
