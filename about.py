import calendar
from datetime import datetime
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk
from os import name,system
from getpass import getpass
import webbrowser
import time
from  random import *
import  os
import ast

class aboutclass:
	def __init__(self,window):
		self.window=window
		self.image = Image.open("boy.jpg")
		self.desired_width = 200
		self.desired_height = 200
		self.resized_image = self.image.resize((self.desired_width, self.desired_height))
		self.tk_image = ImageTk.PhotoImage(self.resized_image)

		# Create a label to display the resized image
		self.name=tk.Label(window,text='BAv2',font=("Courier New",70),
                          bg='limegreen',
                          )
		self.name.pack(pady=40)
		self.label = tk.Label(window, image=self.tk_image)
		self.label.pack(padx=50,pady=50)
		self.hello=tk.Label(window,text="About Developer",
								font=("Courier New", 16,"bold"),
                                bg="limegreen",
                                fg="black",
                                cursor="hand2"
												)
		self.hello.pack(padx=0,pady=0)
		self.about=""" 
Welcome to BAv2 !

I'm Srinadh Chintakindi, and I'm thrilled to introduce myself to you as the developer behind this application.

As a developer, I've poured my passion for coding into crafting this tool with the aim of providing you with a seamless and efficient experience.
I've always been fascinated by the endless possibilities that technology offers, and 
I strive to create solutions that are not only user-friendly but also innovative and impactful.
With BAv2, my goal is to empower users like you by providing a [brief description of your application's purpose or features]. 
Whether you're a seasoned professional or just starting your journey in [relevant field], I hope that this application serves as a valuable asset in your endeavors.

Thank you for choosing BAv2 , and I'm excited to continue evolving and improving this platform to meet your needs.

		"""
		self.myself=tk.Label(window,text=self.about,
								font=("Courier New", 11,'bold'),
                                bg="limegreen",
                                fg="black",
                                cursor="hand2"
												)
		self.myself.pack(padx=0,pady=0)
		self.send = tk.Button(window, text="Back",font=("Courier New", 20),width=10,command=window.destroy,bg='royalblue',fg='black',bd=3)
		self.send.pack(padx=0, pady=0)
		

def about():

# Create a Tkinter window
	window = tk.Tk()
	window.title("Resized Image")
	window.attributes('-fullscreen', True)
	window.configure(background='lightblue',bg='limegreen')
	start=aboutclass(window)
	window.mainloop()
if __name__ =="__main__":
	about()