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
        inputFrame().grid(row=0, column=0, columnspan=2, sticky='nsew', padx=12, pady=5)
        reqFrame(self).grid(row=1, column=0, columnspan=2, sticky='nsew', padx=12, pady=5)
        optFrame(self).grid(row=2, column=0, columnspan=2, sticky='nsew', padx=12, pady=5)
        runFrame(self).grid(row=3, column=0, sticky='nsew', padx=(12, 6), pady=5)
        visualFrame(self).grid(row=3, column=1, sticky='nsew', padx=(6, 12), pady=5)
        self.mainloop()


class inputFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        tk.Button(self, text='Pre-Processing Operational Data', command=lambda: runPreprocess(filedialog.askopenfilename(title='Open operational data file'))).pack(side='left')


class reqFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' 1. Required Model Settings ')
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
        ttk.LabelFrame.__init__(self, text=' 2. Optional Model Enablers ')
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


class runFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' 3. Final Run Settings ')
        master.run = {
            'n_times_input': tk.IntVar(value='1'),
            'var7': tk.IntVar(),
            'var14': tk.IntVar()
        }
        tk.Label(self, text='Number of runs').grid(row=0, column=0, sticky='w')
        tk.Entry(self, width=8, textvariable=master.run['n_times_input']).grid(row=0, column=1, sticky='e')
        tk.Checkbutton(self, text='I want to feel confident!', variable=master.run['var7']).grid(row=1, column=0, columnspan=2, sticky='w')
        tk.Checkbutton(self, text='Print a debug tab', variable=master.run['var14']).grid(row=2, column=0, columnspan=2, sticky='w')
        tk.Button(self, text='Load Data', command=lambda: self.loadModel(master)).grid(row=3, column=0, sticky='w')
        tk.Button(self, text='Run Model', command=lambda: runModel(master)).grid(row=3, column=1, sticky='w')

    def loadModel(self, master):
        master.name_input_file = filedialog.askopenfilename(title='Open existing INPUT_*.xlsx file')
        if master.name_input_file != '':
            runModel(master)


class visualFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, text=' 4. Visualise Results ')
        master.vis = {
            'compare_op': tk.IntVar(),
            'compare_set': tk.IntVar(),
            'compare_set_num': tk.StringVar()
        }
        tk.Checkbutton(self, text="Compare to operational data", variable=master.vis['compare_op']).grid(row=0, column=0, columnspan=2, sticky='w')
        tk.Checkbutton(self, text="Compare to other results (<6)", variable=master.vis['compare_set']).grid(row=1, column=0, columnspan=2, sticky='w')
        tk.Entry(self, width=5, textvariable=master.vis['compare_set_num']).grid(row=2, column=0, columnspan=2, sticky='we')
        tk.Button(self, text='Load Data', command=lambda: self.loadVisual(master)).grid(row=3, column=0, sticky='w')
        tk.Button(self, text='Run Visual', command=lambda: runVisual(master)).grid(row=3, column=1, sticky='e')

    def loadVisual(self, master):
        master.name_output_file = filedialog.askopenfilename(title='Open existing OUTPUT_*.xlsx file')
        if master.name_output_file != '':
            runVisual(master)


if __name__ == '__main__':
    mainWindow()
