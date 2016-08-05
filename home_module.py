""" Import GUI modules """
import tkinter as tk                        # Import the Tkinter module
from tkinter import ttk                     # Make the updated widgets available

""" Import module sections of this program """
import watts_to_decibels                    # Watts to decibels converter
import decibels_to_watts                    # Decibels to watts converter
import reflection                           # Reflection converter
import parallel_resistance                  # Parallel resistance calculator
import potential_divider                    # Potential divider calculator
import frequency_to_wavelength              # Frequency to wavelength converter
import return_loss                          # Return loss calculator
import length_converter                     # Length converter
import weight_converter                     # Weight converter

""" Start of program """
class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ttk.Label(self, text = " Please select a calculator or convertor : ").grid(column = 1, row = 0, columnspan = 3)#, sticky = "nwes")

        WDB_Button = ttk.Button(self, text = "Watts To dB", command = lambda: controller.show_frame(watts_to_decibels.WDB))# Button to open W to dB screen
        WDB_Button.grid(column = 1, row = 2, sticky = "nwes")

        DBW_Button = ttk.Button(self, text = "dB To Watts", command = lambda: controller.show_frame(decibels_to_watts.DBW)) # Button to open dB to W screen
        DBW_Button.grid(column = 2, row = 2, sticky = "nwes")

        Reflection_Button = ttk.Button(self, text = "Reflection", command = lambda: controller.show_frame(reflection.Ref)) # Button to open Reflection screen
        Reflection_Button.grid(column = 3, row = 2, sticky = "nwes")

        Parallel_Resistance_Button = ttk.Button(self, text = "Parallel Resistance", command = lambda: controller.show_frame(parallel_resistance.P_Res))    # Button to open Parallel Resistance screen
        Parallel_Resistance_Button.grid(column = 1, row = 3, sticky = "nwes")

        Potential_divider_Button = ttk.Button(self, text = "Potential Divider", command = lambda: controller.show_frame(potential_divider.P_Div))    # Button to open Potential Divider screen
        Potential_divider_Button.grid(column = 2, row = 3, sticky = "nwes")

        Wavelength_Calculator_Button = ttk.Button(self, text = "Wavelength Calculator", command = lambda: controller.show_frame(frequency_to_wavelength.W_Calc))    # Button to open Wavelength Calculator screen
        Wavelength_Calculator_Button.grid(column = 3, row = 3, sticky = "nwes")

        Return_Loss_Calculator_Button = ttk.Button(self, text = "Return Loss Calculator", command = lambda: controller.show_frame(return_loss.RL_Calc))    # Button to open Return Loss Calculator screen
        Return_Loss_Calculator_Button.grid(column = 1, row = 4, sticky = "nwes")

        Length_Converter_Button = ttk.Button(self, text = "Length Converter", command = lambda: controller.show_frame(length_converter.Length))    # Button to open Length Converter screen
        Length_Converter_Button.grid(column = 2, row = 4, sticky = "nwes")

        Weight_Converter_Button = ttk.Button(self, text = "Weight Converter", command = lambda: controller.show_frame(weight_converter.Weight))    # Button to open Weight Converter screen
        Weight_Converter_Button.grid(column = 3, row = 4, sticky = "nwes")

        for child in Home.winfo_children(self):

            child.grid_configure(padx = 5, pady = 5)
