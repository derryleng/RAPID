import tkinter as tk
from tkinter import ttk, filedialog
from input_module import runPreprocess
from core_module import runModel
from visual_module import runVisual


class mainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('RAPID')
        self.resizable(False, False)
        inputFrame(self).grid(row=0, column=0, sticky='nsew', padx=(12,6), pady=5)
        runFrame(self).grid(row=0, column=1, sticky='nsew', padx=(6,12), pady=5)
        reqFrame(self).grid(row=1, column=0, columnspan=2, sticky='nsew', padx=12, pady=5, ipady=3)
        optFrame(self).grid(row=2, column=0, columnspan=2, sticky='nsew', padx=12, pady=5)
        visualFrame(self).grid(row=3, column=0, columnspan=2, sticky='nsew', padx=12, pady=(5,12), ipady=3)
        self.mainloop()


class inputFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' Input Settings ')
        self.procFlag = tk.IntVar()
        tk.Radiobutton(self, text='Process operational data', var=self.procFlag, value=1).pack(anchor='w')
        tk.Radiobutton(self, text='Load existing input file', var=self.procFlag, value=0).pack(anchor='w')
        self.loadedText = tk.StringVar(value='')
        tk.Label(self, textvariable=self.loadedText).pack()
        tk.Button(self, text='Choose File', command=lambda: self.getInput(master)).pack(expand=True, fill='both')

    def getInput(self, master):
        """
        Switch between the two input options:
        Option 0 (Analyse & Filter Operation Data) - leads to input_pre_process
        Option 1 (Load existing INPUT file) - skips straight to core module (bypass input_pre_process)
        """
        master.filename = filedialog.askopenfilename()
        if master.filename != '':
            if bool(self.procFlag.get()):
                runPreprocess(master.filename)
            self.loadedText.set(master.filename.split('/')[-1])


class reqFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' Model Settings ')
        master.req = {
            'n_input': tk.IntVar(value='50'),
            'minDep_altSID_input': tk.IntVar(value='60'),
            'minDep_sameSID_input': tk.IntVar(value='109'),
            'SIDmax_input': tk.IntVar(value='4'),
            'SIDgroup_separation_input': tk.StringVar(value='(2,4)(3,4)'),
            'queue_type': tk.StringVar(value='2x4'),
            'SID_queue_assign_input': tk.StringVar(value='1 3 | 2 4')
        }
        tk.Label(self, text='[Arrival lead time] n value (secs)').grid(row=0, column=0, columnspan=2, sticky='w')
        tk.Entry(self, width=29, textvariable=master.req['n_input']).grid(row=0, column=6, columnspan=4,  sticky='w')
        tk.Label(self, text='Minimum separation alternating SIDs (secs)   ').grid(row=1, column=0, columnspan=2, sticky='w') # Trailing spaces are for spacing
        tk.Entry(self, width=29, textvariable=master.req['minDep_altSID_input']).grid(row=1, column=6, columnspan=4,  sticky='w')
        tk.Label(self, text='Minimum separation same SIDs (secs)').grid(row=2, column=0, columnspan=2, sticky='w')
        tk.Entry(self, width=29, textvariable=master.req['minDep_sameSID_input']).grid(row=2, column=6, columnspan=4,  sticky='w')
        tk.Label(self, text='Maximum number of SID groups').grid(row=3, column=0, columnspan=2, sticky='w')
        tk.Entry(self, width=29, textvariable=master.req['SIDmax_input']).grid(row=3, column=6, columnspan=4,  sticky='w')
        tk.Label(self, text='SID groups pairs with minimum separation').grid(row=4, rowspan=2, column=0, columnspan=2, sticky='w')
        tk.Entry(self, width=29,  textvariable=master.req['SIDgroup_separation_input']).grid(row=4, column=6, columnspan=4, sticky='w')
        tk.Label(self, text='Type of queue').grid(row=6, column=0, sticky='w')
        tk.Radiobutton(self, text='1x8', variable=master.req['queue_type'], value='1x8').grid(row=6, column=6, sticky='w')
        tk.Radiobutton(self, text='2x4', variable=master.req['queue_type'], value='2x4').grid(row=6, column=7, sticky='w')
        tk.Radiobutton(self, text='4x2', variable=master.req['queue_type'], value='4x2').grid(row=6, column=8, sticky='w')
        tk.Radiobutton(self, text='8x1', variable=master.req['queue_type'], value='8x1').grid(row=6, column=9, sticky='w')
        tk.Label(self, text='SID groups to RWY queue').grid(row=7, column=0, columnspan=2, sticky='w')
        tk.Entry(self, width=29, textvariable=master.req['SID_queue_assign_input']).grid(row=7, column=6, columnspan=4, sticky='w')


class optFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' Enablers ')
        master.opt = {
            'var6': tk.IntVar(),
            'var17': tk.IntVar(),
            'separation_type': tk.IntVar(value='0'),
            'ADA_x_input': tk.IntVar(value='10'),
            'MRS_4dme': tk.IntVar(),
            'WAKE_4dme': tk.IntVar(),
            'ADA_4dme': tk.IntVar(),
            'ADDA_4dme': tk.IntVar(),
            'MRS_thr': tk.IntVar(),
            'WAKE_thr': tk.IntVar(),
            'ADA_thr': tk.IntVar(),
            'ADDA_thr': tk.IntVar()
        }
        tk.Label(self, text='RECAT type').grid(row=0, column=0, columnspan=2, sticky='w')
        tk.Checkbutton(self, text='RECAT', variable=master.opt['var6']).grid(row=0, column=6, columnspan=2,  sticky='w')
        tk.Checkbutton(self, text='RECAT-PWS', variable=master.opt['var17']).grid(row=0, column=8, columnspan=2,  sticky='w')
        tk.Label(self, text='Arrivals separation type').grid(row=1, column=0, columnspan=2, sticky='w')
        tk.Radiobutton(self, text='Distance based', var=master.opt['separation_type'], value=0).grid(row=1, column=6, columnspan=2,  sticky='w')
        tk.Radiobutton(self, text='Time based', var=master.opt['separation_type'], value=1).grid(row=1, column=8, columnspan=2,  sticky='w')
        tk.Label(self, text='ADA target time X-value                      ').grid(row=2, column=0, columnspan=2, sticky='w') # Trailing spaces are for spacing
        tk.Entry(self, width=36, textvariable=master.opt['ADA_x_input']).grid(row=2, column=6, columnspan=4,  sticky='w')
        tk.Label(self, text='4DME Separation Delivery').grid(row=3, column=0, sticky='w')
        tk.Checkbutton(self, text='MRS', variable=master.opt['MRS_4dme']).grid(row=3, column=6, sticky='w')
        tk.Checkbutton(self, text='WAKE', variable=master.opt['WAKE_4dme']).grid(row=3, column=7, sticky='w')
        tk.Checkbutton(self, text='ADA', variable=master.opt['ADA_4dme']).grid(row=3, column=8, sticky='w')
        tk.Checkbutton(self, text='ADDA', variable=master.opt['ADDA_4dme']).grid(row=3, column=9, sticky='w')
        tk.Label(self, text='Threshold Separation Delivery').grid(row=4, column=0, sticky='w')
        tk.Checkbutton(self, text='MRS', variable=master.opt['MRS_thr']).grid(row=4, column=6, sticky='w')
        tk.Checkbutton(self, text='WAKE', variable=master.opt['WAKE_thr']).grid(row=4, column=7, sticky='w')
        tk.Checkbutton(self, text='ADA', variable=master.opt['ADA_thr']).grid(row=4, column=8, sticky='w')
        tk.Checkbutton(self, text='ADDA', variable=master.opt['ADDA_thr']).grid(row=4, column=9, sticky='w')


class visualFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' Visualise Results ')
        master.vis = {
            'var11': tk.IntVar(),
            'var12': tk.IntVar()
        }
        tk.Label(self, text="Compare results to").grid(row=1, column=0, columnspan=10, sticky='w')
        tk.Checkbutton(self, text="operational data", variable=master.vis['var11']).place(x=105, y=-2)
        tk.Checkbutton(self, text="other results", variable=master.vis['var12']).place(x=218, y=-2)
        tk.Label(self, text=" - no. (up to 5)").place(x=306, y=0)
        tk.Entry(self, width=5, text='0', variable=master.vis['var13']).place(x=390, y=1)
        tk.Button(self, text='Visualise existing output data', command=lambda: self.runVisualExisting(master)).grid(row=2, column=0, sticky='w')

    def runVisualExisting(self, master):
        master.name_output_file = filedialog.askopenfilename(title='Open existing OUTPUT_*.xlsx file')
        if master.name_output_file != '':
            runVisual(master)


class runFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' Run Settings ')
        master.run = {
            'n_times_input': tk.IntVar(value='1'),
            'var7': tk.IntVar(),
            'var14': tk.IntVar()
        }
        tk.Label(self, text='Number of runs            ').pack(anchor='w') # Trailing spaces are for spacing
        tk.Entry(self, width=8, textvariable=master.run['n_times_input']).place(x=147, y=0)
        tk.Checkbutton(self, text='I want to feel confident!', variable=master.run['var7']).pack(anchor='w')
        tk.Checkbutton(self, text='Print a debug tab', variable=master.run['var14']).pack(anchor='w')
        tk.Button(self, text='Run Model', command=lambda: self.runRAPID(master)).pack(expand=True, fill='both')

    def runRAPID(self, master):
        """
        Wrapper function which first runs the core RAPID model,
        then runs the visual module.
        """
        runModel(master)
        runVisual(master)


if __name__ == '__main__':
    mainWindow()
