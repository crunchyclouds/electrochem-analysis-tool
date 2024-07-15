from imports import *

def prelim_prog():
    #root dimensions
    root = Tk()
    root.geometry('1200x600')
    root.resizable(False,False)
    root.title('Electronic Materials Analysis')
    root.config(bg='gray15')

    #frame parameters
    frm = ttk.Frame()

    #raman label
    txt_1 = StringVar()
    txt_1.set('Raman Spectra Analysis')

    l_1 = Label(root,
                  textvariable=txt_1,
                  anchor=CENTER,
                  bg="gray40",
                  height=4,
                  width=30,
                  bd=3,
                  font=(11),
                  cursor="hand2",
                  fg="old lace",
                  padx=15,
                  pady=15,
                  justify=CENTER,
                  relief=RAISED,
                  underline=0,
                  #wraplength=250
                  )
    l_1.pack()

#    ttk.Button(root,
#               text='hello').grid()

    #run the program in main loop
    root.mainloop()

prelim_prog()
