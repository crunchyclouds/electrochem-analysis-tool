#importing relevant libraries
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import pathlib
import re
import warnings
import numpy as np
from scipy.signal import savgol_filter

'''plots capacity retention as a percentage'''

folder=r"D:\Data\Graphs\Compiled Controls\New folder"


matplotlib.rcParams.update({'font.size': 24})

#red gridline
plt.plot([0,100], [80,80],
         'r--'
         )

#identifying excel files within the folder
files = [file for file in pathlib.Path(folder).glob("*.xlsx")]

#excluding temporary files
for file in files:
    if "~" in str(file):
        files.remove(file)
#checking one file for cycle length
df_0 = pd.read_excel(files[0],
                     sheet_name='cycle',
                     usecols='A')
#looping through all files
n=1
for file in files:
    print(f'Reading from {file}')
    print('Processing your files...')

    #reading excel data for cycle index and current capacity
    df = pd.read_excel(file,
                       sheet_name='cycle',
                       usecols='A,E,G',
                       )[:-1]
    x_axis = df['Cycle Index'] #reading for x axis

    #ensuring full capacity is actually a large value
    full_capacity = 0
    i=0
    while full_capacity < 5:
        full_capacity = df.loc[i,'DChg. Spec. Cap.(mAh/g)']
        i+=1

    #reading for y axis
    y_axis = df[r'DChg. Spec. Cap.(mAh/g)'] / full_capacity * 100

    #smoothing the y axis with savitzky golay
    smooth_y_axis = savgol_filter(y_axis, 5, 1)

    #creating a plot
    series = str(pathlib.Path(file).stem)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.tight_layout()
    plt.plot(x_axis,
             smooth_y_axis,
             linewidth=3,
             marker='',
             label=series)
    plt.legend(loc='best')

    #updating the user
    print(f'Data set {n}/{len(files)} complete.')
    n += 1

#assigned constant values
plt.xlabel("Cycle Number")
plt.ylabel(r"Capacity Retention (%)")
plt.title(str(pathlib.Path(folder).stem))
plt.grid()
plt.show()


#calling capacity_plots while avoiding error message
warnings.filterwarnings("ignore",
                    category=UserWarning,
                    module=re.escape('openpyxl.styles.stylesheet'))
