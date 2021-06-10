#=== FOR CORE: ===#

# Default DROT + buffer value ('n') variable for main runway
n = 50
# Default DROT + buffer value ('n') variable for northern runway
northern_n = 20
# Default minimum Departure Separation (Alt SIDs) in secs
minDep_altSID = 60 # minDep_altSID = 60
# Default minimum Departure Separation (Same SIDs) in secs
minDep_sameSID = 109 #minDep_sameSID = 120
SIDmax = 4
n_times = 1
ADA_x = 10
#SIDmax = 4
SIDgroup_separation = "(2,4)(3,4)"
SID_queue_assign = "1 3 | 2 4"

debugFLAG = False
debugFLAG2 = False # TAXI - RWY queue checks
multipleFLAG = False # used for multiple runs
TBS_Flag = False
RECatFLAG = False
averagethrFLAG = False
taxi_outliers = True

distance_based_FLAG = True
time_based_FLAG = False

MRS_4dme_FLAG = False
WAKE_4dme_FLAG = False
ADA_4dme_FLAG = False
ADDA_4dme_FLAG = False
MRS_thr_FLAG = False
WAKE_thr_FLAG = False
ADA_thr_FLAG = False
ADDA_thr_FLAG = False

#=== FOR VISUAL MODULE ===#

m = 0

Thr_FLAG = False
Delay_FLAG = False
Seq_FLAG = False
OP_FLAG = False
new_set_FLAG = False
average_FLAG = False
arr_delay_FLAG = False
convergenceFLAG = False
ADA_buffer_FLAG = False

#=== DON'T ADJUST ===#

open_file1 = ""
open_file = ""
name_input_file = ""
input_excel_sheet = ""
operational_data = ""
new_data2 = ""
new_data4 = ""
new_data5 = ""
new_data6 = ""
