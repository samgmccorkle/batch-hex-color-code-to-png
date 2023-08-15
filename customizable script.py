from PIL import Image
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import shutil



#fc = folder counter, ic = image counter

# Determine the user's download folder path
download_folder = os.path.expanduser("~" + os.sep + "Downloads")
output_dir_base = "hexbatch"
fc = 1
output_dir = os.path.join(download_folder, output_dir_base)
while os.path.exists(output_dir):
    output_dir = os.path.join(download_folder, f"{output_dir_base}({fc})")
fc += 1
os.makedirs(output_dir, exist_ok=True)



# Create the root window and simpledialog window
root = tk.Tk()
root.withdraw()
input_hex = simpledialog.askstring("input", "paste your hex code list here:")



if not input_hex and os.path.exists(output_dir):
    shutil.rmtree(output_dir)
    messagebox.showerror("error", "no input recorded!")
else:
    if "#" not in input_hex and os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        messagebox.showerror("error", "make sure your hex codes contain # before their values!")
    else:
# format input 
        input_hex = input_hex.replace("\n", " ")
        split_hex = input_hex.split()

 # Loop through hex color codes and create images
        for ic, hex_code in enumerate(split_hex):  
            try:
                image = Image.new("RGB", (500, 500), color=hex_code)
            except ValueError:
                messagebox.showerror("error", "one or more of your hex codes are invalid!")
# Delete recent folder directory, download failed
                if os.path.exists(output_dir):
                     shutil.rmtree(output_dir)
                break
            else:
                image.save(os.path.join(output_dir, f"{ic+1}_{hex_code.lstrip('#')}.png"))
                
           
                
# Open the newly created folder in the file explorer
try:
    if os.path.exists(output_dir):
        subprocess.Popen(["explorer", output_dir])
    else:
        exit
except:
    if os.path.exists(output_dir):
        messagebox.showinfo("downloads", "download finished, check your downloads!")
    else:
        exit
