import tkinter as tk
from tkinter import ttk
import pyttsx4
from ttkthemes import ThemedStyle

def Speak():
     text = input_field.get() # Get the text from the input field
     engine = pyttsx4.init()
     engine.setProperty("rate", 150) # Adjust the speech rate (optional)
     engine.setProperty("volume", 1.0) # Adjust the speech volume (optional)
     engine.say(text) # Convert the text to speech
     engine.runAndWait()
     output_area.configure(state="normal") # Enable editing of the output area
     output_area.delete("1.0", "end") # Clear the output area
     output_area.insert("1.0", text) # Display the spoken text in the output area
     output_area.configure(state="disabled") # Disable editing of the output area

# Create the main Tkinter window
window = tk.Tk()
window.title("Text-to-Speech Converter (Group 7)")

# Apply Glassmorphic style using ttkthemes
style = ThemedStyle(window)
style.set_theme("equilux")


# Create a style object
styleobj = ttk.Style()

# Configure the background color of the Entry widget
styleobj.configure("Custom.TEntry",foreground="white", font=("Arial", 12))

# Create the input field
input_field = ttk.Entry(window, width=30,style="Custom.TEntry")
input_field.pack(pady=10)

# Create the submit button
submit_button = ttk.Button(window, text="Convert to Speech", command=Speak)
submit_button.pack(pady=5)

# Create the output area
output_area = tk.Text(window, height=5, width=30)
output_area.pack(pady=10)
output_area.configure(state="disabled") # Disable editing of the output area

# Start the Tkinter event loop
window.mainloop()