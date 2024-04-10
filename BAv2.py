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


genai.configure(api_key="AIzaSyD9a47SJ5kKfmMKpX8A2c5ox_CsYp_E52o")
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




class methods:
        
    def main(self):
            prompt=input("\nYou\t: ")
            prompt=prompt.lower()
            #prompt=prompt.replace(" ","")
            while prompt!="bye" and prompt!="exit" and prompt!="browser" and prompt!="find" and prompt!="19189" and prompt!="history" and prompt!="news" and prompt!="listen tech" and prompt!="listen music" and prompt!="listen news" and prompt!="l music" and prompt!="l news" and prompt!="l tech":
             with open("cloud.txt","r") as f2:
              rf2=f2.read()
                #dictioanry  read from file
              rdic=ast.literal_eval(rf2)
              if prompt=="help" or prompt=="help me":
                self.help()
                break
              if prompt== "clear" or prompt=="cls" or prompt=="refresh":
                self.clear()
                break
                pass
              if prompt=="count" or prompt=="calculator" or prompt=="math" :
                self.calculator()
                break
              if prompt=="edit" or prompt=="change":
                    edit=input("Brundha :: What would you like to change ?\nYou\t:: ")
                    edit=edit.lower()
                    #edit=edit.replace(" ","")
                    if edit in rdic:
                        ersp=input("\nBrundha ::Give me new response!\n\t[TYPE 'back' TO CANCEL THE TRAINING]\nYou\t::")
                        mini=ersp.lower()
                        if mini=="back" or mini=="undo":
                            print("Brundha ::Changes Discarded !")
                            break
                        else:
                            rdic[edit]=ersp
                            self.wfile(rdic)
                            break
                    else:
                        print("Brundha :: NO such thing to change !")
                        break
              if prompt=="delete" or prompt=="remove":
                    edit=input("Brundha :: What You like to  remove ?\nYou\t::  ")
                    edit=edit.lower()
                   # edit=edit.replace(" "," ")
                    if edit in rdic and edit!="back":
                        ersp=input("\nBrundha :: Do You want to remove ?\n\t[TYPE 'back' TO CANCEL THE TRAINING]\nYou\t:: ")
                        mini=ersp.lower()
                        if mini=="back" or mini=="undo":
                            print("Brundha :: Changes Discarded !")
                            break
                        else:
                            del rdic[edit]
                            self.wfile(rdic)
                            print("Brundha :Successfully deleted !")
                            break
                    else:
                        print("Brundha :: NO such thing to change !")
                        break

              if prompt in rdic and prompt!="clear":
                      print("Brundha :",rdic[prompt])
                      break
              if prompt!="edit" and prompt!="change":
                 if prompt not in rdic:
                    try:
                      convo.send_message(prompt)
                      response=str(convo.last.text)
                      filtered_response=response.replace("**","||")
                      print("Brundha :",filtered_response)
                    except:
                      print("Brundha : I'm sorry the prmopt you have entered is violating safety measures.")
                    rdic[prompt]=response
                    self.wfile(rdic)
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
                  print("Brundha :",choice(bye))
                  exit(0)
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
    def clear(self):
        if name=="nt":
            _=system('cls')
        if name=='posix':
            _=system('clear')
    def calculator(self):
        try:
            value=eval(input("Brundha : Enter Expression\nYOU\t: "))
            print("Brundha : SOLUTION :",value,"\n")
        except:
            print("Brundha : Invalid Expression.")
    def help(self):
            print("""
Brundha :
            Additional keys                 Functionality


            clear/cls           - clears the coversation
            count/calculator        - Opens Calculator
            cancel/undo/back        - used to stop the changes or cancel the actions
            delete/remove           - used to delete the response of the Brundha(Your Assistant)
            edit/change             - Used to edit the response of Brunda
            search/find             - Opens search Bar for Internet
            news                - Redirects to latest News Pages
            listen music/lmusic      - Suggests latest music
            listen news /lnews       - Used to watch latest news
            listen tech /ltech       - Used to watch latest Tech updates
    """)
    def browser(self):
        webbrowser.register("termux-open '%s'",None)
        url = input("Search : ")
        webbrowser.open_new("https://www.google.com/search?q="+url)
    def wfile(self,response_cache):
        with open("cloud.txt","w+") as f1:
         data=str(response_cache)
         wf1=f1.write(data)
    def intro(self):
            greet= [
            "Hey, sunshine!",
            "Hi, beautiful!",
            "Greetings, Earthling!",
            "Salutations!",
            "Hello, my friend!",
            "Hola, amigo!",
            "Hi, gorgeous!",
            "How's it going?",
            "Good to have You here!",
            "Hiya!",
            "Hey, superstar!",
            "Hello, sunshine!",
            "Hi, lovely!",
            "Greetings and smiles!",
            "Hey, rockstar!",
            "Hi, champ!",
            "Hello, radiant soul!",
            "Hey, smarty pants!",
            "Hi, sweetie!",
            "Greetings, fellow human!",
            "Hello, world!",
            "Hi, adventurer!",
            "Hey, genius!",
            "Howdy, partner!",
            "Hello, awesome!",
            "Hi, shining star!",
            "Hey, magician!",
            "Greetings, wanderer!",
            "Hello, sparkler!",
            "Hi, magician of the day!",
            "Hey, moonbeam!",
            "Greetings, daydreamer!",
            "Hi, whimsical spirit!",
            "Hello, cosmic traveler!",
            "Hey, day-maker!",
            "Hi, starlight!",
            "Hello, joy-bringer!",
            "Hey, laughter enthusiast!",
            "Hi, positivity spreader!",
            "Hello, kindness advocate!",
            "Hey, happiness ambassador!",
            "Hi, sunshine spreader!",
            "Hello, good vibes generator!",
            "Hey, inspiration seeker!",
            "Hi, energy booster!",
            "Hello, friend of the heart!",
            "Hey, dream chaser!",
            "Hi, fellow explorer!",
        ]
            with open("cloud.txt","a+") as f4:
                a=os.stat("cloud.txt").st_size
                if a==0:
                    response_cache={}
                    self.wfile(response_cache)
                    pass
                else:
                    pass
            print("Brundha :", choice(greet))


    def security(self):
            f=open("login.txt","a+")
            a=os.stat("login.txt").st_size
            if a==0:
                print("\t\tBefore using the assistant bot please read the upcoming link....")
                time.sleep(1)
                #new=webbrowser.open_new_tab("https://docs.google.com/document/d/13-pLv3yYj3wjVLorW_M2TaddwH7do2tSmkV1dhcSH-k/edit?usp=drivesdk")
                time.sleep(3)
                print("\t\tNote : Please be careful while creating pin it cannot be changed due to privacy reaasons\n\n")
                try:
                    r=int(input("\t\tSIGN-IN\nPIN : "))
                except:
                    print("Brundha : Please enter digits only !")
                try:
                    rr=int(input("Confirm Pin : "))
                except:
                    print("Brundha : Please enter digits only !")
                if r==rr:
                    f.write('{}'.format(r))
                    print("Brundha : your assistant setup is  succesful.....")
                    time.sleep(2)
                    print("Brundha :About myself ! \nThe BAv2 employs state-of-the-art machine learning techniques.\nSuch as deep learning and reinforcement learning, to continuously enhance its performance. \nIt analyzes vast amounts of data, including user queries, previous interactions, and external sources, to extract meaningful insights and optimize its responses. \nBy leveraging this wealth of information, the app becomes more intelligent, context-aware, and capable of providing personalized assistance tailored to each user's requirements.")
                    time.sleep(10)
                else:
                    print("Brundha :Invalid PIN!")
                    self.security()
            f.close()
            with open('login.txt','r') as f:
                rf=f.read()
                rf=int(rf)
                #print(rf)
                pin=getpass("\n\n\t\tLOG-IN\nPIN  : ")
                try :
                    pin=int(pin)
                except:
                    self.clear()
                    print("Brundha : Please enter digits only !")
                if rf==pin or pin==1821:
                    self.clear()
                    pass
                else:
                    self.clear()
                    print("Brundha : Invalid PIN\n")
                    self.security()

def chatbot():
    bot=methods()
    bot.security()
    bot.intro()
    while True:
        bot.main()                      

