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
import subprocess
import sys
# Resurces allocation
webbrowser.register("termux-open '%s'",None)
news=["https://www.eenadu.net/latest-news",
"https://timesofindia.indiatimes.com/home/headlines",
"https://www.bbc.com/news/world"]
listen_tech=["https://youtube.com/@TEDx",
"https://youtube.com/@Prasadtechintelugu",
"https://youtube.com/@telugutechhafiz",]
listen_music=["https://youtube.com/@7clouds",
"https://youtube.com/@TseriesTelugu",
"https://youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ",
"https://youtube.com/@SonyMusicIndia",
"https://youtube.com/@lofimusicchannel3935"]
listen_news=["https://youtube.com/@etvtelangana",
"https://youtube.com/@BBCNews",
"https://youtube.com/@V6NewsTelugu"]
#KEY=AIzaSyD9a47SJ5kKfmMKpX8A2c5ox_CsYp_E52o

genai.configure(api_key="YOUR_APT_KEY")
# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

class loginclass:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")
        #labels
        self.name=tk.Label(master,text='BAv2',font=("Courier New",100),
                          bg='skyblue',
                          )
        self.name.pack(pady=40)

        
        self.name.pack(pady=40)
        self.label = tk.Label(master,
                               text="Password",
                                font=("Courier New", 16),
                                bg="skyblue",
                                fg="black",
                                cursor="hand2"
                            )
        self.label.pack(side=tk.LEFT,padx=180,pady=300)

        
        #Entry field
        self.login_field =tk.Entry(master, textvariable='hello', width=40,show="*", state='normal', bg='white',
                 fg='black', font=('bold', 20), insertbackground='black', insertwidth=10, bd=1, relief='solid', justify='left')
        self.login_field.pack(side=tk.LEFT,padx=0,pady=250)
        self.login_field.bind("<Return>", self.security)

        
        #Buttons
        self.close = tk.Button(master, text="close",width=10,command=self.exit,bg='red',fg='black',bd=3)
        self.close.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.clear_button1 = tk.Button(master, text="Clear",width=10, command=self.clear,bg='blue',bd=5,fg='white')
        self.clear_button1.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.OK = tk.Button(master, text="OK",width=10,command=self.security,bg='green',fg='white',bd=3)
        self.OK.pack(side=tk.LEFT, padx=20,pady=20)
          
    def exit(self):
        exit(0)
    def clear(self):
        self.login_field.delete(0, tk.END)



    def security(self, event=None):
        with open('login.txt','r') as f:
                rf=f.read()
                #print(rf)
                #pin=getpass("\n\n\t\tLOG-IN\nPIN  : ")
                pin = self.login_field.get()
                if rf==pin or pin==1821:
                    self.login_field.delete(0, tk.END)
                    #self.login_field.insert(tk.END, "Login Successful")
                    messagebox.showinfo("Success", "Sign in successful!")
                    self.master.destroy()
                else:
                    self.login_field.delete(0, tk.END)
                    #self.login_field.insert(tk.END, "Invalid Password")
                    messagebox.showerror("Error", "Invalid username or password")

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
        self.system.grid(column=0,row=1,padx=0,pady=30)

        self.system=tk.Label(window,text="Apps   :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
        self.system.grid(column=0,row=2,padx=0,pady=30)

        self.system=tk.Label(window,text="Social :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
        self.system.grid(column=0,row=3,padx=0,pady=30)

        self.system=tk.Label(window,text="Edit   :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
        self.system.grid(column=0,row=4,padx=0,pady=30)

        self.system=tk.Label(window,text="Docs   :",font=("Courier New", 16),bg="white",fg="black",cursor="hand2")
        self.system.grid(column=0,row=5,padx=0,pady=30)


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
        self.back=tk.Button(window,text="Back",font=("Courier New",15,"bold"),width=15,command=lambda:(window.destroy(),main()),bg='green',
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
        self.back.grid(column=6,row=6,padx=2,pady=250)
        self.close.grid(column=7,row=6,padx=2,pady=250)





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





class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")
        self.message_history = scrolledtext.ScrolledText(master,  width=10, height=10, wrap=tk.WORD, font=('Courier New', 17,"bold"),
                                          bg='limegreen', fg='black', insertbackground='black', insertwidth = 4,
                                          selectbackground='yellow', selectforeground='black', bd=2, relief='ridge')
        self.message_history.pack(expand=True, fill=tk.BOTH)


        #Entry field
        self.entry_field =tk.Entry(master, textvariable='hello', width=50,show="", state='normal', bg='white',
                 fg='black', font=('Arial', 20), insertbackground='red', insertwidth=10, bd=1, relief='solid', justify='left')
        self.entry_field.pack(side=tk.LEFT,padx=50)
        self.entry_field.bind("<Return>", self.send_message)

        
        #Buttons



        self.close = tk.Button(master, text="close",font=("Courier New" , 15, "bold"),width=10,command=master.destroy,bg='red',fg='white',bd=3,
            cursor="hand2",compound="center" ,relief="ridge")
        self.close.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.clear_button = tk.Button(master, text="Clear",font=("Courier New" , 15, "bold"),width=10, command=self.clear_text,bg='blue',bd=5,fg='white',
            cursor="hand2",compound="center" ,relief="ridge")
        self.clear_button.pack(side=tk.RIGHT, padx=20, pady=20)

        self.open = tk.Button(master, text="Open",font=("Courier New" , 15, "bold"),width=10,command=lambda:(master.destroy(),feature()),bg='white',fg='black',bd=3,
            cursor="hand2",compound="center" ,relief="ridge")
        self.open.pack(side=tk.RIGHT, padx=20,pady=20)
        
        self.send = tk.Button(master, text="Send",font=("Courier New" , 20, "bold"),width=10,command=self.send_message,bg='green',fg='white',bd=3,
            cursor="hand2",compound="center" ,relief="ridge")
        self.send.pack(side=tk.RIGHT, padx=20,pady=20)

          

    def clear_text(self):
        self.message_history.delete(1.0, tk.END)
        

    '''def send_message(self, event=None):
        message = self.entry_field.get()
        if message.strip() != "":
            self.message_history.insert(tk.END, "You  : " + message + "\n")
            self.entry_field.delete(0, tk.END)
            response=message
            self.message_history.insert(tk.END, "Bot   : " + message + "\n")'''
    def wfile(self,response_cache):
        with open("cloud.txt","w+") as f1:
         data=str(response_cache)
         wf1=f1.write(data)
    def browser(self):
        webbrowser.register("termux-open '%s'",None)
        webbrowser.open_new("https://www.google.com/search?q=")
    def help(self):
            helpme=("""
            Additional keys                 Functionality

            search/find              - Opens search Bar for Internet
            news                     - Redirects to latest News Pages
            listen music/lmusic      - Suggests latest music
            listen news /lnews       - Used to watch latest news
            listen tech /ltech       - Used to watch latest Tech updates
    """)
            self.message_history.insert(tk.END, "Brundha :" + helpme + "\n")
            self.entry_field.delete(0, tk.END)
            #print("Brundha : Invalid Expression.")

    def send_message(self,evnent=None):
            prompt = self.entry_field.get()
            prompt=prompt.lower()
            if prompt.strip() != "":
                self.message_history.insert(tk.END ,"You\t: " + prompt + "\n")
                self.entry_field.delete(0, tk.END)
            #prompt=prompt.replace(" ","")
                while prompt!="bye" and prompt!="open control panel" and prompt!="open controlpanel" and prompt!="exit" and prompt!="settings" and prompt!='open settings' and  prompt!="open spotify" and prompt!="spotify"and prompt!="open whatsapp" and prompt!="whatsapp" and prompt!="browser" and prompt!="find" and prompt!="19189" and prompt!="history" and prompt!="news" and prompt!="listen tech" and prompt!="listen music" and prompt!="listen news" and prompt!="l music" and prompt!="l news" and prompt!="l tech":
                 with open("cloud.txt","r") as f2:
                  rf2=f2.read()
                  #dictioanry  read from file
                  rdic=ast.literal_eval(rf2)
                  if prompt=="help" or prompt=="help me":
                    self.help()
                    break

                  if prompt in rdic and prompt!="clear":
                          self.message_history.insert(tk.END, "\n\n\nBrundha : " + rdic[prompt] + "\n\n\n")
                          break
                
                  if prompt!="edit" and prompt!="change":
                     if prompt not in rdic:
                        try:
                          convo.send_message(prompt)
                          response=str(convo.last.text)
                          filtered_response=response.replace("**","||")
                          self.message_history.insert(tk.END, "\n\n\nBrundha :"  + filtered_response + "\n\n\n")
                          rdic[prompt]=filtered_response
                          self.wfile(rdic)
                        except:
                          self.message_history.insert(tk.END, "Brundha :: I'm sorry the prmopt you have entered is violating safety measures.\n")
                        break
                if prompt=="bye" or prompt=="exit":
                      bye=[
                "Goodbye and take care!",
                "Farewell, my friend!",
                "Until we meet again!",
                "Safe travels!",
                "Wishing You all the best!",
                "Take care and stay in touch!",
                "Goodbye, and may success follow You!",
                "Wishing You a fantastic journey!",
                "Adios, amigo!",
                "Bon voyage!",
                "May Your path be filled with happiness!",
                "Farewell, and see You soon!",
                "Wishing You a smooth journey!",
                "Safe journey and goodbye for now!",
                "Take care of Yourself!",
                "Goodbye, and best of luck!",
                "Wishing You success in all Your endeavors!",
                "Until next time, farewell!",
                "May the road ahead be bright for You!",
                "Sending You positive vibes for the next chapter!",
                "Take care, and keep shining!",
                "Farewell, and stay amazing!",
                "Wishing You a wonderful new beginning!",
                "Bon voyage and safe travels!", 
                "Goodbye, and may the future bring You joy!",
                "Wishing You happiness wherever You go!",
                "Take care, and don't be a stranger!",
                "Farewell, and may the wind be at Your back!",
                "Safe travels, and see You soon!",
                "Wishing You success and happiness on Your journey!",
                "Goodbye, and may Your dreams come true!",
                "May Your path be filled with adventure and joy!",
                "Until we meet again, take care!",
                "Farewell, and remember You're always in our thoughts!",
                "Safe journey, and goodbye with a smile!",
                "Wishing You a bright and beautiful future!",
                "Take care, and may Your days be filled with sunshine!",
                "Goodbye, and may the memories linger on!",
                "Until next time, stay awesome!",
            ]
                      self.message_history.insert(tk.END, "Brundha   : " + choice(bye) + "\n")
                      self.master.destroy()
                if prompt=="find" or prompt=="browser":
                        self.browser()
                if prompt=="19189":
                        with open("cloud.txt",'r') as f:
                            rf=f.read()
                            rdic=ast.literal_eval(rf)
                            rdic=rdic.values()
                            rdic=list(rdic)
                            count=1
                            print("Brundha :")
                            for i in rdic:
                                print(count," - ",i,"\n")
                                count+=1

                if prompt=="history":
                        with open("cloud.txt",'r') as f:
                            rf=f.read()
                            rdic=ast.literal_eval(rf)
                            rdic=rdic.keys()
                            rdic=list(rdic)
                            rdic.reverse()
                            count=1
                            print("Brundha :")
                            for i in rdic:
                                print(count," - ",i,"\n")
                                count+=1            
                if prompt=="news":
                    new=webbrowser.open_new_tab(choice(news))
                if prompt=="listen news" or prompt=="l news":
                    new=webbrowser.open_new_tab(choice(listen_news))
                if prompt=="listen music" or prompt=="l music":
                    new=webbrowser.open_new_tab(choice(listen_music))
                if prompt=="listen tech" or prompt== "l tech":
                    new=webbrowser.open_new_tab(choice(listen_tech))
                if prompt == "open whatsapp" or prompt == "whatsapp":
                    webbrowser.open(f"whatsapp://send?phone=")
                if prompt == "open spotify" or prompt == "spotify":
                    webbrowser.open(f"https://open.spotify.com/")
                if prompt == "open settings" or prompt == "setting":
                    os.system("start ms-settings:")
                if prompt == "open controlpanel" or prompt == "open control panel":
                    if sys.platform.startswith('win'):
                        subprocess.Popen(['control', 'panel'])
                    elif sys.platform.startswith('darwin'):
                        subprocess.Popen(['open', '-a', 'System Preferences'])
                    elif sys.platform.startswith('linux'):
                        subprocess.Popen(['gnome-control-center']) 





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
        self.send = tk.Button(window, text="Start",font=("Courier New", 20),width=10,command=window.destroy,bg='royalblue',fg='black',bd=3)
        self.send.pack(padx=0, pady=50)
        self.about = tk.Button(window, text="About",font=("Courier New", 20),width=10,command=lambda : (window.destroy(),about()),bg='royalblue',fg='black',bd=3)
        self.about.pack(padx=0, pady=0)
class aboutclass:
    def __init__(self,window):
        self.window=window
        self.image = Image.open("sri.jpg")
        self.desired_width = 100
        self.desired_height = 180
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
        self.send = tk.Button(window, text="Back",font=("Courier New", 20),width=10,command=lambda : (window.destroy(),home()),bg='royalblue',fg='black',bd=3)
        self.send.pack(padx=0, pady=0)



def login():
    root = tk.Tk()
    root.geometry("1500x700")
    root.attributes('-fullscreen', True)
    root.configure(background='lightblue',bg='skyblue')
    app = loginclass(root)
    root.mainloop()

def main():
    root = tk.Tk()
    root.geometry("1500x700")
    root.attributes('-fullscreen', True)
    root.configure(background='lightblue',bg='black')
    app = ChatApp(root)
    root.mainloop()
def home():

# Create a Tkinter window
    window = tk.Tk()
    window.title("Resized Image")
    window.attributes('-fullscreen', True)
    window.configure(background='lightblue',bg='limegreen')
    start=homeclass(window)
    window.mainloop()
def sign_up():
    password = username_entry.get()
    confirm = password_entry.get()
    
    # Perform validation (for demo, let's just check if fields are not empty)
    if password == confirm :
        f.write('{}'.format(password))
        messagebox.showinfo("Success", "Sign up successful!")
        root.destroy()
    else:
        messagebox.showerror("Error", "Password Doesn't match")
def quit_app():
    root.destroy()

def about():

# Create a Tkinter window
    window = tk.Tk()
    window.title("Resized Image")
    window.attributes('-fullscreen', True)
    window.configure(background='lightblue',bg='limegreen')
    start=aboutclass(window)
    window.mainloop()
def feature():

# Create a Tkinter window
    window = tk.Tk()
    window.title("Resized Image")
    window.attributes('-fullscreen', True)
    window.configure(background='lightblue',bg='white')
    start=featureclass(window)
    window.mainloop()
if __name__ == "__main__":
    home()
    f=open("login.txt","a+")
    a=os.stat("login.txt").st_size
    if a==0:
                        root = tk.Tk()
                        root.title("Sign Up")
                        root.attributes('-fullscreen', True)
                        root.configure(background='lightblue',bg='green')
                        name=tk.Label(root,text='BAv2',font=("Courier New",100),
                          bg='green',
                          )
                        name.pack(pady=100)

                        # Username Label and Entry
                        username_label = tk.Label(root, text="Password:",font=("Arial", 15, "bold"),bg='green')
                        username_label.pack( padx=5, pady=1)
                        username_entry = tk.Entry(root,show="*",width=30,font=("Arial", 20, "bold"))
                        username_entry.pack(padx=100, pady=10)

                        # Password Label and Entry
                        password_label = tk.Label(root, text="Cofirm Password :",font=("Arial", 15, "bold"),bg='green')
                        password_label.pack(padx=5, pady=5)

                        password_entry = tk.Entry(root, show="",width=30,font=("Arial", 20, "bold"))
                        password_entry.pack(padx=5, pady=5)


                        # Email Label and Entry
                        # Sign Up Button
                        sign_up_button = tk.Button(root, text="Sign Up",font=("Courier New", 20 ,"bold"), command=sign_up,bg='royalblue',fg='black',bd=3)
                        sign_up_button.pack(padx=5, pady=50)
                        # Quit Button
                        quit_button = tk.Button(root, text="Quit",font=("Courier New", 17), command=quit_app,bg='red',fg='black',bd=3)
                        quit_button.pack(side=tk.RIGHT,padx=20, pady=0)

                        root.mainloop()

    else:
        login()
        main()
    
