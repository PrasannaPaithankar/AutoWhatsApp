import tkinter as tk
import functions

infile=""

def fileSelect():
    global infile
    infile = tk.filedialog.askopenfilename(title="Select Input File", filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")))
    infilepathLabel.config(text=infile)
    return True

if __name__ == "__main__":
    root = tk.Tk()
    root.title("AutoWhatsApp")

    # Select input file and display its path
    input_file_label = tk.Label(root, text="Input File: ")
    input_file_label.grid(row=0, column=0, padx=5, pady=5)
    infilepathLabel = tk.Label(root, text=infile)
    infilepathLabel.grid(row=0, column=1, padx=5, pady=5)
    infileButton = tk.Button(root, text="Select", command=lambda: fileSelect())
    infileButton.grid(row=0, column=2, padx=5, pady=5)

    # Send message to all numbers in input file
    sendMsgsButton = tk.Button(root, text="Send Messages", command=lambda: functions.sendMsgs_excel(infile))
    sendMsgsButton.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()
    
