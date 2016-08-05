""" Import GUI modules """
import tkinter as tk   					# Import the Tkinter module
from tkinter import ttk   				# Make the updated widgets available
from tkinter import StringVar   		# To create string variables
from tkinter import DoubleVar   		# To create float variables

""" Import mathematical modules """
import math

""" Import module sections of this program """
import home_module
import decibels_to_watts

""" Start of program """
class WDB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(home_module.Home))
        Home_Button.grid(column = 2, row = 9, sticky = "nwes")

        DBW_Button = ttk.Button(self, text = "dB To Watts", command = lambda: controller.show_frame(decibels_to_watts.DBW)) # Button to open dB to W screen
        DBW_Button.grid(column = 1, row = 9, sticky = "nwes")

        def W_dB(*args):
            try:
                Value = float(Data_In.get())
                Range_Set = str(Range_1.get())
                if Range_Set == 'mW':
                    dBm.set(10 * math.log10(Value))
                    dBW.set((10 * math.log10(Value)) - 30)
                    dBk.set((10 * math.log10(Value)) - 60)
                    mW.set(Value)
                    W.set(Value / 1000)
                    kW.set(Value / 1000000.0)
                if Range_Set == 'W':
                    dBm.set((10 * math.log10(Value)) + 30)
                    dBW.set(10 * math.log10(Value))
                    dBk.set((10 * math.log10(Value)) - 30)
                    mW.set(Value * 1000)
                    W.set(Value)
                    kW.set(Value / 1000)
                if Range_Set == 'kW':
                    dBm.set((10 * math.log10(Value)) + 60)
                    dBW.set((10 * math.log10(Value)) + 30)
                    dBk.set((10 * math.log10(Value)))
                    mW.set(Value * 1000000)
                    W.set(Value * 1000)
                    kW.set(Value)

            except ValueError:
                dBm.set(0.0)
                dBW.set(0.0)
                mW.set(0.0)
                W.set(0.0)
                kW.set(0.0)

        def w_range_select(*args):
            Range_Set = str(Range_1.get())
            if Range_Set == 'mW':
                Range_2.set("dBm")
            if Range_Set == 'W':
                Range_2.set("dBW")
            if Range_Set == 'kW':
                Range_2.set("dBk")

        Range_1 = StringVar()
        Range_1.set('mW')
        Range_2 = StringVar()
        Range_2.set('dBm')
        Range_Selection = ttk.Combobox(self, textvariable = Range_1, state = 'readonly')
        Range_Selection['values'] = ('mW', 'W', 'kW')
        Range_Selection.grid(column = 2, row = 1, sticky = "nwes")
        Range_Selection.bind('<<ComboboxSelected>>', w_range_select)

        Data_In = StringVar()
        Data_In.set(0.0)
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

        watts_entry = ttk.Entry(self, width = 7, textvariable = Data_In)
        watts_entry.grid(column = 2, row = 2, sticky = "nwes")

        ttk.Label(self, textvariable = dBm).grid(column = 2, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = dBW).grid(column = 2, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = dBk).grid(column = 2, row = 5, sticky = "nwes")
        ttk.Label(self, textvariable = mW).grid(column = 2, row = 6, sticky = "nwes")
        ttk.Label(self, textvariable = W).grid(column = 2, row = 7, sticky = "nwes")
        ttk.Label(self, textvariable = kW).grid(column = 2, row = 8, sticky = "nwes")

        ttk.Button(self, text = "Calculate", command = W_dB).grid(column = 3, row = 9, sticky = "nwes")

        ttk.Label(self, text = "Please choose a range :").grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = "Please enter a number :").grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, textvariable = Range_1).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = "Is equivalent to :").grid(column = 1, row = 3, sticky = "nwes")

        ttk.Label(self, text = "dBm").grid(column = 3, row = 3, sticky = "nwes")
        ttk.Label(self, text = "dBW").grid(column = 3, row = 4, sticky = "nwes")
        ttk.Label(self, text = "dBk").grid(column = 3, row = 5, sticky = "nwes")
        ttk.Label(self, text = "mW").grid(column = 3, row = 6, sticky = "nwes")
        ttk.Label(self, text = "W").grid(column = 3, row = 7, sticky = "nwes")
        ttk.Label(self, text = "kW").grid(column = 3, row = 8, sticky = "nwes")

        for child in WDB.winfo_children(self):
		
            child.grid_configure(padx = 5, pady = 5)

        self.bind('<Return>', W_dB)
