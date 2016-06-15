""" Import GUI modules """
import tkinter as tk            # Import the Tkinter module
from tkinter import StringVar   # To create string variables
#from tkinter import DoubleVar   # To create float variables
#from tkinter import IntVar      # To create integer variables
from tkinter import ttk         # Make the updated widgets available

""" Import Excel read and write modules """
#import openpyxl as op           # Import the OpenPyXl module
#import datetime as dt           # Import the Datetime method of OpenPyXL to change the format of dates and times

""" Import module sections of this program """
import Home_Module              # Home Page
# import Module_1
# import Module_2
# import Module_3
# import Module_4
# import Module_5
# import Module_6

""" Start of program """
class Length(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(Home_Module.Home)) # Button to open Home Page
        Home_Button.grid(column = 2, row = 10, sticky = "nwes")

        def Length_Conversion(*args):
            try:
                Value = float(Data_In.get())
                Range_Set = str(Range_1.get())
                if Range_Set == 'Centimeters':
                    Meters.set(Value / 100)
                    Centimeters.set(Value)
                    Inches.set(Value / 2.5399999999999873)
                    Feet.set(Value / 30.47999999999998476)
                    Yards.set(Value / 91.44)
                    Kilometers.set(Value / 100000)
                    Miles.set(Value / 160934.4)

                if Range_Set == 'Inches':
                    Meters.set(Value / 39.3700787401575)
                    Centimeters.set(Value * 2.5399999999999873)
                    Inches.set(Value)
                    Feet.set(Value / 12)
                    Yards.set(Value / 36)
                    Kilometers.set(Value / 39370.00787401575)
                    Miles.set(Value / 63360)

                if Range_Set == 'Feet':
                    Meters.set(Value / 3.2808398950131235)
                    Centimeters.set(Value * 30.47999999999998476)
                    Inches.set(Value * 12)
                    Feet.set(Value)
                    Yards.set(Value / 3)
                    Kilometers.set(Value / 3280.839895013123)
                    Miles.set(Value / 5280)

                if Range_Set == 'Yards':
                    Meters.set(Value / 1.0936132983377078)
                    Centimeters.set(Value * 91.44)
                    Inches.set(Value * 36)
                    Feet.set(Value * 3)
                    Yards.set(Value)
                    Kilometers.set(Value / 1093.6132983377078)
                    Miles.set(Value / 1760)

                if Range_Set == 'Meters':
                    Meters.set(Value)
                    Centimeters.set(Value * 100)
                    Inches.set(Value * 39.3700787401575)
                    Feet.set(Value * 3.2808398950131235)
                    Yards.set(Value * 1.0936132983377078)
                    Kilometers.set(Value / 1000)
                    Miles.set(Value / 1609.344)

                if Range_Set == 'Kilometers':
                    Meters.set(Value * 1000)
                    Centimeters.set(Value * 100000)
                    Inches.set(Value * 39370.0787401575)
                    Feet.set(Value * 3280.8398950131235)
                    Yards.set(Value * 1093.6132983377078)
                    Kilometers.set(Value)
                    Miles.set(Value / 1.609344)

                if Range_Set == 'Miles':
                    Meters.set(Value * 1609.344)
                    Centimeters.set(Value * 160934.4)
                    Inches.set(Value * 63360)
                    Feet.set(Value * 5280)
                    Yards.set(Value * 1760)
                    Kilometers.set(Value  * 1.609344)
                    Miles.set(Value)

            except ValueError:
                Centimeters.set(0)
                Inches.set(0)
                Feet.set(0)
                Yards.set(0)
                Meters.set(0)
                Kilometers.set(0)
                Miles.set(0)

        Data_In = StringVar()
        Data_In.set(0)

        Range_1 = StringVar()
        Range_1.set('Centimeters')
        Range_Selection = ttk.Combobox(self, textvariable = Range_1, state = 'readonly', justify = "right")
        Range_Selection['values'] = ('Centimeters', 'Inches', 'Feet', 'Yards', 'Meters', 'Kilometers', 'Miles')
        Range_Selection.grid(column = 2, row = 1, sticky = "nwes")

        Centimeters = StringVar()
        Centimeters.set(0)
        Inches = StringVar()
        Inches.set(0)
        Feet = StringVar()
        Feet.set(0)
        Yards = StringVar()
        Yards.set(0)
        Meters = StringVar()
        Meters.set(0)
        Kilometers = StringVar()
        Kilometers.set(0)
        Miles = StringVar()
        Miles.set(0)

        ttk.Entry(self, width = 7, textvariable = Data_In, justify = "right").grid(column = 2, row = 2, sticky = "nwes")

        ttk.Button(self, text = "Calculate", command = Length_Conversion).grid(column = 3, row = 10, sticky = "nwes")

        ttk.Label(self, text = 'Please Select A Range: ').grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = 'Please Enter Your Measurement: ').grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, text = 'Is Equivalent To: ').grid(column = 1, row = 3, sticky = "nwes")

        ttk.Label(self, textvariable = Centimeters, anchor = "e").grid(column = 2, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = Inches, anchor = "e").grid(column = 2, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = Feet, anchor = "e").grid(column = 2, row = 5, sticky = "nwes")
        ttk.Label(self, textvariable = Yards, anchor = "e").grid(column = 2, row = 6, sticky = "nwes")
        ttk.Label(self, textvariable = Meters, anchor = "e").grid(column = 2, row = 7, sticky = "nwes")
        ttk.Label(self, textvariable = Kilometers, anchor = "e").grid(column = 2, row = 8, sticky = "nwes")
        ttk.Label(self, textvariable = Miles, anchor = "e").grid(column = 2, row = 9, sticky = "nwes")

        ttk.Label(self, textvariable = Range_1).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = 'Centimeters').grid(column = 3, row = 3, sticky = "nwes")
        ttk.Label(self, text = 'Inches').grid(column = 3, row = 4, sticky = "nwes")
        ttk.Label(self, text = 'Feet').grid(column = 3, row = 5, sticky = "nwes")
        ttk.Label(self, text = 'Yards').grid(column = 3, row = 6, sticky = "nwes")
        ttk.Label(self, text = 'Meters').grid(column = 3, row = 7, sticky = "nwes")
        ttk.Label(self, text = 'Kilometers').grid(column = 3, row = 8, sticky = "nwes")
        ttk.Label(self, text = 'Miles').grid(column = 3, row = 9, sticky = "nwes")

        for child in Length.winfo_children(self): child.grid_configure(padx = 5, pady = 5)