import tkinter
from tkinter import *
import os
import pandas.io.data
import pandas as pd
from pandas import DataFrame
import re
import time
import numpy
from scipy import stats
from scipy import array
import datetime
import math
import itertools
import csv
from pylab import *


# -----------------------------------------------------------
# Import DB
#
# Open Payment Data: "https://openpaymentsdata.cms.gov"
# -----------------------------------------------------------


filepathDB=r"C:\MyWork\OP_DTL_GNRL_PGYR2015_P06302016.csv"

fieldnames= ['Physician_Profile_ID','Physician_Primary_Type',
            'Physician_Specialty','Total_Amount_of_Payment_USDollars',
            'Physician_Last_Name','Physician_First_Name',
            'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name',
            'Recipient_City',
            'Recipient_State',
            'Recipient_Zip_Code']

data=DataFrame(pd.read_csv(filepathDB),columns=fieldnames)

aggregations = {
               'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name': {'NumberOfCompanies': 'count'},
                'Total_Amount_of_Payment_USDollars': {'TotalMoney': 'sum'}
}

list=data.Physician_Primary_Type



# -----------------------------------------------------------
# Dialog Box with List to Select Physician Type/Speicality
# -----------------------------------------------------------

#main_window = tkinter.Tk()
#listbox = Listbox(main_window)
#for item in [data['Physician_Primary_Type']]:
#    listbox.insert(END, item)
#listbox.pack()
#mainloop()


aggregated=data[data['Physician_Primary_Type'] == 'Doctor of Dentistry'].groupby('Physician_Profile_ID').agg(aggregations)
# List TOP 5 PHYSICIANS
print (aggregated.head())


#results_amount=int(aggregated.max()[0])
#results_count=int(aggregated.max()[1])
#result_idx=aggregated.idxmax()[1]
#result_txt=data[data['Physician_Profile_ID'] == result_idx].max()
#print (result_txt)