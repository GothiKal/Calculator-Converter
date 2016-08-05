""" Import GUI modules """
import tkinter as tk 				# Import the Tkinter module
from tkinter import ttk 			# Make the updated widgets available
from tkinter import StringVar 		# To create string variables

""" Import module sections of this program """
import home_module

class P_Res(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(home_module.Home))
        Home_Button.grid(column = 2, row = 6, sticky = "nwes")
        
        def resistance_input(*args):
            
            try:
                resistance2 = float(resistance.get())
                resistances.append(resistance2)
                resistance3.set(resistances)
                ttk.Label(self, textvariable = resistance3).grid(column = 10, row = 3, sticky = "nwes")
            except ValueError:
                ttk.Label(self, text = "Error").grid(column = 100, row = 100, sticky = "nwes")
    
        def parallelcalc(*args):
            
            try:                
                validate = float(number.get())        
                control = 1
                resistances2 = []        
                while(control <= validate):
                    resistance2 = float(1 / float(resistances[control - 1]))
                    resistances2.append(resistance2)
                    control = control + 1
                    
                control = 1
                resistances3 = 0
                while(control <= validate):
                    resistances3 = float(resistances3 + float(resistances2[control-1]))
                    control = control + 1
                    p_resistance.set(1 / resistances3)
                    
                ttk.Label(self, text = "Loop Ran OK").grid(column = 100, row = 100, sticky = "nwes")
                
            except ValueError or validate <= 1:
                number.set(0)
                resistance.set(0)
                p_resistance.set(0)
                ttk.Label(self, text = "Error").grid(column = 100, row = 100, sticky = "nwes")
        
        resistances = []
        Ohm_Read_Out = StringVar()
        Ohm_Read_Out.set(0)
        number = StringVar()
        number.set(0)
        resistance = StringVar()
        resistance.set(0)
        p_resistance = StringVar()
        p_resistance.set(0)
        resistance3 = StringVar()
        
        number_entry = ttk.Entry(self, width = 7, textvariable = number)
        number_entry.grid(column = 2, row = 2, sticky = "nwes")
        
        resistance_entry = ttk.Entry(self, width = 7, textvariable = resistance)
        resistance_entry.grid(column = 2, row = 3, sticky = "nwes")
        
        ttk.Label(self, text = "Please enter the number of parallel resistors:").grid(column = 1, row = 1, columnspan = 3, sticky = "nwes")
        ttk.Label(self, text = "Resistors").grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = "Ohms").grid(column = 3, row = 3, sticky = "nwes")
        ttk.Label(self, text = "Ohms").grid(column = 3, row = 5, sticky = "nwes")
        ttk.Label(self, textvariable = p_resistance).grid(column = 2, row = 5, sticky = "nwes")
        
        ttk.Button(self, text = "Add", command = resistance_input).grid(column = 4, row = 3, sticky = "nwes")
        ttk.Button(self, text = "Calculate", command = parallelcalc).grid(column = 3, row = 6, sticky = "nwes")
    
        for child in P_Res.winfo_children(self):

            child.grid_configure(padx = 5, pady = 5)
    
        self.bind('<Return>', parallelcalc)            
