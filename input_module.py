import openpyxl
import time
import math
import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def runPreprocess(inputModule, app, filename):

    tdf = pd.read_csv(filename)

    """WARNING: mostly copied over from previous version, not yet tested"""

    f1 = ttk.Frame(inputModule)
    f2 = ttk.Frame(inputModule)
    f3 = ttk.Frame(inputModule)
    f4 = ttk.Frame(inputModule)
    f5 = ttk.Frame(inputModule)
    f6 = ttk.Frame(inputModule)

    for frame in (f1,f2):
        frame.grid(row=0, column=0, sticky='NWES')
        frame.columnconfigure(0, weight=0)
        frame.rowconfigure(0, weight=0)

    # AROT FRAME

    f1_help = ttk.LabelFrame(f1, text=" Quick Help ")
    f1_help.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    ttk.Label(f1_help, text="Section used to filter AROT data for when runway is 'Constrained'", font=12).grid(column=1, row=1, sticky='W')
    ttk.Label(f1_help, text="Select values for the demand and maximum AROT", font=12).grid(column=1, row=2, sticky='W')

    f1_content = tk.LabelFrame(f1, text="    AROT    ", font="Helvetica 14 bold")
    f1_content.grid(row=0, column=0, sticky='E', padx=10, pady=20, ipadx=5, ipady=5)

    #####################################################################
    #                             AROT DATA                             #
    #####################################################################

    Final_demand_output = tk.IntVar()
    AROT_output = tk.IntVar()

    columns_to_drop_AROT =['B1','DROT_Callsign','DROT_Line up time','DROT_Start to roll','DROT_Take off time','DROT_Runway Entry','DROT_Take off speed [kts]','DROT','DROT_Runway','DROT_Demand','DROT_Final Wake','DROT_Aircraft Type ICAO','DROT_SID (shortened)','B2','TAXI_OUT_S1','TAXI_OUT_S2','TAXI_OUT_S3','TAXI_OUT_S4','TAXI_OUT_S5','TAXI_OUT_S6','TAXI_OUT_S7','TAXI_OUT_S8','TAXI_OUT_S9','TAXI_OUT_S10','TAXI_OUT_S11','TAXI_OUT_S12','TAXI_OUT_S13','TAXI_OUT_S14','TAXI_OUT_S15','B3','TAXI_IN_S1','TAXI_IN_S2','TAXI_IN_S3','TAXI_IN_S4','TAXI_IN_S5','TAXI_IN_S6','TAXI_IN_S7','TAXI_IN_S8','TAXI_IN_S9','TAXI_IN_S10','TAXI_IN_S11','TAXI_IN_S12','TAXI_IN_S13','TAXI_IN_S14','TAXI_IN_S15','B4','ADA_id','ADA_ADA','ADA_Combined ROT','ADA_Buffer','ADA_Uniques','ADA_ADA counts','ADA_C_ROT counts','ADA_Buffer_Unique','ADA_Buffer_counts']
    df = tdf.drop(columns = columns_to_drop_AROT)

    # xl = pd.ExcelFile(airport_data)
    # xl = pd.ExcelFile("AROT_example_input.xlsx")

    # Find min max values
    max_demand = df['AROT_Demand'].max()
    min_demand = df['AROT_Demand'].min()
    # max_arot = df['AROT'].max()
    max_arot = 160 # Initialise to remove unrealistic outliers from data
    min_arot = df['AROT'].min()

    demand_output = min_demand
    arot_filter_output = max_arot

    def getThrottle(event):

        ax0.clear() # Needed otherwise creates a new series but old series remains - GG matplotlib...
        ax1.clear()
        ax2.clear()

        # Add titles back in every update...
        ax0.set_title('  Filter data by Runway Demand & max AROT ')
        ax0.set_ylabel('Aircraft Count')

        demand_output = Throttle.get()
        arot_filter_output = Throttle_arot.get()

        df_demand = df.loc[df['AROT_Demand'] >= demand_output]
        df_filtered = df_demand.loc[df_demand['AROT'] <= arot_filter_output]

        ## Update label value ##
        ttk.Label(DemandInputFrame, text=str(round((len(df_filtered.index) / total_df_entries)*100,2))).grid(column=2, row=3, sticky='N')

        ########## CHANGE ###
        df_plots = df_filtered.groupby(['AROT_Runway', 'AROT'])['AROT_Callsign'].count()
        df_plots = df_plots.reset_index(level=[0,1])
        df_plots.pivot(index='AROT', columns='AROT_Runway', values='AROT_Callsign').plot(kind='line', ax=ax0)
        #####################

        df_plots2 = df_filtered.groupby(['AROT_Runway', 'AROT_Final Wake'])['AROT_Callsign'].count()
        df_plots2 = df_plots2.reset_index(level=[0,1])
        df_plots2 = df_plots2.sort_values(by=['AROT_Runway', 'AROT_Final Wake', 'AROT_Callsign'], ascending=True)

        arrival_wakes = df_plots2['AROT_Final Wake'].unique()
        arrival_wakes = arrival_wakes.tolist()

        df_plots2.pivot(index='AROT_Final Wake', columns='AROT_Runway', values='AROT_Callsign').plot(kind='pie', ax=ax1, subplots=True, labels=arrival_wakes, autopct='%1.1f%%', shadow=False, startangle=90)

        df_plots3 = df_filtered.groupby(['AROT_Runway', 'AROT_RwyExit'])['AROT_Callsign'].count()
        df_plots3 = df_plots3.reset_index(level=[0,1])
        df_plots3 = df_plots3.pivot(index='AROT_RwyExit', columns='AROT_Runway', values='AROT_Callsign').fillna(0).plot(kind='bar', subplots=True, ax=ax2)
        plt.show()

        canvas.draw()
        canvas1.draw()
        canvas2.draw()


    def define_final_AROT():
        # Final_max_arot = 330
        # Final_demand = 45
        Final_demand = Throttle.get()
        Final_demand_output.set(Final_demand)
        Final_max_arot = Throttle_arot.get()
        # Final_max_arot = arot_filter.get() # Old method (takes last value entered)
        print("AROT=", Final_max_arot, "Demand=", Final_demand)
        # print(Final_max_arot)
        AROT_output.set(Final_max_arot)
        button_check.set(True)

        ##AROT filtering + save it it a data frame rady to be exported to file

        df_final_AROT = pd.DataFrame()
        df_final_AROT_H = pd.DataFrame()
        df_final_AROT_M = pd.DataFrame()
        df_final_AROT_L = pd.DataFrame()
        df_final_AROT_UM = pd.DataFrame()
        df_final_AROT_J = pd.DataFrame()
        df_final_AROT_S = pd.DataFrame()

        df_final_AROT_H['AROT_H'] = ""
        df_final_AROT_H['AROT_H'] = df.loc[(df['AROT']<=Final_max_arot) & (df['AROT_Demand']>=Final_demand)& (df['AROT_Final Wake']=="H"),'AROT']
        df_final_AROT_H=df_final_AROT_H.reset_index()
        df_final_AROT_H = df_final_AROT_H.drop(columns='index')

        df_final_AROT_M['AROT_M'] = ""
        df_final_AROT_M['AROT_M'] = df.loc[(df['AROT']<=Final_max_arot) & (df['AROT_Demand']>=Final_demand)& (df['AROT_Final Wake']=="M"),'AROT']
        df_final_AROT_M=df_final_AROT_M.reset_index()
        df_final_AROT_M = df_final_AROT_M.drop(columns='index')

        df_final_AROT_L['AROT_L'] = ""
        df_final_AROT_L['AROT_L'] = df.loc[(df['AROT']<=Final_max_arot) & (df['AROT_Demand']>=Final_demand)& (df['AROT_Final Wake']=="L"),'AROT']
        df_final_AROT_L=df_final_AROT_L.reset_index()
        df_final_AROT_L = df_final_AROT_L.drop(columns='index')

        df_final_AROT_UM['AROT_UM'] = ""
        df_final_AROT_UM['AROT_UM'] = df.loc[(df['AROT']<=Final_max_arot) & (df['AROT_Demand']>=Final_demand)& (df['AROT_Final Wake']=="UM"),'AROT']
        df_final_AROT_UM=df_final_AROT_UM.reset_index()
        df_final_AROT_UM = df_final_AROT_UM.drop(columns='index')

        df_final_AROT_J['AROT_J'] = ""
        df_final_AROT_J['AROT_J'] = df.loc[(df['AROT']<=Final_max_arot) & (df['AROT_Demand']>=Final_demand)& (df['AROT_Final Wake']=="J"),'AROT']
        df_final_AROT_J=df_final_AROT_J.reset_index()
        df_final_AROT_J = df_final_AROT_J.drop(columns='index')

        df_final_AROT_S['AROT_S'] = ""
        df_final_AROT_S['AROT_S'] = df.loc[(df['AROT']<=Final_max_arot) & (df['AROT_Demand']>=Final_demand)& (df['AROT_Final Wake']=="S"),'AROT']
        df_final_AROT_S=df_final_AROT_S.reset_index()
        df_final_AROT_S = df_final_AROT_S.drop(columns='index')

        frames_AROT = [df_final_AROT_H, df_final_AROT_M,df_final_AROT_L,df_final_AROT_UM,df_final_AROT_J,df_final_AROT_S]

        df_final_AROT = pd.concat(frames_AROT, axis=1)
        return df_final_AROT


    def define_arot_parameters():
        df_final_AROT = define_final_AROT()
        print("AROTs defined | Filters AROT = ", Throttle_arot.get(), "Demand=", Throttle.get())
        # print('inside the NEXT function = ', df_final_AROT)
        ttk.Label(inner, text=" AROT Data Exported!  ").grid(column=1, row=2, sticky='N', pady=10)
        f2.tkraise()

        return df_final_AROT
        # window.destroy()


    # Specify GUI Structure -------->
    DemandInputFrame = tk.LabelFrame(f1_content, text="    Filter data based on the Demand    ", font="Helvetica 12")
    DemandInputFrame.grid(row=0, column=1, columnspan=1, sticky='N', padx=5, pady=10, ipadx=5, ipady=5)


    AROTInputFrame = tk.LabelFrame(f1_content, text="    Filter data based on max. AROT    ", font="Helvetica 12")
    AROTInputFrame.grid(row=0, column=4, columnspan=7, sticky='N', padx=5, pady=10, ipadx=5, ipady=5)

    ResultsFrame = tk.LabelFrame(f1_content, text="   [  Results :  ]   ", font="Helvetica 12")
    ResultsFrame.grid(row=1, columnspan=14, sticky='N', padx=5, pady=5, ipadx=5, ipady=5)

    # Defines expected inputs (i.e. GUI expects integers) and assigns default values
    demand_input = tk.IntVar(f1_content, value=min_demand)
    arot_filter = tk.IntVar(f1_content, value=max_arot)
    button_check = tk.StringVar(f1_content, value='0')

    # OLD Filter for AROT
    # input_entry1 = ttk.Entry(AROTInputFrame, width=7, textvariable=arot_filter)
    # input_entry1.grid(row=1, column=2, sticky='N', padx=5, pady=35)

    ################## matplotlib figure ##################
    fig0 = plt.Figure()
    canvas = FigureCanvasTkAgg(fig0, ResultsFrame)
    canvas.get_tk_widget().grid(column=1, row=1, sticky='N', rowspan=2, padx=5, pady=5)
    ax0 = fig0.add_subplot(111)
    ax0.set_title('  Filter data by Runway Demand & max AROT ')
    ax0.set_ylabel('Aircraft Count')

    fig1 = plt.Figure(figsize=(6,2.8))
    canvas1 = FigureCanvasTkAgg(fig1, ResultsFrame)
    canvas1.get_tk_widget().grid(column=2, row=1, sticky='N', padx=5, pady=5)
    ax1 = fig1.add_subplot(111, aspect=1) #aspect=1 #aspect='equal'
    # ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    fig2 = plt.Figure(figsize=(6,2.8))
    canvas2 = FigureCanvasTkAgg(fig2, ResultsFrame)
    canvas2.get_tk_widget().grid(column=2, row=2, sticky='N', padx=5, pady=5)
    ax2 = fig2.add_subplot(111) #aspect=1 #aspect='equal'
    fig2.subplots_adjust(hspace=0.4)

    ResultsFrame.columnconfigure(1, weight=1)
    ResultsFrame.columnconfigure(2, weight=1)
    ResultsFrame.rowconfigure(1, weight=1)
    ResultsFrame.rowconfigure(2, weight=1)

    # PLOT Initialisation

    ############ CHANGE #####
    df_demand = df.loc[df['AROT_Demand'] >= min_demand]
    df_filtered = df_demand.loc[df_demand['AROT'] <= max_arot]

    total_df_entries = len(df_filtered.index)

    df_plots = df_filtered.groupby(['AROT_Runway', 'AROT'])['AROT_Callsign'].count()
    df_plots = df_plots.reset_index(level=[0,1])
    df_plots.pivot(index='AROT', columns='AROT_Runway', values='AROT_Callsign').plot(kind='line', ax=ax0)
    #########################

    df_plots2 = df_demand.groupby(['AROT_Runway', 'AROT_Final Wake'])['AROT_Callsign'].count()
    df_plots2 = df_plots2.reset_index(level=[0,1])

    arrival_wakes = df_plots2['AROT_Final Wake'].unique()
    arrival_wakes = arrival_wakes.tolist()

    df_plots2.pivot(index='AROT_Final Wake', columns='AROT_Runway', values='AROT_Callsign').plot(kind='pie', subplots=True, ax=ax1, labels=arrival_wakes, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    df_plots3 = df_demand.groupby(['AROT_Runway', 'AROT_RwyExit'])['AROT_Callsign'].count()
    df_plots3 = df_plots3.reset_index(level=[0,1])
    df_plots3 = df_plots3.pivot(index='AROT_RwyExit', columns='AROT_Runway', values='AROT_Callsign').fillna(0).plot(kind='bar', subplots=True, ax=ax2)

    ttk.Label(DemandInputFrame, text=" Select a 'Demand value' from the Input file ->  ", font="Helvetica 10").grid(row=1, column=1, sticky='W', padx=140)

    Throttle = tk.Scale(DemandInputFrame, from_=min_demand, to=max_demand, width=10, orient=tk.HORIZONTAL, tickinterval=5, command=getThrottle)#variable = var)
    Throttle.grid(row=2, column=1, sticky='EW', padx=5)
    Throttle.set(0)

    Throttle_arot = tk.Scale(AROTInputFrame, from_=min_arot, to=max_arot, width=10, orient=tk.HORIZONTAL, tickinterval=20, command=getThrottle)#variable = var)
    Throttle_arot.grid(row=2, column=1, sticky='EW', padx=5)
    Throttle_arot.set(max_arot)

    ttk.Label(DemandInputFrame, text=" Percentage of original entries = ", font="Helvetica 10").grid(row=3, column=1, sticky='N', padx=5)
    ttk.Label(AROTInputFrame, text="      Select a Max. value for AROT ->             ", font="Helvetica 10").grid(row=1, column=1, sticky='N', padx=240)

    # =============================================================================
    #         DemandInputFrame.columnconfigure(1, weight=1)
    #         DemandInputFrame.rowconfigure(0, weight=1)
    #         DemandInputFrame.rowconfigure(1, weight=1)
    #         DemandInputFrame.rowconfigure(2, weight=1)
    #         DemandInputFrame.rowconfigure(3, weight=1)
    #
    #         AROTInputFrame.columnconfigure(1, weight=1)
    #         AROTInputFrame.rowconfigure(0, weight=1)
    #         AROTInputFrame.rowconfigure(1, weight=1)
    #         AROTInputFrame.rowconfigure(2, weight=1)
    #         AROTInputFrame.rowconfigure(3, weight=1)
    # =============================================================================

    # f1_content.columnconfigure(0, weight=0)
    # f1_content.rowconfigure(0, weight=0)

    # f1_help.columnconfigure(1, weight=0)
    # f1_help.rowconfigure(0, weight=0)
    # f1_help.rowconfigure(1, weight=0)

    # f1_content.columnconfigure(0, weight=1)
    # f1_content.columnconfigure(1, weight=1)
    # f1_content.columnconfigure(4, weight=1)
    # f1_content.rowconfigure(0, weight=1)
    # f1_content.rowconfigure(1, weight=1)

    # inner = tk.LabelFrame(f1_content, bg='pink')
    inner = tk.Frame(f1_content)
    inner.grid(row=2, column=1, sticky='E', padx=5, pady=10, ipadx=15, ipady=15)

    inner.grid_rowconfigure(0, weight=1)
    inner.grid_rowconfigure(2, weight=1)
    inner.grid_columnconfigure(0, weight=1)
    inner.grid_columnconfigure(2, weight=1)

    # ttk.Button(inner, text="Confirm Settings and Save", command=define_arot_parameters).grid(column=1, row=1, sticky='N', ipadx=5, ipady=5)
    tk.Button(inner, text='Confirm Settings and Save | NEXT ->', command=define_arot_parameters, activebackground = "pink", font=16, height = 1, overrelief="raised", width = 30).grid(column=1, row=1, sticky='N', ipadx=5, ipady=5)

    f1_content.bind('<Return>', define_arot_parameters)

    # DROT FRAME ###############################################################################################

    f2_help = ttk.LabelFrame(f2, text=" Quick Help ")
    f2_help.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    ttk.Label(f2_help, text="Section used to filter DROT data for when runway is 'Constrained'", font=12).grid(column=1, row=1, sticky='W')
    ttk.Label(f2_help, text="Select values for the demand and maximum DROT", font=12).grid(column=1, row=2, sticky='W')

    f2_content = tk.LabelFrame(f2, text="    DROT    ", font="Helvetica 14 bold")
    f2_content.grid(row=0, column=0, sticky='E', padx=10, pady=20, ipadx=5, ipady=5)
    # ttk.Label(f2_content, text="DROT Content...", font=16).grid(column=1, row=1, sticky='W')

    #####################################################################
    #                             DROT DATA                             #
    #####################################################################

    columns_to_drop_drot = ['AROT_Callsign','AROT_Threshold','AROT_RWY exit time','AROT','AROT_Runway','AROT_Demand','AROT_Final Wake','AROT_RwyExit','AROT_Aircraft Type ICAO','AROT_Threshold Speed [kts]','AROT_Speed @ TDZ [kts]','AROT_RWY Exit Speed 1','AROT_RWY Exit Speed 2','AROT_RWY Exit Speed 3','B1','B2','TAXI_OUT_S1','TAXI_OUT_S2','TAXI_OUT_S3','TAXI_OUT_S4','TAXI_OUT_S5','TAXI_OUT_S6','TAXI_OUT_S7','TAXI_OUT_S8','TAXI_OUT_S9','TAXI_OUT_S10','TAXI_OUT_S11','TAXI_OUT_S12','TAXI_OUT_S13','TAXI_OUT_S14','TAXI_OUT_S15','B3','TAXI_IN_S1','TAXI_IN_S2','TAXI_IN_S3','TAXI_IN_S4','TAXI_IN_S5','TAXI_IN_S6','TAXI_IN_S7','TAXI_IN_S8','TAXI_IN_S9','TAXI_IN_S10','TAXI_IN_S11','TAXI_IN_S12','TAXI_IN_S13','TAXI_IN_S14','TAXI_IN_S15','B4','ADA_id','ADA_ADA','ADA_Combined ROT','ADA_Buffer','ADA_Uniques','ADA_ADA counts','ADA_C_ROT counts','ADA_Buffer_Unique','ADA_Buffer_counts']
    df_drot = tdf.drop(columns = columns_to_drop_drot)

    Final_demand_output_d = tk.IntVar()
    DROT_output = tk.IntVar()

    # Find min max values
    d_max_demand = df_drot['DROT_Demand'].max()
    d_min_demand = df_drot['DROT_Demand'].min()

    max_drot = 160 # Initialise to remove unrealistic outliers from data
    min_drot = df_drot['DROT'].min()

    # total_drot_entries = len(df_drot.index)

    drot_demand_output = d_min_demand
    drot_filter_output = max_drot

    #####################################################################
    #                             DROT GUI                              #
    #####################################################################

    def getThrottle_d(event):

        ax4.clear() #ax
        ax5.clear() #ax1
        ax6.clear() #ax2

        # Add titles back in every update...
        ax4.set_title('  Filter data by Runway Demand & max DROT ')
        ax4.set_ylabel('Aircraft Count')

        drot_demand_output = Throttle_d.get()
        drot_filter_output = Throttle_drot.get()

        df_drot_demand = df_drot.loc[df_drot['DROT_Demand'] >= drot_demand_output]
        df_drot_filtered = df_drot_demand.loc[df_drot_demand['DROT'] <= drot_filter_output]

        ## Update label value ##
        ttk.Label(DemandInputFrame_d, text=str(round((len(df_drot_filtered.index) / total_drot_entries)*100,2))).grid(column=2, row=3, sticky='N')

        ########## CHANGE ###
        df_plots_d = df_drot_filtered.groupby(['DROT_Runway', 'DROT'])['DROT_Callsign'].count()
        df_plots_d = df_plots_d.reset_index(level=[0,1])
        df_plots_d.pivot(index='DROT', columns='DROT_Runway', values='DROT_Callsign').plot(kind='line', ax=ax4)
        #####################

        df_plots2_d = df_drot_filtered.groupby(['DROT_Runway', 'DROT_Final Wake'])['DROT_Callsign'].count()
        df_plots2_d = df_plots2_d.reset_index(level=[0,1])
        df_plots2_d = df_plots2_d.sort_values(by=['DROT_Runway', 'DROT_Final Wake', 'DROT_Callsign'], ascending=True)

        dep_wakes = df_plots2_d['DROT_Final Wake'].unique()
        dep_wakes = dep_wakes.tolist()

        df_plots2_d.pivot(index='DROT_Final Wake', columns='DROT_Runway', values='DROT_Callsign').plot(kind='pie', ax=ax5, subplots=True, labels=dep_wakes, autopct='%1.1f%%', shadow=False, startangle=90)
        ax5.axis('equal')

        df_plots3_d = df_drot_filtered.groupby(['DROT_Runway', 'DROT_SID (shortened)'])['DROT_Callsign'].count()
        df_plots3_d = df_plots3_d.reset_index(level=[0,1])
        ######### OPTION ONE - DOUBLE BAR CHART ##############
        # df_plots3_d = df_plots3_d.pivot(index='SID (shortened)', columns='Runway', values='Callsign').fillna(0).plot(kind='bar', subplots=True, ax=ax6)

        ######### OPTION TWO - DOUBLE PIE CHART ##############
        dep_SIDs = df_plots3_d['DROT_SID (shortened)'].unique()
        dep_SIDs = dep_SIDs.tolist()
        df_plots3_d = df_plots3_d.rename(columns = {'DROT_SID (shortened)':'DROT_SID'})
        df_plots3_d.pivot(index='DROT_SID', columns='DROT_Runway', values='DROT_Callsign').plot(kind='pie', subplots=True, ax=ax6, labels=dep_SIDs, autopct='%1.1f%%', legend=False, startangle=90)
        ax6.axis('equal')

        plt.show()

        canvas4.draw() #canvas
        canvas5.draw() #canvas1
        canvas6.draw() #canvas2


    def define_final_DROT():
        # Final_max_DROT = 3330
        # Final_demand_d = 45
        Final_demand_d = Throttle_d.get()
        Final_demand_output_d.set(Final_demand_d)
        Final_max_DROT = Throttle_drot.get()
        print("DROT=", Final_max_DROT, "Demand=", Final_demand_d)
        DROT_output.set(Final_max_DROT)
        button_check_d.set(True)

        # DROT filtering + save it it a data frame ready to be exported to file
        df_final_DROT = pd.DataFrame()
        df_final_DROT_H = pd.DataFrame()
        df_final_DROT_M = pd.DataFrame()
        df_final_DROT_L = pd.DataFrame()
        df_final_DROT_UM = pd.DataFrame()
        df_final_DROT_J = pd.DataFrame()
        df_final_DROT_S = pd.DataFrame()

        # F
        df_final_DROT_H['DROT_H'] = ""
        df_final_DROT_H['DROT_H'] = df_drot.loc[(df_drot['DROT']<=Final_max_DROT) & (df_drot['DROT_Demand']>=Final_demand_d)& (df_drot['DROT_Final Wake']=="H"),'DROT']
        df_final_DROT_H=df_final_DROT_H.reset_index()
        df_final_DROT_H = df_final_DROT_H.drop(columns='index')

        df_final_DROT_M['DROT_M'] = ""
        df_final_DROT_M['DROT_M'] = df_drot.loc[(df_drot['DROT']<=Final_max_DROT) & (df_drot['DROT_Demand']>=Final_demand_d)& (df_drot['DROT_Final Wake']=="M"),'DROT']
        df_final_DROT_M=df_final_DROT_M.reset_index()
        df_final_DROT_M = df_final_DROT_M.drop(columns='index')

        df_final_DROT_L['DROT_L'] = ""
        df_final_DROT_L['DROT_L'] = df_drot.loc[(df_drot['DROT']<=Final_max_DROT) & (df_drot['DROT_Demand']>=Final_demand_d)& (df_drot['DROT_Final Wake']=="L"),'DROT']
        df_final_DROT_L=df_final_DROT_L.reset_index()
        df_final_DROT_L = df_final_DROT_L.drop(columns='index')

        df_final_DROT_UM['DROT_UM'] = ""
        df_final_DROT_UM['DROT_UM'] = df_drot.loc[(df_drot['DROT']<=Final_max_DROT) & (df_drot['DROT_Demand']>=Final_demand_d)& (df_drot['DROT_Final Wake']=="UM"),'DROT']
        df_final_DROT_UM=df_final_DROT_UM.reset_index()
        df_final_DROT_UM = df_final_DROT_UM.drop(columns='index')

        df_final_DROT_J['DROT_J'] = ""
        df_final_DROT_J['DROT_J'] = df_drot.loc[(df_drot['DROT']<=Final_max_DROT) & (df_drot['DROT_Demand']>=Final_demand_d)& (df_drot['DROT_Final Wake']=="J"),'DROT']
        df_final_DROT_J=df_final_DROT_J.reset_index()
        df_final_DROT_J = df_final_DROT_J.drop(columns='index')

        df_final_DROT_S['DROT_S'] = ""
        df_final_DROT_S['DROT_S'] = df_drot.loc[(df_drot['DROT']<=Final_max_DROT) & (df_drot['DROT_Demand']>=Final_demand_d)& (df_drot['DROT_Final Wake']=="S"),'DROT']
        df_final_DROT_S=df_final_DROT_S.reset_index()
        df_final_DROT_S = df_final_DROT_S.drop(columns='index')

        frames_DROT = [df_final_DROT_H, df_final_DROT_M,df_final_DROT_L,df_final_DROT_UM,df_final_DROT_J,df_final_DROT_S]

        df_final_DROT = pd.concat(frames_DROT, axis=1)
        return df_final_DROT


    def define_drot_parameters():
        df_final_DROT = define_final_DROT()
        #ttk.Label(inner_d, text=" DROT Data Exported!  ").grid(column=1, row=2, sticky='N', pady=10) # Grids are banned FNAR!
        print("DROTs defined | Filters DROT = ", Throttle_drot.get(), "Demand=", Throttle_d.get())
        ttk.Label(inner_d, text=" DROT Data Exported!  ").pack(side="right")
        f5.tkraise()
        return df_final_DROT
        # window.destroy()


    # Specify GUI Structure -------->
    DemandInputFrame_d = tk.LabelFrame(f2_content, text="   Filter data based on the Demand   ", font="Helvetica 12")
    DemandInputFrame_d.grid(row=0, column=1, columnspan=1, sticky='N', padx=5, pady=10, ipadx=5, ipady=5)

    DROTInputFrame = tk.LabelFrame(f2_content, text="Filter data by max. DROT     ", font="Helvetica 12")
    DROTInputFrame.grid(row=0, column=4, columnspan=7, sticky='N', padx=10, pady=10, ipadx=5, ipady=5)

    ResultsFrame_d = tk.LabelFrame(f2_content, text="  [  Results :  ]   ", font="Helvetica 12")
    ResultsFrame_d.grid(row=1, columnspan=14, sticky='N', padx=5, pady=5, ipadx=5, ipady=5)

    # Defines expected inputs (i.e. GUI expects integers) and assigns default values
    demand_input_d = tk.IntVar(f2_content, value=d_min_demand)
    drot_filter = tk.IntVar(f2_content, value=max_drot)
    button_check_d = tk.StringVar(f2_content, value='0')

    # OLD METHOD for Filtering DROT
    # in_max_drot = df_drot['DROT'].max()
    # input_entry1_d = ttk.Entry(DROTInputFrame, width=7, textvariable=drot_filter)
    # input_entry1_d.grid(row=1, column=2, sticky='N', padx=10, pady=35)

    # matplotlib figures
    fig_d = plt.Figure()
    canvas4 = FigureCanvasTkAgg(fig_d, ResultsFrame_d)
    canvas4.get_tk_widget().grid(column=1, row=1, sticky='N', rowspan=2, padx=5, pady=5)
    ax4 = fig_d.add_subplot(111)
    ax4.set_title('  Filter data by Runway Demand & max DROT ')
    ax4.set_ylabel('Aircraft Count')

    fig1_d = plt.Figure(figsize=(6,2.8))
    canvas5 = FigureCanvasTkAgg(fig1_d, ResultsFrame_d)
    canvas5.get_tk_widget().grid(column=2, row=1, sticky='N', padx=5, pady=5)
    ax5 = fig1_d.add_subplot(111, aspect=1)

    fig2_d = plt.Figure(figsize=(6,2.8))
    canvas6 = FigureCanvasTkAgg(fig2_d, ResultsFrame_d)
    canvas6.get_tk_widget().grid(column=2, row=2, sticky='N', padx=5, pady=5)
    ax6 = fig2_d.add_subplot(111)
    fig2_d.subplots_adjust(hspace=0.4)

    # PLOT Initialisation

    ########## CHANGE ###
    df_drot_demand = df_drot.loc[df_drot['DROT_Demand'] >= d_min_demand]
    df_drot_filtered = df_drot_demand.loc[df_drot_demand['DROT'] <= max_drot]

    total_drot_entries = len(df_drot_filtered.index)

    df_plots_d = df_drot_filtered.groupby(['DROT_Runway', 'DROT'])['DROT_Callsign'].count()
    df_plots_d = df_plots_d.reset_index(level=[0,1])
    df_plots_d.pivot(index='DROT', columns='DROT_Runway', values='DROT_Callsign').plot(kind='line', ax=ax4)
    #####################

    df_plots2_d = df_drot_filtered.groupby(['DROT_Runway', 'DROT_Final Wake'])['DROT_Callsign'].count()
    df_plots2_d = df_plots2_d.reset_index(level=[0,1])

    dep_wakes = df_plots2_d['DROT_Final Wake'].unique()
    dep_wakes = dep_wakes.tolist()

    df_plots2_d.pivot(index='DROT_Final Wake', columns='DROT_Runway', values='DROT_Callsign').plot(kind='pie', subplots=True, ax=ax5, labels=dep_wakes, autopct='%1.1f%%', startangle=90)
    ax5.axis('equal')

    df_plots3_d = df_drot_filtered.groupby(['DROT_Runway', 'DROT_SID (shortened)'])['DROT_Callsign'].count()
    df_plots3_d = df_plots3_d.reset_index(level=[0,1])
    ######### OPTION ONE - DOUBLE BAR CHART ##############

    ######### OPTION TWO - DOUBLE PIE CHART ##############
    dep_SIDs = df_plots3_d['DROT_SID (shortened)'].unique()
    dep_SIDs = dep_SIDs.tolist()
    df_plots3_d = df_plots3_d.rename(columns = {'DROT_SID (shortened)':'DROT_SID'})
    df_plots3_d.pivot(index='DROT_SID', columns='DROT_Runway', values='DROT_Callsign').plot(kind='pie', subplots=True, ax=ax6, labels=dep_SIDs, autopct='%1.1f%%', legend=False, startangle=90)
    ax6.axis('equal')

    ######################################################

    ttk.Label(DemandInputFrame_d, text="Select a 'Demand value' from the Input file ->", font="Helvetica 10").grid(row=1, column=1, sticky='W', padx=140)

    Throttle_d = tk.Scale(DemandInputFrame_d, from_=d_min_demand, to=d_max_demand, width=10, orient=tk.HORIZONTAL, tickinterval=5, command=getThrottle_d)#variable = var)
    Throttle_d.grid(row=2, column=1, sticky='EW', padx=5)
    Throttle_d.set(0)

    Throttle_drot = tk.Scale(DROTInputFrame, from_=min_drot, to=max_drot, width=10, orient=tk.HORIZONTAL, tickinterval=20, command=getThrottle_d)#variable = var)
    Throttle_drot.grid(row=2, column=1, sticky='EW', padx=5)
    Throttle_drot.set(max_drot)

    ttk.Label(DemandInputFrame_d, text="  Percentage of original entries =  ", font="Helvetica 10").grid(row=3, column=1, sticky='N', padx=5)
    ttk.Label(DROTInputFrame, text="      Select a Max. value for DROT ->             ", font="Helvetica 10").grid(row=1, column=1, sticky='N', padx=240)

    inner_d = tk.Frame(f2_content)
    inner_d.grid(row=2, column=1, sticky='E', padx=5, pady=10, ipadx=15, ipady=15)

    inner_d.grid_rowconfigure(0, weight=1)
    inner_d.grid_rowconfigure(2, weight=1)
    inner_d.grid_columnconfigure(0, weight=1)
    inner_d.grid_columnconfigure(2, weight=1)


    tk.Button(inner_d, text='Confirm Settings and Save | NEXT ->', command=define_drot_parameters, activebackground = "pink", font=16, height = 1, overrelief="raised", width = 30).pack(side="right")
    tk.Button(inner_d, text='<- BACK', command=lambda: f1.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")
    f2_content.bind('<Return>', define_drot_parameters)

    # TAXI-OUT FRAME #############################################################################################

    # f3_help = ttk.LabelFrame(f3, text=" Quick Help ")
    # f3_help.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    # ttk.Label(f3_help, text="Provides example analysis for Taxi-out distribution", font=12).grid(column=1, row=1, sticky='W')
    # ttk.Label(f3_help, text="Note the analysis only considers:", font=12).grid(column=1, row=2, sticky='W')
    # ttk.Label(f3_help, text="  - 'Medium' wake aircraft", font=12).grid(column=1, row=3, sticky='W')

    # f3_buttons= ttk.Frame(f3)
    # f3_buttons.grid(column = 0, row=1, columnspan = 7, sticky='NWES')

    # tk.Button(f3_buttons, text='NEXT ->', command=lambda: f4.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")
    # tk.Button(f3_buttons, text='<- BACK', command=lambda: f2.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")

    # f3_content = tk.LabelFrame(f3, text=" TAXI-OUT ", font="Helvetica 14 bold")
    # f3_content.grid(row=0, column=0, sticky='E', padx=10, pady=40, ipadx=5, ipady=10)

    # columns_to_drop_taxi_out = ['AROT_Callsign','AROT_Threshold','AROT_RWY exit time','AROT','AROT_Runway','AROT_Demand','AROT_Final Wake','AROT_RwyExit','AROT_Aircraft Type ICAO','AROT_Threshold Speed [kts]','AROT_Speed @ TDZ [kts]','AROT_RWY Exit Speed 1','AROT_RWY Exit Speed 2','AROT_RWY Exit Speed 3','B1','DROT_Callsign','DROT_Line up time','DROT_Start to roll','DROT_Take off time','DROT_Runway Entry','DROT_Take off speed [kts]','DROT','DROT_Runway','DROT_Demand','DROT_Final Wake','DROT_Aircraft Type ICAO','DROT_SID (shortened)','B2','B3','TAXI_IN_S1','TAXI_IN_S2','TAXI_IN_S3','TAXI_IN_S4','TAXI_IN_S5','TAXI_IN_S6','TAXI_IN_S7','TAXI_IN_S8','TAXI_IN_S9','TAXI_IN_S10','TAXI_IN_S11','TAXI_IN_S12','TAXI_IN_S13','TAXI_IN_S14','TAXI_IN_S15','B4','ADA_id','ADA_ADA','ADA_Combined ROT','ADA_Buffer','ADA_Uniques','ADA_ADA counts','ADA_C_ROT counts','ADA_Buffer_Unique','ADA_Buffer_counts']
    # df_final_TAXIOUT = tdf.drop(columns=columns_to_drop_taxi_out)
    # df_taxi_out = df_final_TAXIOUT.rename(columns = {'TAXI_OUT_S1':'S1','TAXI_OUT_S2':'S2','TAXI_OUT_S3':'S3','TAXI_OUT_S4':'S4','TAXI_OUT_S5':'S5','TAXI_OUT_S6':'S6','TAXI_OUT_S7':'S7','TAXI_OUT_S8':'S8','TAXI_OUT_S9':'S9','TAXI_OUT_S10':'S10','TAXI_OUT_S11':'S11','TAXI_OUT_S12':'S12','TAXI_OUT_S13':'S13','TAXI_OUT_S14':'S14','TAXI_OUT_S15':'S15'})

    # TOUT_output = tk.IntVar()

    # max_tout = df_taxi_out['S1'].max() #160 # Initialise to remove unrealistic outliers from data
    # min_tout = df_taxi_out['S1'].min()

    # TOUT_filter_output = max_tout

    # def getThrottle_to(event):

    #     ax92.clear() #ax

    #     ax92.set_title('  Taxi-out distribution example - Runway Direction = 26L, All Mediums ')
    #     ax92.set_xlabel(' Taxi-out time (secs) ')
    #     ax92.set_ylabel(' Aircraft count ')

    #     TOUT_filter_output = Throttle_tout.get()

    #     df_tout_filtered = df_taxi_out.loc[df_taxi_out['S1'] <= TOUT_filter_output]

    #     df_tout_filtered['S1'].plot(kind='hist', bins=100, rwidth=0.7, ax=ax92)

    #     plt.show()

    #     canvas92.draw() #canvas ax92.clear() #ax


    # ResultsFrame_tout = tk.LabelFrame(f3_content, text="  [  Taxi-out Results :  ]  ", font="Helvetica 12")
    # ResultsFrame_tout.grid(row=1, columnspan=14, sticky='N', padx=5, pady=15, ipadx=5, ipady=5)

    # ttk.Label(ResultsFrame_tout, text="      Analysis of 2017 Summer Data from Airport X :  ", font="Helvetica 12").grid(column=1, row=0, sticky='N', pady=10, padx=20)

    # fig_tout = plt.Figure()
    # canvas9 = FigureCanvasTkAgg(fig_tout, ResultsFrame_tout)
    # canvas9.get_tk_widget().grid(column=1, row=1, sticky='N', padx=5, pady=5)
    # ax9 = fig_tout.add_subplot(111)
    # ax9.set_title('  Taxi-out movements shown for Runway Direction = 26L ')
    # ax9.set_xlabel('Wake Category = [ Medium ] ')
    # ax9.set_ylabel('Time (secs)')

    # df_taxi_out.plot(kind='box', ax=ax9)

    # ## EXTRA Taxi-out plots!

    # fig_tout_2 = plt.Figure()
    # canvas92 = FigureCanvasTkAgg(fig_tout_2, ResultsFrame_tout)
    # canvas92.get_tk_widget().grid(column=2, row=1, sticky='N', padx=5, pady=5)
    # ax92 = fig_tout_2.add_subplot(111)
    # ax92.set_title('  Taxi-out distribution example - Runway Direction = 26L, All Mediums ')
    # ax92.set_xlabel(' Taxi-out time (secs) ')
    # ax92.set_ylabel(' Aircraft count ')

    # #df_taxi_out.plot(kind='box', ax=ax92)

    # df_taxi_out['S1'].plot(kind='hist', bins=100, rwidth=0.7, ax=ax92)

    # ttk.Label(ResultsFrame_tout, text="   Filter by Max. Taxi-out value ->     ", font="Helvetica 10").grid(row=2, column=2, sticky='N', padx=5, pady=10)

    # Throttle_tout = tk.Scale(ResultsFrame_tout, from_=min_tout, to=max_tout, width=10, orient=tk.HORIZONTAL, tickinterval=100, command=getThrottle_to)#variable = var)
    # Throttle_tout.grid(row=3, column=2, sticky='EW', padx=5)
    # Throttle_tout.set(max_tout)

    # # TAXI-IN FRAME #############################################################################################

    # f4_help = ttk.LabelFrame(f4, text=" Quick Help ")
    # f4_help.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    # ttk.Label(f4_help, text="Provides example analysis for Taxi-in distribution", font=12).grid(column=1, row=1, sticky='W')
    # ttk.Label(f4_help, text="Note the analysis only considers:", font=12).grid(column=1, row=2, sticky='W')
    # ttk.Label(f4_help, text="  - 'Medium' wake aircraft", font=12).grid(column=1, row=3, sticky='W')

    # f4_buttons= ttk.Frame(f4)
    # f4_buttons.grid(column = 0, row=1, columnspan = 7, sticky='NWES')

    # tk.Button(f4_buttons, text='NEXT ->', command=lambda: f5.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")
    # tk.Button(f4_buttons, text='<- BACK', command=lambda: f3.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")

    # f4_content = tk.LabelFrame(f4, text=" TAXI-IN ", font="Helvetica 14 bold")
    # f4_content.grid(row=0, column=0, sticky='E', padx=10, pady=40, ipadx=5, ipady=10)

    # columns_to_drop_taxi_in = ['AROT_Callsign','AROT_Threshold','AROT_RWY exit time','AROT','AROT_Runway','AROT_Demand','AROT_Final Wake','AROT_RwyExit','AROT_Aircraft Type ICAO','AROT_Threshold Speed [kts]','AROT_Speed @ TDZ [kts]','AROT_RWY Exit Speed 1','AROT_RWY Exit Speed 2','AROT_RWY Exit Speed 3','B1','DROT_Callsign','DROT_Line up time','DROT_Start to roll','DROT_Take off time','DROT_Runway Entry','DROT_Take off speed [kts]','DROT','DROT_Runway','DROT_Demand','DROT_Final Wake','DROT_Aircraft Type ICAO','DROT_SID (shortened)','B2','TAXI_OUT_S1','TAXI_OUT_S2','TAXI_OUT_S3','TAXI_OUT_S4','TAXI_OUT_S5','TAXI_OUT_S6','TAXI_OUT_S7','TAXI_OUT_S8','TAXI_OUT_S9','TAXI_OUT_S10','TAXI_OUT_S11','TAXI_OUT_S12','TAXI_OUT_S13','TAXI_OUT_S14','TAXI_OUT_S15','B3','B4','ADA_id','ADA_ADA','ADA_Combined ROT','ADA_Buffer','ADA_Uniques','ADA_ADA counts','ADA_C_ROT counts','ADA_Buffer_Unique','ADA_Buffer_counts']
    # df_final_TAXIIN= tdf.drop(columns=columns_to_drop_taxi_in)
    # df_taxi_in = df_final_TAXIIN.rename(columns = { 'TAXI_IN_S1':'S1','TAXI_IN_S2':'S2','TAXI_IN_S3':'S3','TAXI_IN_S4':'S4','TAXI_IN_S5':'S5','TAXI_IN_S6':'S6','TAXI_IN_S7':'S7','TAXI_IN_S8':'S8','TAXI_IN_S9':'S9','TAXI_IN_S10':'S10','TAXI_IN_S11':'S11','TAXI_IN_S12':'S12','TAXI_IN_S13':'S13','TAXI_IN_S14':'S14','TAXI_IN_S15':'S15'})

    # TIN_output = tk.IntVar()

    # max_tin = df_taxi_out['S1'].max() #160 # Initialise to remove unrealistic outliers from data
    # min_tin = df_taxi_out['S1'].min()

    # TIN_filter_output = max_tin

    # def getThrottle_ti(event):

    #     ax102.clear() #ax

    #     ax102.set_title('  Taxi-in distribution example - Runway Direction = 26L, All Mediums ')
    #     ax102.set_xlabel(' Taxi-in time (secs) ')
    #     ax102.set_ylabel(' Aircraft count ')

    #     TIN_filter_output = Throttle_tin.get()

    #     df_tin_filtered = df_taxi_in.loc[df_taxi_in['S1'] <= TIN_filter_output]

    #     df_tin_filtered['S1'].plot(kind='hist', bins=100, rwidth=0.7, ax=ax102)

    #     plt.show()

    #     canvas102.draw() #canvas


    # ResultsFrame_tin = tk.LabelFrame(f4_content, text="  [  Taxi-in Results :  ]  ", font="Helvetica 12")
    # ResultsFrame_tin.grid(row=1, columnspan=14, sticky='N', padx=5, pady=15, ipadx=5, ipady=5)

    # ttk.Label(ResultsFrame_tin, text="      Analysis of 2017 Summer Data from Airport X :  ", font="Helvetica 12").grid(column=1, row=0, sticky='N', pady=10, padx=20)

    # fig_tin = plt.Figure()
    # canvas10 = FigureCanvasTkAgg(fig_tin, ResultsFrame_tin)
    # canvas10.get_tk_widget().grid(column=1, row=1, sticky='N', padx=5, pady=5)
    # ax10 = fig_tin.add_subplot(111)
    # ax10.set_title('  Taxi-in movements shown for Runway Direction = 26L ')
    # ax10.set_xlabel('Wake Category = [ Medium ] ')
    # ax10.set_ylabel('Time (secs)')

    # df_taxi_in.plot(kind='box', ax=ax10)

    # ## EXTRA Taxi-out plots!

    # fig_tin_2 = plt.Figure()
    # canvas102 = FigureCanvasTkAgg(fig_tin_2, ResultsFrame_tin)
    # canvas102.get_tk_widget().grid(column=2, row=1, sticky='N', padx=5, pady=5)
    # ax102 = fig_tin_2.add_subplot(111)
    # ax102.set_title('  Taxi-out distribution example - Runway Direction = 26L, All Mediums ')
    # ax102.set_xlabel(' Taxi-out time (secs) ')
    # ax102.set_ylabel(' Aircraft count ')

    # #df_taxi_out.plot(kind='box', ax=ax92)

    # df_taxi_in['S1'].plot(kind='hist', bins=100, rwidth=0.7, ax=ax102)

    # ttk.Label(ResultsFrame_tin, text="   Filter by Max. Taxi-in value ->     ", font="Helvetica 10").grid(row=2, column=2, sticky='N', padx=5, pady=10)

    # Throttle_tin = tk.Scale(ResultsFrame_tin, from_=min_tin, to=max_tin, width=10, orient=tk.HORIZONTAL, tickinterval=100, command=getThrottle_ti)#variable = var)
    # Throttle_tin.grid(row=3, column=2, sticky='EW', padx=5)
    # Throttle_tin.set(max_tin)

    # ADA/ADDA #############################################################################################

    f5_help = ttk.LabelFrame(f5, text=" Quick Help ")
    f5_help.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    ttk.Label(f5_help, text="Provides example analysis for an 'A-D-A' distribution", font=12).grid(column=1, row=1, sticky='W')
    ttk.Label(f5_help, text="Note the analysis only considers: a single Runway direction (26L)", font=12).grid(column=1, row=2, sticky='W')
    ttk.Label(f5_help, text="  - A single Runway direction (26L)", font=12).grid(column=1, row=3, sticky='W')
    ttk.Label(f5_help, text="  - A single (on the day) wind condition", font=12).grid(column=1, row=4, sticky='W')

    f5_content = tk.LabelFrame(f5, text="   Actual Speed Profiles   ", font="Helvetica 14 bold")
    f5_content.grid(row=0, column=0, sticky='E', padx=10, pady=40, ipadx=5, ipady=10)
    ttk.Label(f5_content, text = "Not available yet.", font=12).grid(column=1, row=1, sticky='W')

    # NOTE ! : this frame used to be for ADA, but now we use it for Speed profile as the ADA comes from a normal distribution

    # f5_content = tk.LabelFrame(f5, text="   ADA / ADDA   ", font="Helvetica 14 bold")
    # f5_content.grid(row=0, column=0, sticky='E', padx=10, pady=40, ipadx=5, ipady=10)

    # #####################################################################
    # #                        ADA/ADDA  DATA                             #
    # #####################################################################

    # columns_to_drop_ada = ['AROT_Callsign','AROT_Threshold','AROT_RWY exit time','AROT','AROT_Runway','AROT_Demand','AROT_Final Wake','AROT_RwyExit','AROT_Aircraft Type ICAO','AROT_Threshold Speed [kts]','AROT_Speed @ TDZ [kts]','AROT_RWY Exit Speed 1','AROT_RWY Exit Speed 2','AROT_RWY Exit Speed 3','B1','DROT_Callsign','DROT_Line up time','DROT_Start to roll','DROT_Take off time','DROT_Runway Entry','DROT_Take off speed [kts]','DROT','DROT_Runway','DROT_Demand','DROT_Final Wake','DROT_Aircraft Type ICAO','DROT_SID (shortened)','B2','TAXI_OUT_S1','TAXI_OUT_S2','TAXI_OUT_S3','TAXI_OUT_S4','TAXI_OUT_S5','TAXI_OUT_S6','TAXI_OUT_S7','TAXI_OUT_S8','TAXI_OUT_S9','TAXI_OUT_S10','TAXI_OUT_S11','TAXI_OUT_S12','TAXI_OUT_S13','TAXI_OUT_S14','TAXI_OUT_S15','B3','TAXI_IN_S1','TAXI_IN_S2','TAXI_IN_S3','TAXI_IN_S4','TAXI_IN_S5','TAXI_IN_S6','TAXI_IN_S7','TAXI_IN_S8','TAXI_IN_S9','TAXI_IN_S10','TAXI_IN_S11','TAXI_IN_S12','TAXI_IN_S13','TAXI_IN_S14','TAXI_IN_S15','B4']
    # df_ada = tdf.drop(columns=columns_to_drop_ada)

    # ResultsFrame_ada = tk.LabelFrame(f5_content, text="  [  ADA Results :  ]   ", font="Helvetica 12")
    # ResultsFrame_ada.grid(row=1, columnspan=14, sticky='N', padx=5, pady=15, ipadx=5, ipady=5)

    # ttk.Label(ResultsFrame_ada, text="      Analysis of 2017 Summer Data from Airport X :  ", font="Helvetica 12").grid(column=1, row=0, sticky='N', pady=10, padx=20)

    # fig_ada = plt.Figure()
    # canvas7 = FigureCanvasTkAgg(fig_ada, ResultsFrame_ada)
    # canvas7.get_tk_widget().grid(column=1, row=1, sticky='N', padx=5, pady=5)
    # ax7 = fig_ada.add_subplot(111)
    # ax7.set_title('  ADA data shown for Runway Direction [ 26L ] ')
    # ax7.set_xlabel('Time (secs)')
    # ax7.set_ylabel('Frequency')

    # df_ada_main_plot = df_ada

    # df_ada_main_plot = df_ada_main_plot.drop(columns=['ADA_id','ADA_ADA','ADA_Combined ROT', 'ADA_Buffer', 'ADA_Buffer_Unique', 'ADA_Buffer_counts'])
    # df_ada_main_plot = df_ada_main_plot.rename(columns = {'ADA_ADA counts':'ADA_ADA'})
    # df_ada_main_plot = df_ada_main_plot.rename(columns = {'ADA_C_ROT counts':'ADA_Combined ROT'})
    # df_ada_main_plot = df_ada_main_plot.rename(columns = {'ADA_Uniques':'ADA_Time (secs)'})
    # df_ada_main_plot = df_ada_main_plot.set_index('ADA_Time (secs)')

    # df_ada_main_plot.plot(kind='line', ax=ax7)

    # fig_buffer = plt.Figure()
    # canvas8 = FigureCanvasTkAgg(fig_buffer, ResultsFrame_ada)
    # canvas8.get_tk_widget().grid(column=2, row=1, sticky='N', padx=5, pady=5)
    # ax8 = fig_buffer.add_subplot(111)
    # ax8.set_title('  Resulting Buffer before next Arrival aircraft  ')
    # ax8.set_xlabel('Buffer Spacing (secs)')
    # ax8.set_ylabel('Frequency')

    # df_ada_sub_plot = df_ada

    # df_ada_sub_plot = df_ada_sub_plot.drop(columns=['ADA_id','ADA_ADA','ADA_Combined ROT', 'ADA_Buffer', 'ADA_Uniques', 'ADA_ADA counts', 'ADA_C_ROT counts'])
    # df_ada_sub_plot = df_ada_sub_plot.rename(columns = {'ADA_Buffer_counts':'ADA_Buffer'})
    # df_ada_sub_plot = df_ada_sub_plot.rename(columns = {'ADA_Buffer_Unique':'ADA_Time (secs)'})
    # df_ada_sub_plot = df_ada_sub_plot.set_index('ADA_Time (secs)')

    # df_ada_sub_plot.plot(kind='line', ax=ax8)

    # df_buffer_limit =  df_ada_sub_plot.loc[df_ada_sub_plot.index <= 15, 'ADA_Buffer']
    # df_buffer_limit = df_buffer_limit.reset_index(level=[0])

    # ############ ADA data filtering! ############

    # ######### Interesting Buffer stats! #########

    # Buffer_Analysis = tk.LabelFrame(ResultsFrame_ada, text="  [  Buffer Analysis :  ]   ", font="Helvetica 12")
    # Buffer_Analysis.grid(row=2, column=2, sticky='N', padx=5, pady=15, ipadx=5, ipady=5)

    # ttk.Label(Buffer_Analysis, text="   Average buffer value from selection :     ", font="Helvetica 10").grid(row=1, column=1, sticky='N', padx=5, pady=10)
    # ## Update label value ##
    # ttk.Label(Buffer_Analysis, text=str(round(df_ada['ADA_Buffer'].mean(),2))).grid(column=1, row=2, sticky='N') # Mean Buffer value

    # #Option 2
    # ttk.Label(Buffer_Analysis, text="   Count of instances with buffer < 15 seconds :     ", font="Helvetica 10").grid(row=1, column=2, sticky='N', padx=5, pady=10)
    # ttk.Label(Buffer_Analysis, text=str(df_buffer_limit['ADA_Buffer'].count())).grid(column=2, row=2, sticky='N') # Equivalent to numpy.percentile

    output_extension_empty_file = time.strftime("%H_%M", time.localtime(time.time()))
    input_files_name = 'Input_File_RAPID_v3.0_' + output_extension_empty_file

    def define_final_distribution_parameters():

        ################################################################################################
        df_final_AROT = define_final_AROT()
        print("AROTs defined FINAL | Filters AROT = ", Throttle_arot.get(), "Demand=", Throttle.get())

        df_final_DROT = define_final_DROT()
        print("DROTs defined FINAL | Filters DROT = ", Throttle_drot.get(), "Demand=", Throttle_d.get())
        ################################################################################################

        #final_distribution_labels=[df_final_AROT,df_final_DROT,df_final_TAXIOUT, df_final_TAXIIN]
        final_distribution_labels=[df_final_AROT,df_final_DROT]
        df_final_distribution = pd.concat(final_distribution_labels, axis=1)

        distribution_file_name = 'utility/AROTDROT_distributions.csv'
        print(' !#!#!#!# CSV FILE NAME= ',distribution_file_name)
        df_final_distribution.to_csv(distribution_file_name)
        f6.tkraise()


    f5_buttons= ttk.Frame(f5)
    f5_buttons.grid(column = 0, row=1, columnspan = 7, sticky='NWES')

    tk.Button(f5_buttons, text='NEXT ->', command=define_final_distribution_parameters, activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")
    tk.Button(f5_buttons, text='<- BACK', command=lambda: f2.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")

    # STRATEGY #############################################################################################

    f6_help = ttk.LabelFrame(f6, text=" Quick Help ")
    f6_help.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    ttk.Label(f6_help, text="Strategy tool assigns 'ADA, ADDA, or none' based on % of Scheduled Arrivals", font=12).grid(column=1, row=1, sticky='W')
    ttk.Label(f6_help, text="Note - the Operational Analysis saves the key distributions to the INPUT file", font=12).grid(column=1, row=2, sticky='W')

    f6_buttons= ttk.Frame(f6)
    f6_buttons.grid(column = 0, row=1, columnspan = 7, sticky='NWES')

    tk.Button(f6_buttons, text='TO CORE MODULE ->', command=lambda: app.select('.!coremodule'), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 25).pack(side="right")
    tk.Button(f6_buttons, text='<- BACK', command=lambda: f5.tkraise(), activebackground = "pink", font=16, height = 1, overrelief="raised", width = 15).pack(side="right")

    f6_content = tk.LabelFrame(f6, text="    RAPID - INPUT FILE GENERATION    ", font="Helvetica 14 bold")
    f6_content.grid(row=0, column=0, sticky='E', padx=10, pady=40, ipadx=5, ipady=10)


    #####################################################################
    #                         SCHEDULE  DATA                            #
    #####################################################################

    #import_excel_schedule = ""
    import_excel_schedule = tk.StringVar()

    ##########################################################################################################################################
    def actual_strat_tool():
        input_excel_sheet = import_excel_schedule.get()
        xl = pd.ExcelFile(input_excel_sheet)
        # xl = pd.ExcelFile('inputs/Input_File_RAPID_2.05_CORE_Gatwick_SINGLE.xlsx')
        df_arr = xl.parse("Arrivals")
        df_dep = xl.parse("Departures")

        #                       ARRIVAL Intervals                           #
        # Find min max arrival limits  # Only care about Arrivals - If no arrivals set strategy to 'none'

        #replace nan with 0:
        df_arr['SIBT'] = df_arr['SIBT'].fillna(0)
        df_dep['SOBT'] = df_dep['SOBT'].fillna(0)

        max_arr_SIBT = df_arr['SIBT'].max()
        min_arr_SIBT = df_arr['SIBT'].min()
        #df_arr['SIBT'] = df_arr['SIBT'].fillna(0)
        if df_arr.at[0,'SIBT']==0: # seconds
            df_arr['SIBT'] = pd.to_datetime(df_arr['SIBT(sec)'],unit='s')
            max_arr_SIBT = df_arr['SIBT'].max()
            min_arr_SIBT = df_arr['SIBT'].min()

        if df_dep.at[0,'SOBT']==0: # seconds
            df_dep['SOBT'] = pd.to_datetime(df_dep['SOBTsec)'],unit='s')


        # Generate list of all schedule times (15min intervals)
        SIBT_intervals = []

        min_arr_SIBT = str(min_arr_SIBT)
        h1, m1, s1 = min_arr_SIBT.split(':')
        min_interval = (math.floor((int(m1)/60)*(60/15)))*15
        min_arr_SIBT = datetime(2000, 1, 1, int(h1), int(min_interval), int(0))
        # min_arr_SIBT = min_arr_SIBT.datetime.time

        max_arr_SIBT = str(max_arr_SIBT)
        h2, m2, s2 = max_arr_SIBT.split(':')
        max_interval = (math.floor((int(m2)/60)*(60/15)))*15
        max_arr_SIBT = datetime(2000, 1, 1, int(h2), int(max_interval), int(0))
        # max_arr_SIBT = max_arr_SIBT.datetime.time

        temp = min_arr_SIBT
        while temp <= max_arr_SIBT:
            SIBT_intervals.append(temp)
            temp += timedelta(minutes=15)

        sch_list = pd.DataFrame(SIBT_intervals, columns = ["SIBT"])
        sch_list['SIBT'] = sch_list['SIBT'].dt.time

        #                            ARRIVAL SORT                            #

        df_arr['SIBT'] = df_arr['SIBT'].astype(str) # Buggy data - have to convert to str then datetime ?!?
        df_arr['SIBT'] = pd.DatetimeIndex(df_arr['SIBT']) # Converts to dtype <M8[ns]
        df_arr['rounded_SIBT'] = df_arr['SIBT'].dt.round('15min')
        df_arr['rounded_SIBT'] = df_arr['rounded_SIBT'].dt.time

        df_arr_count = df_arr.groupby(['rounded_SIBT'])['ID'].count()
        df_arr_count = df_arr_count.reset_index(level=[0])
        df_arr_count = df_arr_count.rename(columns = {'ID':'Arrival_counts', 'rounded_SIBT':'SIBT'})

        df_arr_final = pd.merge(sch_list, df_arr_count, how='left', on=['SIBT'], copy=True).fillna(0)

        #                           DEPARTURE SORT                            #

        df_dep['SOBT'] = df_dep['SOBT'].astype(str) # Buggy data - have to convert to str then datetime ?!?
        df_dep['SOBT'] = pd.DatetimeIndex(df_dep['SOBT']) # Converts to dtype <M8[ns]
        df_dep['rounded_SOBT'] = df_dep['SOBT'].dt.round('15min')
        df_dep['rounded_SOBT'] = df_dep['rounded_SOBT'].dt.time

        df_dep_count = df_dep.groupby(['rounded_SOBT'])['ID'].count()
        df_dep_count = df_dep_count.reset_index(level=[0])
        df_dep_count = df_dep_count.rename(columns = {'ID':'Departure_counts', 'rounded_SOBT':'SIBT'})

        #                           ASSIGN STRATEGY                            #

        df_schedule_counts = pd.merge(df_arr_final, df_dep_count, how='left', on=['SIBT'], copy=True).fillna(0)

        df_schedule_counts['Perc_Arrs'] = round(df_schedule_counts['Arrival_counts'] / (df_schedule_counts['Departure_counts'] + df_schedule_counts['Arrival_counts']), 2) * 100

        df_schedule_counts['Strategy'] = ""

        df_schedule_counts.loc[(df_schedule_counts['Perc_Arrs'] > 40),'Strategy'] = 'ADA'
        df_schedule_counts.loc[(df_schedule_counts['Perc_Arrs'] <= 40) & (df_schedule_counts['Perc_Arrs'] >= 30),'Strategy'] = 'ADDA'
        df_schedule_counts.loc[(df_schedule_counts['Perc_Arrs'] < 30),'Strategy'] = 'none'

        # No assumption here about when aircraft are expected to be on runway
        # I.e. Arrival will land approx 10 mins before SIBT? Departure uses runway 10mins after SOBT? This does not account for delay!!!!

        #####################################################################
        #                      1st Pass Complete                            #
        #####################################################################

        df_schedule_counts['Next_Strategy'] = df_schedule_counts['Strategy'].shift(-1)
        df_schedule_counts['Prev_Strategy'] = df_schedule_counts['Strategy'].shift(+1)
        df_schedule_counts['P2_Strategy'] = df_schedule_counts['Strategy'].shift(+2)

        #                             METHOD ONE                            #

        df_schedule_counts['Strategy_v2'] = df_schedule_counts['Strategy']

        df_schedule_counts.loc[(df_schedule_counts['Strategy'].astype(str) == str('none')) & (df_schedule_counts['Prev_Strategy'] != df_schedule_counts['Strategy']) & (df_schedule_counts['Next_Strategy'] != df_schedule_counts['Strategy']),'Strategy_v2'] = 'ADDA'

        df_schedule_counts.loc[(df_schedule_counts['Prev_Strategy'] ==  df_schedule_counts['Next_Strategy']) & (df_schedule_counts['Prev_Strategy'] ==  df_schedule_counts['P2_Strategy']),'Strategy_v2'] = df_schedule_counts['Prev_Strategy']

        df_schedule_counts['Final_Strategy'] = df_schedule_counts['Strategy_v2']

        df_schedule_counts = df_schedule_counts.drop(columns=['Next_Strategy', 'Prev_Strategy', 'P2_Strategy'])

        df_schedule_counts['Next_Strategy'] = df_schedule_counts['Strategy_v2'].shift(-1)
        df_schedule_counts['Prev_Strategy'] = df_schedule_counts['Strategy_v2'].shift(+1)
        df_schedule_counts['P2_Strategy'] = df_schedule_counts['Strategy_v2'].shift(+2)

        df_schedule_counts.loc[(df_schedule_counts['Prev_Strategy'] == df_schedule_counts['Next_Strategy']) & (df_schedule_counts['Prev_Strategy'] ==  df_schedule_counts['P2_Strategy']),'Final_Strategy'] = df_schedule_counts['Prev_Strategy']

        df_schedule_counts = df_schedule_counts.drop(columns=['Next_Strategy', 'Prev_Strategy', 'P2_Strategy'])
        # Extra drops for final result
        df_schedule_counts = df_schedule_counts.drop(columns=['Arrival_counts', 'Departure_counts', 'Perc_Arrs', 'Strategy', 'Strategy_v2'])

        df_schedule_counts = df_schedule_counts.rename(columns = {'SIBT':'rounded_SIBT'})

        #####################################################################
        #                     2nd Pass Complete                             #
        #####################################################################

        #                           FINAL MERGE                             #
        df_temp = df_arr

        df_temp = pd.merge(df_temp, df_schedule_counts, how='left', on=['rounded_SIBT'], copy=True)

        #####################################################################
        #                        WRITE OUTPUT                               #
        #####################################################################
        # output_ex = time.strftime("%H_%M", time.localtime(time.time()))
        master_column = df_temp['Final_Strategy']

        output_file_to_edit = openpyxl.load_workbook(input_excel_sheet)
        arrival_sheet = output_file_to_edit.get_sheet_by_name('Arrivals')
        arrival_sheet['U' + str(1)].value = 'Master Column'
        for i in range (0, len(master_column)):
            arrival_sheet['U' + str(i+2)].value = master_column[i]

        name_input_file = input_files_name + '.xlsx'
        output_file_to_edit.save(name_input_file)
        print(' !#!#!#!# XLSX FILE NAME= ', name_input_file)
        # name_excel_sheet.set(name_input_file) # ??? don't know what this does but I commented it :O

    ##########################################################################################################################################

    def sch_load_file():
        import_schedule = tk.filedialog.askopenfilename()
        import_excel_schedule.set(import_schedule)
        ttk.Label(SchImportFrame, text="File Successfully Imported!").grid(column=1, row=3, sticky='N', pady=10)
        # print("#####", import_excel_schedule, "###", import_schedule)

    def define_gen_parameters():
        button_check.set(True)
        ttk.Label(SchGenFrame, text="Generation Successful!").grid(column=1, row=4, sticky='N', pady=10)
        import_schedule = import_excel_schedule.get()
    # name_input_file = ""
    def assign_strat_tool():
        button_check.set(True)
        actual_strat_tool()

        ttk.Label(StratInputFrame, text="Strategies Successfully Applied!").grid(column=1, row=3, sticky='N', pady=10)


    # Specify GUI Structure -------->

    # Left Side -------->
    IntroFrameLeft = tk.LabelFrame(f6_content, text="   [ STEP 1  -  SCHEDULE INPUT ]   ", font="Helvetica 12")
    IntroFrameLeft.grid(row=0, column=1, sticky='N', padx=5, pady=40, ipadx=5, ipady=5)

    # Right Side -------->
    IntroFrameRight = tk.LabelFrame(f6_content, text="   [ STEP 2  -  ASSIGN STRATEGY ]   ", font="Helvetica 12")
    IntroFrameRight.grid(row=0, column=2, sticky='N', padx=5, pady=40, ipadx=5, ipady=5)

    SchImportFrame = tk.LabelFrame(IntroFrameLeft, text="   [ A ] - Import a Flight Schedule   ", font="Helvetica 12 bold")
    SchImportFrame.grid(row=1, column=1, columnspan=7, sticky='N', padx=40, pady=0, ipadx=5, ipady=5)

    ttk.Label(IntroFrameLeft, text="Select one of the following Options : ", font="Helvetica 12 italic").grid(column=3, row=0, sticky='N', pady=20, padx=40)

    ttk.Label(IntroFrameRight, text="    Mixed-mode Runway Only :", font="Helvetica 12 italic").grid(column=3, row=0, sticky='N', pady=20, padx=40)

    ttk.Label(SchImportFrame, text="                    Note - Ensure that the dataset includes SIBT/SOBT times             ", font="Helvetica 9 italic").grid(column=1, row=1, sticky='N', pady=10, padx=20, ipadx=45)
    ttk.Button(SchImportFrame, text="Import a Flight Schedule ->", command=sch_load_file).grid(column=1, row=2, sticky='N', padx=10, pady=10, ipadx=5, ipady=5)

    SchGenFrame = tk.LabelFrame(IntroFrameLeft, text="   OR   [ B ] - Generate a Flight Schedule   ", font="Helvetica 12 bold")
    SchGenFrame.grid(row=2, column=1, columnspan=7, sticky='N', padx=40, pady=15, ipadx=5, ipady=5)

    ttk.Label(SchGenFrame, text="   ( Generated Schedule will use Wake/SID/Stand Group proportions based on operational data )   ", font="Helvetica 9 italic").grid(column=1, row=1, sticky='N', pady=10)

    General = tk.LabelFrame(SchGenFrame, text=" General Settings ")
    General.grid(column=1, row=2, rowspan=1, sticky='N', padx=10, pady=10, ipadx=40, ipady=10)

    perc_arrivals = tk.IntVar(General, value='20')
    total_aircraft = tk.IntVar(General, value='60')

    ttk.Label(General, text=" Set the peak number of hourly Aircraft ").grid(column=1, row=1, sticky='W', padx=20, pady=5)
    Gen_entry1 = ttk.Entry(General, width=7, textvariable=total_aircraft)
    Gen_entry1.grid(column=2, row=1, sticky='WE')

    ttk.Label(General, text=" Set Arrival Percentage in Schedule (%) ").grid(column=1, row=2, sticky='W', padx=20, pady=5)
    Gen_entry2 = ttk.Entry(General, width=7, textvariable=perc_arrivals)
    Gen_entry2.grid(column=2, row=2, sticky='WE')


    ttk.Button(SchGenFrame, text=" Generate and Save  ", command=define_gen_parameters).grid(column=1, row=4, sticky='N', ipadx=5, ipady=5)

    SchGenFrame.bind('<Return>', define_gen_parameters)

    # Strategy Assessment:

    StratInputFrame = tk.LabelFrame(IntroFrameRight, text="   Generate a Spacing Strategy ->  ", font="Helvetica 12 bold")
    StratInputFrame.grid(row=1, column=1, columnspan=7, sticky='N', padx=10, pady=5, ipadx=5, ipady=5)

    ttk.Label(StratInputFrame, text="      Each Scheduled Aircraft is assigned a Strategy (15min intervals) :", font="Helvetica 9 italic").grid(column=1, row=0, sticky='N', pady=10, padx=40)

    ttk.Button(StratInputFrame, text=" Assign Strategy  ", command=assign_strat_tool).grid(column=1, row=2, sticky='N', ipadx=5, ipady=5)

    f1.tkraise()
