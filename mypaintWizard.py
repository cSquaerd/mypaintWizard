# Created by Charlie Cook,
# [Insert your name here if you also work on this]
# on Nov. 24th, 2019

#Import tkinter modules
import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox as mbx

#Initialize main tk window
base = tk.Tk()
base.title("MyPaint Configuration Wizard")
base.resizable(False, False)

#Declare a font
fontNormal = tkf.Font(family = "Courier New", size = 12)

#Declare a main frame to contain all wizard pages
frameMain = tk.Frame(base, bd = 2, relief = "raised")
#Pack the main frame
frameMain.pack(padx = 4, pady = 4)

#Delcare subframes a.k.a. pages of the wizard
frameP1 = tk.LabelFrame(frameMain, bd = 0, text = "Page 1")
frameP2 = tk.LabelFrame(frameMain, bd = 0, text = "Page 2")
frameP3 = tk.LabelFrame(frameMain, bd = 0, text = "Page 3")
frameP4 = tk.LabelFrame(frameMain, bd = 0, text = "Page 4")

#Page Change Button Functions
def nextPage(n):
	if n == 1:
		frameP1.pack_forget()
		frameP2.pack()
	elif n == 2:
		frameP2.pack_forget()
		frameP3.pack()
	elif n == 3:
		frameP3.pack_forget()
		frameP4.pack()

def prevPage(n):
	if n == 4:
		frameP4.pack_forget()
		frameP3.pack()
	elif n == 3:
		frameP3.pack_forget()
		frameP2.pack()
	elif n == 2:
		frameP2.pack_forget()
		frameP1.pack()

#Declare next/prev buttons
buttonNext1 = tk.Button(frameP1, text = "Next >", font = fontNormal, command = lambda : nextPage(1), cursor = "hand2")
buttonPrev2 = tk.Button(frameP2, text = "< Previous", font = fontNormal, command = lambda : prevPage(2), cursor = "hand2")
buttonNext2 = tk.Button(frameP2, text = "Next >", font = fontNormal, command = lambda : nextPage(2), cursor = "hand2")
buttonPrev3 = tk.Button(frameP3, text = "< Previous", font = fontNormal, command = lambda : prevPage(3), cursor = "hand2")
buttonNext3 = tk.Button(frameP3, text = "Next >", font = fontNormal, command = lambda : nextPage(3), cursor = "hand2")
buttonPrev4 = tk.Button(frameP4, text = "< Previous", font = fontNormal, command = lambda : prevPage(4), cursor = "hand2")

#Grid-arrage the buttons
buttonNext1.grid(row = 12, column = 2)
buttonPrev2.grid(row = 12, column = 1)
buttonNext2.grid(row = 12, column = 2)
buttonPrev3.grid(row = 12, column = 1)
buttonNext3.grid(row = 12, column = 2)
buttonPrev4.grid(row = 12, column = 1)

#Decorate page 1
imageWizard = tk.PhotoImage(file = "secretlondon_Wizard_s_Hat.png")
imagePaint = tk.PhotoImage(file = "johnny_automatic_paint_can_and_brush.png")
labelWizard = tk.Label(frameP1, image = imageWizard)
labelPaint = tk.Label(frameP1, image = imagePaint)
labelWizard.grid(row = 1, column = 1)
labelPaint.grid(row = 1, column = 2)

labelGreeting = tk.Label(frameP1, text = "Hello there! This wizard will assist you in setting up all the various widgets, menus, and tools MyPaint has to offer. There are three sections that you will see shortly: Brushes, Colors, and Tool Settings. Click \"Next >\" to proceed to the Brushes page.", font = fontNormal, wraplength = 640, justify = tk.LEFT)
labelGreeting.grid(row = 2, column = 1, columnspan = 2)

#Pack page 1
frameP1.pack()

#Start the main window
base.mainloop()
