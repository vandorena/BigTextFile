import os
import tempfile
import threading
import multiprocessing
import random
import string
import tkinter as tk
from tkinter import messagebox
import subprocess

# List of colors to cycle through
colors = ["orange", "blue", "green", "red", "purple", "yellow", "pink", "cyan"]

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
    num_lines = 10000  # Number of lines in each file
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
        # Change the button color to a random color from the list
        new_color = random.choice(colors)
        generate_button.config(bg=new_color)

def uninstall_chrome():
    # Check if Google Chrome is installed hi
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

def start_clicker_game():
    click_count = 0

    def on_click():
        nonlocal click_count
        click_count += 1
        click_count_label.config(text=f"Click Count: {click_count}")

    # Create a new window for the clicker game
    clicker_window = tk.Toplevel(root)
    clicker_window.title("Clicker Game")
    clicker_window.geometry("800x600")

    # Create a label to display the click count
    click_count_label = tk.Label(clicker_window, text="Click Count: 0", font=("Arial", 24))
    click_count_label.pack(pady=20)

    # Create a large green button in the middle of the screen
    click_button = tk.Button(clicker_window, text="Click Me!", command=on_click, font=("Arial", 24), bg="green", fg="white", width=20, height=5)
    click_button.pack(expand=True)
def main():
    # Create the main window
    global root
    root = tk.Tk()
    root.title("File Generator")

    # Set the window size
    root.geometry("1920x1080")

    # Create a canvas to add the gradient background
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Create the gradient background
    gradient = canvas.create_rectangle(0, 0, 1920, 1080, fill="red", outline="")
    canvas.itemconfig(gradient, fill="red")
    for i in range(256):
        color = f"#{255-i:02x}0000"
        canvas.create_rectangle(0, i*2, 1920, (i+1)*2, fill=color, outline="")

    # Add ASCII art
    ascii_art = """
      ___           ___           ___           ___                    ___           ___           ___           ___         ___                       ___           ___                  
     /__/\         /  /\         /__/\         /  /\                  /  /\         /  /\         /__/\        __/\          ___        /  /\         /  /\             
     \  \:\       /  /:/_        \  \:\       /  /:/_                /  /:/        /  /::\       |  |::\       /  /::\      \  \:\        /  /\      /  /:/_       /  /::\                 
      \__\:\     /  /:/ /\        \__\:\     /  /:/ /\              /  /:/        /  /:/\:\      |  |:|:\     /  /:/\:\      \  \:\      /  /:/     /  /:/ /\     /  /:/\:\            
  ___ /  /::\   /  /:/ /:/_   ___ /  /::\   /  /:/ /:/_            /  /:/  ___   /  /:/  \:\   __|__|:|\:\   /  /:/~/:/  ___  \  \:\    /  /:/     /  /:/ /:/_   /  /:/~/:/             
 /__/\  /:/\:\ /__/:/ /:/ /\ /__/\  /:/\:\ /__/:/ /:/ /\          /__/:/  /  /\ /__/:/ \__\:\ /__/::::| \:\ /__/:/ /:/  /__/\  \__\:\  /  /::\    /__/:/ /:/ /\ /__/:/ /:/___          
 \  \:\/:/__\/ \  \:\/:/ /:/ \  \:\/:/__\/ \  \:\/:/ /:/          \  \:\ /  /:/ \  \:\ /  /:/ \  \:\~~\__\/ \  \:  \:\ /  /:/ /__/:/\:\   \  \:\/:/ /:/ \  \:\/:::::/          
  \  \::/       \  \::/ /:/   \  \::/       \  \::/ /:/            \  \:\  /:/   \  \:\  /:/   \  \:\        \  \::/     \  \:\  /:/  \__\/  \:\   \  \::/ /:/   \  \::/~~~~         
   \  \:\        \  \:\/:/     \  \:\        \  \:\/:/              \  \:\/:/     \  \:\/:/     \  \:\        \  \:\      \  \:\/:/        \  \:\   \  \:\/:/     \  \:\             
    \  \:\        \  \::/       \  \:\        \  \::/                \  \::/       \  \::/       \  \:\        \  \:\      \  \::/          \__\/    \  \::/       \  \:\              
     \__\/         \__\/         \__\/         \__\/                  \__\/         \__\/         \__\/         \__\/       \__\/                     \__\/         \__\/              
    """
    canvas.create_text(1920*0.4, 150, text=ascii_art, font=("Courier", 10), fill="white")

    # Create a frame to hold_frame = tk.Frame(root, bg="red")

    button_frame = tk.Frame(canvas, bg="blue")
    button_frame.place(x=0.5, y=0, relwidth=1, relheight=1)
    button_frame.place(relx=0.5, rely=0.85, anchor="center")

    # Create buttons in a single row
    global generate_button
    generate_button = tk.Button(button_frame, text="Generate Files", command=on_generate_button_click, font=("Arial", 16), width=25, height=3, bg="orange", fg="white")
    generate_button.pack(side="left", padx=2)

    uninstall_button = tk.Button(button_frame, text="Uninstall Chrome", command=uninstall_chrome, font=("Arial", 16), width=25, height=3, bg="red", fg="white")
    uninstall_button.pack(side="left", padx=2)

    clicker_game_button = tk.Button(button_frame, text="Start Clicker Game", command=start_clicker_game, font=("Arial", 16), width=25, height=3, bg="green", fg="white")
    clicker_game_button.pack(side="left", padx=2)

    # Run the GUI event loop
    root.mainloop()

if __name__ == '__main__':
    main()
