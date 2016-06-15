""" Import GUI modules """
import tkinter as tk            # Import the Tkinter module
from tkinter import ttk

""" Import module sections of this program """
import Home_Module              # Home Page
import Watts_To_Decibels        # Watts to decibels converter
import Decibels_To_Watts        # Decibels to watts converter
import Reflection               # Reflection converter
import Parallel_Resistance      # Parallel resistance calculator
import Potential_Divider        # Potential divider calculator
import Frequency_To_Wavelength  # Frequency to wavelength converter
import Return_Loss              # Return loss calculator
import Length                   # Length converter
import Weight                   # Weight converter

""" Start of program """
class Main(tk.Tk):                          # Main container which houses all frames.

    def __init__(self, *args):              # Necessary initiaLisation method.

        tk.Tk.__init__(self, *args)         # Initialise Tkinter.

        tk.Tk.iconbitmap(self, default="icon1.ico")             # Add custom icon to the window.
        tk.Tk.wm_title(self, "RF Calculations & Conversions")   # Add custom title to the window.
        
        ttk.Style().configure("TLabel", foreground = "dark blue", font = "Calibri 12", anchor = "w")
        ttk.Style().configure("TButton", foreground = "dark blue",  font = "Calibri 12")
        ttk.Style().configure("TCombobox", foreground = "dark blue",  font = "Calibri 12")
        ttk.Style().configure("TEntry", foreground = "dark blue",  font = "Calibri 12")

        container = tk.Frame(self)                  # Create the container for all frames.
        container.grid(column = 0, row = 0, sticky="nwes")   # Set grid parameters for this container.
        container.grid_columnconfigure(0, weight=1) # Configure the column weight of this container.
        container.grid_rowconfigure(0, weight=1)    # Configure the row weight of this container.

        self.frames = {}                    # Create a dictionary for the frames in this program.
        for F in (Home_Module.Home, Decibels_To_Watts.DBW, Watts_To_Decibels.WDB, Reflection.ref, Parallel_Resistance.P_Res, Potential_Divider.P_Div, Return_Loss.RL_Calc, Frequency_To_Wavelength.W_Calc, Length.Length, Weight.Weight): # Create a loop to define the usable frames in this program.

            frame = F(container, self)      # Create a variable to hold each of the frames one at a time for use below.
            self.frames[F] = frame          # Add frame to the dictionary.
            frame.grid(row = 0, column = 0, sticky = "nwes")    # Define positional parameters for each frame.

        self.show_frame(Home_Module.Home)   # Make the 'Home' frame show on start of program.

        for child in Main.winfo_children(self): child.grid_configure(padx = 20, pady = 5) # Add a gap around each item in this frame to improve readability.

    def show_frame(self, cont):             # Define the method to make a particular frame show on command.

        frame = self.frames[cont]           # Frame name is passed into 'cont' and becomes 'frame'.
        frame.tkraise()                     # Brings the frame passed into this method to the foreground.

app = Main()
app.mainloop()

# -*- coding: utf-8 -*-
""" @author: Eric Overall """