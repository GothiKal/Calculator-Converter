""" Import GUI modules """
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import DoubleVar   # To create float variables

""" Import module sections of this program """
import home_module
import watts_to_decibels

""" Start of program """
class DBW(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(home_module.Home)) # Button to open Home screen
        Home_Button.grid(column = 2, row = 9, sticky = "nwes")
        
        WDB_Button = ttk.Button(self, text = "Watts To dB", command = lambda: controller.show_frame(watts_to_decibels.WDB))# Button to open W to dB screen
        WDB_Button.grid(column = 1, row = 9, sticky = "nwes")
            
        def dB_W(*args):
            try:
                Value = float(Data_In.get())
                Range_Set = str(Range_1.get())
                if Range_Set == 'dBm':
                    dBm.set(Value)
                    dBW.set(Value - 30)
                    dBk.set(Value - 60)
                    mW.set(pow(10, (Value / 10)))
                    W.set(pow(10, (Value / 10)) / 1000)
                    kW.set(pow(10, (Value / 10)) / 1000000)
                if Range_Set == 'dBW':
                    dBm.set(Value + 30)
                    dBW.set(Value)
                    dBk.set(Value - 30)
                    mW.set(pow(10, (Value / 10)) * 1000)
                    W.set(pow(10, (Value / 10)))
                    kW.set(pow(10, (Value / 10)) / 1000)
                if Range_Set == 'dBk':
                    dBm.set(Value + 60)
                    dBW.set(Value + 30)
                    dBk.set(Value)
                    mW.set(pow(10, (Value / 10)) * 1000000)
                    W.set(pow(10, (Value / 10)) * 1000)
                    kW.set(pow(10, (Value / 10)))
                      
            except ValueError:
                dBm.set(0.0)
                dBW.set(0.0)
                dBk.set(0.0)
                mW.set(0.0)
                W.set(0.0)
                kW.set(0.0)   
                
        def dB_range_select(*args):
            Range_Set = str(Range_1.get())
            if Range_Set == 'dBm':
                Range_2.set("mW")
            if Range_Set == 'dBW':
                Range_2.set("W")
            if Range_Set == 'dBk':
                Range_2.set("kW")
    
        Range_1 = StringVar()
        Range_1.set('dBm')
        Range_2 = StringVar()
        Range_2.set('mW')
        Range_Selection = ttk.Combobox(self, textvariable = Range_1, state = 'readonly')
        Range_Selection['values'] = ('dBm', 'dBW', 'dBk')
        Range_Selection.grid(column = 2, row = 1, sticky = "nwes")
        Range_Selection.bind('<<ComboboxSelected>>', dB_range_select)
        
        Data_In = StringVar()
        Data_In.set(0)
        dBm = StringVar()
        dBm.set(0.0)
        dBW = StringVar()
        dBW.set(0.0)
        dBk = StringVar()
        dBk.set(0.0)
        mW = StringVar()
        mW.set(0.0)
        W = StringVar()
        W.set(0.0)
        kW = DoubleVar()
        kW.set(0.0)

        dB_entry = ttk.Entry(self, width = 7, textvariable = Data_In)
        dB_entry.grid(column = 2, row = 2, sticky = "nwes")
        
        ttk.Label(self, textvariable = dBm).grid(column = 2, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = dBW).grid(column = 2, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = dBk).grid(column = 2, row = 5, sticky = "nwes")
        ttk.Label(self, textvariable = mW).grid(column = 2, row = 6, sticky = "nwes")
        ttk.Label(self, textvariable = W).grid(column = 2, row = 7, sticky = "nwes")
        ttk.Label(self, textvariable = kW).grid(column = 2, row = 8, sticky = "nwes")
    
        ttk.Button(self, text = "Calculate", command = dB_W).grid(column = 3, row = 9, sticky = "nwes")
        
        ttk.Label(self, text = "Please choose a range :").grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = "Please enter a number :").grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, textvariable = Range_1).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = "Is equivalent to :").grid(column = 1, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = Range_2).grid(column = 3, row = 3, sticky = "nwes")
        
        ttk.Label(self, text = "dBm").grid(column = 3, row = 3, sticky = "nwes")
        ttk.Label(self, text = "dBW").grid(column = 3, row = 4, sticky = "nwes")
        ttk.Label(self, text = "dBk").grid(column = 3, row = 5, sticky = "nwes")
        ttk.Label(self, text = "mW").grid(column = 3, row = 6, sticky = "nwes")
        ttk.Label(self, text = "W").grid(column = 3, row = 7, sticky = "nwes")
        ttk.Label(self, text = "kW").grid(column = 3, row = 8, sticky = "nwes")
    
        for child in DBW.winfo_children(self):

            child.grid_configure(padx = 5, pady = 5)
