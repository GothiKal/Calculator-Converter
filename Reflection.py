""" Import GUI modules """
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

import math
from math import sqrt

""" Import module sections of this program """
import Home_Module

""" Start of program """
class ref(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(Home_Module.Home))
        Home_Button.grid(column = 2, row = 6, sticky = "nwes")

        def rlosscalc(*args):

            Range_Set_2 = str(Ref_Range.get())

            if Range_Set_2 == 'Return Loss':
                try:
                    Value_1 = float(Data_In.get())                                              # Inside loop or 'except ValueError' does not work
                    Output_1.set((pow(10, (Value_1 / 20)) + 1)/(pow(10, (Value_1 / 20)) - 1))   # rloss to VSWR
                    Value_2 = float(Output_1.get())                                             # Capture VSWR result
                    Output_2.set((Value_2 - 1) / (Value_2 + 1))                                 # VSWR to r_coef
                    Value_3 = float(Output_2.get())                                             # Capture Reflection Coefficient Result
                    Output_3.set(100 * (1 - pow(Value_3, 2)))                                   # Reflection coefficient to match efficiency
                    
                    # 100 * (1 - pow(rcoef, 2))

                except ValueError:
                    Output_1.set(0)                                                             # If value is not a float/int set outputs to 0 - prevents crash
                    Output_2.set(0)
                    Output_3.set(0)

            if Range_Set_2 == 'VSWR':
                try:
                    Value_1 = float(Data_In.get())                                              # Inside loop or 'except ValueError' does not work
                    Output_1.set((Value_1 - 1) / (Value_1 + 1))                                 # VSWR to r_coef
                    Value_2 = float(Output_1.get())                                             # Capture r_coef result
                    Output_2.set(-20 * math.log10(Value_2))                                     # r_coef to rloss
                    Output_3.set(100 * (1 - pow(Value_2, 2)))                                   # Reflection coefficient to match efficiency
                    
                except ValueError:
                    Output_1.set(0)                                                             # If value is not a float/int set outputs to 0 - prevents crash
                    Output_2.set(0)
                    Output_3.set(0)

            if Range_Set_2 == 'Reflection Coefficient':
                try:
                    Value_1 = float(Data_In.get())                                              # Inside loop or 'except ValueError' does not work
                    Output_1.set(-20 * math.log10(Value_1))                                     # r_coef to rloss
                    Value_2 = float(Output_1.get())                                             # Capture rloss result
                    Output_2.set((pow(10, (Value_2 / 20)) + 1) / (pow(10, (Value_2 / 20)) - 1)) # rloss to VSWR
                    Output_3.set(100 * (1 - pow(Value_1, 2)))                                   # Reflection coefficient to match efficiency

                except ValueError:
                    Output_1.set(0)                                                             # If value is not a float/int set outputs to 0 - prevents crash
                    Output_2.set(0)
                    Output_3.set(0)

            if Range_Set_2 == 'Match Efficiency':
                try:
                    Value_1 = float(Data_In.get())                                              # Inside loop or 'except ValueError' does not work
                    Output_1.set(sqrt(1-(Value_1/100)))                                         # Match efficiency to Reflection coefiicient
                    Value_2 = float(Output_1.get())                                             # Capture Reflection coefficient result
                    Output_2.set((-20 * math.log10(Value_2)))                                   # Reflection coefficient to Return loss
                    Value_3 = float(Output_2.get())                                             # Capture Return loss result
                    Output_3.set((pow(10, (Value_2 / 20)) + 1) / (pow(10, (Value_3 / 20)) - 1)) # Return loss to VSWR

                except ValueError:
                    Output_1.set(0)                                                             # If value is not a float/int set outputs to 0 - prevents crash
                    Output_2.set(0)
                    Output_3.set(0)

        def ref_range_select(*args):
            Range_Set = str(Ref_Range.get())
            if Range_Set == 'Return Loss':
                Ref_Range_2.set(":1 VSWR Ratio")
                Ref_Range_3.set("Reflection Coefficient")
                Ref_Range_4.set("dB Return Loss")
                Ref_Range_5.set('% Match Efficiency')
            if Range_Set == 'VSWR':
                Ref_Range_2.set("Reflection Coefficient")
                Ref_Range_3.set("dB Return Loss")
                Ref_Range_4.set(":1 VSWR Ratio")
                Ref_Range_5.set('% Match Efficiency')
            if Range_Set == 'Reflection Coefficient':
                Ref_Range_2.set("dB Return Loss")
                Ref_Range_3.set(":1 VSWR Ratio")
                Ref_Range_4.set("Reflection Coefficient")
                Ref_Range_5.set('% Match Efficiency')
            if Range_Set == 'Match Efficiency':
                Ref_Range_2.set('Reflection Coefficient')
                Ref_Range_3.set("dB Return Loss")
                Ref_Range_4.set("% Match Efficiency")
                Ref_Range_5.set(":1 VSWR Ratio")

        Ref_Range = StringVar()
        Ref_Range.set('Return Loss')
        Ref_Range_2 = StringVar()
        Ref_Range_2.set(':1 VSWR Ratio')
        Ref_Range_3 = StringVar()
        Ref_Range_3.set('Reflection Coefficient')
        Ref_Range_4 = StringVar()
        Ref_Range_4.set('dB Return Loss')
        Ref_Range_5 = StringVar()
        Ref_Range_5.set('Match Efficiency')
        ranges3 = ttk.Combobox(self, textvariable = Ref_Range, state = 'readonly')
        ranges3['values'] = ('Return Loss', 'VSWR', 'Reflection Coefficient', 'Match Efficiency')
        ranges3.grid(column = 2, row = 1, sticky = "nwes")
        ranges3.bind('<<ComboboxSelected>>', ref_range_select)

        Data_In = StringVar()
        Data_In.set(0)
        Output_1 = StringVar()
        Output_1.set(0)
        Output_2 = StringVar()
        Output_2.set(0)
        Output_3 = StringVar()
        Output_3.set(0)

        input_entry = ttk.Entry(self, width = 7, textvariable = Data_In)
        input_entry.grid(column = 2, row = 2, sticky = "nwes")

        ttk.Label(self, textvariable = Output_1).grid(column = 2, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = Output_2).grid(column = 2, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = Output_3).grid(column = 2, row = 5, sticky = "nwes")
        ttk.Button(self, text = "Calculate", command = rlosscalc).grid(column = 3, row = 6, sticky = "nwes")

        ttk.Label(self, text = "Please choose a range :").grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = "Please enter a number :").grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, textvariable = Ref_Range_4).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = "Is equivalent to :").grid(column = 1, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = Ref_Range_2).grid(column = 3, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = Ref_Range_3).grid(column = 3, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = Ref_Range_5).grid(column = 3, row = 5, sticky = "nwes")

        for child in ref.winfo_children(self): child.grid_configure(padx = 5, pady = 5)

        self.bind('<Return>', rlosscalc)