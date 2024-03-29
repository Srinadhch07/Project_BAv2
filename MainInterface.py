#main programs



import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")
        self.message_history = scrolledtext.ScrolledText(master,  width=10, height=10, wrap=tk.WORD, font=('Arial', 15),
                                          bg='skyblue', fg='black', insertbackground='black', insertwidth=4,
                                          selectbackground='yellow', selectforeground='black', bd=2, relief='ridge')
        self.message_history.pack(expand=True, fill=tk.BOTH)


        #Entry field
        self.entry_field =tk.Entry(master, textvariable='hello', width=40,show="", state='normal', bg='white',
                 fg='black', font=('bold', 20), insertbackground='white', insertwidth=10, bd=1, relief='solid', justify='left')
        self.entry_field.pack(side=tk.LEFT,padx=50)
        self.entry_field.bind("<Return>", self.send_message)

        
        #Buttons
        self.send = tk.Button(master, text="close",width=10,command=master.destroy,bg='red',fg='black',bd=3)
        self.send.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.clear_button = tk.Button(master, text="Clear",width=10, command=self.clear_text,bg='blue',bd=5,fg='white')
        self.clear_button.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.close = tk.Button(master, text="Send",width=10,command=self.send_message,bg='green',fg='white',bd=3)
        self.close.pack(side=tk.RIGHT, padx=20,pady=20)
          

    def clear_text(self):
        self.message_history.delete(1.0, tk.END)


    def send_message(self, event=None):
        message = self.entry_field.get()
        if message.strip() != "":
            self.message_history.insert(tk.END, "You  : " + message + "\n")
            self.entry_field.delete(0, tk.END)
            response=message
            self.message_history.insert(tk.END, "Bot   : " + message + "\n")

def main():
    root = tk.Tk()
    root.geometry("1500x700")
    root.attributes('-fullscreen', True)
    root.configure(background='lightblue',bg='black')
    app = ChatApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
