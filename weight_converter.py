""" Import GUI modules """
import tkinter as tk            		# Import the Tkinter module
from tkinter import ttk				# Make the updated widgets available
from tkinter import StringVar   		# To create string variables

""" Import module sections of this program """
import home_module

""" Start of program """
class Weight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Home_Button = ttk.Button(self, text = "Home", command = lambda: controller.show_frame(home_module.Home)) # Button to open Home Page
        Home_Button.grid(column = 2, row = 10, sticky = "nwes")

        def Length_Conversion(*args):
            try:
                Value = float(Data_In.get())
                Range_Set = str(Range_1.get())
                if Range_Set == 'Grams':
                    Grams.set(Value)
                    Ounces.set(Value / 28.349523125)
                    Pounds.set(Value / 453.59237)
                    Kilograms.set(Value / 1000)
                    Hundred_Weight.set(Value / 50802.34544)
                    Tons.set(Value / 907184.74)
                    Tonnes.set(Value / 1000000)

                if Range_Set == 'Ounces':
                    Grams.set(Value * 28.349523125)
                    Ounces.set(Value)
                    Pounds.set(Value / 16)
                    Kilograms.set(Value / 35.27396194958041)
                    Hundred_Weight.set(Value / 1792)
                    Tons.set(Value / 32000)
                    Tonnes.set(Value / 35273.96194958041)

                if Range_Set == 'Pounds':
                    Grams.set(Value * 453.59237)
                    Ounces.set(Value * 16)
                    Pounds.set(Value)
                    Kilograms.set(Value / 2.2046226218487756)
                    Hundred_Weight.set(Value / 112)
                    Tons.set(Value / 2000)
                    Tonnes.set(Value / 2204.6226218487756)

                if Range_Set == 'Kilograms':
                    Grams.set(Value * 1000)
                    Ounces.set(Value * 35.27396194958041)
                    Pounds.set(Value * 2.2046226218487756)
                    Kilograms.set(Value)
                    Hundred_Weight.set(Value / 50.80234544)
                    Tons.set(Value / 907.18474)
                    Tonnes.set(Value / 1000)

                if Range_Set == 'Hundred Weight':
                    Grams.set(Value * 50802.34544)
                    Ounces.set(Value * 1792)
                    Pounds.set(Value * 112)
                    Kilograms.set(Value * 50.80234544)
                    Hundred_Weight.set(Value)
                    Tons.set(Value / 17.857142857142857)
                    Tonnes.set(Value / 19.68413055222121066378804243868216872215270996093)

                if Range_Set == 'Tons':
                    Grams.set(Value * 907184.74)
                    Ounces.set(Value * 32000)
                    Pounds.set(Value * 2000)
                    Kilograms.set(Value * 907.18474)
                    Hundred_Weight.set(Value * 17.857142857142857)
                    Tons.set(Value)
                    Tonnes.set(Value / 1.1023113109243878)

                if Range_Set == 'Tonnes':
                    Grams.set(Value * 1000000)
                    Ounces.set(Value * 35273.96194958041)
                    Pounds.set(Value * 2204.6226218487756)
                    Kilograms.set(Value * 1000)
                    Hundred_Weight.set(Value * 19.68413055222121066378804243868216872215270996093)
                    Tons.set(Value * 1.1023113109243878)
                    Tonnes.set(Value)

            except ValueError:
                Grams.set(0)
                Ounces.set(0)
                Pounds.set(0)
                Kilograms.set(0)
                Hundred_Weight.set(0)
                Tons.set(0)
                Tonnes.set(0)

        Data_In = StringVar()
        Data_In.set(0)

        Range_1 = StringVar()
        Range_1.set('Grams')
        Range_Selection = ttk.Combobox(self, textvariable = Range_1, state = 'readonly', justify = "right")
        Range_Selection['values'] = ('Grams', 'Ounces', 'Pounds', 'Kilograms', 'Hundred Weight', 'Tons', 'Tonnes')
        Range_Selection.grid(column = 2, row = 1, sticky = "nwes")

        Grams = StringVar()
        Grams.set(0)
        Ounces = StringVar()
        Ounces.set(0)
        Pounds = StringVar()
        Pounds.set(0)
        Kilograms = StringVar()
        Kilograms.set(0)
        Hundred_Weight = StringVar()
        Hundred_Weight.set(0)
        Tons = StringVar()
        Tons.set(0)
        Tonnes = StringVar()
        Tonnes.set(0)

        ttk.Entry(self, width = 7, textvariable = Data_In, justify = "right").grid(column = 2, row = 2, sticky = "nwes")

        ttk.Button(self, text = "Calculate", command = Length_Conversion).grid(column = 3, row = 10, sticky = "nwes")

        ttk.Label(self, text = 'Please Select A Range: ').grid(column = 1, row = 1, sticky = "nwes")
        ttk.Label(self, text = 'Please Enter Your Measurement: ').grid(column = 1, row = 2, sticky = "nwes")
        ttk.Label(self, text = 'Is Equivalent To: ').grid(column = 1, row = 3, sticky = "nwes")

        ttk.Label(self, textvariable = Grams, anchor = "e").grid(column = 2, row = 3, sticky = "nwes")
        ttk.Label(self, textvariable = Ounces, anchor = "e").grid(column = 2, row = 4, sticky = "nwes")
        ttk.Label(self, textvariable = Pounds, anchor = "e").grid(column = 2, row = 5, sticky = "nwes")
        ttk.Label(self, textvariable = Kilograms, anchor = "e").grid(column = 2, row = 6, sticky = "nwes")
        ttk.Label(self, textvariable = Hundred_Weight, anchor = "e").grid(column = 2, row = 7, sticky = "nwes")
        ttk.Label(self, textvariable = Tons, anchor = "e").grid(column = 2, row = 8, sticky = "nwes")
        ttk.Label(self, textvariable = Tonnes, anchor = "e").grid(column = 2, row = 9, sticky = "nwes")

        ttk.Label(self, textvariable = Range_1).grid(column = 3, row = 2, sticky = "nwes")
        ttk.Label(self, text = 'Grams (g)').grid(column = 3, row = 3, sticky = "nwes")
        ttk.Label(self, text = 'Ounces (oz)').grid(column = 3, row = 4, sticky = "nwes")
        ttk.Label(self, text = 'Pounds (lb)').grid(column = 3, row = 5, sticky = "nwes")
        ttk.Label(self, text = 'Kilograms (kg)').grid(column = 3, row = 6, sticky = "nwes")
        ttk.Label(self, text = 'Hundredwt (cwt)').grid(column = 3, row = 7, sticky = "nwes")
        ttk.Label(self, text = 'Tons (ton)').grid(column = 3, row = 8, sticky = "nwes")
        ttk.Label(self, text = 'Tonnes (t)').grid(column = 3, row = 9, sticky = "nwes")

        for child in Weight.winfo_children(self):

            child.grid_configure(padx = 5, pady = 5)
