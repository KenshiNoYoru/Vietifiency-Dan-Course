import json
import customtkinter as ctk
import flask
import requests

with open("LangServer.json", 'r') as f:
    Lang = json.load(f)

class GUI():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("500x600")
        self.root.resizable(0, 0)
        self.root.title("Vietifiency Dan Course Admin server")
        
        self.title = ctk.CTkLabel(self.root, text= Lang['Title'], font= ("Comics Sans", 30))
        self.title.pack()
        
        self.entry = ctk.CTkEntry(self.root, width= 500, height= 80, font= ("Script MT Bold", 30), placeholder_text= Lang["Entry"])
        self.entry.pack()
        self.entry.place(x = 0, y = 110)
        
        self.entry2 = ctk.CTkEntry(self.root, width= 500, height= 80, font= ("Script MT Bold", 30), placeholder_text= Lang["Entry1"])
        self.entry2.pack()
        self.entry2.place(x = 0, y = 220)
        
        self.add = ctk.CTkButton(self.root, width= 150, height= 50, font= ("Script MT Bold", 30), text= Lang["Button"])
        self.add.pack()
        self.add.place(x = 20, y = 500)
        
        self.delete = ctk.CTkButton(self.root, width= 150, height= 50, text= Lang["Button1"], font= ("Script MT Bold", 30))
        self.delete.pack()
        self.delete.place(x = 330, y = 500)
        
        self.data_push = {
            "code": self.entry,
            "name": self.entry2
        }
        
        def publish_to_server():
            requests.post("127.0.0.1:25565/student-code/", self.data_push)
        
    def run(self):
        self.root.mainloop()
        
        

        
if __name__ == "__main__":
    Gui = GUI()
    Gui.run()