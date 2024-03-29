import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime
import google.generativeai as genai
from os import name,system
from getpass import getpass
import webbrowser
import time
from  random import *
import  os
import ast

						def sign_up():
						    password = username_entry.get()
						    confirm = password_entry.get()
						    
						    # Perform validation (for demo, let's just check if fields are not empty)
						    if password == confirm :
						        f.write('{}'.format(password))
						        messagebox.showinfo("Success", "Sign up successful!")
						        root.destroy()
						    else:
						        messagebox.showerror("Error", "Please fill in all fields")

						def quit_app():
						    root.destroy()

                        root = tk.Tk()
                        root.title("Sign Up")

                        # Username Label and Entry
                        username_label = tk.Label(root, text="Password:")
                        username_label.grid(row=0, column=0, padx=5, pady=5)
                        username_entry = tk.Entry(root)
                        username_entry.grid(row=0, column=1, padx=5, pady=5)

                        # Password Label and Entry
                        password_label = tk.Label(root, text="Password:")
                        password_label.grid(row=1, column=0, padx=5, pady=5)
                        password_entry = tk.Entry(root, show="*")
                        password_entry.grid(row=1, column=1, padx=5, pady=5)

                        # Email Label and Entry
                        # Sign Up Button
                        sign_up_button = tk.Button(root, text="Sign Up",font=("Courier New", 20), command=sign_up,bg='royalblue',fg='black',bd=3)
                        sign_up_button.pack(padx=5, pady=5)

                        # Quit Button
                        quit_button = tk.Button(root, text="Quit", command=quit_app)
                        quit_button.pack(padx=5, pady=5)

                        root.mainloop()

