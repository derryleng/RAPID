import pandas as pd
import numpy as np
import json
import scipy.stats as stats

import tkinter as tk
from tkinter import ttk, filedialog

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

def load_file(filename):
    filename.set(filedialog.askopenfilename())

def runVisual(parentFrame):

    n_times_input= tk.IntVar(value='1')
    n_times_output = tk.IntVar()

    n_times = int(n_times_input.get())
    n_times_output.set(n_times)

    m_input = tk.IntVar(value='0')
    Throughput_check_output = tk.IntVar()
    Delay_check_output = tk.IntVar()
    Seq_check_output = tk.IntVar()
    op_yes_output = tk.IntVar()
    new_set_output = tk.IntVar()
    m_output = tk.IntVar()
    arr_delay_output = tk.IntVar()
    convergence_output = tk.IntVar()

    ADA_buffer_output = tk.IntVar()

    n_times = 1

    #====FOR VISUAL MODULE======#

    m = 0

    Seq_FLAG = False
    average_FLAG = False

    # VISUAL
    m = int(m_input.get())
    m_output.set(m)

    convergenceFLAG = bool(int(parentFrame.vis['var0'].get()))
    Thr_FLAG = bool(int(parentFrame.vis['var8'].get()))
    Delay_FLAG = bool(int(parentFrame.vis['var9'].get()))
    Seq_FLAG = bool(int(parentFrame.vis['var10'].get()))
    ADA_buffer_FLAG = bool(int(parentFrame.vis['var18'].get()))
    OP_FLAG = bool(int(parentFrame.vis['var11'].get()))
    new_set_FLAG = bool(int(parentFrame.vis['var12'].get()))
    arr_delay_FLAG = bool(int(parentFrame.vis['var13'].get()))

    n_times = n_times_output.get()
    m = m_output.get()

    #----Operational Data -----#
    if OP_FLAG:
        win = tk.Tk()
        win.title("Operational Data import")
        mainframe = ttk.Frame(win, padding="10 10 30 40")
        mainframe.grid(column=0, row=0, sticky='NWES')
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        innerframe = ttk.Frame(win, padding="5 5 0 0")

        op_data_sheet = tk.StringVar()
        ttk.Label(mainframe, text="Import the Operational Data File : ").grid(column=1, row=1, sticky='W')
        open_op_data = ttk.Button(mainframe, text="Import operational data", command=lambda: load_file(op_data_sheet)).grid(column=2, row=1, sticky='W')
        inner = tk.Frame(win, bg='pink', width=0, height=0, padx=20, pady=20)
        inner.grid(column=0, row=1)
        inner.columnconfigure(0, weight=1)
        inner.rowconfigure(0, weight=1)
        # ttk.Button(inner, text="Visualize results", command=define_input_parameters).grid(column=0, row=0, sticky='W')

        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)
        win.rowconfigure(1, weight=1)

        win.mainloop()
        operational_data = op_data_sheet.get()

    #----New set of data---#
    if new_set_FLAG == True:
        if m >= 1 :
            win = tk.Tk()
            win.title("New set of data import")

            mainframe = ttk.Frame(win, padding="10 10 30 40")
            mainframe.grid(column=0, row=0, sticky='NWES')
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)

            innerframe = ttk.Frame(win, padding="5 5 0 0")

            average_check_output = tk.IntVar()
            new_data_sheet2 = tk.StringVar()
            ttk.Label(mainframe, text="Import new data set 2: ").grid(column=1, row=1, sticky='W')
            open_new_data2 = ttk.Button(mainframe, text="Import data 2", command=lambda: load_file(new_data_sheet2)).grid(column=2, row=1, sticky='W')

            if m >=2:
                new_data_sheet3 = tk.StringVar()
                ttk.Label(mainframe, text="Import new data set 3: ").grid(column=1, row=2, sticky='W')
                open_new_data3 = ttk.Button(mainframe, text="Import data 3", command=lambda: load_file(new_data_sheet3)).grid(column=2, row=2, sticky='W')

                if m >=3:
                    new_data_sheet4 = tk.StringVar()
                    ttk.Label(mainframe, text="Import new data set 4: ").grid(column=1, row=3, sticky='W')
                    open_new_data4 = ttk.Button(mainframe, text="Import data 4", command=lambda: load_file(new_data_sheet4)).grid(column=2, row=3, sticky='W')
                    if m >=4:
                        new_data_sheet5 = tk.StringVar()
                        ttk.Label(mainframe, text="Import new data set 5: ").grid(column=1, row=4, sticky='W')
                        open_new_data5 = ttk.Button(mainframe, text="Import data 5", command=lambda: load_file(new_data_sheet5)).grid(column=2, row=4, sticky='W')
                        if m >=5:
                            new_data_sheet6 = tk.StringVar()
                            ttk.Label(mainframe, text="Import new data set 6: ").grid(column=1, row=5, sticky='W')
                            open_new_data6 = ttk.Button(mainframe, text="Import data 6", command=lambda: load_file(new_data_sheet6)).grid(column=2, row=5, sticky='W')


            inner = tk.Frame(win, bg='pink', width=0, height=0, padx=20, pady=20)
            inner.grid(column=0, row=1)
            inner.columnconfigure(0, weight=1)
            inner.rowconfigure(0, weight=1)
            # ttk.Button(inner, text="Visualize results", command=define_input_parameters).grid(column=0, row=0, sticky='W')

            win.columnconfigure(0, weight=1)
            win.rowconfigure(0, weight=1)
            win.rowconfigure(1, weight=1)

            win.mainloop()
            if average_check_output.get() == 1:
                average_FLAG = True
            else:
                average_FLAG = False

        if m>=1:
            new_data2 = new_data_sheet2.get()
            xls2 = pd.ExcelFile(new_data2)
            df_thr2 = xls2.parse(5)
            df_delay2 = xls2.parse(6)
            df_dep_output2 = xls2.parse(4)
            df_arr_output2 = xls2.parse(3)
            df_rwy_calcs2 = xls2.parse(2)

            if m>=2:
                new_data3 = new_data_sheet3.get()
                xls3 = pd.ExcelFile(new_data3)
                df_thr3 = xls3.parse(5)
                df_delay3 = xls3.parse(6)
                df_dep_output3 = xls3.parse(4)
                df_arr_output3 = xls3.parse(3)
                df_rwy_calcs3 = xls3.parse(2)
                if m>=3:
                    new_data4 = new_data_sheet4.get()
                    xls4 = pd.ExcelFile(new_data4)
                    df_thr4 = xls4.parse(5)
                    df_delay4 = xls4.parse(6)
                    df_dep_output4 = xls4.parse(4)
                    df_arr_output4 = xls4.parse(3)
                    df_rwy_calcs4 = xls4.parse(2)
                    if m>=4:
                        new_data5 = new_data_sheet5.get()
                        xls5 = pd.ExcelFile(new_data5)
                        df_thr5 = xls5.parse(5)
                        df_delay5 = xls5.parse(6)
                        df_dep_output5 = xls5.parse(4)
                        df_arr_output5 = xls5.parse(3)
                        df_rwy_calcs5 = xls5.parse(2)
                        if m>=5:
                            new_data6 = new_data_sheet6.get()
                            xls6 = pd.ExcelFile(new_data6)
                            df_thr6 = xls6.parse(5)
                            df_delay6 = xls6.parse(6)
                            df_dep_output6 = xls6.parse(4)
                            df_arr_output6 = xls6.parse(3)
                            df_rwy_calcs6 = xls6.parse(2)

    xls = pd.ExcelFile(parentFrame.name_output_file)
    df_thr = xls.parse(5)
    df_delay = xls.parse(6)
    df_dep_output = xls.parse(4)
    df_arr_output = xls.parse(3)
    df_rwy_calcs = xls.parse(2)
    df_sequence_output =xls.parse(7)
    df_thr['Mean Thr'] = 0

    if OP_FLAG == True:
        opr_xls = pd.ExcelFile(operational_data)
        op_data = opr_xls.parse(0)
        #Transform date format into seconds
        op_data['Time Bin-H'] = op_data['Time Bin-H'] .astype(str)
        op_data['Time Bin-H'] = pd.DatetimeIndex(op_data['Time Bin-H'])
        op_data['Time Bin-H'] = pd.to_timedelta(op_data['Time Bin-H']) # convert to timedelta to calculate seconds
        op_data['Time Bin-H'] = op_data['Time Bin-H'].dt.seconds

        op_data['Time Bin - PS'] = op_data['Time Bin - PS'] .astype(str)
        op_data['Time Bin - PS'] = pd.DatetimeIndex(op_data['Time Bin - PS'])
        op_data['Time Bin - PS'] = pd.to_timedelta(op_data['Time Bin - PS']) # convert to timedelta to calculate seconds
        op_data['Time Bin - PS'] = op_data['Time Bin - PS'].dt.seconds

        #Extract lists to plot them
        OD_Thr_Hour = op_data['Hour'].tolist()
        OD_Thr = op_data['Total Throughput'].tolist()
        OP_H_Delay = op_data['Hold-Delay'].tolist()
        OP_Time_H_Delay = op_data['Time Bin-H'].tolist()
        OP_PS_Delay = op_data['PS-Delay'].tolist()
        OP_Time_PS_Delay = op_data['Time Bin - PS'].tolist()


    class RAPIDvisual(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            # tk.Tk.iconbitmap(self, text="clienticon.ico")
            tk.Tk.wm_title(self, "RAPID VISUAL")
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand = True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            self.frames = {}
            for F in (StartPage, Conv, Thr, DepDelay, DepDelay2, ArrivalDelay, Seq, ADAbuffer):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky='NWES')
            self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()


    class StartPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            tk.Label(self, text="Start Page").pack(pady=10,padx=10)
            if convergenceFLAG ==True:
                ttk.Button(self, text="Convergence Throughput", command=lambda: controller.show_frame(Conv)).pack()
            if Thr_FLAG == True:
                ttk.Button(self, text="Throughput", command=lambda: controller.show_frame(Thr)).pack()
            if Delay_FLAG == True:
                ttk.Button(self, text="RWY Hold Delay", command=lambda: controller.show_frame(DepDelay)).pack()
            if Delay_FLAG == True:
                ttk.Button(self, text="Push/Start Delay", command=lambda: controller.show_frame(DepDelay2)).pack()
            if arr_delay_FLAG == True:
                ttk.Button(self, text="Arrivals Delay", command=lambda: controller.show_frame(ArrivalDelay)).pack()
            if Seq_FLAG == True:
                ttk.Button(self, text="Sequence", command=lambda: controller.show_frame(Seq)).pack()
            if ADA_buffer_FLAG == True:
                ttk.Button(self, text="ADA Buffer", command=lambda: controller.show_frame(ADAbuffer)).pack()
            ttk.Label(self, text=".").pack()
            ttk.Label(self, text=".").pack()
            ttk.Label(self, text=".").pack()
            ttk.Label(self, text="I want to compare my results").pack()
            ttk.Label(self, text="_____________________________").pack()
            ttk.Label(self, text="How many new sets?").pack()

            def show_button():
                m2 = int(m2_input.get())
                m2_output.set(m2)
                app.destroy()
                m2 = m2_output.get()

                # def define_input_parameters3():
                #     convergence = int(parentFrame.vis['var0'].get())
                #     convergence_output.set(convergence)
                #     Throughput_check = int(parentFrame.vis['var8'].get())
                #     Throughput_check_output.set(Throughput_check)
                #     Delay_check = int(parentFrame.vis['var9'].get())
                #     Delay_check_output.set(Delay_check)
                #     arr_delay = int(parentFrame.vis['var13'].get())
                #     arr_delay_output.set(arr_delay)
                #     Seq_check = int(parentFrame.vis['var10'].get())
                #     Seq_check_output.set(Seq_check)
                #     op_yes = int(parentFrame.vis['var11'].get())
                #     op_yes_output.set(op_yes)
                #     new_set = int(parentFrame.vis['var12'].get())
                #     new_set_output.set(new_set)
                #     ADA_buffer = int(parentFrame.vis['var18'].get())
                #     ADA_buffer_output.set(ADA_buffer)
                #     average_check = int(parentFrame.vis['var6'].get())
                #     average_check_output.set(average_check)
                #     window.destroy()

                if m2 >= 1 :
                    window = tk.Tk()
                    window.title("New set of data import")

                    mainframe = ttk.Frame(window, padding="10 10 30 40")
                    mainframe.grid(column=0, row=0, sticky='NWES')
                    mainframe.columnconfigure(0, weight=1)
                    mainframe.rowconfigure(0, weight=1)

                    #innerframe = ttk.Frame(window, padding="5 5 0 0")

                    average_check_output = tk.IntVar()
                    new_data_sheet2 = tk.StringVar()
                    ttk.Label(mainframe, text="Import new data set 2: ").grid(column=1, row=1, sticky='W')
                    ttk.Button(mainframe, text="Import data 2", command=lambda: load_file(new_data_sheet2)).grid(column=2, row=1, sticky='W')

                    if m2 >=2:
                        new_data_sheet3 = tk.StringVar()
                        ttk.Label(mainframe, text="Import new data set 3: ").grid(column=1, row=2, sticky='W')
                        ttk.Button(mainframe, text="Import data 3", command=lambda: load_file(new_data_sheet3)).grid(column=2, row=2, sticky='W')

                        if m2 >=3:
                            new_data_sheet4 = tk.StringVar()
                            ttk.Label(mainframe, text="Import new data set 4: ").grid(column=1, row=3, sticky='W')
                            ttk.Button(mainframe, text="Import data 4", command=lambda: load_file(new_data_sheet4)).grid(column=2, row=3, sticky='W')
                            if m2 >=4:
                                new_data_sheet5 = tk.StringVar()
                                ttk.Label(mainframe, text="Import new data set 5: ").grid(column=1, row=4, sticky='W')
                                ttk.Button(mainframe, text="Import data 5", command=lambda: load_file(new_data_sheet5)).grid(column=2, row=4, sticky='W')
                                if m2 >=5:
                                    new_data_sheet6 = tk.StringVar()
                                    ttk.Label(mainframe, text="Import new data set 6: ").grid(column=1, row=5, sticky='W')
                                    ttk.Button(mainframe, text="Import data 6", command=lambda: load_file(new_data_sheet6)).grid(column=2, row=5, sticky='W')

                    inner = tk.Frame(window, bg='pink', width=0, height=0, padx=20, pady=20)
                    inner.grid(column=0, row=1)
                    inner.columnconfigure(0, weight=1)
                    inner.rowconfigure(0, weight=1)
                    # tk.Button(inner, text="Visualize results", command=define_input_parameters3).grid(column=0, row=0, sticky='W')

                    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
                    # window.bind('<Return>', define_input_parameters)

                    window.columnconfigure(0, weight=1)
                    window.rowconfigure(0, weight=1)
                    window.rowconfigure(1, weight=1)

                    window.mainloop()

                if m2>=1:
                    new_data2 = new_data_sheet2.get()
                    xls2 = pd.ExcelFile(new_data2)
                    df_thr2 = xls2.parse(5)
                    df_delay2 = xls2.parse(6)
                    df_dep_output2 = xls2.parse(4)
                    df_arr_output2 = xls2.parse(3)
                    df_rwy_calcs2 = xls2.parse(2)

                    if m2>=2:
                        new_data3 = new_data_sheet3.get()
                        xls3 = pd.ExcelFile(new_data3)
                        df_thr3 = xls3.parse(5)
                        df_delay3 = xls3.parse(6)
                        df_dep_output3 = xls3.parse(4)
                        df_arr_output3 = xls3.parse(3)
                        df_rwy_calcs3 = xls3.parse(2)
                        if m2>=3:
                            new_data4 = new_data_sheet4.get()
                            xls4 = pd.ExcelFile(new_data4)
                            df_thr4 = xls4.parse(5)
                            df_delay4 = xls4.parse(6)
                            df_dep_output4 = xls4.parse(4)
                            df_arr_output4 = xls4.parse(3)
                            df_rwy_calcs4 = xls4.parse(2)
                            if m2>=4:
                                new_data5 = new_data_sheet5.get()
                                xls5 = pd.ExcelFile(new_data5)
                                df_thr5 = xls5.parse(5)
                                df_delay5 = xls5.parse(6)
                                df_dep_output5 = xls5.parse(4)
                                df_arr_output5 = xls5.parse(3)
                                df_rwy_calcs5 = xls5.parse(2)
                                if m2>=5:
                                    new_data6 = new_data_sheet6.get()
                                    xls6 = pd.ExcelFile(new_data6)
                                    df_thr6 = xls6.parse(5)
                                    df_delay6 = xls6.parse(6)
                                    df_dep_output6 = xls6.parse(4)
                                    df_arr_output6 = xls6.parse(3)
                                    df_rwy_calcs6 = xls6.parse(2)

                # ============================================================================#
                #                       VISUAL GUI                                            #
                # ============================================================================#

                class RAPIDvisual2(tk.Tk):

                    def __init__(self, *args, **kwargs):

                        tk.Tk.__init__(self, *args, **kwargs)

                        #tk.Tk.iconbitmap(self, text="clienticon.ico")
                        tk.Tk.wm_title(self, "RAPID VISUAL")


                        container = tk.Frame(self)
                        container.pack(side="top", fill="both", expand = True)
                        container.grid_rowconfigure(0, weight=1)
                        container.grid_columnconfigure(0, weight=1)

                        self.frames = {}
                        for F in (StartPage2, Conv2, Thr2, DepDelay22, DepDelay222, ArrivalDelay2, Seq2, ADAbuffer2):

                            frame = F(container, self)

                            self.frames[F] = frame

                            frame.grid(row=0, column=0, sticky='NWES')

                        self.show_frame(StartPage2)

                    def show_frame(self, cont):

                        frame = self.frames[cont]
                        frame.tkraise()


                class StartPage2(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self,parent)
                        label = tk.Label(self, text="Start Page")
                        label.pack(pady=10,padx=10)

                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()
                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY Hold Delay",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()
                        if Delay_FLAG == True:
                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()
                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()
                        if Seq_FLAG == True:
                            button4 = ttk.Button(self, text="Sequence",
                                                command=lambda: controller.show_frame(Seq2))
                            button4.pack()


                # ============================================================================#
                #                           CONVERGENCE                                       #
                # ============================================================================#
                #if convergenceFLAG ==True:
                class Conv2(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="THROUGHPUT CONVERGENCE")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()


                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()

                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY Hold Delay",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()
                        if Delay_FLAG == True:
                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()
                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()
                        if Seq_FLAG == True:
                            button4 = ttk.Button(self, text="Sequence",
                                                command=lambda: controller.show_frame(Seq2))
                            button4.pack()

                        if ADA_buffer_FLAG == True:
                            button5 = ttk.Button(self, text="ADA Buffer",
                                                command=lambda: controller.show_frame(ADAbuffer))
                            button5.pack()

                        thr_av_diff = pd.DataFrame(df_thr['Difference in thr averages'])
                        thr_av_diff=thr_av_diff.dropna(subset=['Difference in thr averages'])

                        thr_av_diff['Tags'] = thr_av_diff['Difference in thr averages'].apply(lambda x: json.loads(x))
                        thr_av_difference = thr_av_diff['Tags'].tolist()

                        print(len(thr_av_difference[0][0]))
                        print(len(thr_av_difference[0]))
                        thr_abc=[]
                        total_runs =[]
                        runs_Thr = []
                        for i in range (1,(len(thr_av_difference[0])+1)):
                            runs_Thr.append(i)

                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)

                        for j in range (0, len(thr_av_difference[0][0])):
                            for i in range (0, len(thr_av_difference[0])):
                                total_thr = thr_av_difference[0][i][j]
                                runs_Thrx = runs_Thr[i]
                                total_runs.append(runs_Thrx)
                                thr_abc.append(total_thr)
                            A.plot(total_runs,thr_abc)
                            thr_abc = []
                            total_runs =[]

                        A.set_xlabel('No. of Runs')
                        A.set_ylabel('Difference in average throughput per hour')
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        #A.title('Throughput')
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # ============================================================================#
                #                          THROUGHPUT                                         #
                # ============================================================================#

                #if Thr_FLAG == True:
                class Thr2(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="THROUGHPUT")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()

                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY Hold Delay",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()

                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()
                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()
                        if Seq_FLAG == True:
                            button4 = ttk.Button(self, text="Sequence",
                                                command=lambda: controller.show_frame(Seq2))
                            button4.pack()
                        if ADA_buffer_FLAG == True:
                            button5 = ttk.Button(self, text="ADA Buffer",
                                                command=lambda: controller.show_frame(ADAbuffer2))
                            button5.pack()

                        def create_first_df_thr():
                            df_thr_to_plot = pd.DataFrame()
                            df_thr_to_plot['Hour'] = df_thr['Hour']
                            x = 'Hour'
                            df_thr_to_plot['RUN 1'] = df_thr['Total Throughput']
                            y = 'RUN 1'

                            df_thr_to_plot2 = df_thr_to_plot[[x,y]].groupby(x).sum()

                            return df_thr_to_plot2


                        def create_multiple_df_thr(df_thr_to_plot2, df_thr_input, name):
                            df_thr_to_plot2[name] = df_thr_input['Total Throughput']
                            df_thr_to_plot_temp = pd.DataFrame()
                            df_thr_to_plot_temp['Hour'] = df_thr_input['Hour']
                            a = 'Hour'
                            df_thr_to_plot_temp[name] = df_thr_input['Total Throughput']
                            b = name
                            df_thr_to_plot_temp = df_thr_to_plot_temp.dropna(subset=['Hour'])
                            df_thr_to_plot_temp2 = df_thr_to_plot_temp[[a,b]].groupby(a).sum()

                            df_thr_to_plot2[name] = df_thr_to_plot_temp2[name]

                            return df_thr_to_plot2


                        def plot_bar_thr(df_thr_to_plot2, A):
                            df_thr_to_plot2.plot(kind='bar', legend=False, ax=A)


                        def total_thr(df_thr_input):
                            total_thr = df_thr_input['Total Throughput']
                            total_thr = total_thr.reset_index()
                            return(total_thr)


                        def hour_thr(df_thr_input):
                            hour_Thr = df_thr_input['Hour'].tolist()
                            return(hour_Thr)


                        if m2>= 1:
                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            # throughput(df_thr, 'k')
                            # throughput(df_thr2, 'g')
                            df_thr_to_plot2 = create_first_df_thr()
                            df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr2, 'RUN 2')

                            if OP_FLAG == True:
                                df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                A.legend(('Model','Operational Data', 'Model 2'), loc = 'upper right')
                            else:
                                A.legend(('Model', 'Model 2'), loc = 'upper right')
                            if m2>= 2:
                                df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr3, 'RUN 3')

                                if OP_FLAG ==True:
                                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                    A.legend(('Model','Operational Data', 'Model 2', 'Model 3'), loc = 'upper right')
                                else:
                                    A.legend(('Model','Model 2', 'Model 3'), loc = 'upper right')
                                if m2>=3:
                                    #throughput(df_thr4, 'm')
                                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr4, 'RUN 4')

                                    if OP_FLAG ==True:
                                        df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                        A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                    else:
                                        A.legend(('Model','Model 2', 'Model 3','Model 4'), loc = 'upper right')
                                    if m2>=4:
                                        #throughput(df_thr5, 'y')
                                        df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr5, 'RUN 5')

                                        if OP_FLAG ==True:
                                            df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                            A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                        else:
                                            df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                            A.legend(('Model','Model 2', 'Model 3','Model 4', 'Model 5'), loc = 'upper right')
                                        if m2>=5:
                                            df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr6, 'RUN 6')
                                            #throughput(df_thr6, color = 'purple')

                                            if OP_FLAG ==True:
                                                df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                                A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                            else:
                                                A.legend(('Model','Model 2', 'Model 3','Model 4','Model 5','Model 6'), loc = 'upper right')
                            plot_bar_thr(df_thr_to_plot2, A)
                            if OP_FLAG ==True:
                                df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                            A.set_xlabel('Hours of the day')
                            A.set_ylabel('No of A/C')
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            #A.title('Throughput')
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # ============================================================================#
                #                         DEPARTURE DELAY - RWY hold delay                    #
                # ============================================================================#

                #if Delay_FLAG == True:
                class DepDelay22(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="RWY HOLD DELAY")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()

                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()

                        if Delay_FLAG == True:
                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()
                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()
                        if Seq_FLAG == True:
                            button4 = ttk.Button(self, text="Sequence",
                                                command=lambda: controller.show_frame(Seq2))
                            button4.pack()
                        if ADA_buffer_FLAG == True:
                            button5 = ttk.Button(self, text="ADA Buffer",
                                                command=lambda: controller.show_frame(ADAbuffer2))
                            button5.pack()
                        if (df_delay.empty == True):
                            print("No departures. Nothing to show")
                        else:
                            def delay(df_delay,df_dep_output):

                                interval15=[]
                                df_ps_delay = pd.DataFrame()
                                # Add arrival delay values
                                df_ps_delay['RWYhold_Delay'] = df_delay['RWY HOLD Delay']
                                # print when those values occure
                                df_ps_delay['Time1'] = df_dep_output['Departure_RWY_ENTRY']
                                # round each time value to 15 minutes
                                df_ps_delay= df_ps_delay.dropna(subset=['Time1'])
                                time1_list = df_ps_delay['Time1'].tolist()
                                #a=[]
                                for a in time1_list:
                                    b = int(int(a/900)*900)
                                    interval15.append(b)

                                df_ps_delay['interval15'] = interval15
                                df_ps_delay = df_ps_delay.drop(columns=['Time1'])
                                #Group data by the time interval, if there are multiple values for the same time interval, take the mean.
                                df_ps_delay = df_ps_delay.groupby(['interval15'])['RWYhold_Delay'].mean()
                                #make the rolling average
                                df_ps_delay = df_ps_delay.reset_index()
                                df_ps_delay2 = df_ps_delay.rolling(window=4, on='interval15')['RWYhold_Delay'].mean()
                                RWYhold_Delay = df_ps_delay2.tolist()
                                df_ps_delay['DATE'] = pd.to_datetime(df_ps_delay['interval15'],unit='s')
                                df_ps_delay['DATE'] = df_ps_delay['DATE'].apply(lambda x: x.time())

                                time_interval = df_ps_delay['DATE']
                                return {'a': time_interval,
                                        'b': RWYhold_Delay}


                            def print_Hold_delay(ab, color):

                                H_delay_time = ab['a']
                                H_delay = ab['b']

                                A = f.add_subplot(111)
                                A.plot(H_delay_time, H_delay, color)
                                #A.set_title('RWY HOLD DELAY', loc='left')
                                if OP_FLAG == True: #Plot Operational Data
                                    A.plot(OP_Time_H_Delay,OP_H_Delay, 'b')
                                    A.legend(('Model','Operational Data'), loc = 'upper right')


                            if m2 >=1:
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                hold_delay = delay(df_delay,df_dep_output)
                                print_Hold_delay(hold_delay,'k')
                                hold_delay2 = delay(df_delay2,df_dep_output2)
                                print_Hold_delay(hold_delay2,'g')

                                if OP_FLAG == True:
                                    A.legend(('Model','Operational Data', 'Model 2'), loc = 'upper right')
                                else:
                                    A.legend(('Model', 'Model 2'), loc = 'upper right')
                                if m2>=2:
                                    hold_delay3 = delay(df_delay3,df_dep_output3)
                                    print_Hold_delay(hold_delay3,'c')

                                    if OP_FLAG == True:
                                        A.legend(('Model','Operational Data', 'Model 2', 'Model 3'), loc = 'upper right')
                                    else:
                                        A.legend(('Model', 'Model 2', 'Model 3'), loc = 'upper right')
                                    if m2>=3:
                                        hold_delay4 = delay(df_delay4,df_dep_output4)
                                        print_Hold_delay(hold_delay4,'m')

                                        if OP_FLAG == True:
                                            A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                        else:
                                            A.legend(('Model', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                        if m2>=4:
                                            hold_delay5 = delay(df_delay5,df_dep_output5)
                                            print_Hold_delay(hold_delay5,'y')

                                            if OP_FLAG == True:
                                                A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                            else:
                                                A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                            if m2>=5:
                                                hold_delay6 = delay(df_delay6,df_dep_output6)
                                                print_Hold_delay(hold_delay6,color='purple')

                                                if OP_FLAG == True:
                                                    A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                                else:
                                                    A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                A.set_xlabel('Seconds of the day')
                                A.set_ylabel('Seconds of delay')
                                A.grid(color='b', linestyle='-', linewidth=0.1)

                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # ============================================================================#
                #                   DEPARTURE DELAY - PS delay                                #
                # ============================================================================#

                class DepDelay222(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="PUSH/START DELAY")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()

                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()
                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY HOLD DELAY",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()
                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()
                        if Seq_FLAG == True:
                            button4 = ttk.Button(self, text="Sequence",
                                                command=lambda: controller.show_frame(Seq2))
                            button4.pack()
                        if ADA_buffer_FLAG == True:
                            button5 = ttk.Button(self, text="ADA Buffer",
                                                command=lambda: controller.show_frame(ADAbuffer2))
                            button5.pack()
                        if (df_delay.empty == True):
                            print("No departures. Nothing to show")
                        else:
                            def delay(df_delay, df_dep_output):
                                interval15=[]
                                df_ps_delay = pd.DataFrame()
                                # Add arrival delay values
                                df_ps_delay['PS_Delay'] = df_delay['Push/Start Delay']
                                # print when those values occure
                                df_ps_delay['Time1'] = df_dep_output['Departure_RWY_ENTRY']
                                # round each time value to 15 minutes
                                df_ps_delay= df_ps_delay.dropna(subset=['Time1'])
                                time1_list = df_ps_delay['Time1'].tolist()
                                #a=[]
                                for a in time1_list:
                                    b = int(int(a/900)*900)
                                    interval15.append(b)

                                df_ps_delay['interval15'] = interval15
                                df_ps_delay = df_ps_delay.drop(columns=['Time1'])
                                #Group data by the time interval, if there are multiple values for the same time interval, take the mean.
                                df_ps_delay = df_ps_delay.groupby(['interval15'])['PS_Delay'].mean()
                                #make the rolling average
                                df_ps_delay = df_ps_delay.reset_index()
                                df_ps_delay2 = df_ps_delay.rolling(window=4, on='interval15')['PS_Delay'].mean()
                                PS_delay = df_ps_delay2.tolist()
                                df_ps_delay['DATE'] = pd.to_datetime(df_ps_delay['interval15'],unit='s')
                                df_ps_delay['DATE'] = df_ps_delay['DATE'].apply(lambda x: x.time())

                                time_interval = df_ps_delay['DATE']

                                return {'c': time_interval,
                                        'd': PS_delay}


                            def print_PS_delay(ab, color):
                                PS_time = ab['c']
                                PS_delay = ab['d']
                                B = f.add_subplot(111)
                                B.plot(PS_time, PS_delay, color)
                                #B.set_title('PUSH/START DELAY', loc = 'right')
                                if OP_FLAG == True:#Plot Operational Data

                                    B.plot(OP_Time_PS_Delay,OP_PS_Delay, 'b')
                                    #plt.legend(('Model','Operational Data'), loc = 'upper right')


                            if m2 >=1:
                                f = Figure(figsize=(5,5), dpi=100)
                                B = f.add_subplot(111)
                                Push_delay = delay(df_delay, df_dep_output)
                                print_PS_delay(Push_delay,'k')
                                Push_delay2 = delay(df_delay2, df_dep_output2)
                                print_PS_delay(Push_delay2,'g')

                                if OP_FLAG == True:
                                    B.legend(('Model','Operational Data', 'Model 2'), loc = 'upper right')
                                else:
                                    B.legend(('Model', 'Model 2'), loc = 'upper right')
                                if m2>=2:
                                    Push_delay3 = delay(df_delay3, df_dep_output3)
                                    print_PS_delay(Push_delay3,'c')

                                    if OP_FLAG == True:
                                        B.legend(('Model','Operational Data', 'Model 2', 'Model 3'), loc = 'upper right')
                                    else:
                                        B.legend(('Model', 'Model 2', 'Model 3'), loc = 'upper right')
                                    if m2>=3:
                                        Push_delay4 = delay(df_delay4, df_dep_output4)
                                        print_PS_delay(Push_delay4,'m')


                                        if OP_FLAG == True:
                                            B.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                        else:
                                            B.legend(('Model', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                        if m2>=4:
                                            Push_delay5 = delay(df_delay5, df_dep_output5)
                                            print_PS_delay(Push_delay5,'y')


                                            if OP_FLAG == True:
                                                B.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                            else:
                                                B.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                            if m2>=5:
                                                Push_delay6 = delay(df_delay6, df_dep_output6)
                                                print_PS_delay(Push_delay6, color='purple')


                                                if OP_FLAG == True:
                                                    B.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                                else:
                                                    B.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')

                                B.grid(color='b', linestyle='-', linewidth=0.1)
                                B.set_xlabel('Time')
                                B.set_ylabel('Seconds of delay')
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # ============================================================================#
                #                          ARRIVAL DELAY                                      #
                # ============================================================================#

                #if arr_delay_FLAG == True:
                class ArrivalDelay2(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="ARRIVALS DELAY")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()

                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()
                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY Hold Delay",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()
                        if Delay_FLAG == True:
                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()

                        if Seq_FLAG == True:
                            button4 = ttk.Button(self, text="Sequence",
                                                command=lambda: controller.show_frame(Seq2))
                            button4.pack()
                        if ADA_buffer_FLAG == True:
                            button5 = ttk.Button(self, text="ADA Buffer",
                                                command=lambda: controller.show_frame(ADAbuffer2))
                            button5.pack()

                        if (df_delay.empty == True):
                                print("No departures. Nothing to show")
                        else:
                            def ArrDelay(df_delay, df_arr_output):
                                interval15=[]
                                df_arr_delay = pd.DataFrame()
                                # Add arrival delay values
                                df_arr_delay['ARR_Delay'] = df_delay['Arrival Delay']
                                # print when those values occure
                                df_arr_delay['Time1'] = df_arr_output['ACTUAL Landing Time']
                                # round each time value to 15 minutes
                                df_arr_delay= df_arr_delay.dropna(subset=['Time1'])
                                time1_list = df_arr_delay['Time1'].tolist()
                                #a=[]
                                for a in time1_list:
                                    b = int(int(a/900)*900)
                                    interval15.append(b)

                                df_arr_delay['interval15'] = interval15
                                df_arr_delay = df_arr_delay.drop(columns=['Time1'])
                                #Group data by the time interval, if there are multiple values for the same time interval, take the mean.
                                df_arr_delay = df_arr_delay.groupby(['interval15'])['ARR_Delay'].mean()
                                #make the rolling average
                                df_arr_delay = df_arr_delay.reset_index()
                                df_arr_delay2 = df_arr_delay.rolling(window=4, on='interval15')['ARR_Delay'].mean()
                                ARR_delay = df_arr_delay2.tolist()
                                df_arr_delay['DATE'] = pd.to_datetime(df_arr_delay['interval15'],unit='s')
                                df_arr_delay['DATE'] = df_arr_delay['DATE'].apply(lambda x: x.time())

                                time_interval = df_arr_delay['DATE']
                                #        return(H_delay_time,H_delay,PS_time,PS_delay)
                                return {'a': time_interval,
                                        'b': ARR_delay}


                            def plotArrDelay(ab, color):
                                arr_delay_time = ab['a']
                                arr_delay = ab['b']
                                A = f.add_subplot(111)
                                A.plot(arr_delay_time, arr_delay, color)


                            if m2 >=1:
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                plotArrDelay(ArrDelay(df_delay, df_arr_output),'k')
                                plotArrDelay(ArrDelay(df_delay2, df_arr_output2),'g')

                                A.legend(('Model', 'Model 2'), loc = 'upper right')
                                if m2>=2:
                                    plotArrDelay(ArrDelay(df_delay3, df_arr_output3),'c')

                                    A.legend(('Model', 'Model 2', 'Model 3'), loc = 'upper right')
                                    if m2>=3:
                                        plotArrDelay(ArrDelay(df_delay4, df_arr_output4),'m')

                                        A.legend(('Model', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                        if m2>=4:
                                            plotArrDelay(ArrDelay(df_delay5, df_arr_output5),'y')

                                            A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                            if m2>=5:
                                                plotArrDelay(ArrDelay(df_delay6, df_arr_output6),'purple')

                                                A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                A.set_xlabel('Time')
                                A.set_ylabel('Seconds of delay')
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # ============================================================================#
                #                           SEQUENCE                                          #
                # ============================================================================#

                #if Seq_FLAG == True:
                class Seq2(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="SEQUENCE")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()
                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()

                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY Hold Delay",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()
                        if Delay_FLAG == True:
                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()

                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()

                        if ADA_buffer_FLAG == True:
                            button5 = ttk.Button(self, text="ADA Buffer",
                                                command=lambda: controller.show_frame(ADAbuffer2))
                            button5.pack()

                        def sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, number):

                            df_sequence = pd.DataFrame()
                            #Arrivals

                            df_sequence['ARRIVAL'] = df_arr_output['ACTUAL Landing Time'] + (df_arr_output['AROT']/2)
                            df_sequence['ARRIVAL_error'] = df_arr_output['AROT']/2
                            df_sequence['ARRIVAL_spacing'] = df_arr_output['ACTUAL Landing Time']
                            df_temp = pd.DataFrame()
                            df_temp['MAX Constraint'] = df_arr_output['MAX Constraint']
                            df_temp = df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['Arrival_ZERO'] = 0
                            df_sequence['ARRIVAL_spacing_error'] = df_temp['MAX Constraint']
                            df_sequence['Arrival_ZERO'] = df_temp['Arrival_ZERO']

                            #Positions
                            df_sequence['main_position'] = number
                            df_sequence['arr_spacing_position'] = number+0.005

                            #Annotation

                            df_temp = pd.DataFrame()
                            df_temp['ARR_ID'] = df_arr_output['Arrival ID'].astype(str)
                            df_temp['ARR_WAKE'] = df_rwy_calcs['ARRIVAL actual WAKE'].astype(str)
                            df_temp['ARR_DELAY'] = df_arr_output['Arrival DELAY'].astype(str)
                            df_temp['ARRIVAL_LABEL'] = 'ID = ' + df_temp['ARR_ID'] + ' | WAKE = ' + df_temp['ARR_WAKE'] + ' | Delay = ' + df_temp['ARR_DELAY']

                            df_sequence['ARRIVAL_LABEL'] = df_temp['ARRIVAL_LABEL']

                            df_temp = pd.DataFrame()
                            df_temp['reason'] = df_arr_output['MAX Constraint Label']
                            df_temp = df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['value'] = df_sequence['ARRIVAL_spacing_error'].astype(str)
                            df_temp['ARRIVAL_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                            df_sequence['ARRIVAL_spacing_LABEL'] = df_temp['ARRIVAL_spacing_LABEL']

                            # LISTS to plot

                            #----ARRIVALS----#
                            main_arrival = df_sequence['ARRIVAL'].tolist()
                            main_arrival_error = df_sequence['ARRIVAL_error'].tolist()
                            arrival_spacing = df_sequence['ARRIVAL_spacing'].tolist()
                            arrival_spacing_error = df_sequence['ARRIVAL_spacing_error'].tolist()
                            arrival_zero = df_sequence['Arrival_ZERO'].tolist()
                            #-Labels:
                            arrival_label = df_sequence['ARRIVAL_LABEL'].tolist()
                            arrival_spacing_label = df_sequence['ARRIVAL_spacing_LABEL'].tolist()

                            #-----POSITIONS------#
                            main_data_position = df_sequence['main_position'].tolist()
                            arrival_spacing_position = df_sequence['arr_spacing_position'].tolist()
                            #Data prep for tags
                            labels = arrival_label +  arrival_spacing_label
                            labels_y = main_data_position +  arrival_spacing_position
                            labels_x = main_arrival +  arrival_spacing

                            return{'0a': arrival_zero,
                                   '1' : main_arrival,
                                   '2' : main_arrival_error,
                                   '3' : arrival_spacing,
                                   '4' : arrival_spacing_error,
                                   '9' : main_data_position,
                                   '10' : arrival_spacing_position,
                                   '12' : labels,
                                   '13' : labels_y,
                                   '14' : labels_x}


                        def sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, number):
                            df_sequence = pd.DataFrame()
                            #Departure

                            df_sequence['DEPARTURES'] = df_dep_output['Departure_RWY_ENTRY'] + (df_dep_output['DROT']/2)
                            df_sequence['DEPARTURES_error'] = df_dep_output['DROT']/2
                            df_sequence['DEPARTURES_spacing'] = df_dep_output['Departure_RWY_ENTRY']
                            df_temp = pd.DataFrame()
                            df_temp['Dep MIN Separation'] = df_dep_output['Dep MIN Separation']
                            df_temp=df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['Departure_ZERO'] = 0
                            df_sequence['DEPARTURES_spacing_error'] = df_temp['Dep MIN Separation']
                            df_sequence['Departure_ZERO'] = df_temp['Departure_ZERO']

                            #Positions
                            df_sequence['main_position'] = number
                            df_sequence['dep_spacing_position'] = number-0.005

                            df_temp = pd.DataFrame()
                            df_temp['DEP_ID'] = df_dep_output['Departure ID'].astype(str)
                            df_temp['DEP_SID'] = df_dep_output['SID GROUP'].astype(str)
                            df_temp['DEP_WAKE'] = df_dep_output['WAKE'].astype(str)
                            df_temp['DEP_DELAY1'] = df_dep_output['DELAY DepSTANDqueue'] + df_dep_output['DELAY TAXIhold'] + df_dep_output['DELAY RWYqueue']
                            df_temp['DEP_DELAY'] = df_temp['DEP_DELAY1'].astype(str)
                            df_temp['DEPARTURE_LABEL'] = 'ID = ' + df_temp['DEP_ID'] + ' | SID = ' +df_temp['DEP_SID'] +' | WAKE = ' + df_temp['DEP_WAKE'] + ' | Delay = ' + df_temp['DEP_DELAY']

                            df_sequence['DEPARTURE_LABEL'] = df_temp['DEPARTURE_LABEL']

                            df_temp = pd.DataFrame()
                            df_temp['reason'] = df_dep_output['Dep MIN Separation Label']
                            df_temp = df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['value'] = df_sequence['DEPARTURES_spacing_error'].astype(str)
                            df_temp['DEPARTURES_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                            df_sequence['DEPARTURES_spacing_LABEL'] = df_temp['DEPARTURES_spacing_LABEL']

                            # LISTS to plot

                            #----DEPARTURES----#
                            main_departure = df_sequence['DEPARTURES'].tolist()
                            main_departure_error = df_sequence['DEPARTURES_error'].tolist()
                            departure_spacing = df_sequence['DEPARTURES_spacing'].tolist()
                            departure_spacing_error = df_sequence['DEPARTURES_spacing_error'].tolist()
                            departure_zero = df_sequence['Departure_ZERO']
                            #-Labels:
                            departure_label = df_sequence['DEPARTURE_LABEL'].tolist()
                            departure_spacing_label = df_sequence['DEPARTURES_spacing_LABEL'].tolist()

                            #-----POSITIONS------#
                            main_data_position = df_sequence['main_position'].tolist()
                            departure_spacing_position = df_sequence['dep_spacing_position'].tolist()

                            #Data prep for tags
                            labels = departure_label +  departure_spacing_label
                            labels_y = main_data_position + departure_spacing_position
                            labels_x = main_departure +  departure_spacing

                            return{'0b': departure_zero,
                                   '5' : main_departure,
                                   '6' : main_departure_error,
                                   '7' : departure_spacing,
                                   '8' : departure_spacing_error,
                                   '9' : main_data_position,
                                   '11' : departure_spacing_position,
                                   '12' : labels,
                                   '13' : labels_y,
                                   '14' : labels_x}


                        def sequence(df_arr_output, df_rwy_calcs, df_dep_output, number): ######MIX MODE

                            df_sequence = pd.DataFrame()
                            #Arrivals

                            df_sequence['ARRIVAL'] = df_arr_output['ACTUAL Landing Time'] + (df_arr_output['AROT']/2)
                            df_sequence['ARRIVAL_error'] = df_arr_output['AROT']/2
                            df_sequence['ARRIVAL_spacing'] = df_arr_output['ACTUAL Landing Time']
                            df_temp = pd.DataFrame()
                            df_temp['MAX Constraint'] = df_arr_output['MAX Constraint']
                            df_temp = df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['Arrival_ZERO'] = 0
                            df_sequence['ARRIVAL_spacing_error'] = df_temp['MAX Constraint']
                            df_sequence['Arrival_ZERO'] = df_temp['Arrival_ZERO']

                            #Departure

                            df_sequence['DEPARTURES'] = df_dep_output['Departure_RWY_ENTRY'] + (df_dep_output['DROT']/2)
                            df_sequence['DEPARTURES_error'] = df_dep_output['DROT']/2
                            df_sequence['DEPARTURES_spacing'] = df_dep_output['Departure_RWY_ENTRY']
                            df_temp = pd.DataFrame()
                            df_temp['Dep MIN Separation'] = df_dep_output['Dep MIN Separation']
                            df_temp=df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['Departure_ZERO'] = 0
                            df_sequence['DEPARTURES_spacing_error'] = df_temp['Dep MIN Separation']
                            df_sequence['Departure_ZERO'] = df_temp['Departure_ZERO']

                            #Positions
                            df_sequence['main_position'] = number
                            df_sequence['arr_spacing_position'] = number+0.005
                            df_sequence['dep_spacing_position'] = number-0.005

                            #Annotation

                            df_temp = pd.DataFrame()
                            df_temp['ARR_ID'] = df_arr_output['Arrival ID'].astype(str)
                            df_temp['ARR_WAKE'] = df_rwy_calcs['ARRIVAL actual WAKE'].astype(str)
                            df_temp['ARR_DELAY'] = df_arr_output['Arrival DELAY'].astype(str)
                            df_temp['ARRIVAL_LABEL'] = 'ID = ' + df_temp['ARR_ID'] + ' | WAKE = ' + df_temp['ARR_WAKE'] + ' | Delay = ' + df_temp['ARR_DELAY']

                            df_sequence['ARRIVAL_LABEL'] = df_temp['ARRIVAL_LABEL']

                            df_temp = pd.DataFrame()
                            df_temp['DEP_ID'] = df_dep_output['Departure ID'].astype(str)
                            df_temp['DEP_SID'] = df_dep_output['SID GROUP'].astype(str)
                            df_temp['DEP_WAKE'] = df_dep_output['WAKE'].astype(str)
                            df_temp['DEP_DELAY1'] = df_dep_output['DELAY DepSTANDqueue'] + df_dep_output['DELAY TAXIhold'] + df_dep_output['DELAY RWYqueue']
                            df_temp['DEP_DELAY'] = df_temp['DEP_DELAY1'].astype(str)
                            df_temp['DEPARTURE_LABEL'] = 'ID = ' + df_temp['DEP_ID'] + ' | SID = ' +df_temp['DEP_SID'] +' | WAKE = ' + df_temp['DEP_WAKE'] + ' | Delay = ' + df_temp['DEP_DELAY']

                            df_sequence['DEPARTURE_LABEL'] = df_temp['DEPARTURE_LABEL']

                            df_temp = pd.DataFrame()
                            df_temp['reason'] = df_arr_output['MAX Constraint Label']
                            df_temp = df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['value'] = df_sequence['ARRIVAL_spacing_error'].astype(str)
                            df_temp['ARRIVAL_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                            df_sequence['ARRIVAL_spacing_LABEL'] = df_temp['ARRIVAL_spacing_LABEL']

                            df_temp = pd.DataFrame()
                            df_temp['reason'] = df_dep_output['Dep MIN Separation Label']
                            df_temp = df_temp.drop([0])
                            df_temp = df_temp.reset_index()
                            df_temp = df_temp.drop(columns=['index'])
                            df_temp['value'] = df_sequence['DEPARTURES_spacing_error'].astype(str)
                            df_temp['DEPARTURES_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                            df_sequence['DEPARTURES_spacing_LABEL'] = df_temp['DEPARTURES_spacing_LABEL']

                            # LISTS to plot

                            #----ARRIVALS----#
                            main_arrival = df_sequence['ARRIVAL'].tolist()
                            main_arrival_error = df_sequence['ARRIVAL_error'].tolist()
                            arrival_spacing = df_sequence['ARRIVAL_spacing'].tolist()
                            arrival_spacing_error = df_sequence['ARRIVAL_spacing_error'].tolist()
                            arrival_zero = df_sequence['Arrival_ZERO'].tolist()
                            #-Labels:
                            arrival_label = df_sequence['ARRIVAL_LABEL'].tolist()
                            arrival_spacing_label = df_sequence['ARRIVAL_spacing_LABEL'].tolist()

                            #----DEPARTURES----#
                            main_departure = df_sequence['DEPARTURES'].tolist()
                            main_departure_error = df_sequence['DEPARTURES_error'].tolist()
                            departure_spacing = df_sequence['DEPARTURES_spacing'].tolist()
                            departure_spacing_error = df_sequence['DEPARTURES_spacing_error'].tolist()
                            departure_zero = df_sequence['Departure_ZERO']
                            #-Labels:
                            departure_label = df_sequence['DEPARTURE_LABEL'].tolist()
                            departure_spacing_label = df_sequence['DEPARTURES_spacing_LABEL'].tolist()

                            #-----POSITIONS------#
                            main_data_position = df_sequence['main_position'].tolist()
                            arrival_spacing_position = df_sequence['arr_spacing_position'].tolist()
                            departure_spacing_position = df_sequence['dep_spacing_position'].tolist()

                            #Data prep for tags
                            labels = arrival_label + departure_label + arrival_spacing_label  + departure_spacing_label
                            labels_y = main_data_position + main_data_position + arrival_spacing_position + departure_spacing_position
                            labels_x = main_arrival + main_departure + arrival_spacing + departure_spacing

                            return{'0a': arrival_zero,
                                   '0b': departure_zero,
                                   '1' : main_arrival,
                                   '2' : main_arrival_error,
                                   '3' : arrival_spacing,
                                   '4' : arrival_spacing_error,
                                   '5' : main_departure,
                                   '6' : main_departure_error,
                                   '7' : departure_spacing,
                                   '8' : departure_spacing_error,
                                   '9' : main_data_position,
                                   '10' : arrival_spacing_position,
                                   '11' : departure_spacing_position,
                                   '12' : labels,
                                   '13' : labels_y,
                                   '14' : labels_x}


                        #------ ARRIVALS only -------#

                        if df_dep_output.empty ==True:

                            if df_dep_output2.empty ==True:#arr only
                                if m2==1: # two arr only comparison
                                    f = Figure(figsize=(5,5), dpi=100)
                                    A = f.add_subplot(111)
                                    ax = f.add_subplot(111)

                                    labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                    tag_text_use = np.array(list(labels))
                                    labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                    labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                    #plt.axhline(y = 10, color='w')
                                    #A.axhline(y=0.5, color='w')

                                    A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                    bbox=dict(boxstyle="round", fc="w"),
                                                    arrowprops=dict(arrowstyle="->"))
                                    annot.set_visible(False)

                                    def update_annot(ind):

                                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                        annot.xy = pos
                                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                        annot.set_text(text)


                                    def hover(event):
                                        vis = annot.get_visible()
                                        if event.inaxes == ax:
                                            cont, ind = tags_main_data.contains(event)
                                            if cont:
                                                update_annot(ind)
                                                annot.set_visible(True)
                                                canvas.draw_idle()
                                            else:
                                                if vis:
                                                    annot.set_visible(False)
                                                    canvas.draw_idle()


                                    A.set_xlabel('Seconds of the day')
                                    A.axes.get_yaxis().set_visible(False)
                                    A.grid(color='b', linestyle='-', linewidth=0.1)
                                    A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Arrivals M2", "Arrivals Spacing M2"), loc = 'upper right')
                                    #plt.title("Sequence analysis")
                                    canvas = FigureCanvasTkAgg(f, self)
                                    canvas.draw()
                                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                    canvas.mpl_connect("motion_notify_event", hover)
                                    toolbar = NavigationToolbar2Tk(canvas, self)
                                    toolbar.update()
                                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                                elif m2==2: # 3 ARRonly comparison
                                    f = Figure(figsize=(5,5), dpi=100)
                                    A = f.add_subplot(111)
                                    ax = f.add_subplot(111)

                                    labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12']
                                    tag_text_use = np.array(list(labels))
                                    labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13']
                                    labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] + sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14']

                                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                    #plt.axhline(y = 10, color='w')
                                    #A.axhline(y=0.5, color='w')

                                    A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='salmon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='orchid', fmt='o', markersize=8, capsize=10, )

                                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                    bbox=dict(boxstyle="round", fc="w"),
                                                    arrowprops=dict(arrowstyle="->"))
                                    annot.set_visible(False)

                                    def update_annot(ind):

                                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                        annot.xy = pos
                                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                        annot.set_text(text)


                                    def hover(event):
                                        vis = annot.get_visible()
                                        if event.inaxes == ax:
                                            cont, ind = tags_main_data.contains(event)
                                            if cont:
                                                update_annot(ind)
                                                annot.set_visible(True)
                                                canvas.draw_idle()
                                            else:
                                                if vis:
                                                    annot.set_visible(False)
                                                    canvas.draw_idle()


                                    A.set_xlabel('Seconds of the day')
                                    A.axes.get_yaxis().set_visible(False)
                                    A.grid(color='b', linestyle='-', linewidth=0.1)
                                    A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Arrivals M2", "Arrivals Spacing M2","Arrivals M3", "Arrivals Spacing M3"), loc = 'upper right')
                                    #plt.title("Sequence analysis")
                                    canvas = FigureCanvasTkAgg(f, self)
                                    canvas.draw()
                                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                    canvas.mpl_connect("motion_notify_event", hover)
                                    toolbar = NavigationToolbar2Tk(canvas, self)
                                    toolbar.update()
                                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                                    #f.canvas.figure.savefig('sequence.png')

                            elif df_arr_output2.empty ==True: # ARR only + DEP only
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['4'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['5'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['6']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['8'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['11'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['9']], color='purple', fmt='o', markersize=8, capsize=10)

                                A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], fmt='o', markersize=8, capsize=10)

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot(ind):

                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)


                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Departures M2", "Departures Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                            else:#ARR only + MIXED
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot2(ind):
                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)


                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot2(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                        #-------DEPARTURES only --------#

                        elif df_arr_output.empty ==True:

                            if df_dep_output2.empty ==True: # DEPonly + ARRonly
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']+ sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_x = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                                labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                                A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot(ind):

                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)


                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Departures M1","Departures Spacing M1","Arrivals M2", "Arrivals Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                            elif df_arr_output2.empty ==True: # DEPonly + DEPonly
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                labels_x = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                                A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='indigo',fmt = 'o', markersize=8, capsize=10)

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot(ind):

                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)


                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Departures M1","Departures Spacing M1","Departures M2", "Departures Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                            else: # DEPonly + MIXED
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequenceDepOnly(df_dep_output, 1)['3'], sequenceDepOnly(df_dep_output, 1)['4'], xerr=[sequenceDepOnly(df_dep_output, 1)['5'], sequenceDepOnly(df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequenceDepOnly(df_dep_output, 1)['10'], sequenceDepOnly(df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_dep_output, 1)['11'], sequenceDepOnly(df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['15']], color='navy', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['18'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['19'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['17'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['16']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot2(ind):
                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)

                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot2(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Departures M1","Departures Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                        #------------------ MIXED MODE ------------------------#

                        else:

                            if (df_dep_output2.empty ==False) and (df_arr_output2.empty ==False): #mixed both
                                if m2==2: #MIXED +MIXED + MIXED

                                    f = Figure(figsize=(5,5), dpi=100)
                                    A = f.add_subplot(111)
                                    ax = f.add_subplot(111)

                                    labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12']
                                    tag_text_use = np.array(list(labels))
                                    labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14']
                                    labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13']
                                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                    #plt.axhline(y = 10, color='w')
                                    ##A.axhline(y=0.5, color='w')

                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['5'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6']], color='limegreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='orangered', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['7'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['11'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0b'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['8']], color='royalblue',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='magenta', fmt='o', markersize=8, capsize=10, )

                                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                    bbox=dict(boxstyle="round", fc="w"),
                                                    arrowprops=dict(arrowstyle="->"))
                                    annot.set_visible(False)
                                    def update_annot2(ind):
                                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                        annot.xy = pos
                                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                        annot.set_text(text)

                                    def hover(event):
                                        vis = annot.get_visible()
                                        if event.inaxes == ax:
                                            cont, ind = tags_main_data.contains(event)
                                            if cont:
                                                update_annot2(ind)
                                                annot.set_visible(True)
                                                canvas.draw_idle()
                                            else:
                                                if vis:
                                                    annot.set_visible(False)
                                                    canvas.draw_idle()


                                    A.set_xlabel('Seconds of the day')
                                    A.axes.get_yaxis().set_visible(False)
                                    A.grid(color='b', linestyle='-', linewidth=0.1)
                                    A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2", "Departures M3","Arrivals M3","Departures Spacing M3","Arrivals Spacing M3"), loc = 'upper right')
                                    #plt.title("Sequence analysis")
                                    canvas = FigureCanvasTkAgg(f, self)
                                    canvas.draw()
                                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                    canvas.mpl_connect("motion_notify_event", hover)
                                    toolbar = NavigationToolbar2Tk(canvas, self)
                                    toolbar.update()
                                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                                    #f.canvas.figure.savefig('sequence.png')

                                elif m2==3:#MIXED +MIXED + MIXED + MIXED

                                    f = Figure(figsize=(5,5), dpi=100)
                                    A = f.add_subplot(111)
                                    ax = f.add_subplot(111)

                                    labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['12']
                                    tag_text_use = np.array(list(labels))
                                    labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['14']
                                    labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['13']
                                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                    #plt.axhline(y = 10, color='w')
                                    #A.axhline(y=0.5, color='w')

                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['5'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6']], color='limegreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='orangered', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['7'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['11'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0b'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['8']], color='royalblue',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='magenta', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['5'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6']], color='lime', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['1'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2']], color='salmon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['7'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['11'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0b'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['8']], color='cyan',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['3'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['10'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0a'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['4']], color='orchid', fmt='o', markersize=8, capsize=10, )

                                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                    bbox=dict(boxstyle="round", fc="w"),
                                                    arrowprops=dict(arrowstyle="->"))
                                    annot.set_visible(False)
                                    def update_annot2(ind):
                                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                        annot.xy = pos
                                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                        annot.set_text(text)

                                    def hover(event):
                                        vis = annot.get_visible()
                                        if event.inaxes == ax:
                                            cont, ind = tags_main_data.contains(event)
                                            if cont:
                                                update_annot2(ind)
                                                annot.set_visible(True)
                                                canvas.draw_idle()
                                            else:
                                                if vis:
                                                    annot.set_visible(False)
                                                    canvas.draw_idle()

                                    A.set_xlabel('Seconds of the day')
                                    A.axes.get_yaxis().set_visible(False)
                                    A.grid(color='b', linestyle='-', linewidth=0.1)
                                    A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2", "Departures M3","Arrivals M3","Departures Spacing M3","Arrivals Spacing M3", "Departures M4","Arrivals M4","Departures Spacing M4","Arrivals Spacing M4"), loc = 'upper right')
                                    #plt.title("Sequence analysis")
                                    canvas = FigureCanvasTkAgg(f, self)
                                    canvas.draw()
                                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                    canvas.mpl_connect("motion_notify_event", hover)
                                    toolbar = NavigationToolbar2Tk(canvas, self)
                                    toolbar.update()
                                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                                    #f.canvas.figure.savefig('sequence.png')
                                elif m2==4: #MIXED +MIXED + MIXED +MIXED + MIXED

                                    f = Figure(figsize=(5,5), dpi=100)
                                    A = f.add_subplot(111)
                                    ax = f.add_subplot(111)

                                    labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['12'] + sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['12']
                                    tag_text_use = np.array(list(labels))
                                    labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['14'] + sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['14']
                                    labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['13'] + sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['13']
                                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                    #plt.axhline(y = 10, color='w')
                                    #A.axhline(y=0.5, color='w')

                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['5'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6']], color='limegreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='orangered', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['7'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['11'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0b'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['8']], color='royalblue',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='magenta', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['5'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6']], color='lime', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['1'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2']], color='salmon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['7'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['11'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0b'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['8']], color='cyan',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['3'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['10'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0a'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['4']], color='orchid', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['5'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['9'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['6'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['6']], color='olive', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['1'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['9'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['2'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['2']], color='firebrick', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['7'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['11'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['0b'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['8']], color='mediumblue',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['3'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['10'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['0a'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['4']], color='deeppink', fmt='o', markersize=8, capsize=10, )

                                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                    bbox=dict(boxstyle="round", fc="w"),
                                                    arrowprops=dict(arrowstyle="->"))
                                    annot.set_visible(False)

                                    def update_annot2(ind):
                                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                        annot.xy = pos
                                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                        annot.set_text(text)

                                    def hover(event):
                                        vis = annot.get_visible()
                                        if event.inaxes == ax:
                                            cont, ind = tags_main_data.contains(event)
                                            if cont:
                                                update_annot2(ind)
                                                annot.set_visible(True)
                                                canvas.draw_idle()
                                            else:
                                                if vis:
                                                    annot.set_visible(False)
                                                    canvas.draw_idle()


                                    A.set_xlabel('Seconds of the day')
                                    A.axes.get_yaxis().set_visible(False)
                                    A.grid(color='b', linestyle='-', linewidth=0.1)
                                    A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2", "Departures M3","Arrivals M3","Departures Spacing M3","Arrivals Spacing M3", "Departures M4","Arrivals M4","Departures Spacing M4","Arrivals Spacing M4"), loc = 'upper right')
                                    #plt.title("Sequence analysis")
                                    canvas = FigureCanvasTkAgg(f, self)
                                    canvas.draw()
                                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                    canvas.mpl_connect("motion_notify_event", hover)
                                    toolbar = NavigationToolbar2Tk(canvas, self)
                                    toolbar.update()
                                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                                    #f.canvas.figure.savefig('sequence.png')

                                else: # only 2 to compare

                                    f = Figure(figsize=(5,5), dpi=100)
                                    A = f.add_subplot(111)
                                    ax = f.add_subplot(111)

                                    labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                    tag_text_use = np.array(list(labels))
                                    labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                                    labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                    #plt.axhline(y = 10, color='w')
                                    ##A.axhline(y=0.5, color='w')

                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                                    A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                    bbox=dict(boxstyle="round", fc="w"),
                                                    arrowprops=dict(arrowstyle="->"))
                                    annot.set_visible(False)

                                    def update_annot2(ind):
                                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                        annot.xy = pos
                                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                        annot.set_text(text)


                                    def hover(event):
                                        vis = annot.get_visible()
                                        if event.inaxes == ax:
                                            cont, ind = tags_main_data.contains(event)
                                            if cont:
                                                update_annot2(ind)
                                                annot.set_visible(True)
                                                canvas.draw_idle()
                                            else:
                                                if vis:
                                                    annot.set_visible(False)
                                                    canvas.draw_idle()


                                    A.set_xlabel('Seconds of the day')
                                    A.axes.get_yaxis().set_visible(False)
                                    A.grid(color='b', linestyle='-', linewidth=0.1)
                                    A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2"), loc = 'upper right')
                                    #plt.title("Sequence analysis")
                                    canvas = FigureCanvasTkAgg(f, self)
                                    canvas.draw()
                                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                    canvas.mpl_connect("motion_notify_event", hover)
                                    toolbar = NavigationToolbar2Tk(canvas, self)
                                    toolbar.update()
                                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                            elif df_dep_output2.empty ==True:#arr only
                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                                labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #plt.axhline(y = 10, color='w')
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot2(ind):
                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)


                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot2(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Arrivals M2", "Arrivals Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                            elif df_arr_output2.empty ==True: # MIXED + ARRonly

                                f = Figure(figsize=(5,5), dpi=100)
                                A = f.add_subplot(111)
                                ax = f.add_subplot(111)

                                #plt.axhline(y = 10, color='w')

                                labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                                tag_text_use = np.array(list(labels))
                                labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                                labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                                tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                                #plt.axhline(y = 10, color='w')
                                #A.axhline(y=0.5, color='w')

                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                                A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='g', fmt='o', markersize=8, capsize=10)
                                A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], fmt='o', markersize=8, capsize=10)

                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                                bbox=dict(boxstyle="round", fc="w"),
                                                arrowprops=dict(arrowstyle="->"))
                                annot.set_visible(False)

                                def update_annot2(ind):
                                    pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                    annot.xy = pos
                                    text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                    annot.set_text(text)

                                def hover(event):
                                    vis = annot.get_visible()
                                    if event.inaxes == ax:
                                        cont, ind = tags_main_data.contains(event)
                                        if cont:
                                            update_annot2(ind)
                                            annot.set_visible(True)
                                            canvas.draw_idle()
                                        else:
                                            if vis:
                                                annot.set_visible(False)
                                                canvas.draw_idle()


                                A.set_xlabel('Seconds of the day')
                                A.axes.get_yaxis().set_visible(False)
                                A.grid(color='b', linestyle='-', linewidth=0.1)
                                A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2", "Departures Spacing M2"), loc = 'upper right')
                                #plt.title("Sequence analysis")
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                canvas.mpl_connect("motion_notify_event", hover)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                # ============================================================================#
                #                           ADA buffer                                        #
                # ============================================================================#

                class ADAbuffer2(tk.Frame):

                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)
                        label = tk.Label(self, text="SEQUENCE")
                        label.pack(pady=10,padx=10)

                        button1 = ttk.Button(self, text="Back to Home",
                                            command=lambda: controller.show_frame(StartPage2))
                        button1.pack()
                        if convergenceFLAG ==True:
                            button1 = ttk.Button(self, text="Convergence Throughput",
                                                command=lambda: controller.show_frame(Conv2))
                            button1.pack()
                        if Thr_FLAG == True:
                            button = ttk.Button(self, text="Throughput",
                                                command=lambda: controller.show_frame(Thr2))
                            button.pack()

                        if Delay_FLAG == True:
                            button2 = ttk.Button(self, text="RWY Hold Delay",
                                                command=lambda: controller.show_frame(DepDelay22))
                            button2.pack()
                        if Delay_FLAG == True:
                            button5 = ttk.Button(self, text="Push/Start Delay",
                                                command=lambda: controller.show_frame(DepDelay222))
                            button5.pack()

                        if arr_delay_FLAG == True:
                            button3 = ttk.Button(self, text="Arrivals Delay",
                                                command=lambda: controller.show_frame(ArrivalDelay2))
                            button3.pack()

                        df_Buffer = pd.DataFrame()
                        df_Buffer['ADA_Buffer'] = df_sequence_output['ADA Buffer']
                        df_Buffer = df_Buffer.dropna(subset = ['ADA_Buffer'])
                        #df_Buffer = df_Buffer.drop([0])
                        ADA_buffer = df_Buffer['ADA_Buffer'].tolist()
                        a = int(min(ADA_buffer))
                        b = int(max(ADA_buffer))
                        number_bins = b-a
                        h = [0]+sorted(ADA_buffer)

                        coord = [[0,0], [15,0], [15,0.013], [0,0.013]]
                        coord.append(coord[0]) #repeat the first point to create a 'closed loop'

                        xs, ys = zip(*coord) #create lists of x and y values

                        fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        A.plot(h,fit,'-o')
                        A.hist(h,normed=True,bins=number_bins)

                        A.plot(xs,ys,"r")

                        A.set_xlabel('SECONDS')
                        A.set_ylabel('%')
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        #A.title('Throughput')
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


                app2 = RAPIDvisual2()

                app2.columnconfigure(0, weight=1)
                app2.rowconfigure(0, weight=1)
                app2.rowconfigure(1, weight=1)

                app2.mainloop()


            m2_input = tk.IntVar(self, value='0')
            m2_output = tk.IntVar()
            entry4 = ttk.Entry(self, width=7, textvariable=m2_input)
            entry4.pack()

            button6 = tk.Button(self, text="SHOW", command=show_button)
            button6.pack()


    # ============================================================================#
    #                           CONVERGENCE                                       #
    # ============================================================================#

    #if convergenceFLAG ==True:
    class Conv(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="THROUGHPUT CONVERGENCE")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()

            if Thr_FLAG == True:
                button = ttk.Button(self, text="Throughput",
                                    command=lambda: controller.show_frame(Thr))
                button.pack()

            if Delay_FLAG == True:
                button2 = ttk.Button(self, text="RWY Hold Delay",
                                    command=lambda: controller.show_frame(DepDelay))
                button2.pack()

            if Delay_FLAG == True:
                button5 = ttk.Button(self, text="Push/Start Delay",
                                    command=lambda: controller.show_frame(DepDelay2))
                button5.pack()

            if arr_delay_FLAG == True:
                button3 = ttk.Button(self, text="Arrivals Delay",
                                    command=lambda: controller.show_frame(ArrivalDelay))
                button3.pack()

            if Seq_FLAG == True:
                button4 = ttk.Button(self, text="Sequence",
                                    command=lambda: controller.show_frame(Seq))
                button4.pack()

            if ADA_buffer_FLAG == True:
                button5 = ttk.Button(self, text="ADA Buffer",
                                    command=lambda: controller.show_frame(ADAbuffer))
                button5.pack()

            thr_av_diff = pd.DataFrame(df_thr['Difference in thr averages'])
            thr_av_diff=thr_av_diff.dropna(subset=['Difference in thr averages'])

            thr_av_diff['Tags'] = thr_av_diff['Difference in thr averages'].apply(lambda x: json.loads(x))
            thr_av_difference = thr_av_diff['Tags'].tolist()

            print(len(thr_av_difference[0][0]))
            print(len(thr_av_difference[0]))
            thr_abc=[]
            total_runs =[]
            runs_Thr = []
            for i in range (1,(len(thr_av_difference[0])+1)):
                runs_Thr.append(i)

            f = Figure(figsize=(5,5), dpi=100)
            A = f.add_subplot(111)

            for j in range (0, len(thr_av_difference[0][0])):
                for i in range (0, len(thr_av_difference[0])):
                    total_thr = thr_av_difference[0][i][j]
                    runs_Thrx = runs_Thr[i]
                    total_runs.append(runs_Thrx)
                    thr_abc.append(total_thr)
                A.plot(total_runs,thr_abc)
                thr_abc = []
                total_runs =[]

            A.set_xlabel('No. of Runs')
            A.set_ylabel('Difference in average throughput per hour')
            A.grid(color='b', linestyle='-', linewidth=0.1)
            #A.title('Throughput')
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # ============================================================================#
    #                          THROUGHPUT                                         #
    # ============================================================================#

    #if Thr_FLAG == True:
    class Thr(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="THROUGHPUT")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()

            if convergenceFLAG ==True:
                button1 = ttk.Button(self, text="Convergence Throughput",
                                    command=lambda: controller.show_frame(Conv))
                button1.pack()

            if Delay_FLAG == True:
                button2 = ttk.Button(self, text="RWY Hold Delay",
                                    command=lambda: controller.show_frame(DepDelay))
                button2.pack()

                button5 = ttk.Button(self, text="Push/Start Delay",
                                    command=lambda: controller.show_frame(DepDelay2))
                button5.pack()

            if arr_delay_FLAG == True:
                button3 = ttk.Button(self, text="Arrivals Delay",
                                    command=lambda: controller.show_frame(ArrivalDelay))
                button3.pack()

            if Seq_FLAG == True:
                button4 = ttk.Button(self, text="Sequence",
                                    command=lambda: controller.show_frame(Seq))
                button4.pack()

            if ADA_buffer_FLAG == True:
                button5 = ttk.Button(self, text="ADA Buffer",
                                    command=lambda: controller.show_frame(ADAbuffer))
                button5.pack()

            def create_first_df_thr():
                df_thr_to_plot = pd.DataFrame()
                df_thr_to_plot['Hour'] = df_thr['Hour']
                x = 'Hour'
                df_thr_to_plot['RUN 1'] = df_thr['Total Throughput']
                y = 'RUN 1'

                df_thr_to_plot2 = df_thr_to_plot[[x,y]].groupby(x).sum()

                return df_thr_to_plot2


            def create_multiple_df_thr(df_thr_to_plot2, df_thr_input, name):
                df_thr_to_plot2[name] = df_thr_input['Total Throughput']
                df_thr_to_plot_temp = pd.DataFrame()
                df_thr_to_plot_temp['Hour'] = df_thr_input['Hour']
                a = 'Hour'
                df_thr_to_plot_temp[name] = df_thr_input['Total Throughput']
                b = name
                df_thr_to_plot_temp = df_thr_to_plot_temp.dropna(subset=['Hour'])
                df_thr_to_plot_temp2 = df_thr_to_plot_temp[[a,b]].groupby(a).sum()

                df_thr_to_plot2[name] = df_thr_to_plot_temp2[name]


                return df_thr_to_plot2


            # def add_operational_data ():
            #     #df_thr_to_plot2['Operational Data'] = op_data['Total Throughput']
            #     df_thr_to_plot_temp = pd.DataFrame()
            #     df_thr_to_plot_temp['Hour'] = op_data['Hour']
            #     a = 'Hour'
            #     df_thr_to_plot_temp['Operational Data'] = op_data['Total Throughput']
            #     b = 'Operational Data'
            #     df_thr_to_plot_temp = df_thr_to_plot_temp.dropna(subset=['Hour'])

            #     df_thr_to_plot_temp2 = df_thr_to_plot_temp[[a,b]].groupby(a).sum()

            #     df_thr_to_plot2['Operational Data'] = df_thr_to_plot_temp2['Operational Data']


            def plot_bar_thr(df_thr_to_plot2, A):
                df_thr_to_plot2.plot(kind='bar', legend=False, ax=A)


            def total_thr(df_thr_input):
                total_thr = df_thr_input['Total Throughput']
                total_thr = total_thr.reset_index()
                return(total_thr)


            def hour_thr(df_thr_input):
                hour_Thr = df_thr_input['Hour'].tolist()
                return(hour_Thr)


            if new_set_FLAG == True:
                if m>= 1:
                    f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    # throughput(df_thr, 'k')
                    # throughput(df_thr2, 'g')
                    df_thr_to_plot2 = create_first_df_thr()
                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr2, 'RUN 2')

                    if (m == 1) and (average_FLAG == True):
                        a=total_thr(df_thr)
                        b=total_thr(df_thr2)
                        average = pd.DataFrame()
                        average = (a+b)/2
                        average_thr = average['Total Throughput'].tolist()
                        A.plot(hour_thr(df_thr),average_thr, linewidth=3.0, color = 'red', linestyle='dashed', alpha = 0.5)

                    if OP_FLAG == True:
                        df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                        A.legend(('Model','Operational Data', 'Model 2'), loc = 'upper right')
                    else:
                        A.legend(('Model', 'Model 2'), loc = 'upper right')
                    if m>= 2:
                        df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr3, 'RUN 3')
                        # throughput(df_thr3, 'c')
                        if (m==2) and (average_FLAG ==True):
                            a=total_thr(df_thr)
                            b=total_thr(df_thr2)
                            c=total_thr(df_thr3)
                            average = pd.DataFrame()
                            average = (a+b+c)/3
                            average_thr = average['Total Throughput'].tolist()
                            A.plot(hour_thr(df_thr),average_thr, linewidth=3.0, color = 'red', linestyle='dashed', alpha = 0.5)

                        if OP_FLAG ==True:
                            df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                            A.legend(('Model','Operational Data', 'Model 2', 'Model 3'), loc = 'upper right')
                        else:
                            A.legend(('Model','Model 2', 'Model 3'), loc = 'upper right')
                        if m>=3:
                            # throughput(df_thr4, 'm')
                            df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr4, 'RUN 4')
                            if (m==3) and (average_FLAG ==True):
                                a=total_thr(df_thr)
                                b=total_thr(df_thr2)
                                c=total_thr(df_thr3)
                                d=total_thr(df_thr4)
                                average = pd.DataFrame()
                                average = (a+b+c+d)/4
                                average_thr = average['Total Throughput'].tolist()
                                A.plot(hour_thr(df_thr),average_thr, linewidth=3.0, color = 'red',linestyle='dashed', alpha = 0.5)

                            if OP_FLAG ==True:
                                df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                            else:
                                A.legend(('Model','Model 2', 'Model 3','Model 4'), loc = 'upper right')
                            if m>=4:
                                # throughput(df_thr5, 'y')
                                df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr5, 'RUN 5')
                                if (m==4) and (average_FLAG ==True):
                                    a=total_thr(df_thr)
                                    b=total_thr(df_thr2)
                                    c=total_thr(df_thr3)
                                    d=total_thr(df_thr4)
                                    e=total_thr(df_thr5)
                                    average = pd.DataFrame()
                                    average = (a+b+c+d+e)/5
                                    average_thr = average['Total Throughput'].tolist()
                                    A.plot(hour_thr(df_thr),average_thr, linewidth=3.0, color = 'red', linestyle='dashed', alpha = 0.5)

                                if OP_FLAG ==True:
                                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                    A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                else:
                                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                    A.legend(('Model','Model 2', 'Model 3','Model 4', 'Model 5'), loc = 'upper right')
                                if m>=5:
                                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, df_thr6, 'RUN 6')
                                    #throughput(df_thr6, color = 'purple')
                                    if (m==5) and (average_FLAG ==True):
                                        a=total_thr(df_thr)
                                        b=total_thr(df_thr2)
                                        c=total_thr(df_thr3)
                                        d=total_thr(df_thr4)
                                        e=total_thr(df_thr5)
                                        f=total_thr(df_thr6)
                                        average = pd.DataFrame()
                                        average = (a+b+c+d+e+f)/6
                                        average_thr = average['Total Throughput'].tolist()
                                        A.plot(hour_thr(df_thr),average_thr, linewidth=3.0, color = 'red',linestyle='dashed',  alpha = 0.5)

                                    if OP_FLAG ==True:
                                        df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                                        A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                    else:
                                        A.legend(('Model','Model 2', 'Model 3','Model 4','Model 5','Model 6'), loc = 'upper right')
                    plot_bar_thr(df_thr_to_plot2, A)
                    if OP_FLAG ==True:
                        df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')
                        A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                    A.set_xlabel('Hours of the day')
                    A.set_ylabel('No of A/C')
                    A.grid(color='b', linestyle='-', linewidth=0.1)
                    # A.title('Throughput')
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            else:
                f = Figure(figsize=(5,5), dpi=100)
                A = f.add_subplot(111)
                # df_thr_to_plot2 = throughput2(df_thr)
                df_thr_to_plot2 = create_first_df_thr()

                # df_thr_to_plot2.plot(kind='bar', legend=False, ax=A)

                if OP_FLAG == True:
                    df_thr_to_plot2 = create_multiple_df_thr(df_thr_to_plot2, op_data, 'OPERATIONA_DATA')

                plot_bar_thr(df_thr_to_plot2, A)
                A.set_xlabel('Hours of the day')
                A.set_ylabel('No of A/C')
                A.grid(color='b', linestyle='-', linewidth=0.1)
                # A.title('Throughput')
                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                toolbar = NavigationToolbar2Tk(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # ============================================================================#
    #                         DEPARTURE DELAY - RWY hold delay                    #
    # ============================================================================#

    # if Delay_FLAG == True:
    class DepDelay(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="RWY HOLD DELAY")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()

            if convergenceFLAG ==True:
                button1 = ttk.Button(self, text="Convergence Throughput",
                                    command=lambda: controller.show_frame(Conv))
                button1.pack()

            if Thr_FLAG == True:
                button = ttk.Button(self, text="Throughput",
                                    command=lambda: controller.show_frame(Thr))
                button.pack()

            if Delay_FLAG == True:
                button5 = ttk.Button(self, text="Push/Start Delay",
                                    command=lambda: controller.show_frame(DepDelay2))
                button5.pack()

            if arr_delay_FLAG == True:
                button3 = ttk.Button(self, text="Arrivals Delay",
                                    command=lambda: controller.show_frame(ArrivalDelay))
                button3.pack()

            if Seq_FLAG == True:
                button4 = ttk.Button(self, text="Sequence",
                                    command=lambda: controller.show_frame(Seq))
                button4.pack()

            if ADA_buffer_FLAG == True:
                button5 = ttk.Button(self, text="ADA Buffer",
                                    command=lambda: controller.show_frame(ADAbuffer))
                button5.pack()

            if (df_delay.empty == True):
                print("No departures. Nothing to show")
            else:
                def delay(df_delay,df_dep_output):

                    interval15=[]
                    df_ps_delay = pd.DataFrame()
                    # Add arrival delay values
                    df_ps_delay['RWYhold_Delay'] = df_delay['RWY HOLD Delay']
                    # print when those values occure
                    df_ps_delay['Time1'] = df_dep_output['Departure_RWY_ENTRY']
                    # round each time value to 15 minutes
                    df_ps_delay= df_ps_delay.dropna(subset=['Time1'])
                    time1_list = df_ps_delay['Time1'].tolist()
                    #a=[]
                    for a in time1_list:
                        b = int(int(a/900)*900)
                        interval15.append(b)

                    df_ps_delay['interval15'] = interval15
                    df_ps_delay = df_ps_delay.drop(columns=['Time1'])
                    #Group data by the time interval, if there are multiple values for the same time interval, take the mean.
                    df_ps_delay = df_ps_delay.groupby(['interval15'])['RWYhold_Delay'].mean()
                    #make the rolling average
                    df_ps_delay = df_ps_delay.reset_index()
                    df_ps_delay2 = df_ps_delay.rolling(window=4, on='interval15')['RWYhold_Delay'].mean()
                    RWYhold_Delay = df_ps_delay2.tolist()
                    df_ps_delay['DATE'] = pd.to_datetime(df_ps_delay['interval15'],unit='s')
                    df_ps_delay['DATE'] = df_ps_delay['DATE'].apply(lambda x: x.time())

                    time_interval = df_ps_delay['DATE']

                    # df_delay_input['Time interval'] = pd.DatetimeIndex(df_delay_input['Time interval'])
                    # #For RWY_Hold Delay
                    # df_rwy = df_delay_input
                    # df_rwy = df_rwy.groupby(['Time interval'])['RWY_Hold Delay'].mean()
                    # df_rwy = df_rwy.reset_index()
                    # df_rwy_avg = df_rwy.rolling(window='3600s', on='Time interval')['RWY_Hold Delay'].mean()
                    # df_rwy_avg = df_rwy_avg.reset_index()
                    # df_rwy = df_rwy.reset_index()
                    # df_rwy = df_rwy.drop(columns=['RWY_Hold Delay'])

                    # df_final_rwy = pd.merge(df_rwy, df_rwy_avg,  how='left', on=['index'], copy=True)
                    # df_final_rwy = df_final_rwy.drop(columns=['index'])
                    # df_final_rwy['Time interval'] = pd.to_timedelta(df_final_rwy['Time interval']) # convert to timedelta to calculate seconds
                    # df_final_rwy['Time interval'] = df_final_rwy['Time interval'].dt.seconds

                    # #For Push/Start Delay
                    # df_ps = df_delay_input
                    # df_ps = df_ps.groupby(['Time interval'])['Push/Start Delay'].mean()
                    # df_ps = df_ps.reset_index()
                    # dh_ps_avg = df_ps.rolling(window='3600s', on='Time interval')['Push/Start Delay'].mean()
                    # dh_ps_avg = dh_ps_avg.reset_index()
                    # df_ps = df_ps.reset_index()
                    # df_ps = df_ps.drop(columns=['Push/Start Delay'])
                    # #df_ps['Time interval'] = df_ps['Time interval'].apply(lambda x: x.time())
                    # #df_rwy_arr['Arr Time Interval'] = df_rwy_arr['Arr Time Interval'].apply(lambda x: x.time())

                    # df_final_ps = pd.merge(df_ps, dh_ps_avg,  how='left', on=['index'], copy=True)
                    # df_final_ps = df_final_ps.drop(columns=['index'])
                    # df_final_ps['Time interval'] = pd.to_timedelta(df_final_ps['Time interval']) # convert to timedelta to calculate seconds
                    # df_final_ps['Time interval'] = df_final_ps['Time interval'].dt.seconds

                    # df_rwy['Time interval'] = df_rwy['Time interval'].apply(lambda x: x.time())
                    # #Extract lists to plot
                    # H_delay_time = df_rwy['Time interval'].tolist()
                    # H_delay = df_final_rwy['RWY_Hold Delay'].tolist()

                    # # return(H_delay_time,H_delay,PS_time,PS_delay)
                    return {'a': time_interval,
                            'b': RWYhold_Delay}


                def print_Hold_delay(ab, color):

                    H_delay_time = ab['a']
                    H_delay = ab['b']

                    A = f.add_subplot(111)
                    A.plot(H_delay_time, H_delay, color)
                    #A.set_title('RWY HOLD DELAY', loc='left')
                    if OP_FLAG == True: #Plot Operational Data
                        A.plot(OP_Time_H_Delay,OP_H_Delay, 'b')
                        A.legend(('Model','Operational Data'), loc = 'upper right')


                if new_set_FLAG == True:
                    if m >=1:
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        hold_delay = delay(df_delay,df_dep_output)
                        print_Hold_delay(hold_delay,'k')
                        hold_delay2 = delay(df_delay2,df_dep_output2)
                        print_Hold_delay(hold_delay2,'g')

                        if OP_FLAG == True:
                            A.legend(('Model','Operational Data', 'Model 2'), loc = 'upper right')
                        else:
                            A.legend(('Model', 'Model 2'), loc = 'upper right')
                        if m>=2:
                            hold_delay3 = delay(df_delay3,df_dep_output3)
                            print_Hold_delay(hold_delay3,'c')

                            if OP_FLAG == True:
                                A.legend(('Model','Operational Data', 'Model 2', 'Model 3'), loc = 'upper right')
                            else:
                                A.legend(('Model', 'Model 2', 'Model 3'), loc = 'upper right')
                            if m>=3:
                                hold_delay4 = delay(df_delay4,df_dep_output4)
                                print_Hold_delay(hold_delay4,'m')

                                if OP_FLAG == True:
                                    A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                else:
                                    A.legend(('Model', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                if m>=4:
                                    hold_delay5 = delay(df_delay5,df_dep_output5)
                                    print_Hold_delay(hold_delay5,'y')

                                    if OP_FLAG == True:
                                        A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                    else:
                                        A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                    if m>=5:
                                        hold_delay6 = delay(df_delay6,df_dep_output6)
                                        print_Hold_delay(hold_delay6,color='purple')

                                        if OP_FLAG == True:
                                            A.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                        else:
                                            A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                        A.set_xlabel('Seconds of the day')
                        A.set_ylabel('Seconds of delay')
                        A.grid(color='b', linestyle='-', linewidth=0.1)

                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                else:
                    f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    hold_delay = delay(df_delay,df_dep_output)
                    print_Hold_delay(hold_delay,'r')

                    A.set_xlabel('Time')
                    A.set_ylabel('Seconds of delay')
                    A.grid(color='b', linestyle='-', linewidth=0.1)

                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # ============================================================================#
    #                   DEPARTURE DELAY - PS delay                                #
    # ============================================================================#

    class DepDelay2(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="PUSH/START DELAY")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()

            if convergenceFLAG ==True:
                button1 = ttk.Button(self, text="Convergence Throughput",
                                    command=lambda: controller.show_frame(Conv))
                button1.pack()

            if Thr_FLAG == True:
                button = ttk.Button(self, text="Throughput",
                                    command=lambda: controller.show_frame(Thr))
                button.pack()

            if Delay_FLAG == True:
                button2 = ttk.Button(self, text="RWY HOLD DELAY",
                                    command=lambda: controller.show_frame(DepDelay))
                button2.pack()

            if arr_delay_FLAG == True:
                button3 = ttk.Button(self, text="Arrivals Delay",
                                    command=lambda: controller.show_frame(ArrivalDelay))
                button3.pack()

            if Seq_FLAG == True:
                button4 = ttk.Button(self, text="Sequence",
                                    command=lambda: controller.show_frame(Seq))
                button4.pack()

            if ADA_buffer_FLAG == True:
                button5 = ttk.Button(self, text="ADA Buffer",
                                    command=lambda: controller.show_frame(ADAbuffer))
                button5.pack()

            if (df_delay.empty == True):
                print("No departures. Nothing to show")
            else:
                def delay(df_delay, df_dep_output):
                    interval15=[]
                    df_ps_delay = pd.DataFrame()
                    # Add arrival delay values
                    df_ps_delay['PS_Delay'] = df_delay['Push/Start Delay']
                    # print when those values occure
                    df_ps_delay['Time1'] = df_dep_output['Departure_RWY_ENTRY']
                    # round each time value to 15 minutes
                    df_ps_delay= df_ps_delay.dropna(subset=['Time1'])
                    time1_list = df_ps_delay['Time1'].tolist()
                    #a=[]
                    for a in time1_list:
                        b = int(int(a/900)*900)
                        interval15.append(b)

                    df_ps_delay['interval15'] = interval15
                    df_ps_delay = df_ps_delay.drop(columns=['Time1'])
                    #Group data by the time interval, if there are multiple values for the same time interval, take the mean.
                    df_ps_delay = df_ps_delay.groupby(['interval15'])['PS_Delay'].mean()
                    #make the rolling average
                    df_ps_delay = df_ps_delay.reset_index()
                    df_ps_delay2 = df_ps_delay.rolling(window=4, on='interval15')['PS_Delay'].mean()
                    PS_delay = df_ps_delay2.tolist()
                    df_ps_delay['DATE'] = pd.to_datetime(df_ps_delay['interval15'],unit='s')
                    df_ps_delay['DATE'] = df_ps_delay['DATE'].apply(lambda x: x.time())

                    time_interval = df_ps_delay['DATE']

                    # df_delay_input['Time interval'] = pd.DatetimeIndex(df_delay_input['Time interval'])
                    # # For RWY_Hold Delay
                    # df_rwy = df_delay_input
                    # df_rwy = df_rwy.groupby(['Time interval'])['RWY_Hold Delay'].mean()
                    # df_rwy = df_rwy.reset_index()
                    # df_rwy_avg = df_rwy.rolling(window='3600s', on='Time interval')['RWY_Hold Delay'].mean()
                    # df_rwy_avg = df_rwy_avg.reset_index()
                    # df_rwy = df_rwy.reset_index()
                    # df_rwy = df_rwy.drop(columns=['RWY_Hold Delay'])


                    # df_final_rwy = pd.merge(df_rwy, df_rwy_avg,  how='left', on=['index'], copy=True)
                    # df_final_rwy = df_final_rwy.drop(columns=['index'])
                    # df_final_rwy['Time interval'] = pd.to_timedelta(df_final_rwy['Time interval']) # convert to timedelta to calculate seconds
                    # df_final_rwy['Time interval'] = df_final_rwy['Time interval'].dt.seconds

                    # # For Push/Start Delay
                    # df_ps = df_delay_input
                    # df_ps = df_ps.groupby(['Time interval'])['Push/Start Delay'].mean()
                    # df_ps = df_ps.reset_index()
                    # dh_ps_avg = df_ps.rolling(window='3600s', on='Time interval')['Push/Start Delay'].mean()
                    # dh_ps_avg = dh_ps_avg.reset_index()
                    # df_ps = df_ps.reset_index()
                    # df_ps = df_ps.drop(columns=['Push/Start Delay'])
                    # #df_ps['Time interval'] = df_ps['Time interval'].apply(lambda x: x.time())
                    # #df_rwy_arr['Arr Time Interval'] = df_rwy_arr['Arr Time Interval'].apply(lambda x: x.time())


                    # df_final_ps = pd.merge(df_ps, dh_ps_avg,  how='left', on=['index'], copy=True)
                    # df_final_ps = df_final_ps.drop(columns=['index'])
                    # df_final_ps['Time interval'] = pd.to_timedelta(df_final_ps['Time interval']) # convert to timedelta to calculate seconds
                    # df_final_ps['Time interval'] = df_final_ps['Time interval'].dt.seconds

                    # df_rwy['Time interval'] = df_rwy['Time interval'].apply(lambda x: x.time())
                    # # Extract lists to plot
                    # # H_delay_time = df_rwy['Time interval'].tolist()
                    # # H_delay = df_final_rwy['RWY_Hold Delay'].tolist()
                    # PS_time = df_rwy['Time interval'].tolist()
                    # PS_delay = df_final_ps['Push/Start Delay'].tolist()

                    return {'c': time_interval,
                            'd': PS_delay}


                def print_PS_delay(ab, color):
                    PS_time = ab['c']
                    PS_delay = ab['d']
                    B = f.add_subplot(111)
                    B.plot(PS_time, PS_delay, color)
                    # B.set_title('PUSH/START DELAY', loc = 'right')
                    if OP_FLAG == True:#Plot Operational Data
                        B.plot(OP_Time_PS_Delay,OP_PS_Delay, 'b')
                        # plt.legend(('Model','Operational Data'), loc = 'upper right')

                if new_set_FLAG == True:

                    if m >=1:
                        f = Figure(figsize=(5,5), dpi=100)
                        B = f.add_subplot(111)
                        Push_delay = delay(df_delay, df_dep_output)
                        print_PS_delay(Push_delay,'k')
                        Push_delay2 = delay(df_delay2, df_dep_output2)
                        print_PS_delay(Push_delay2,'g')

                        if OP_FLAG == True:
                            B.legend(('Model','Operational Data', 'Model 2'), loc = 'upper right')
                        else:
                            B.legend(('Model', 'Model 2'), loc = 'upper right')
                        if m>=2:
                            Push_delay3 = delay(df_delay3, df_dep_output3)
                            print_PS_delay(Push_delay3,'c')

                            if OP_FLAG == True:
                                B.legend(('Model','Operational Data', 'Model 2', 'Model 3'), loc = 'upper right')
                            else:
                                B.legend(('Model', 'Model 2', 'Model 3'), loc = 'upper right')
                            if m>=3:
                                Push_delay4 = delay(df_delay4, df_dep_output4)
                                print_PS_delay(Push_delay4,'m')

                                if OP_FLAG == True:
                                    B.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                else:
                                    B.legend(('Model', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                if m>=4:
                                    Push_delay5 = delay(df_delay5, df_dep_output5)
                                    print_PS_delay(Push_delay5,'y')

                                    if OP_FLAG == True:
                                        B.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                    else:
                                        B.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                    if m>=5:
                                        Push_delay6 = delay(df_delay6, df_dep_output6)
                                        print_PS_delay(Push_delay6, color='purple')


                                        if OP_FLAG == True:
                                            B.legend(('Model','Operational Data', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                                        else:
                                            B.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')

                        B.grid(color='b', linestyle='-', linewidth=0.1)
                        B.set_xlabel('Time')
                        B.set_ylabel('Seconds of delay')
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                else:
                    f = Figure(figsize=(5,5), dpi=100)

                    B = f.add_subplot(111)
                    Push_delay = delay(df_delay, df_dep_output)
                    print_PS_delay(Push_delay,'r')
                    B.set_xlabel('Time')
                    B.set_ylabel('Seconds of delay')
                    B.grid(color='b', linestyle='-', linewidth=0.1)
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # ============================================================================#
    #                          ARRIVAL DELAY                                      #
    # ============================================================================#

    #if arr_delay_FLAG == True:
    class ArrivalDelay(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="ARRIVALS DELAY")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()

            if convergenceFLAG ==True:
                button1 = ttk.Button(self, text="Convergence Throughput",
                                    command=lambda: controller.show_frame(Conv))
                button1.pack()

            if Thr_FLAG == True:
                button = ttk.Button(self, text="Throughput",
                                    command=lambda: controller.show_frame(Thr))
                button.pack()

            if Delay_FLAG == True:
                button2 = ttk.Button(self, text="RWY Hold Delay",
                                    command=lambda: controller.show_frame(DepDelay))
                button2.pack()

            if Delay_FLAG == True:
                button5 = ttk.Button(self, text="Push/Start Delay",
                                    command=lambda: controller.show_frame(DepDelay2))
                button5.pack()

            if Seq_FLAG == True:
                button4 = ttk.Button(self, text="Sequence",
                                    command=lambda: controller.show_frame(Seq))
                button4.pack()

            if ADA_buffer_FLAG == True:
                button5 = ttk.Button(self, text="ADA Buffer",
                                    command=lambda: controller.show_frame(ADAbuffer))
                button5.pack()

            if (df_delay.empty == True):
                    print("No departures. Nothing to show")
            else:
                def ArrDelay(df_delay, df_arr_output):
                    interval15=[]
                    df_arr_delay = pd.DataFrame()
                    # Add arrival delay values
                    df_arr_delay['ARR_Delay'] = df_delay['Arrival Delay']
                    # print when those values occure
                    df_arr_delay['Time1'] = df_arr_output['ACTUAL Landing Time']
                    # round each time value to 15 minutes
                    df_arr_delay= df_arr_delay.dropna(subset=['Time1'])
                    time1_list = df_arr_delay['Time1'].tolist()
                    #a=[]
                    for a in time1_list:
                        b = int(int(a/900)*900)
                        interval15.append(b)

                    df_arr_delay['interval15'] = interval15
                    df_arr_delay = df_arr_delay.drop(columns=['Time1'])
                    #Group data by the time interval, if there are multiple values for the same time interval, take the mean.
                    df_arr_delay = df_arr_delay.groupby(['interval15'])['ARR_Delay'].mean()
                    #make the rolling average
                    df_arr_delay = df_arr_delay.reset_index()
                    df_arr_delay2 = df_arr_delay.rolling(window=4, on='interval15')['ARR_Delay'].mean()
                    ARR_delay = df_arr_delay2.tolist()
                    df_arr_delay['DATE'] = pd.to_datetime(df_arr_delay['interval15'],unit='s')
                    df_arr_delay['DATE'] = df_arr_delay['DATE'].apply(lambda x: x.time())

                    time_interval = df_arr_delay['DATE']
                    # print(df_arr_delay['Time1'].value())
                    # df_delay_input['Arr Time Interval'] = pd.DatetimeIndex(df_delay_input['Arr Time Interval'])
                    # #For RWY_Hold Delay
                    # df_rwy_arr = df_delay_input
                    # df_rwy_arr = df_rwy_arr.groupby(['Arr Time Interval'])['Arr Delay'].mean()
                    # df_rwy_arr = df_rwy_arr.reset_index()
                    # df_rwy_arr_avg = df_rwy_arr.rolling(window='3600s', on='Arr Time Interval')['Arr Delay'].mean()
                    # df_rwy_arr_avg = df_rwy_arr_avg.reset_index()
                    # df_rwy_arr = df_rwy_arr.reset_index()
                    # df_rwy_arr = df_rwy_arr.drop(columns=['Arr Delay'])

                    # df_final_arr_rwy = pd.merge(df_rwy_arr, df_rwy_arr_avg,  how='left', on=['index'], copy=True)
                    # df_final_arr_rwy = df_final_arr_rwy.drop(columns=['index'])
                    # df_final_arr_rwy['Arr Time Interval'] = pd.to_timedelta(df_final_arr_rwy['Arr Time Interval']) # convert to timedelta to calculate seconds
                    # df_final_arr_rwy['Arr Time Interval'] = df_final_arr_rwy['Arr Time Interval'].dt.seconds

                    # df_rwy_arr['Arr Time Interval'] = df_rwy_arr['Arr Time Interval'].apply(lambda x: x.time())

                    # #Extract lists to plot
                    # arr_delay_time = df_rwy_arr['Arr Time Interval'].tolist()
                    # arr_delay = df_final_arr_rwy['Arr Delay'].tolist()

                    # return(H_delay_time,H_delay,PS_time,PS_delay)
                    return {'a': time_interval,
                            'b': ARR_delay}


                def plotArrDelay(ab, color):
                    arr_delay_time = ab['a']
                    arr_delay = ab['b']
                    # f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    A.plot(arr_delay_time, arr_delay, color)


                if new_set_FLAG == True:

                    if m >=1:
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        plotArrDelay(ArrDelay(df_delay, df_arr_output),'k')
                        plotArrDelay(ArrDelay(df_delay2, df_arr_output2),'g')

                        A.legend(('Model', 'Model 2'), loc = 'upper right')
                        if m>=2:
                            plotArrDelay(ArrDelay(df_delay3, df_arr_output3),'c')

                            A.legend(('Model', 'Model 2', 'Model 3'), loc = 'upper right')
                            if m>=3:
                                plotArrDelay(ArrDelay(df_delay4, df_arr_output4),'m')

                                A.legend(('Model', 'Model 2', 'Model 3', 'Model 4'), loc = 'upper right')
                                if m>=4:
                                    # A.plot(ArrDelay(df_delay5)['a'],ArrDelay(df_delay2)['b'],'y')
                                    plotArrDelay(ArrDelay(df_delay5, df_arr_output5),'y')

                                    A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5'), loc = 'upper right')
                                    if m>=5:
                                        # A.plot(ArrDelay(df_delay6)['a'],ArrDelay(df_delay2)['b'],'purple')
                                        plotArrDelay(ArrDelay(df_delay6, df_arr_output6),'purple')

                                        A.legend(('Model', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6'), loc = 'upper right')
                        A.set_xlabel('Time')
                        A.set_ylabel('Seconds of delay')
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                else:
                    f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    A.plot(ArrDelay(df_delay, df_arr_output)['a'],ArrDelay(df_delay, df_arr_output)['b'],'k')
                    A.set_xlabel('Time')
                    A.set_ylabel('Seconds of delay')
                    A.grid(color='b', linestyle='-', linewidth=0.1)

                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # ============================================================================#
    #                           SEQUENCE                                          #
    # ============================================================================#

    # if Seq_FLAG == True:
    class Seq(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="SEQUENCE")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()

            if convergenceFLAG ==True:
                button1 = ttk.Button(self, text="Convergence Throughput",
                                    command=lambda: controller.show_frame(Conv))
                button1.pack()

            if Thr_FLAG == True:
                button = ttk.Button(self, text="Throughput",
                                    command=lambda: controller.show_frame(Thr))
                button.pack()

            if Delay_FLAG == True:
                button2 = ttk.Button(self, text="RWY Hold Delay",
                                    command=lambda: controller.show_frame(DepDelay))
                button2.pack()

            if Delay_FLAG == True:
                button5 = ttk.Button(self, text="Push/Start Delay",
                                    command=lambda: controller.show_frame(DepDelay2))
                button5.pack()

            if arr_delay_FLAG == True:
                button3 = ttk.Button(self, text="Arrivals Delay",
                                    command=lambda: controller.show_frame(ArrivalDelay))
                button3.pack()

            if ADA_buffer_FLAG == True:
                button5 = ttk.Button(self, text="ADA Buffer",
                                    command=lambda: controller.show_frame(ADAbuffer))
                button5.pack()

            def sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, number):

                df_sequence = pd.DataFrame()
                # Arrivals
                df_sequence['ARRIVAL'] = df_arr_output['ACTUAL Landing Time'] + (df_arr_output['AROT']/2)
                df_sequence['ARRIVAL_error'] = df_arr_output['AROT']/2
                df_sequence['ARRIVAL_spacing'] = df_arr_output['ACTUAL Landing Time']
                df_temp = pd.DataFrame()
                df_temp['MAX Constraint'] = df_arr_output['MAX Constraint']
                df_temp = df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['Arrival_ZERO'] = 0
                df_sequence['ARRIVAL_spacing_error'] = df_temp['MAX Constraint']
                df_sequence['Arrival_ZERO'] = df_temp['Arrival_ZERO']

                # Positions
                df_sequence['main_position'] = number
                df_sequence['arr_spacing_position'] = number+0.005

                # Annotation

                df_temp = pd.DataFrame()
                df_temp['ARR_ID'] = df_arr_output['Arrival ID'].astype(str)
                df_temp['ARR_WAKE'] = df_rwy_calcs['ARRIVAL actual WAKE'].astype(str)
                df_temp['ARR_DELAY'] = df_arr_output['Arrival DELAY'].astype(str)
                df_temp['ARRIVAL_LABEL'] = 'ID = ' + df_temp['ARR_ID'] + ' | WAKE = ' + df_temp['ARR_WAKE'] + ' | Delay = ' + df_temp['ARR_DELAY']

                df_sequence['ARRIVAL_LABEL'] = df_temp['ARRIVAL_LABEL']

                df_temp = pd.DataFrame()
                df_temp['reason'] = df_arr_output['MAX Constraint Label']
                df_temp = df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['value'] = df_sequence['ARRIVAL_spacing_error'].astype(str)
                df_temp['ARRIVAL_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                df_sequence['ARRIVAL_spacing_LABEL'] = df_temp['ARRIVAL_spacing_LABEL']

                # LISTS to plot

                #----ARRIVALS----#
                main_arrival = df_sequence['ARRIVAL'].tolist()
                main_arrival_error = df_sequence['ARRIVAL_error'].tolist()
                arrival_spacing = df_sequence['ARRIVAL_spacing'].tolist()
                arrival_spacing_error = df_sequence['ARRIVAL_spacing_error'].tolist()
                arrival_zero = df_sequence['Arrival_ZERO'].tolist()
                #-Labels:
                arrival_label = df_sequence['ARRIVAL_LABEL'].tolist()
                arrival_spacing_label = df_sequence['ARRIVAL_spacing_LABEL'].tolist()

                #-----POSITIONS------#
                main_data_position = df_sequence['main_position'].tolist()
                arrival_spacing_position = df_sequence['arr_spacing_position'].tolist()
                #Data prep for tags
                labels = arrival_label +  arrival_spacing_label
                labels_y = main_data_position +  arrival_spacing_position
                labels_x = main_arrival +  arrival_spacing

                return{'0a': arrival_zero,
                       '1' : main_arrival,
                       '2' : main_arrival_error,
                       '3' : arrival_spacing,
                       '4' : arrival_spacing_error,
                       '9' : main_data_position,
                       '10' : arrival_spacing_position,
                       '12' : labels,
                       '13' : labels_y,
                       '14' : labels_x}


            def sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, number):
                df_sequence = pd.DataFrame()
                # Departure

                df_sequence['DEPARTURES'] = df_dep_output['Departure_RWY_ENTRY'] + (df_dep_output['DROT']/2)
                df_sequence['DEPARTURES_error'] = df_dep_output['DROT']/2
                df_sequence['DEPARTURES_spacing'] = df_dep_output['Departure_RWY_ENTRY']
                df_temp = pd.DataFrame()
                df_temp['Dep MIN Separation'] = df_dep_output['Dep MIN Separation']
                df_temp=df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['Departure_ZERO'] = 0
                df_sequence['DEPARTURES_spacing_error'] = df_temp['Dep MIN Separation']
                df_sequence['Departure_ZERO'] = df_temp['Departure_ZERO']

                # Positions
                df_sequence['main_position'] = number
                df_sequence['dep_spacing_position'] = number-0.005

                df_temp = pd.DataFrame()
                df_temp['DEP_ID'] = df_dep_output['Departure ID'].astype(str)
                df_temp['DEP_SID'] = df_dep_output['SID GROUP'].astype(str)
                df_temp['DEP_WAKE'] = df_dep_output['WAKE'].astype(str)
                df_temp['DEP_DELAY1'] = df_dep_output['DELAY DepSTANDqueue'] + df_dep_output['DELAY TAXIhold'] + df_dep_output['DELAY RWYqueue']
                df_temp['DEP_DELAY'] = df_temp['DEP_DELAY1'].astype(str)
                df_temp['DEPARTURE_LABEL'] = 'ID = ' + df_temp['DEP_ID'] + ' | SID = ' +df_temp['DEP_SID'] +' | WAKE = ' + df_temp['DEP_WAKE'] + ' | Delay = ' + df_temp['DEP_DELAY']

                df_sequence['DEPARTURE_LABEL'] = df_temp['DEPARTURE_LABEL']

                df_temp = pd.DataFrame()
                df_temp['reason'] = df_dep_output['Dep MIN Separation Label']
                df_temp = df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['value'] = df_sequence['DEPARTURES_spacing_error'].astype(str)
                df_temp['DEPARTURES_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                df_sequence['DEPARTURES_spacing_LABEL'] = df_temp['DEPARTURES_spacing_LABEL']

                # LISTS to plot

                #----DEPARTURES----#
                main_departure = df_sequence['DEPARTURES'].tolist()
                main_departure_error = df_sequence['DEPARTURES_error'].tolist()
                departure_spacing = df_sequence['DEPARTURES_spacing'].tolist()
                departure_spacing_error = df_sequence['DEPARTURES_spacing_error'].tolist()
                departure_zero = df_sequence['Departure_ZERO']
                #-Labels:
                departure_label = df_sequence['DEPARTURE_LABEL'].tolist()
                departure_spacing_label = df_sequence['DEPARTURES_spacing_LABEL'].tolist()

                #-----POSITIONS------#
                main_data_position = df_sequence['main_position'].tolist()
                departure_spacing_position = df_sequence['dep_spacing_position'].tolist()

                #Data prep for tags
                labels = departure_label +  departure_spacing_label
                labels_y = main_data_position + departure_spacing_position
                labels_x = main_departure +  departure_spacing

                return{'0b': departure_zero,
                       '5' : main_departure,
                       '6' : main_departure_error,
                       '7' : departure_spacing,
                       '8' : departure_spacing_error,
                       '9' : main_data_position,
                       '11' : departure_spacing_position,
                       '12' : labels,
                       '13' : labels_y,
                       '14' : labels_x}


            def sequence(df_arr_output, df_rwy_calcs, df_dep_output, number): ######MIX MODE

                df_sequence = pd.DataFrame()
                #Arrivals
                df_sequence['ARRIVAL'] = df_arr_output['ACTUAL Landing Time'] + (df_arr_output['AROT']/2)
                df_sequence['ARRIVAL_error'] = df_arr_output['AROT']/2
                df_sequence['ARRIVAL_spacing'] = df_arr_output['ACTUAL Landing Time']
                df_temp = pd.DataFrame()
                df_temp['MAX Constraint'] = df_arr_output['MAX Constraint']
                df_temp = df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['Arrival_ZERO'] = 0
                df_sequence['ARRIVAL_spacing_error'] = df_temp['MAX Constraint']
                df_sequence['Arrival_ZERO'] = df_temp['Arrival_ZERO']

                #Departure
                df_sequence['DEPARTURES'] = df_dep_output['Departure_RWY_ENTRY'] + (df_dep_output['DROT']/2)
                df_sequence['DEPARTURES_error'] = df_dep_output['DROT']/2
                df_sequence['DEPARTURES_spacing'] = df_dep_output['Departure_RWY_ENTRY']
                df_temp = pd.DataFrame()
                df_temp['Dep MIN Separation'] = df_dep_output['Dep MIN Separation']
                df_temp=df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['Departure_ZERO'] = 0
                df_sequence['DEPARTURES_spacing_error'] = df_temp['Dep MIN Separation']
                df_sequence['Departure_ZERO'] = df_temp['Departure_ZERO']

                #Positions
                df_sequence['main_position'] = number
                df_sequence['arr_spacing_position'] = number+0.005
                df_sequence['dep_spacing_position'] = number-0.005

                #Annotation
                df_temp = pd.DataFrame()
                df_temp['ARR_ID'] = df_arr_output['Arrival ID'].astype(str)
                df_temp['ARR_WAKE'] = df_rwy_calcs['ARRIVAL actual WAKE'].astype(str)
                df_temp['ARR_DELAY'] = df_arr_output['Arrival DELAY'].astype(str)
                df_temp['ARRIVAL_LABEL'] = 'ID = ' + df_temp['ARR_ID'] + ' | WAKE = ' + df_temp['ARR_WAKE'] + ' | Delay = ' + df_temp['ARR_DELAY']

                df_sequence['ARRIVAL_LABEL'] = df_temp['ARRIVAL_LABEL']

                df_temp = pd.DataFrame()
                df_temp['DEP_ID'] = df_dep_output['Departure ID'].astype(str)
                df_temp['DEP_SID'] = df_dep_output['SID GROUP'].astype(str)
                df_temp['DEP_WAKE'] = df_dep_output['WAKE'].astype(str)
                df_temp['DEP_DELAY1'] = df_dep_output['DELAY DepSTANDqueue'] + df_dep_output['DELAY TAXIhold'] + df_dep_output['DELAY RWYqueue']
                df_temp['DEP_DELAY'] = df_temp['DEP_DELAY1'].astype(str)
                df_temp['DEPARTURE_LABEL'] = 'ID = ' + df_temp['DEP_ID'] + ' | SID = ' +df_temp['DEP_SID'] +' | WAKE = ' + df_temp['DEP_WAKE'] + ' | Delay = ' + df_temp['DEP_DELAY']

                df_sequence['DEPARTURE_LABEL'] = df_temp['DEPARTURE_LABEL']

                df_temp = pd.DataFrame()
                df_temp['reason'] = df_arr_output['MAX Constraint Label']
                df_temp = df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['value'] = df_sequence['ARRIVAL_spacing_error'].astype(str)
                df_temp['ARRIVAL_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                df_sequence['ARRIVAL_spacing_LABEL'] = df_temp['ARRIVAL_spacing_LABEL']

                df_temp = pd.DataFrame()
                df_temp['reason'] = df_dep_output['Dep MIN Separation Label']
                df_temp = df_temp.drop([0])
                df_temp = df_temp.reset_index()
                df_temp = df_temp.drop(columns=['index'])
                df_temp['value'] = df_sequence['DEPARTURES_spacing_error'].astype(str)
                df_temp['DEPARTURES_spacing_LABEL'] = df_temp['reason'] + ' : ' + df_temp['value']

                df_sequence['DEPARTURES_spacing_LABEL'] = df_temp['DEPARTURES_spacing_LABEL']

                # LISTS to plot

                #----ARRIVALS----#
                main_arrival = df_sequence['ARRIVAL'].tolist()
                main_arrival_error = df_sequence['ARRIVAL_error'].tolist()
                arrival_spacing = df_sequence['ARRIVAL_spacing'].tolist()
                arrival_spacing_error = df_sequence['ARRIVAL_spacing_error'].tolist()
                arrival_zero = df_sequence['Arrival_ZERO'].tolist()
                #-Labels:
                arrival_label = df_sequence['ARRIVAL_LABEL'].tolist()
                arrival_spacing_label = df_sequence['ARRIVAL_spacing_LABEL'].tolist()

                #----DEPARTURES----#
                main_departure = df_sequence['DEPARTURES'].tolist()
                main_departure_error = df_sequence['DEPARTURES_error'].tolist()
                departure_spacing = df_sequence['DEPARTURES_spacing'].tolist()
                departure_spacing_error = df_sequence['DEPARTURES_spacing_error'].tolist()
                departure_zero = df_sequence['Departure_ZERO']
                #-Labels:
                departure_label = df_sequence['DEPARTURE_LABEL'].tolist()
                departure_spacing_label = df_sequence['DEPARTURES_spacing_LABEL'].tolist()

                #-----POSITIONS------#
                main_data_position = df_sequence['main_position'].tolist()
                arrival_spacing_position = df_sequence['arr_spacing_position'].tolist()
                departure_spacing_position = df_sequence['dep_spacing_position'].tolist()

                #Data prep for tags
                labels = arrival_label + departure_label + arrival_spacing_label  + departure_spacing_label
                labels_y = main_data_position + main_data_position + arrival_spacing_position + departure_spacing_position
                labels_x = main_arrival + main_departure + arrival_spacing + departure_spacing

                return{'0a': arrival_zero,
                       '0b': departure_zero,
                       '1' : main_arrival,
                       '2' : main_arrival_error,
                       '3' : arrival_spacing,
                       '4' : arrival_spacing_error,
                       '5' : main_departure,
                       '6' : main_departure_error,
                       '7' : departure_spacing,
                       '8' : departure_spacing_error,
                       '9' : main_data_position,
                       '10' : arrival_spacing_position,
                       '11' : departure_spacing_position,
                       '12' : labels,
                       '13' : labels_y,
                       '14' : labels_x}


            #------ ARRIVALS only -------#

            if df_dep_output.empty ==True:

                if new_set_FLAG == True:
                    if df_dep_output2.empty ==True:#arr only
                        if m==1: # two arr only comparison
                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            ax = f.add_subplot(111)

                            labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                            tag_text_use = np.array(list(labels))
                            labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                            labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                            tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                            # plt.axhline(y = 10, color='w')
                            # A.axhline(y=0.5, color='w')

                            A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="w"),
                                            arrowprops=dict(arrowstyle="->"))
                            annot.set_visible(False)

                            def update_annot(ind):
                                pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                annot.xy = pos
                                text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                annot.set_text(text)


                            def hover(event):
                                vis = annot.get_visible()
                                if event.inaxes == ax:
                                    cont, ind = tags_main_data.contains(event)
                                    if cont:
                                        update_annot(ind)
                                        annot.set_visible(True)
                                        canvas.draw_idle()
                                    else:
                                        if vis:
                                            annot.set_visible(False)
                                            canvas.draw_idle()


                            A.set_xlabel('Seconds of the day')
                            A.axes.get_yaxis().set_visible(False)
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Arrivals M2", "Arrivals Spacing M2"), loc = 'upper right')
                            #plt.title("Sequence analysis")
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                            canvas.mpl_connect("motion_notify_event", hover)
                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                        elif m==2: # 3 ARRonly comparison
                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            ax = f.add_subplot(111)

                            labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12']
                            tag_text_use = np.array(list(labels))
                            labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13']
                            labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] + sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14']

                            tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                            #plt.axhline(y = 10, color='w')
                            #A.axhline(y=0.5, color='w')

                            A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='salmon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequenceArrOnly(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='orchid', fmt='o', markersize=8, capsize=10, )

                            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="w"),
                                            arrowprops=dict(arrowstyle="->"))
                            annot.set_visible(False)

                            def update_annot(ind):

                                pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                annot.xy = pos
                                text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                annot.set_text(text)


                            def hover(event):
                                vis = annot.get_visible()
                                if event.inaxes == ax:
                                    cont, ind = tags_main_data.contains(event)
                                    if cont:
                                        update_annot(ind)
                                        annot.set_visible(True)
                                        canvas.draw_idle()
                                    else:
                                        if vis:
                                            annot.set_visible(False)
                                            canvas.draw_idle()


                            A.set_xlabel('Seconds of the day')
                            A.axes.get_yaxis().set_visible(False)
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Arrivals M2", "Arrivals Spacing M2","Arrivals M3", "Arrivals Spacing M3"), loc = 'upper right')
                            #plt.title("Sequence analysis")
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                            canvas.mpl_connect("motion_notify_event", hover)
                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                            #f.canvas.figure.savefig('sequence.png')

                    elif df_arr_output2.empty ==True: # ARR only + DEP only
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        #A.axhline(y=0.5, color='w')

                        A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['4'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['5'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['6']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['8'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['11'], sequenceArrOnly(df_arr_output, df_rwy_calcs, 1)['9']], color='purple', fmt='o', markersize=8, capsize=10)

                        A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], fmt='o', markersize=8, capsize=10)

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot(ind):

                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Departures M2", "Departures Spacing M2"), loc = 'upper right')
                        #plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    else:#ARR only + MIXED
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_y = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        #A.axhline(y=0.5, color='w')

                        A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot2(ind):
                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot2(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Arrivals M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2"), loc = 'upper right')
                        #plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                else:  #only one ARRonly
                    f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    ax = f.add_subplot(111)

                    labels =  sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']
                    tag_text_use = np.array(list(labels))

                    tags_main_data = A.scatter(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'],sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] , c='w', s=100)
                    # plt.axhline(y = 10, color='w')
                    # A.axhline(y=0.5, color='w')

                    A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                    A.errorbar(sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                    bbox=dict(boxstyle="round", fc="w"),
                                    arrowprops=dict(arrowstyle="->"))
                    annot.set_visible(False)

                    def update_annot(ind):
                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                        annot.xy = pos
                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                        annot.set_text(text)


                    def hover(event):
                        vis = annot.get_visible()
                        if event.inaxes == ax:
                            cont, ind = tags_main_data.contains(event)
                            if cont:
                                update_annot(ind)
                                annot.set_visible(True)
                                canvas.draw_idle()
                            else:
                                if vis:
                                    annot.set_visible(False)
                                    canvas.draw_idle()


                    A.set_xlabel('Seconds of the day')
                    A.axes.get_yaxis().set_visible(False)
                    A.grid(color='b', linestyle='-', linewidth=0.1)
                    A.legend(("Legend","Arrivals","Arrivals Spacing"), loc = 'upper right')
                    #plt.title("Sequence analysis")
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                    canvas.mpl_connect("motion_notify_event", hover)
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            #-------DEPARTURES only --------#

            elif df_arr_output.empty ==True:

                if new_set_FLAG == True:

                    if df_dep_output2.empty ==True: # DEPonly + ARRonly
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']+ sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_x = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                        labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        # A.axhline(y=0.5, color='w')

                        A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                        A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot(ind):
                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Departures M1","Departures Spacing M1","Arrivals M2", "Arrivals Spacing M2"), loc = 'upper right')
                        # plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    elif df_arr_output2.empty ==True: # DEPonly + DEPonly
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        labels_x = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        # A.axhline(y=0.5, color='w')

                        A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                        A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='indigo', fmt='o', markersize=8, capsize=10)

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot(ind):
                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Departures M1","Departures Spacing M1","Departures M2", "Departures Spacing M2"), loc = 'upper right')
                        #plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    else: # DEPonly + MIXED
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']  + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        labels_x = sequenceArrOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']

                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        # A.axhline(y=0.5, color='w')

                        A.errorbar(sequenceDepOnly(df_dep_output, 1)['3'], sequenceDepOnly(df_dep_output, 1)['4'], xerr=[sequenceDepOnly(df_dep_output, 1)['5'], sequenceDepOnly(df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequenceDepOnly(df_dep_output, 1)['10'], sequenceDepOnly(df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_dep_output, 1)['11'], sequenceDepOnly(df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='maroon', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['15']], color='navy', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['18'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['19'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['17'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['16']], color='indigo', fmt='o', markersize=8, capsize=10, )

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot2(ind):
                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot2(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Departures M1","Departures Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2"), loc = 'upper right')
                        #plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                else: # DEPonly
                    f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    ax = f.add_subplot(111)

                    labels =  sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']
                    tag_text_use = np.array(list(labels))
                    labels_x = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14']
                    labels_y = sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13']
                    tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                    # A.axhline(y=0.5, color='w')

                    A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                    A.errorbar(sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequenceDepOnly(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)

                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                    bbox=dict(boxstyle="round", fc="w"),
                                    arrowprops=dict(arrowstyle="->"))
                    annot.set_visible(False)

                    def update_annot(ind):
                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                        annot.xy = pos
                        text = "{}".format(" ".join([sequenceDepOnly(df_dep_output, 1)['7'][n] for n in ind["ind"]]))
                        annot.set_text(text)


                    def hover(event):
                        vis = annot.get_visible()
                        if event.inaxes == ax:
                            cont, ind = tags_main_data.contains(event)
                            if cont:
                                update_annot(ind)
                                annot.set_visible(True)
                                canvas.draw_idle()
                            else:
                                if vis:
                                    annot.set_visible(False)
                                    canvas.draw_idle()


                    A.set_xlabel('Seconds of the day')
                    A.axes.get_yaxis().set_visible(False)
                    A.grid(color='b', linestyle='-', linewidth=0.1)
                    A.legend(("Legend","Departures","Departures Spacing"), loc = 'upper right')
                    #plt.title("Sequence analysis")
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                    canvas.mpl_connect("motion_notify_event", hover)
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            #------------------ MIXED MODE ------------------------#

            else:

                if new_set_FLAG == True:
                    if (df_dep_output2.empty ==False) and (df_arr_output2.empty ==False): #mixed both
                        if m==2: #MIXED +MIXED + MIXED

                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            ax = f.add_subplot(111)

                            labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12']
                            tag_text_use = np.array(list(labels))
                            labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14']
                            labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13']
                            tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                            #plt.axhline(y = 10, color='w')
                            ##A.axhline(y=0.5, color='w')

                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['5'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6']], color='limegreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='orangered', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['7'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['11'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0b'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['8']], color='royalblue',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='magenta', fmt='o', markersize=8, capsize=10, )

                            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="w"),
                                            arrowprops=dict(arrowstyle="->"))
                            annot.set_visible(False)


                            def update_annot2(ind):
                                pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                annot.xy = pos
                                text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                annot.set_text(text)


                            def hover(event):
                                vis = annot.get_visible()
                                if event.inaxes == ax:
                                    cont, ind = tags_main_data.contains(event)
                                    if cont:
                                        update_annot2(ind)
                                        annot.set_visible(True)
                                        canvas.draw_idle()
                                    else:
                                        if vis:
                                            annot.set_visible(False)
                                            canvas.draw_idle()


                            A.set_xlabel('Seconds of the day')
                            A.axes.get_yaxis().set_visible(False)
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2", "Departures M3","Arrivals M3","Departures Spacing M3","Arrivals Spacing M3"), loc = 'upper right')
                            #plt.title("Sequence analysis")
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                            canvas.mpl_connect("motion_notify_event", hover)
                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                            #f.canvas.figure.savefig('sequence.png')

                        elif m==3:#MIXED +MIXED + MIXED + MIXED

                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            ax = f.add_subplot(111)

                            labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['12']
                            tag_text_use = np.array(list(labels))
                            labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['14']
                            labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['13']
                            tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                            #plt.axhline(y = 10, color='w')
                            #A.axhline(y=0.5, color='w')

                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['5'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6']], color='limegreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='orangered', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['7'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['11'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0b'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['8']], color='royalblue',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='magenta', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['5'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6']], color='lime', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['1'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2']], color='salmon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['7'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['11'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0b'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['8']], color='cyan',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['3'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['10'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0a'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['4']], color='orchid', fmt='o', markersize=8, capsize=10, )

                            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="w"),
                                            arrowprops=dict(arrowstyle="->"))
                            annot.set_visible(False)

                            def update_annot2(ind):
                                pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                annot.xy = pos
                                text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                annot.set_text(text)


                            def hover(event):
                                vis = annot.get_visible()
                                if event.inaxes == ax:
                                    cont, ind = tags_main_data.contains(event)
                                    if cont:
                                        update_annot2(ind)
                                        annot.set_visible(True)
                                        canvas.draw_idle()
                                    else:
                                        if vis:
                                            annot.set_visible(False)
                                            canvas.draw_idle()


                            A.set_xlabel('Seconds of the day')
                            A.axes.get_yaxis().set_visible(False)
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2", "Departures M3","Arrivals M3","Departures Spacing M3","Arrivals Spacing M3", "Departures M4","Arrivals M4","Departures Spacing M4","Arrivals Spacing M4"), loc = 'upper right')
                            #plt.title("Sequence analysis")
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                            canvas.mpl_connect("motion_notify_event", hover)
                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                            #f.canvas.figure.savefig('sequence.png')

                        elif m==4: #MIXED +MIXED + MIXED +MIXED + MIXED

                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            ax = f.add_subplot(111)

                            labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['12'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['12'] + sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['12']
                            tag_text_use = np.array(list(labels))
                            labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14'] +sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['14'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['14'] + sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['14']
                            labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13'] + sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['13'] + sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['13'] + sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['13']
                            tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                            #plt.axhline(y = 10, color='w')
                            #A.axhline(y=0.5, color='w')

                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['5'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['6']], color='limegreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['1'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['9'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['2']], color='orangered', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['7'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['11'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0b'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['8']], color='royalblue',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['3'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['10'], xerr=[sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['0a'], sequence(df_arr_output3, df_rwy_calcs3, df_dep_output3, 0.96)['4']], color='magenta', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['5'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['6']], color='lime', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['1'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['9'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['2']], color='salmon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['7'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['11'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0b'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['8']], color='cyan',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['3'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['10'], xerr=[sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['0a'], sequence(df_arr_output4, df_rwy_calcs4, df_dep_output4, 0.94)['4']], color='orchid', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['5'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['9'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['6'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['6']], color='olive', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['1'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['9'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['2'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['2']], color='firebrick', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['7'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['11'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['0b'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['8']], color='mediumblue',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['3'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['10'], xerr=[sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['0a'], sequence(df_arr_output5, df_rwy_calcs5, df_dep_output5, 0.92)['4']], color='deeppink', fmt='o', markersize=8, capsize=10, )

                            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="w"),
                                            arrowprops=dict(arrowstyle="->"))
                            annot.set_visible(False)

                            def update_annot2(ind):
                                pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                annot.xy = pos
                                text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                annot.set_text(text)


                            def hover(event):
                                vis = annot.get_visible()
                                if event.inaxes == ax:
                                    cont, ind = tags_main_data.contains(event)
                                    if cont:
                                        update_annot2(ind)
                                        annot.set_visible(True)
                                        canvas.draw_idle()
                                    else:
                                        if vis:
                                            annot.set_visible(False)
                                            canvas.draw_idle()


                            A.set_xlabel('Seconds of the day')
                            A.axes.get_yaxis().set_visible(False)
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2", "Departures M3","Arrivals M3","Departures Spacing M3","Arrivals Spacing M3", "Departures M4","Arrivals M4","Departures Spacing M4","Arrivals Spacing M4"), loc = 'upper right')
                            #plt.title("Sequence analysis")
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                            canvas.mpl_connect("motion_notify_event", hover)
                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                            #f.canvas.figure.savefig('sequence.png')

                        else: # only 2 to compare

                            f = Figure(figsize=(5,5), dpi=100)
                            A = f.add_subplot(111)
                            ax = f.add_subplot(111)


                            labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                            tag_text_use = np.array(list(labels))
                            labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                            labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                            tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                            #plt.axhline(y = 10, color='w')
                            ##A.axhline(y=0.5, color='w')

                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='darkgreen', fmt='o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='maroon', fmt='o', markersize=8, capsize=10, )
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], color='navy',fmt = 'o', markersize=8, capsize=10)
                            A.errorbar(sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequence(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='indigo', fmt='o', markersize=8, capsize=10, )

                            annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="w"),
                                            arrowprops=dict(arrowstyle="->"))
                            annot.set_visible(False)

                            def update_annot2(ind):
                                pos = tags_main_data.get_offsets()[ind["ind"][0]]
                                annot.xy = pos
                                text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                                annot.set_text(text)


                            def hover(event):
                                vis = annot.get_visible()
                                if event.inaxes == ax:
                                    cont, ind = tags_main_data.contains(event)
                                    if cont:
                                        update_annot2(ind)
                                        annot.set_visible(True)
                                        canvas.draw_idle()
                                    else:
                                        if vis:
                                            annot.set_visible(False)
                                            canvas.draw_idle()


                            A.set_xlabel('Seconds of the day')
                            A.axes.get_yaxis().set_visible(False)
                            A.grid(color='b', linestyle='-', linewidth=0.1)
                            A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2","Arrivals M2", "Departures Spacing M2","Arrivals Spacing M2"), loc = 'upper right')
                            #plt.title("Sequence analysis")
                            canvas = FigureCanvasTkAgg(f, self)
                            canvas.draw()
                            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                            canvas.mpl_connect("motion_notify_event", hover)
                            toolbar = NavigationToolbar2Tk(canvas, self)
                            toolbar.update()
                            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    elif df_dep_output2.empty ==True:#arr only
                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                        labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        #plt.axhline(y = 10, color='w')
                        #A.axhline(y=0.5, color='w')

                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                        A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['1'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['3'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['10'], xerr=[sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0a'], sequenceArrOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot2(ind):
                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot2(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Arrivals M2", "Arrivals Spacing M2"), loc = 'upper right')
                        #plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    elif df_arr_output2.empty ==True: # MIXED + ARRonly

                        f = Figure(figsize=(5,5), dpi=100)
                        A = f.add_subplot(111)
                        ax = f.add_subplot(111)

                        #plt.axhline(y = 10, color='w')

                        labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['12']
                        tag_text_use = np.array(list(labels))
                        labels_x = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['14']
                        labels_y = sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] + sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['13']
                        tags_main_data = A.scatter(labels_x,labels_y , c='w', s=100)
                        #plt.axhline(y = 10, color='w')
                        #A.axhline(y=0.5, color='w')

                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                        A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['5'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['9'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['6']], color='g', fmt='o', markersize=8, capsize=10)
                        A.errorbar(sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['7'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['11'], xerr=[sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['0b'], sequenceDepOnly(df_arr_output2, df_rwy_calcs2, df_dep_output2, 0.98)['8']], fmt='o', markersize=8, capsize=10)

                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                        bbox=dict(boxstyle="round", fc="w"),
                                        arrowprops=dict(arrowstyle="->"))
                        annot.set_visible(False)

                        def update_annot2(ind):
                            pos = tags_main_data.get_offsets()[ind["ind"][0]]
                            annot.xy = pos
                            text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                            annot.set_text(text)


                        def hover(event):
                            vis = annot.get_visible()
                            if event.inaxes == ax:
                                cont, ind = tags_main_data.contains(event)
                                if cont:
                                    update_annot2(ind)
                                    annot.set_visible(True)
                                    canvas.draw_idle()
                                else:
                                    if vis:
                                        annot.set_visible(False)
                                        canvas.draw_idle()


                        A.set_xlabel('Seconds of the day')
                        A.axes.get_yaxis().set_visible(False)
                        A.grid(color='b', linestyle='-', linewidth=0.1)
                        A.legend(("Legend","Departures M1","Arrivals M1","Departures Spacing M1","Arrivals Spacing M1","Departures M2", "Departures Spacing M2"), loc = 'upper right')
                        #plt.title("Sequence analysis")
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                        canvas.mpl_connect("motion_notify_event", hover)
                        toolbar = NavigationToolbar2Tk(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                else: # only one MIXED
                    f = Figure(figsize=(5,5), dpi=100)
                    A = f.add_subplot(111)
                    ax = f.add_subplot(111)

                    labels =  sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['12']
                    tag_text_use = np.array(list(labels))

                    tags_main_data = A.scatter(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['14'],sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['13'] , c='w', s=100)
                    #plt.axhline(y = 10, color='w')
                    #A.axhline(y=10, color='w')

                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['5'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['6']], color='g', fmt='o', markersize=8, capsize=10)
                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['1'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['9'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['2']], color='r', fmt='o', markersize=8, capsize=10, )
                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['7'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['11'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0b'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['8']], fmt='o', markersize=8, capsize=10)
                    A.errorbar(sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['3'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['10'], xerr=[sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['0a'], sequence(df_arr_output, df_rwy_calcs, df_dep_output, 1)['4']], color='purple', fmt='o', markersize=8, capsize=10, )

                    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                                    bbox=dict(boxstyle="round", fc="w"),
                                    arrowprops=dict(arrowstyle="->"))
                    annot.set_visible(False)

                    def update_annot2(ind):
                        pos = tags_main_data.get_offsets()[ind["ind"][0]]
                        annot.xy = pos
                        text = "{}".format(" ".join([tag_text_use[n] for n in ind["ind"]]))
                        annot.set_text(text)


                    def hover(event):
                        vis = annot.get_visible()
                        if event.inaxes == ax:
                            cont, ind = tags_main_data.contains(event)
                            if cont:
                                update_annot2(ind)
                                annot.set_visible(True)
                                canvas.draw_idle()
                            else:
                                if vis:
                                    annot.set_visible(False)
                                    canvas.draw_idle()


                    A.set_xlabel('Seconds of the day')
                    A.axes.get_yaxis().set_visible(False)
                    A.grid(color='b', linestyle='-', linewidth=0.1)
                    A.legend(("Legend","Departure","Arrivals ","Departures Spacing ","Arrivals Spacing "), loc = 'upper right')
                    #plt.title("Sequence analysis")
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                    canvas.mpl_connect("motion_notify_event", hover)
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # ============================================================================#
    #                           ADA buffer                                         #
    # ============================================================================#

    # if Seq_FLAG == True:
    class ADAbuffer(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="SEQUENCE")
            label.pack(pady=10,padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()
            if convergenceFLAG ==True:
                button1 = ttk.Button(self, text="Convergence Throughput",
                                    command=lambda: controller.show_frame(Conv))
                button1.pack()
            if Thr_FLAG == True:
                button = ttk.Button(self, text="Throughput",
                                    command=lambda: controller.show_frame(Thr))
                button.pack()

            if Delay_FLAG == True:
                button2 = ttk.Button(self, text="RWY Hold Delay",
                                    command=lambda: controller.show_frame(DepDelay))
                button2.pack()
            if Delay_FLAG == True:
                button5 = ttk.Button(self, text="Push/Start Delay",
                                    command=lambda: controller.show_frame(DepDelay2))
                button5.pack()

            if arr_delay_FLAG == True:
                button3 = ttk.Button(self, text="Arrivals Delay",
                                    command=lambda: controller.show_frame(ArrivalDelay))
                button3.pack()

            df_Buffer = pd.DataFrame()
            df_Buffer['ADA_Buffer'] = df_sequence_output['ADA Buffer']
            df_Buffer = df_Buffer.dropna(subset = ['ADA_Buffer'])
            #df_Buffer = df_Buffer.drop([0])
            ADA_buffer = df_Buffer['ADA_Buffer'].tolist()
            a = int(min(ADA_buffer))
            b = int(max(ADA_buffer))
            number_bins = b-a
            h = [0]+sorted(ADA_buffer)
            # ba = [15,15]
            # bb = [0,0.013]
            # da = [0,15]
            # db = [0.013,0.013]

            coord = [[0,0], [15,0], [15,0.013], [0,0.013]]
            coord.append(coord[0]) #repeat the first point to create a 'closed loop'

            xs, ys = zip(*coord) #create lists of x and y values

            fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

            f = Figure(figsize=(5,5), dpi=100)
            A = f.add_subplot(111)
            A.plot(h,fit,'-o')
            A.hist(h,normed=True,bins=number_bins)
            # A.axvline(x=15, color='red', linestyle='--')
            # A.plot(da,db, color='red',linestyle='--')

            A.plot(xs,ys,"r")

            A.set_xlabel('SECONDS')
            A.set_ylabel('%')
            A.grid(color='b', linestyle='-', linewidth=0.1)
            # A.title('Throughput')
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    app = RAPIDvisual()

    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=1)

    app.mainloop()
