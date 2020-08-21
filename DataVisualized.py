#%% 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('case_time_series.csv')

D = data.iloc[61:,5].values # daily deceased
Y = data.iloc[61:,1].values # daily values
R = data.iloc[61:,3].values # daily recovered

X = data.iloc[61:,0] #stores date column

# plt.plot(X,Y)

plt.figure(figsize=(30,10)) # 30 is the width, 10 is the height

ax = plt.axes() # axes as object of graph
ax.grid(linewidth=0.4, color='#7d7f7c')

ax.set_facecolor("red")
ax.set_xlabel('\nDate',size=25,color='#3c9992')
ax.set_ylabel('# of Confirmed Cases\n', size=20, color='#3c9992')

ax.plot (X,Y,
    color='#1F77B4',
    marker='o',
    linewidth=4,
    markersize=15,
    markeredgecolor='#3c9992')



# %%


# %%
