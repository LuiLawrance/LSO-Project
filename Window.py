import tkinter as tk

# Create the main window
window = tk.Tk()

# Set window title
window.title("Neon Green Fullscreen Window")

# Set the background color to neon green
window.configure(bg='#39FF14')  # Neon green color code

# Make the window fullscreen
window.attributes('-fullscreen', True)

# Bind the Escape key to exit fullscreen mode
window.bind("<Escape>", lambda event: window.attributes('-fullscreen', False))

# Create a label
label = tk.Label(window, text="Welcome to the Neon Green Window!", font=("Arial", 24), bg='#39FF14', fg="white")
label.pack(pady=100)  # Position the label with padding from top

# Create a button
button = tk.Button(window, text="Click Me", font=("Arial", 18), command=lambda: print("Button clicked!"))
button.pack(pady=20)  # Position the button with padding below the label

# Start the Tkinter event loop
window.mainloop()
