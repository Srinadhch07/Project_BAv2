import tkinter as tk
from PIL import Image, ImageTk


class homeclass:
	def __init__(self,window):
		self.window=window
		self.image = Image.open("boy.jpg")
		self.desired_width = 200
		self.desired_height = 200
		self.resized_image = self.image.resize((self.desired_width, self.desired_height))
		self.tk_image = ImageTk.PhotoImage(self.resized_image)

		# Create a label to display the resized image
		self.name=tk.Label(window,text='BAv2',font=("Courier New",100),
                          bg='limegreen',
                          )
		self.name.pack(pady=40)
		self.label = tk.Label(window, image=self.tk_image)
		self.label.pack(padx=50,pady=50)
		self.hello=tk.Label(window,text="Welcome to BAv2",
								font=("Courier New", 16),
                                bg="limegreen",
                                fg="black",
                                cursor="hand2"
												)
		self.hello.pack(padx=0,pady=0)
		self.send = tk.Button(window, text="start",font=("Courier New", 20),width=10,command=window.destroy,bg='royalblue',fg='black',bd=3)
		self.send.pack(padx=0, pady=50)
		

def home():

# Create a Tkinter window
	window = tk.Tk()
	window.title("Resized Image")
	window.attributes('-fullscreen', True)
	window.configure(background='lightblue',bg='limegreen')
	start=homeclass(window)
	window.mainloop()
if __name__ =="__main__":
	home()

# Load the image
  # Replace "example_image.jpg" with your image file path

# Define the desired size


# Resize the image

# Convert the resized image to a format compatible with Tkinter


# Run the Tkinter event loop
