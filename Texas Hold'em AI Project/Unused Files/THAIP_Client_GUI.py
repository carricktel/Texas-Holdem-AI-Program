#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carricktel
#
# Created:     06/10/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *

app = Tk()
app.title("Title Here")
app.geometry("450x300")

labelText = StringVar()
labelText.set("Label Here")
label1 = Label(app,textvariable=labelText)
label1.pack()

app.mainloop()