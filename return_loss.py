""" Import GUI modules """
import tkinter as tk            		# Import the Tkinter module
from tkinter import ttk					# Make the updated widgets available
from tkinter import StringVar   		# To create string variables

""" Import mathematical modules """
import math

""" Import module sections of this program """
import home_module

""" Start of program """
class RL_Calc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(home_module.Home))
        Home_Button.grid(column = 2, row = 6) # , sticky = "nwes"
        
        def calc(*args):
            value = str(Range_1.get())
            value2 = str(Range_2.get())
            try:
                fpow = float(fpow_input.get())
                rpow = float(rpow_input.get())
                
                if (value == 'mW' and value2 == 'mW') or (value == 'W' and value2 == 'W') or (value == 'kW' and value2 == 'kW'):
                    rlc_out.set(10 * math.log10(fpow / rpow))
                    
                elif (value == 'W' and value2 == 'mW') or (value == 'kW' and value2 == 'W'):
                    rpow = rpow / 1000
                    rlc_out.set(10 * math.log10(fpow / rpow))
                    
                elif value == 'kW' and value2 == 'mW':
                    rpow = rpow / 1000000
                    rlc_out.set(10 * math.log10(fpow / rpow))
                    
                else:
                    rlc_out.set('Range Error')
                    rpow_input.set('Range Error')
                    fpow_input.set('Range Error')   
                
                try:
                    if (value == 'mW'):
                        value_3 = fpow / 50000
                        Value_25dB.set(value_3 * 150.0)
                        
                    elif (value == 'W'):
                        value_3 = fpow / 50
                        Value_25dB.set(value_3 * 150.0)
                        
                    elif (value == 'kW'):
                        value_3 = fpow / 0.05
                        Value_25dB.set(value_3 * 150.0)
                        
                except ValueError:
                    Value_25dB.set('ERROR')
                    pass
    
            except ValueError:
                fpow_input.set(0)
                rpow_input.set(0)
                rlc_out.set(0)
                Value_25dB.set(0)
                Range_1.set('mW')
                Range_2.set('mW')
    
        Range_1 = StringVar()
        Range_1.set('mW')
        Range_2 = StringVar()
        Range_2.set('mW')
        ranges = ttk.Combobox(self, textvariable = Range_1, state = 'readonly', justify = "right", exportselection = 0)
        ranges['values'] = ('mW', 'W', 'kW')
        ranges.grid(column = 2, row = 0, sticky = "nwes")
        ranges2 = ttk.Combobox(self, textvariable = Range_2, state = 'readonly', justify = "right")
        ranges2['values'] = ('mW', 'W', 'kW')
        ranges2.grid(column = 2, row = 1, sticky = "nwes")
    
        fpow_input = StringVar()
        fpow_input.set(0)
        rpow_input = StringVar()
        rpow_input.set(0)
        rlc_out = StringVar()
        rlc_out.set(0)
        Value_25dB = StringVar()
        Value_25dB.set(0)
    
        fpow_entry = ttk.Entry(self, width = 7, textvariable = fpow_input, justify = "right")
        fpow_entry.grid(column = 2, row = 2, sticky = "nwes")
    
        rpow_entry = ttk.Entry(self, width = 7, textvariable = rpow_input, justify = "right")
        rpow_entry.grid(column = 2, row = 3, sticky = "nwes")
        
        ttk.Label(self, text = "Maximum Reflected Power").grid(column = 1, row = 14, sticky = "nwes")
        ttk.Label(self, text = "For > 25dB Return Loss: ").grid(column = 1, row = 15, sticky = "nwes")
        ttk.Label(self, textvariable = Value_25dB, anchor = "e").grid(column = 2, row = 15, sticky = "nwes")
        ttk.Label(self, text = "mW").grid(column = 3, row = 15, sticky = "nwes")
        
        ttk.Label(self, textvariable = rlc_out, anchor = "e").grid(column = 2, row = 4, sticky = "nwes")
        ttk.Button(self, text = "Calculate", command = calc).grid(column = 3, row = 6, sticky = "nwes")
    
        ttk.Label(self, text = "Please choose forward range :").grid(column = 1, row = 0, sticky = "nwes")
        ttk.Label(self, text = "Please choose reflected range :").grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = "Please enter forward power :").grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, text = "Please enter reflected power :").grid(column = 1, row = 3, sticky = "nwes")
        ttk.Label(self, text = "Calculated Return Loss :").grid(column = 1, row = 4, sticky = "nwes")
        
        ttk.Label(self, text = "dB").grid(column = 3, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = Range_1).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, textvariable = Range_2).grid(column = 3, row = 3, sticky = "nwes")
    
        for child in RL_Calc.winfo_children(self):
		
            child.grid_configure(padx = 5, pady = 5)
