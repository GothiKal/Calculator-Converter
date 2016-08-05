""" Import GUI modules """
import tkinter as tk            		# Import the Tkinter module
from tkinter import ttk				# Make the updated widgets available

""" Import module sections of this program """
import home_module              		# Home Page
import watts_to_decibels        		# Watts to decibels converter
import decibels_to_watts        		# Decibels to watts converter
import reflection               		# Reflection converter
import parallel_resistance      		# Parallel resistance calculator
import potential_divider        		# Potential divider calculator
import frequency_to_wavelength  		# Frequency to wavelength converter
import return_loss              		# Return loss calculator
import length_converter                   	# Length converter
import weight_converter                   	# Weight converter

""" Start of program """
class Main(tk.Tk):                          					# Main container which houses all frames.

    def __init__(self, *args):              					# Necessary initiaLisation method.

        tk.Tk.__init__(self, *args)         					# Initialise Tkinter.

        tk.Tk.iconbitmap(self, default="icon1.ico")                             # Add custom icon to the window.
        tk.Tk.wm_title(self, "RF Calculations & Conversions")                   # Add custom title to the window.

        ttk.Style().configure("TLabel", foreground = "dark blue", font = "Calibri 12", anchor = "w")
        ttk.Style().configure("TButton", foreground = "dark blue",  font = "Calibri 12")
        ttk.Style().configure("TCombobox", foreground = "dark blue",  font = "Calibri 12")
        ttk.Style().configure("TEntry", foreground = "dark blue",  font = "Calibri 12")

        container = tk.Frame(self)                  			        # Create the container for all frames.
        container.grid(column = 0, row = 0, sticky="nwes")   	                # Set grid parameters for this container.
        container.grid_columnconfigure(0, weight=1) 			        # Configure the column weight of this container.
        container.grid_rowconfigure(0, weight=1)    			        # Configure the row weight of this container.

        self.frames = {}                    					# Create a dictionary for the frames in this program.
        for F in (home_module.Home, decibels_to_watts.DBW, watts_to_decibels.WDB, reflection.Ref, parallel_resistance.P_Res, potential_divider.P_Div, return_loss.RL_Calc, frequency_to_wavelength.W_Calc, length_converter.Length, weight_converter.Weight): # Create a loop to define the usable frames in this program.

            frame = F(container, self)      					# Create a variable to hold each of the frames one at a time for use below.
            self.frames[F] = frame          					# Add frame to the dictionary.
            frame.grid(row = 0, column = 0, sticky = "nwes")                    # Define positional parameters for each frame.

        self.show_frame(home_module.Home)   					# Make the 'Home' frame show on start of program.

        for child in Main.winfo_children(self):

            child.grid_configure(padx = 20, pady = 5) 		                # Add a gap around each item in this frame to improve readability.

    def show_frame(self, cont):             					# Define the method to make a particular frame show on command.

        frame = self.frames[cont]           					# Frame name is passed into 'cont' and becomes 'frame'.
        frame.tkraise()                     					# Brings the frame passed into this method to the foreground.

app = Main()
app.mainloop()

# -*- coding: utf-8 -*-
""" @author: Eric Overall """
