import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

import home_module

class W_Calc(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(home_module.Home))
        Home_Button.grid(column = 3, row = 5, sticky = "nwes")
            
        def wavcalc(*args):        
            try:
                value = float(freq.get())
                sol = 299792458                        #Define speed of light in meters per second
                WL = sol / value
                wave_out.set(WL/1000)
            except ValueError:
                freq.set(0)
                wave_out.set(0)
            
        def freq_range_select(*args):
            value2 = str(range_1.get())
            if value2 == 'Hz':
                range_2.set("kilometers")
            if value2 == 'kHz':
                range_2.set("meters")
            if value2 == 'MHz':
                range_2.set("millimeters(mm)")
            if value2 == 'GHz':
                range_2.set("micrometers(um)")
        
        range_1 = StringVar()
        range_1.set("Hz")
        range_2 = StringVar()
        range_2.set("kilometers")
        
        ranges = ttk.Combobox(self, textvariable = range_1, state = 'readonly')
        ranges['values'] = ('Hz', 'kHz', 'MHz', 'GHz')
        ranges.grid(column = 2, row = 1, sticky = "nwes")
        ranges.bind('<<ComboboxSelected>>', freq_range_select)
        
        freq = StringVar()
        freq.set(0)
        wave_out = StringVar()
        wave_out.set(0)
        
        freq_entry = ttk.Entry(self, width = 7, textvariable = freq)
        freq_entry.grid(column = 2, row = 2, sticky = "nwes")
        
        ttk.Label(self, textvariable = wave_out).grid(column = 2, row = 3, sticky = "nwes")
        ttk.Button(self, text = "Calculate", command = wavcalc).grid(column = 3, row = 4, sticky = "nwes")
        
        ttk.Label(self, text = "Please choose a range :").grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = "Please enter a frequency :").grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, textvariable = range_1).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = "is equivalent to :").grid(column = 1, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = range_2).grid(column = 3, row = 3, sticky = "nwes")
        
        for child in W_Calc.winfo_children(self):

            child.grid_configure(padx = 5, pady = 5)
    
        self.bind('<Return>', wavcalc)
