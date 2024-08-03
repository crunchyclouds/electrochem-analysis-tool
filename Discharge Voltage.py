# importing relevant libraries
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import re
import warnings
import numpy as np
from scipy.signal import savgol_filter
import matplotlib


# capacity_plots function
folder=r"D:\Data\Graphs\Compiled Controls"

matplotlib.rcParams.update({'font.size': 18})

# identifying excel files within the folder
files = [file for file in pathlib.Path(folder).glob("*.xlsx")]

# excluding temporary files
for file in files:
    if "~" in str(file):
        files.remove(file)
# checking one file for cycle length
df_0 = pd.read_excel(files[0],
                     sheet_name='cycle',
                     usecols='A')
# looping through all files
n = 1
for file in files:
    print(f'Reading from {file}')
    print('Processing your files...')

    df = pd.read_excel(file,
                       sheet_name='cycle',
                       usecols='A,AT',
                       )[:-1]
    x_axis = df['Cycle Index']

    y_axis = df[r'Average discharge voltage(V)']
    smooth_y_axis = savgol_filter(y_axis, 5, 1)

    # creating a plot
    series = str(pathlib.Path(file).stem)
    plt.xlim(0, 100)
    plt.ylim(3,4.45)
    plt.plot(x_axis, smooth_y_axis,
             linewidth=3,
             marker='',
             label=series)
    plt.legend(loc='best')

    print(f'Data set {n}/{len(files)} complete.')
    n += 1

    # assigned constant values
plt.xlabel("Cycle Number")
plt.ylabel(r"Discharge Voltage")
plt.title(str(pathlib.Path(folder).stem))
plt.grid()
plt.show()


# calling capacity_plots while avoiding error message
warnings.filterwarnings("ignore",
                    category=UserWarning,
                    module=re.escape('openpyxl.styles.stylesheet'))
