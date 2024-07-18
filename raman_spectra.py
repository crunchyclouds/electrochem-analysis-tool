#importing relevant libraries
from imports import *


#capacity_plots function
def raman_grapher():
    '''taking input for folder
    input_folder = simpledialog.askstring('Determine Folder Path', 'Please input the path of the folder in
                                                which you save all cell data from Neware 8.0. Use the full path as
                                                copied. Note that only xlsx files will be read; all others will be
                                                ignored.')'''

    #input bypass for easy debugging
    folder = r"D:\Data\Raman\LCO-050124-4-2\MK_062024_LCO_050124-4-2_CLA_0619_4h_600c_4h_F"

    #identifying csv files within the folder
    files = [file for file in pathlib.Path(folder).glob("*.csv")]

    #removing temporary files
    for file in files:
        if "~" in str(file):
            files.remove(file)

    #looping through all files
    n=1
    stack=000
    for file in files:
        print(f'Reading from {file}')
        print('Processing your files...')
        #reading excel data for cycle index and current capacity
        df = pd.read_csv(file,
                         header=105)
        y_axis = df['Dark Subtracted #1'] - df['RelativeIntensityCorrection_Ratio #1'] + stack
        x_axis = df['Raman Shift']
        #creating a plot
        series = str(pathlib.Path(file).stem)[-2] + str(pathlib.Path(file).stem)[-1]
        plt.xlim(100,800)
        plt.ylim(0,10000)
        plt.yticks([])
        plt.plot(x_axis, y_axis,
                 marker='',
                 label=series)
        plt.legend(loc='lower right')

        print(f'Data set {n}/{len(files)} complete.')
        n += 1
        stack += 4000

    #assigned constant values
    plt.ylabel(r"Intensity (a.u.)")
    plt.xlabel("Raman Shift (cm^-1)")
    plt.title(str(pathlib.Path(folder).stem))
    plt.show()
