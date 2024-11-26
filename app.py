import os
import tempfile
import threading
import multiprocessing
import random
import string
import tkinter as tk
from tkinter import messagebox
import subprocess

def write_big_file(file_index, num_lines, line_length, directory):
    filename = os.path.join(directory, f'big_text_file_{file_index}.txt')
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=line_length))
            adjusted_string = adjust_string(random_string)
            f.write(adjusted_string + '\n')

def adjust_string(s):
    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] == result[-1]:
            new_char = random.choice(string.ascii_letters + string.digits)
            while new_char == result[-1]:
                new_char = random.choice(string.ascii_letters + string.digits)
            result.append(new_char)
        else:
            result.append(s[i])
    return ''.join(result)

def worker(file_index, num_lines, line_length, directory):
    thread = threading.Thread(target=write_big_file, args=(file_index, num_lines, line_length, directory))
    thread.start()
    thread.join()

def generate_files():
    num_cores = multiprocessing.cpu_count()
    num_lines = 10000000  # Increase the number of lines per file
    line_length = 1000  # Increase the length of each line

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    print(f'Files will be saved in: {temp_dir}')

    processes = []
    for i in range(num_cores):
        p = multiprocessing.Process(target=worker, args=(i, num_lines, line_length, temp_dir))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Display the location of the files in a message box
    messagebox.showinfo("Files Generated", f'Files have been saved in: {temp_dir}')

def on_generate_button_click():
    # Show caution popup
    proceed = messagebox.askokcancel("Warning", "This operation will generate large files and may take some time. Do you want to proceed?")
    if proceed:
        generate_files()

def uninstall_chrome():
    # Check if Google Chrome is installed
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if os.path.exists(chrome_path):
        # Show warning popup
        proceed = messagebox.askokcancel("Warning", "This operation will uninstall Google Chrome. Do you want to proceed?")
        if proceed:
            # Uninstall Google Chrome
            subprocess.run(["wmic", "product", "where", "name='Google Chrome'", "call", "uninstall"], shell=True)
            messagebox.showinfo("Uninstall", "Google Chrome has been uninstalled.")
    else:
        messagebox.showinfo("Uninstall", "Google Chrome is not installed.")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("File Generator")

    # Set the window size
    root.geometry("800x600")

    # Create a canvas to add the gradient background
    canvas = tk.Canvas(root, width=1800, height=1000)
    canvas.pack(fill="both", expand=True)

    # Create the gradient background
    gradient = canvas.create_rectangle(0, 0, 1800, 1000, fill="red", outline="")
    canvas.itemconfig(gradient, fill="red")
    for i in range(256):
        color = f"#{255-i:02x}0000"
        canvas.create_rectangle(0, i*2, 800, (i+1)*2, fill=color, outline="")

    # Add ASCII art
    ascii_art = """
      ___           ___           ___           ___                    ___           ___           ___           ___         ___                       ___           ___                  
     /__/\         /  /\         /__/\         /  /\                  /  /\         /  /\         /__/\         /  /\       /__/\          ___        /  /\         /  /\             
     \  \:\       /  /:/_        \  \:\       /  /:/_                /  /:/        /  /::\       |  |::\       /  /::\      \  \:\        /  /\      /  /:/_       /  /::\                
      \__\:\     /  /:/ /\        \__\:\     /  /:/ /\              /  /:/        /  /:/\:\      |  |:|:\     /  /:/\:\      \  \:\      /  /:/     /  /:/ /\     /  /:/\:\           
  ___ /  /::\   /  /:/ /:/_   ___ /  /::\   /  /:/ /:/_            /  /:/  ___   /  /:/  \:\   __|__|:|\:\   /  /:/~/:/  ___  \  \:\    /  /:/     /  /:/ /:/_   /  /:/~/:/             
 /__/\  /:/\:\ /__/:/ /:/ /\ /__/\  /:/\:\ /__/:/ /:/ /\          /__/:/  /  /\ /__/:/ \__\:\ /__/::::| \:\ /__/:/ /:/  /__/\  \__\:\  /  /::\    /__/:/ /:/ /\ /__/:/ /:/___         
 \  \:\/:/__\/ \  \:\/:/ /:/ \  \:\/:/__\/ \  \:\/:/ /:/          \  \:\ /  /:/ \  \:\ /  /:/ \  \:\~~\__\/ \  \:\/:/   \  \:\ /  /:/ /__/:/\:\   \  \:\/:/ /:/ \  \:\/:::::/         
  \  \::/       \  \::/ /:/   \  \::/       \  \::/ /:/            \  \:\  /:/   \  \:\  /:/   \  \:\        \  \::/     \  \:\  /:/  \__\/  \:\   \  \::/ /:/   \  \::/~~~~        
   \  \:\        \  \:\/:/     \  \:\        \  \:\/:/              \  \:\/:/     \  \:\/:/     \  \:\        \  \:\      \  \:\/:/        \  \:\   \  \:\/:/     \  \:\             
    \  \:\        \  \::/       \  \:\        \  \::/                \  \::/       \  \::/       \  \:\        \  \:\      \  \::/          \__\/    \  \::/       \  \:\               
     \__\/         \__\/         \__\/         \__\/                  \__\/         \__\/         \__\/         \__\/       \__\/                     \__\/         \__\/               
      ___           ___                                  ___           ___           ___           ___           ___           ___           ___     
     /  /\         /  /\                  _____         /  /\         /  /\         /  /\         /  /\         /  /\         /  /\         /  /\    
    /  /:/_       /  /::\                /  /::\       /  /::\       /  /::\       /  /::\       /  /::\       /  /::\       /  /::\       /  /::\   
   /  /:/ /\     /  /:/\:\              /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\  
  /  /:/_/::\   /  /:/  \:\            /  /:/~/::\   /  /:/~/:/    /  /:/~/:/    /  /:/~/:/    /  /:/~/:/    /  /:/~/:/    /  /:/~/:/    /  /:/~/:/  
 /__/:/__\/\:\ /__/:/ \__\:\          /__/:/ /:/\:| /__/:/ /:/___ /__/:/ /:/___ /__/:/ /:/___ /__/:/ /:/___ /__/:/ /:/___ /__/:/ /:/___ /__/:/ /:/___
 \  \:\ /~~/:/ \  \:\ /  /:/          \  \:\/:/~/:/ \  \:\/:::::/ \  \:\/:::::/ \  \:\/:::::/ \  \:\/:::::/ \  \:\/:::::/ \  \:\/:::::/ \  \:\/:::::/
  \  \:\  /:/   \  \:\  /:/            \  \::/ /:/   \  \::/~~~~   \  \::/~~~~   \  \::/~~~~   \  \::/~~~~   \  \::/~~~~   \  \::/~~~~   \  \::/~~~~ 
   \  \:\/:/     \  \:\/:/              \  \:\/:/     \  \:\        \  \:\        \  \:\        \  \:\        \  \:\        \  \:\        \  \:\     
    \  \::/       \  \::/                \  \::/       \  \:\        \  \:\        \  \:\        \  \:\        \  \:\        \  \:\        \  \:\    
     \__\/         \__\/                  \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/     """
    
    canvas.create_text(400, 150, text=ascii_art, font=("Courier", 10), fill="white")

    # Create a button to generate files
    generate_button = tk.Button(root, text="Generate Files", command=on_generate_button_click, font=("Arial", 16), width=25, height=3, bg="orange", fg="white")
    generate_button_window = canvas.create_window(400, 500, window=generate_button)

    # Create a button to uninstall Google Chrome
    uninstall_button = tk.Button(root, text="Uninstall Chrome", command=uninstall_chrome, font=("Arial", 16), width=25, height=3, bg="red", fg="white")
    uninstall_button_window = canvas.create_window(400, 600, window=uninstall_button)

    # Run the GUI event loop
    root.mainloop()
    

if __name__ == '__main__':
    main()
