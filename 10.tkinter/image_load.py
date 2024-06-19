import tkinter as tk
from PIL import Image, ImageTk

# Create a window
window = tk.Tk()
window.title("Image Viewer")

# Load an image using PIL
image_path = "0_empty.jpg"
pil_image = Image.open(image_path)

# Convert the PIL image to a Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(pil_image)

# Create a Label widget to display the image
label = tk.Label(window, image=tk_image)
label.pack()

# Run the Tkinter event loop
window.mainloop()
