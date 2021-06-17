import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd

from input_pre_process import input_pre_process

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
        tk.Label(self, text='Select Input Type').pack()
        self.selection = tk.IntVar()
        tk.Radiobutton(self, text='Analyse & Filter Operational Data', var=self.selection, value=0).pack()
        tk.Radiobutton(self, text='Load existing INPUT file', var=self.selection, value=1).pack()
        tk.Button(self, text='Choose File', command=self.getInput).pack()

    def getInput(self):
        """
        Switch between the two input options:
        Option 0 (Analyse & Filter Operation Data) - leads to input_pre_process
        Option 1 (Load existing INPUT file) - skips straight to core module (bypass input_pre_process)
        """
        filename = filedialog.askopenfilename()
        imported_data = pd.read_csv(filename)
        if len(imported_data.index) > 1:
            if self.selection.get() == 0:
                ### See input_pre_process.py for function input_pre_process
                input_pre_process(self, app, imported_data)
            tk.Label(self, text='Loaded file %s' % filename.split('/')[-1]).pack()
            app.select('.!coremodule')


class coreModule(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self)
        self.test = tk.Label(self, text="This is the core module")
        self.test.pack()


class visualModule(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self)
        self.test = tk.Label(self, text="This is the visual module")
        self.test.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("RAPID")
    app = mainWindow(root)
    root.mainloop()
