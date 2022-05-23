'''The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.'''
from tkinter import *
import os

def restart():
    os.system("shutdow /r /t 1") #restart instantly
def restart_time():
    os.system("shutdown /r /t 20") #restarts after 20 seconds
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

#for making the Window View
window_ = Tk()
window_.title("Shutdown Windows") #Title of the window

#size of the window
window_.geometry("515x240")
window_.resizable(False, False)
window_.config(background="light blue") #window background color

#buttons for restart, logout and shutdown
btn_restart = Button(window_, text="Restart", relief=RAISED, font="Ariel", cursor="plus", command=restart)
btn_restart.place(x=50, y=100, height=40, width = 80)

btn_restartTime = Button(window_, text="Restart Time", relief=RAISED, font="Ariel", cursor="plus", command=restart_time)
btn_restartTime.place(x=140, y=100, height=40, width = 130)

btn_Logout = Button(window_, text="Logout", relief=RAISED, font="Ariel", cursor="plus", command=logout)
btn_Logout.place(x=280, y=100, height=40, width = 80)

btn_shutdown = Button(window_, text="Shutdown", relief=RAISED, font="Ariel", cursor="plus", command= shutdown)
btn_shutdown.place(x=370, y=100, height=40, width = 95)

# finally, the mainloop() method puts everything on the display, and responds to user input until the program terminates.
window_.mainloop()


