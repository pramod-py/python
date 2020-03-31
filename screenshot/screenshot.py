#Mini Project by @pyadda
from datetime import datetime #Save Captured screen file name with current time
import tkinter as tk #for GUI
import pyautogui #for takescreenshot 

def takeScreenshot ():
    '''
    Function to take screenshot and save to specified location.
    '''
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    
    myScreenshot=pyautogui.screenshot()
    #pyautogui.screenshot(r'C:\Users\Shree\Desktop\screenshot\{0}.png'.format(dt_string))
    myScreenshot.save(r'C:\Users\Shree\Desktop\screenshot\{0}.png'.format(dt_string))

root = tk.Tk()# Create TKinter Obj
myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='white')
root.geometry("30x30+900+700")#setting size and Position of app
root.wm_attributes("-topmost", 1)#to set the always top
myButton.pack()#to add button in to window
root.mainloop()
