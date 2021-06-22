import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd

from input_module import runPreprocess
from core_module import runModel
from visual_module import runVisual

class mainWindow(ttk.Notebook):

    def __init__(self, master):
        ttk.Notebook.__init__(self, master)
        self.add(inputModule(self), text='   Input Module   ')
        self.add(coreModule(self), text='   Core Module   ')
        self.add(visualModule(self), text='   Visual Module   ')
        self.pack(fill="both", expand=True)


class inputModule(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self)
        self.input_type = tk.IntVar()
        tk.Radiobutton(self, text='Analyse & Filter Operational Data', var=self.input_type, value=0).pack(anchor='w')
        tk.Radiobutton(self, text='Load existing INPUT file', var=self.input_type, value=1).pack(anchor='w')
        tk.Button(self, text='Choose File', command=lambda: self.getInput(master)).pack()

    def getInput(self, master):
        """
        Switch between the two input options:
        Option 0 (Analyse & Filter Operation Data) - leads to input_pre_process
        Option 1 (Load existing INPUT file) - skips straight to core module (bypass input_pre_process)
        """
        master.filename = filedialog.askopenfilename()
        if master.filename != '':
            if self.input_type.get() == 0:
                imported_data = pd.read_csv(master.filename)
                runPreprocess(self, app, imported_data)
            tk.Label(self, text='Loaded file %s' % master.filename.split('/')[-1]).pack()
            app.select('.!coremodule')


class coreModule(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self)

        # Frame 1: Mandatory Fields
        self.req = {
            'n_input': tk.IntVar(value='50'),
            'minDep_altSID_input': tk.IntVar(value='60'),
            'minDep_sameSID_input': tk.IntVar(value='109'),
            'SIDmax_input': tk.IntVar(value='4'),
            'SIDgroup_separation_input': tk.StringVar(value='(2,4)(3,4)'),
            '1x8':tk.IntVar(),
            '2x4':tk.IntVar(),
            '4x2':tk.IntVar(),
            '8x1':tk.IntVar(),
            'SID_queue_assign_input': tk.StringVar(value='1 3 | 2 4')
        }
        coreframe1 = ttk.LabelFrame(self, text=' Mandatory Fields ')
        ttk.Label(coreframe1, text='[Arrival lead time] n value (in secs) =').pack()
        tk.Entry(coreframe1, width=7, textvariable=self.req['n_input']).pack()
        ttk.Label(coreframe1, text='Minimum Separation (secs) alternating SIDs =').pack()
        tk.Entry(coreframe1, width=7, textvariable=self.req['minDep_altSID_input']).pack()
        ttk.Label(coreframe1, text='Minimum Separation (secs) same SIDs =').pack()
        tk.Entry(coreframe1, width=7, textvariable=self.req['minDep_sameSID_input']).pack()
        ttk.Label(coreframe1, text='Maximum number of SID groups').pack()
        tk.Entry(coreframe1, width=7, textvariable=self.req['SIDmax_input']).pack()
        ttk.Label(coreframe1, text='Enter the pairs of SID groups that require minimum separation.').pack()
        tk.Entry(coreframe1, width=14,  textvariable=self.req['SIDgroup_separation_input']).pack()
        ttk.Label(coreframe1, text='Select the type of queue').pack()
        tk.Checkbutton(coreframe1, text='1x8', variable=self.req['1x8']).pack()
        tk.Checkbutton(coreframe1, text='2x4', variable=self.req['2x4']).pack()
        tk.Checkbutton(coreframe1, text='4x2', variable=self.req['4x2']).pack()
        tk.Checkbutton(coreframe1, text='8x1', variable=self.req['8x1']).pack()
        ttk.Label(coreframe1, text='Assign SID groups to each RWY queue.').pack()
        tk.Entry(coreframe1, width=14, textvariable=self.req['SID_queue_assign_input']).pack()
        coreframe1.grid(row=0, column=1, sticky='nsew')

        # Frame 2: Optional Fields
        self.opt = {
            'var6': tk.IntVar(),
            'var17': tk.IntVar(),
            'separation_type': tk.IntVar(),
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
        coreframe2 = ttk.LabelFrame(self, text=' Enablers (Optional) ')
        tk.Checkbutton(coreframe2, text='RECAT', variable=self.opt['var6']).pack()
        tk.Checkbutton(coreframe2, text='RECAT-PWS', variable=self.opt['var17']).pack()
        tk.Radiobutton(coreframe2, text='DISTANCE-based Arrivals separation', var=self.opt['separation_type'], value=0).pack()
        tk.Radiobutton(coreframe2, text='TIME-based Arrivals separation', var=self.opt['separation_type'], value=1).pack()
        tk.Label(coreframe2, text='ADA target time X-value = ').pack()
        tk.Entry(coreframe2, width=7, textvariable=self.opt['ADA_x_input']).pack()
        tk.Label(coreframe2, text='4DME Separation Delivery').pack()
        tk.Checkbutton(coreframe2, text='MRS', variable=self.opt['MRS_4dme']).pack()
        tk.Checkbutton(coreframe2, text='WAKE', variable=self.opt['WAKE_4dme']).pack()
        tk.Checkbutton(coreframe2, text='ADA', variable=self.opt['ADA_4dme']).pack()
        tk.Checkbutton(coreframe2, text='ADDA', variable=self.opt['ADDA_4dme']).pack()
        tk.Label(coreframe2, text='Threshold Separation Delivery').pack()
        tk.Checkbutton(coreframe2, text='MRS', variable=self.opt['MRS_thr']).pack()
        tk.Checkbutton(coreframe2, text='WAKE', variable=self.opt['WAKE_thr']).pack()
        tk.Checkbutton(coreframe2, text='ADA', variable=self.opt['ADA_thr']).pack()
        tk.Checkbutton(coreframe2, text='ADDA', variable=self.opt['ADDA_thr']).pack()
        coreframe2.grid(row=0, column=2, sticky='nsew')

        # Frame 3: Run Settings
        self.run = {
            'n_times_input': tk.IntVar(value='1'),
            'var7': tk.IntVar(),
            'var14': tk.IntVar()
        }
        coreframe3 = ttk.LabelFrame(self, text=' Run Settings ')
        ttk.Label(coreframe3, text='Number of runs = ').pack()
        tk.Entry(coreframe3, width=7, textvariable=self.run['n_times_input']).pack()
        tk.Checkbutton(coreframe3, text='I want to feel confident!', variable=self.run['var7']).pack()
        tk.Checkbutton(coreframe3, text='Print a debug tab', variable=self.run['var14']).pack()
        tk.Button(coreframe3, text='Run', command=lambda: runModel(self.req, self.opt, self.run, master.filename)).pack()
        coreframe3.grid(row=1, column=1, columnspan=2, sticky='nsew')


class visualModule(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self)
        self.frame1 = ttk.Frame(self)
        self.test = tk.Label(self.frame1, text='This is the visual module')
        self.test.pack()
        tk.Button(self, text='Destroy', command=lambda: root.destroy()).pack()
        self.frame1.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('RAPID')
    app = mainWindow(root)
    root.mainloop()
