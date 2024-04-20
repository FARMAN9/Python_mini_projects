import time
import pyautogui
from datetime import datetime
import re
import tkinter as tk

def sanitize_filename(filename):
    # Replace spaces and special characters with underscores
    return re.sub(r'[: ]', '_', filename)

def main():
    current_time = datetime.now()

    # Format the timestamp and sanitize the filename
    formatted_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
    filename = 'screenshot_{}.png'.format(formatted_time)
    filename = sanitize_filename(filename)
    
    # Pause for 5 seconds
    time.sleep(1)
    
    # Take the screenshot and save it
    img = pyautogui.screenshot(filename)
    
    # Show the image
    img.show()

root=tk.Tk()
fream=tk.Frame(root,height=100,width=100)
fream.pack()

button=tk.Button(fream, text="Take a screenshot",command=main)
button.pack(side='left')

close=tk.Button(fream, text="quit",command=quit)
close.pack(side='right')
root.mainloop()


