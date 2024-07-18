#importing relevant libraries
from imports import *


#capacity_plots function
def capacity_plots():

    #input folder
    folder = r"D:\Data\Electrochemical\LCO-050224-3-2\MK-062724_LCO_050224-3-2_0.6MLi-3h_600c_4h_C"

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
        #beginning either from true zero or cycle index 15 based on amount of data
        if len(df_0) < 25:
            df = pd.read_excel(file,
                               sheet_name='cycle',
                               usecols='A,E,G')
            x_axis = df['Cycle Index']
            plt.figtext(.5, 0, 'Graphing from cycle index 0.', ha='center')
        else:
            df = pd.read_excel(file,
                               sheet_name='cycle',
                               usecols='A,E,G',
                               #cutting out the first 15 cycles
                               skiprows=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            x_axis = df['Cycle Index'] - 15
            plt.figtext(.5, 0, 'Graphing from cycle index 15 as 0.', ha='center')

        # reading excel data for cycle index and current capacity
        full_capacity = 0
        i=0
        while full_capacity < 5:
            full_capacity = df.loc[i,'DChg. Spec. Cap.(mAh/g)']
            i+=1
        y_axis = df[r'DChg. Spec. Cap.(mAh/g)'] / full_capacity * 100

        #creating a plot
        series = str(pathlib.Path(file).stem)[-2] + str(pathlib.Path(file).stem)[-1]
        plt.xlim(0,80)
        plt.ylim(0,100)
        plt.plot(x_axis, y_axis,
                 linewidth=1,
                 marker='.',
                 label=series)
        plt.legend(loc='lower left')

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
#capacity_plots()
