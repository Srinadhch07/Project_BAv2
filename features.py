import calendar
from datetime import datetime
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
import subprocess
import sys


class featureclass:
	def __init__(self,window):
		self.window=window
		# Create a label to display the resized image
		self.name=tk.Label(window,text='BAv2',font=("Courier New",40),
                          bg='white',
                          )
		self.name.grid(column=0,pady=0)

		#Titles:
		self.system=tk.Label(window,text="System :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
		self.system.grid(column=0,row=1,padx=0,pady=15)

		self.system=tk.Label(window,text="Apps   :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
		self.system.grid(column=0,row=2,padx=0,pady=15)

		self.system=tk.Label(window,text="Social :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
		self.system.grid(column=0,row=3,padx=0,pady=15)

		self.system=tk.Label(window,text="Edit   :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
		self.system.grid(column=0,row=4,padx=0,pady=15)

		self.system=tk.Label(window,text="Docs   :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
		self.system.grid(column=0,row=5,padx=0,pady=15)


		self.setting=tk.Button(window,text="Settings",font=("Courier New",15,"bold"),width=15,command=self.settings,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.controlpanel=tk.Button(window,text="Control Panel",font=("Courier New",15,"bold"),width=15,command=self.control_panel,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.filemanager=tk.Button(window,text="File Manager",font=("Courier New",15,"bold"),width=15,command=self.file_manager,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.wordbutton=tk.Button(window,text="Word Document",font=("Courier New",15,"bold"),width=15,command=self.word,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.excelbutton=tk.Button(window,text="Excel Document",font=("Courier New",15,"bold"),width=15,command=self.excel,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.pointButton=tk.Button(window,text="Power Point",font=("Courier New",15,"bold"),width=15,command=self.ppt,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.promptbutton=tk.Button(window,text="Prompt",font=("Courier New",15,"bold"),width=15,command=self.cmd,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.browserbutton=tk.Button(window,text="Browser",font=("Courier New",15,"bold"),width=15,command=self.browser,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.cdrive=tk.Button(window,text="C: Drive",font=("Courier New",15,"bold"),width=15,command=self.file_c,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.ddrive=tk.Button(window,text="D: Drive",font=("Courier New",15,"bold"),width=15,command=self.file_d,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.edrive=tk.Button(window,text="E: Drive",font=("Courier New",15,"bold"),width=15,command=self.file_e,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.pptbutton=tk.Button(window,text="Power Point",font=("Courier New",15,"bold"),width=15,command=self.ppt,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.photobutton=tk.Button(window,text="Photos",font=("Courier New",15,"bold"),width=15,command=self.photos,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.spotifybutton=tk.Button(window,text="Spotify",font=("Courier New",15,"bold"),width=15,command=self.spotify,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.notepadbutton=tk.Button(window,text="NotePad",font=("Courier New",15,"bold"),width=15,command=self.notepad,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.whatsappbutton=tk.Button(window,text="WhatsApp",font=("Courier New",15,"bold"),width=15,command=self.whatsapp,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.instabutton=tk.Button(window,text="Instagram",font=("Courier New",15,"bold"),width=15,command=self.instagram,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.linkedinbutton=tk.Button(window,text="Linkedin",font=("Courier New",15,"bold"),width=15,command=self.linkedin,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.githubbutton=tk.Button(window,text="GitHub",font=("Courier New",15,"bold"),width=15,command=self.github,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.gmailbutton=tk.Button(window,text="G Mail",font=("Courier New",15,"bold"),width=15,command=self.gmail,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.facebookbutton=tk.Button(window,text="FaceBook",font=("Courier New",15,"bold"),width=15,command=self.facebook,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.twitterbutton=tk.Button(window,text="Twitter",font=("Courier New",15,"bold"),width=15,command=self.twitter,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.canvasbutton=tk.Button(window,text="Canvas",font=("Courier New",15,"bold"),width=15,command=self.canvas,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		
		self.removebutton=tk.Button(window,text="R-Background",font=("Courier New",15,"bold"),width=15,command=self.remove,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.adobebutton=tk.Button(window,text="Adobe",font=("Courier New",15,"bold"),width=15,command=self.adobe,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.fotorbutton=tk.Button(window,text="Fotor",font=("Courier New",15,"bold"),width=15,command=self.fotor,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.microsoftimagebutton=tk.Button(window,text="Microsoft AI",font=("Courier New",15,"bold"),width=15,command=self.microsoftimage,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")

		self.conversionbutton=tk.Button(window,text="Doc Converter",font=("Courier New",15,"bold"),width=15,command=self.conversion,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.ocrbutton=tk.Button(window,text="OCR",font=("Courier New",15,"bold"),width=15,command=self.ocr,bg='black',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.back=tk.Button(window,text="Back",font=("Courier New",15,"bold"),width=15,command=window.destroy,bg='green',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		self.close=tk.Button(window,text="Close",font=("Courier New",15,"bold"),width=15,command=window.destroy,bg='red',
			fg='white',bd=5,cursor="hand2",compound="center" ,relief="ridge")
		
		
		

		#arranaging buttons
		self.filemanager.grid(column=1,row=1,padx=2,pady=10)
		self.cdrive.grid(column=2,row=1,padx=2,pady=10)
		self.ddrive.grid(column=3,row=1,padx=2,pady=10)
		self.edrive.grid(column=4,row=1,padx=2,pady=10)
		self.setting.grid(column=5,row=1,padx=2,pady=10)
		self.controlpanel.grid(column=6,row=1,padx=2,pady=10)
		self.promptbutton.grid(column=7,row=1,padx=2,pady=10)
		self.browserbutton.grid(column=1,row=2,padx=2,pady=10)
		self.wordbutton.grid(column=2,row=2,padx=2,pady=10)
		self.excelbutton.grid(column=3,row=2,padx=2,pady=10)
		self.pptbutton.grid(column=4,row=2,padx=2,pady=10)
		self.photobutton.grid(column=5,row=2,padx=2,pady=10)
		self.spotifybutton.grid(column=6,row=2,padx=2,pady=10)
		self.notepadbutton.grid(column=7,row=2,padx=2,pady=10)
		self.whatsappbutton.grid(column=1,row=3,padx=2,pady=10)
		self.instabutton.grid(column=2,row=3,padx=2,pady=10)
		self.githubbutton.grid(column=3,row=3,padx=2,pady=10)
		self.linkedinbutton.grid(column=4,row=3,padx=2,pady=10)
		self.gmailbutton.grid(column=5,row=3,padx=2,pady=10)
		self.facebookbutton.grid(column=6,row=3,padx=2,pady=10)
		self.twitterbutton.grid(column=7,row=3,padx=2,pady=10)
		self.canvasbutton.grid(column=1,row=4,padx=2,pady=10)
		self.removebutton.grid(column=2,row=4,padx=2,pady=10)
		self.adobebutton.grid(column=3,row=4,padx=2,pady=10)
		self.fotorbutton.grid(column=4,row=4,padx=2,pady=10)
		self.microsoftimagebutton.grid(column=5,row=4,padx=2,pady=10)
		self.conversionbutton.grid(column=1,row=5,padx=2,pady=10)
		self.ocrbutton.grid(column=2,row=5,padx=2,pady=10)
		self.back.grid(column=6,row=6,padx=2,pady=350)
		self.close.grid(column=7,row=6,padx=2,pady=350)





	def conversion(self):
		webbrowser.open('https://www.ilovepdf.com/')
	def ocr(self):
		webbrowser.open('https://brandfolder.com/workbench/extract-text-from-image')
	def settings(self):
		os.system("start ms-settings:")
	def control_panel(self):
		if sys.platform.startswith('win'):
			subprocess.Popen(['control', 'panel'])
		elif sys.platform.startswith('linux'):
			subprocess.Popen(['gnome-control-center'])
	def file_manager(self):
		webbrowser.open('file://')
	def file_c(self):
		webbrowser.open('file://C:')
	def file_d(self):
		webbrowser.open('file://D:')
	def file_e(self):
		webbrowser.open('file://E:')
	def browser(self):
		webbrowser.register("termux-open '%s'",None)
		webbrowser.open_new("https://www.google.com/search?q=")
	
	def word(self):
		word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE" 
		subprocess.Popen([word_path])
	def excel(self):
		word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE" 
		subprocess.Popen([word_path])
	def ppt(self):
		word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE" 
		subprocess.Popen([word_path])
	def cmd(self):
		subprocess.Popen('cmd.exe')
	def photos(self):
		os.system("start ms-photos:")
	def whatsapp(self):
		webbrowser.open(f"whatsapp://send?phone=")
	def spotify(self):
		webbrowser.open(f"https://open.spotify.com/")
	def gmail(self):
		webbrowser.open(f"https://mail.google.com/mail/u/0/#inbox")
	def instagram(self):
		webbrowser.open(f"https://www.instagram.com/")
	def linkedin(self):
		webbrowser.open(f"https://www.linkedin.com/")
	def github(self):
		webbrowser.open(f"https://github.com/")
	def notepad(self):
		subprocess.Popen(["notepad.exe"])
	def facebook(self):
		webbrowser.open("https://www.facebook.com/")
	def twitter(self):
		webbrowser.open("https://twitter.com/")
	def canvas(self):
		webbrowser.open("https://www.canva.com/")
	def remove(self):
		webbrowser.open("https://www.remove.bg/upload")
	def adobe(self):
		webbrowser.open("https://www.adobe.com/in/products/photoshop-express.html")
	def fotor(self):
		webbrowser.open("https://www.fotor.com/")
	def microsoftimage(self):
		webbrowser.open("https://designer.microsoft.com/image-creator")








def feature():

# Create a Tkinter window
	window = tk.Tk()
	window.title("Resized Image")
	window.attributes('-fullscreen', True)
	window.configure(background='lightblue',bg='white')
	start=featureclass(window)
	window.mainloop()
if __name__ =="__main__":
	feature()
