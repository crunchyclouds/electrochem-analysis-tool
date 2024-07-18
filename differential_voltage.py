#importing relevant libraries
from imports import *


def dq_dv(cstart=5, cstop=5, wl=16, po=1, nth=2, ks=9):
    #looping through all files in the folder
    file = r"D:\Data\Electrochemical\LCO-050224-3-2\MK_070224_LCO_050224-3-2_CLA0628_4h-600c-4h_D\MK_070224_LCO_050224-3-2_CLA0628_4h_600c_4h_D_s1.xlsx"

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
    i=0
    for value in mini_dqdv:
        if float(value)%float(nth) != float(0):
            mini_dqdv.pop(i)
            mini_voltage.pop(i)
        i+=1

    #moving average
    mini_dqdv = medfilt(mini_dqdv,ks)

    #savitzky golay
    smooth_dqdv = savgol_filter(mini_dqdv, wl, po)

    #plotting and adding plot parameters
    series = str(pathlib.Path(file).stem)[-2] + str(pathlib.Path(file).stem)[-1]
    plt.xlim()
    plt.ylim()
    plt.plot(mini_voltage, smooth_dqdv,
             linewidth=2,
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

'''for users: cstart and cstop are the start and stop cycles. if you want to do just one cycle, list it as the same 
number. wl and po are variables in the smoothing filter. po should be significantly lower than wl. nth is the nth 
skipped voltage for smoothing, ks is the kernel size for a moving average'''
#dq_dv(cstart=5, cstop=5, wl=16, po=1, nth=2, ks=9)