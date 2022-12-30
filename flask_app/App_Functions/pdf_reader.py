import tkinter as tk
import PyPDF2
from tkinter import filedialog

# Create the main window
window = tk.Tk()

# Create a Text widget to display the text from the PDF
text = tk.Text(window)
text.pack()

# Define the function to be called when the "Open" button is clicked
def open_file():
    # Open a file selection dialog
    file_path = filedialog.askopenfilename()

    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Clear the Text widget
        text.delete('1.0', tk.END)

        # Iterate over every page in the PDF
        for page in range(len(reader.pages)):
            # Extract the text from the page
            page_text = reader.pages[page].extract_text()

            # Insert the text into the Text widget
            text.insert(tk.END, page_text)

# Create the "Open" button
button = tk.Button(text="Open", command=open_file)
button.pack()

# Run the main loop
window.mainloop()
