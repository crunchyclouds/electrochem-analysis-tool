#importing relevant libraries
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import re
import warnings
import numpy as np
from scipy.signal import savgol_filter
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

'''capacity retention with dots for important graphs'''


#capacity_plots function
folder=r"D:\Data\Graphs\Compiled Controls\New folder"

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
                     usecols='A'
                     )

#looping through all files
n=1
for file in files:
    print(f'Reading from {file}')
    print('Processing your files...')
    #reading excel data for cycle index and current capacity
    df = pd.read_excel(file,
                       sheet_name='cycle',
                       usecols='A,E,G',
                       skiprows=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
                       )[:-1]

    x_axis = df['Cycle Index'] - 15

    full_capacity = df.loc[0, 'DChg. Spec. Cap.(mAh/g)']
    y_axis = df[r'DChg. Spec. Cap.(mAh/g)'] / full_capacity * 100

    #creating a plot
    series = str(pathlib.Path(file).stem)
    plt.xlim(0,100)
    plt.ylim(50,100)
    plt.plot(x_axis, y_axis,
             linewidth=1,
             marker='.',
             label=series)
    plt.legend(loc='best')

    print(f'Data set {n}/{len(files)} complete.')
    n += 1

#assigned constant values
plt.xlabel("Cycle Number")
#plt.xticks(np.arange(0,100,step=5))
plt.ylabel(r"Capacity Retention (%)")
plt.title(str(pathlib.Path(folder).stem))
plt.grid()
plt.show()


#calling capacity_plots while avoiding error message
warnings.filterwarnings("ignore",
                    category=UserWarning,
                    module=re.escape('openpyxl.styles.stylesheet'))
