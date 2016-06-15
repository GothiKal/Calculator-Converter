import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

import Home_Module

class P_Div(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(Home_Module.Home))
        Home_Button.grid(column = 3, row = 6, sticky = "nwes")

        def potcalc(*args):
            
                   
            try:
                Vr = float(des_input.get())
                Vp = float(pot_input.get())
                Rt = float(res_input.get())
                
                if Vr>=Vp:
                    res1_output.set(0)
                    res2_output.set(0)
                    
                R1 = (Rt / 100) * ((Vr / Vp) * 100)
                res1_output.set(R1)
                res2_output.set(Rt - R1)
                error_codes.set("")
                
            except ValueError:
                error_codes.set("Please enter only numbers.")
                res1_output.set(0)
                res2_output.set(0)
        
        pot_input = StringVar()
        des_input = StringVar()
        res_input = StringVar()
        
        res1_output = StringVar()
        res2_output = StringVar()
        
        error_codes = StringVar()
        error_codes.set(" ")
        
        pot_input_entry = ttk.Entry(self, width = 7, textvariable = pot_input)
        pot_input_entry.grid(column = 2, row = 2, sticky = "nwes")
        des_input_entry = ttk.Entry(self, width = 7, textvariable = des_input)
        des_input_entry.grid(column = 2, row = 3, sticky = "nwes")
        res_input_entry = ttk.Entry(self, width = 7, textvariable=res_input)
        res_input_entry.grid(column = 2, row = 4, sticky = "nwes")
        
        ttk.Label(self, text = "Please enter the potential voltage:").grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, text = "Please enter the desired voltage:").grid(column = 1, row = 3, sticky = "nwes")
        ttk.Label(self, text = "Please enter the total resistance:").grid(column = 1, row = 4, sticky = "nwes")
        ttk.Label(self, text = "Resistance for R1:").grid(column = 1, row = 5, sticky = "nwes")
        ttk.Label(self, text = "Resistance for R2:").grid(column = 1, row = 6, sticky = "nwes")
        ttk.Label(self, textvariable = res1_output).grid(column = 2, row = 5, sticky = "nwes")
        ttk.Label(self, textvariable = res2_output).grid(column = 2, row = 6, sticky = "nwes")
        ttk.Label(self, text = "Resultant voltage must be less than potential voltage.").grid(column = 1, row = 7, columnspan = 5, sticky = "nwes")
        ttk.Label(self, textvariable = error_codes).grid(column = 1, row = 8, sticky = "nwes")
        
        ttk.Button(self, text = "Calculate", command = potcalc).grid(column = 3, row = 5, sticky = "nwes")
        
        for child in P_Div.winfo_children(self): child.grid_configure(padx = 5, pady = 5)
    
        self.bind('<Return>', potcalc)