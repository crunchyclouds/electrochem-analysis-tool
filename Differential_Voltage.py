#importing relevant libraries
import pathlib
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from scipy.signal import medfilt
import matplotlib.pyplot as plt
import re
import warnings
import matplotlib

'''for users: cstart and cstop are the start and stop cycles. if you want to do just one cycle, list it as the same 
number. wl and po are variables in the smoothing filter. po should be significantly lower than wl. nth is the nth 
skipped voltage for smoothing, ks is the kernel size for a moving average'''

file = r"D:\Data\Electrochemical\LCO-050124-4-2\HL_061324_LCO_050124-4-2-LCLA_0607_4h-600c-4h-C\HL_061324_LCO050124-4-2_LCLA0607-4h_600c_4h_s5.xlsx"
cstart=20
cstop=20
wl=16
po=3
nth=15
ks=9

matplotlib.rcParams.update({'font.size': 18})

#informing user of the status
print(f'Reading from {file}')
print('Processing your data...')

#consolidating relevant columns
df = pd.read_excel(file,
                   sheet_name='record',
                   usecols='B,H,X'
                   )
cycle_index = list(df['Cycle Index'])
voltage = list(df['Voltage(V)'])
dqdv = list(df['dQm/dV(mAh/V.g)'])

#making mini lists of only desired cycles
mini_voltage = []
mini_dqdv = []

cycle_list = np.arange(cstart,cstop+1)
for c in cycle_list:
    i=0
    for ind in cycle_index:
        i+=1
        if int(ind) == int(c):
            mini_voltage.append(voltage[i])
            mini_dqdv.append(dqdv[i])

#applying smoothing mechanisms
#removing rest phases
i=0
for value in mini_dqdv:
    if float(value) == float(0):
        mini_dqdv.pop(i)
        mini_voltage.pop(i)
    i+=1

#removing every xth value
# i=0
# for value in mini_dqdv:
#     if float(value)%float(nth) != float(0):
#         mini_dqdv.pop(i)
#         mini_voltage.pop(i)
#     i+=1

#moving average
mini_dqdv = medfilt(mini_dqdv,ks)

#savitzky golay
smooth_dqdv = savgol_filter(mini_dqdv, wl, po)

#plotting and adding plot parameters
series = str(pathlib.Path(file).stem)[-2] + str(pathlib.Path(file).stem)[-1]
plt.xlim()
plt.ylim(-2700,2000)
plt.plot(mini_voltage, smooth_dqdv,
         linewidth=3,
         marker='',
         label=series
         )
plt.title(str(pathlib.Path(file).stem))
plt.xlabel("Voltage (V)")
plt.ylabel(r"dQ/dV")
plt.show()


#avoiding no-default-style error
warnings.filterwarnings("ignore",
                    category=UserWarning,
                    module=re.escape('openpyxl.styles.stylesheet')
                    )