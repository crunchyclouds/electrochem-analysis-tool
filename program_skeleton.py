from imports import *
from raman_spectra import raman_grapher
from capacity_retention import capacity_plots
from differential_voltage import dq_dv

def prelim_prog():
    #root dimensions
    root = tk.Tk()
    root.geometry('1200x600')
    root.resizable(False,False)
    root.title('Electronic Materials Analysis')
    #root.config(bg='gray15')

    #establishing root grid parameters
    height, width = 4, 1
    for column in range(width):
        root.columnconfigure(column, weight=1)

    for row in range(height):
        root.rowconfigure(row, weight=1)

     #turtle title
    canvas = tk.Canvas(master=root, width=1200, height=600)
    draw = turtle.Screen()
    d = draw.getcanvas()
    d.create_line(1,1,90,90)



    #setting frame parameters for title buttons
    frm_1 = tk.Frame(root,
                  bg='gray15',
                  #padx=100,
                  pady=100,
                  )

    #establishing frame grid parameters
    height, width = 4, 7
    for column in range(width):
        frm_1.columnconfigure(column, weight=1)

    for row in range(height):
        frm_1.rowconfigure(row, weight=1)

    #setting button  texts
    txt_1 = tk.StringVar()
    txt_1.set('Raman Spectra Visualization')

    txt_2 = tk.StringVar()
    txt_2.set('Neware Capacity Analysis')

    txt_3 = tk.StringVar()
    txt_3.set('Neware dQ/dV Processing')

    #setting buttons
    b_1 = tk.Button(frm_1,
                 activebackground='old lace',
                 activeforeground='black',
                 textvariable=txt_1,
                 bg="gray40",
                 command= lambda: raman_grapher(),
                 height=2,
                 width=26,
                 bd=3,
                 font=(11),
                 cursor="hand2",
                 fg="old lace",
                 padx=2,
                 pady=2,
                 justify="center",
                 relief="raised",
                 )

    b_2 = tk.Button(frm_1,
                  textvariable=txt_2,
                  bg="gray40",
                  command= lambda: capacity_plots(),
                  height=2,
                  width=26,
                  bd=3,
                  font=(11),
                  cursor="hand2",
                  fg="old lace",
                  padx=2,
                  pady=2,
                  justify="center",
                  relief="raised",
                  )

    b_3 = tk.Button(frm_1,
                  textvariable=txt_3,
                  bg="gray40",
                  command= lambda: dq_dv(),
                  height=2,
                  width=26,
                  bd=3,
                  font=(11),
                  cursor="hand2",
                  fg="old lace",
                  padx=2,
                  pady=2,
                  justify="center",
                  relief="raised",
                  )

    #adding spacers for the grid
    spacer1 = tk.Label(frm_1,
                    text="",
                    bg='gray15',
                    width=2)

    spacer2 = tk.Label(frm_1,
                    text="",
                    bg='gray15',
                    width=2)

    spacer3 = tk.Label(frm_1,
                    text="",
                    bg='gray15',
                    width=2)

    spacer4 = tk.Label(frm_1,
                    text="",
                    bg='gray15',
                    width=2)


    #placing all items onto the grid
    frm_1.grid(column=0, row=3)
    spacer1.grid(column=1, row=0)
    spacer2.grid(column=3, row=1)
    spacer3.grid(column=5, row=2)
    spacer4.grid(column=7, row=3)
    b_1.grid(column=2, row=3)
    b_2.grid(column=4, row=3)
    b_3.grid(column=6, row=3)

    #establishing preliminary button commands


    #run the program in main loop
    root.mainloop()

prelim_prog()
