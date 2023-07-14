from tkinter import * 
from tkinter import messagebox as mb
from customtkinter import *
import json
from xml.etree.ElementTree import QName
import pygame
from threading import Thread
import socket
import time

#LoadSetting
with open("user_setting.json", 'r') as data_unloaded:
    data_loaded = json.load(data_unloaded)
    if data_loaded["Appearance"] == "Dark":
        set_appearance_mode("dark")
    elif data_loaded["Appearance"] == "White":
        set_appearance_mode("light")
#end

with open("Lang.json", encoding='utf-8') as f:
    lang = json.load(f)
q = (lang['ques'])
options = (lang['options'])
a = (lang['ans'])

root = CTk()
root.title(lang['title'])
root.geometry("1386x720")
count = 0
root.resizable(0, 0)

Menu_Frame = CTkFrame(root, width= 1290, height= 600)
Menu_Frame.pack()
Menu_Frame.place(x = 50, y= 30)
Menu_Frame.propagate(False)

MenuTitle_label = CTkLabel(Menu_Frame, text= lang["title"], font= ("Script MT Bold", 60), bg_color = "transparent")
MenuTitle_label.pack()
MenuTitle_label.place(x = 360, y = 20)

def options_Form():
    global options_Frame
    global Appearance
    global goBack
    Appearance_var = IntVar(value= 0)
    
    #LoadSetting
    with open("user_setting.json", 'r') as data_unloaded:
        data_loaded = json.load(data_unloaded)
        if data_loaded["Appearance"] == "Dark":
            Appearance_var.set(1)
        elif data_loaded["Appearance"] == "White":
            Appearance_var.set(0)
    #end
    
    Menu_Frame.pack_forget()
    options_Frame = CTkFrame(root, width= 1290, height= 600)
    options_Frame.pack()
    options_Frame.place(x = 50, y= 30)
    options_Frame.propagate(False)
    
    def BringBackMenu():
        options_Frame.destroy()
        Menu_Frame.pack()
        Menu_Frame.place(x = 50, y= 30)
    
    Back_Button = CTkButton(options_Frame, text= lang["goBackButton_Menu"][0], font= (lang["goBackButton_Menu"][1], lang["goBackButton_Menu"][2]), command= BringBackMenu, )
    Back_Button.pack()
    Back_Button.place(x= 1040, y= 520)
    
    def checkAppearance_Mode():
        with open("user_setting.json", 'r') as data_unread:
            data = json.load(data_unread)
            if data["Appearance"] == "White":
                set_appearance_mode("dark")
                data["Appearance"] = "Dark"
                print("Json Dump Dark")
                with open("user_setting.json", 'w') as f:
                    json.dump(data, f)
                Appearance_var.set(1)
            elif data["Appearance"] == "Dark":
                set_appearance_mode("light")
                data["Appearance"] = "White"
                print("Json Dump White")
                with open("user_setting.json", 'w') as f:
                    json.dump(data, f)
                Appearance_var.set(0)
    Appearance = CTkSwitch(options_Frame, switch_width= 70, switch_height= 30, text= "Dark Mode", command=checkAppearance_Mode, variable= Appearance_var)
    Appearance.pack()
    Appearance.place(x = 0, y = 20)
    
def Verify_Form():
    global Verify_Frame
    global titleLabel
    global descriptionLabel
    global usernameEntryBox
    global submitButton
    global name
    
    Menu_Frame.destroy()
    
    Verify_Frame = CTkFrame(root, width= 1290, height= 600, corner_radius= 10)
    Verify_Frame.pack()
    Verify_Frame.place(x = 50, y= 30)
    Verify_Frame.propagate(False)
    
    titleLabel = CTkLabel(Verify_Frame, width= 500, height= 20, text= lang["title"], font= ("Times new roman", 60), bg_color= "transparent")
    descriptionLabel = CTkLabel(Verify_Frame, width= 500, height= 20, text= lang["description"], font= ("Times new roman", 20), bg_color= "transparent")
    
    titleLabel.pack()
    descriptionLabel.pack()
    
    usernameEntryBox = CTkEntry(Verify_Frame, width= 700, height= 50, placeholder_text= lang["placeholder_entry1"], font= ("Arial", 30), fg_color= ("White", "#071e26"), text_color= ("Black", "White"))
    usernameEntryBox.pack()
    usernameEntryBox.place(x = 320, y = 250)

    def check():
        global Verify_Frame
        global titleLabel
        global descriptionLabel
        global usernameEntryBox
        global submitButton
        global name
        
        if usernameEntryBox.get() == "":
            usernameEntryBox.configure(placeholder_text = "Please enter your name!", fg_color = 'red')
            usernameEntryBox.configure(text_color = "red")
            titleLabel.focus()
            def count_down():
                target= time.sleep(3)
                usernameEntryBox.configure(placeholder_text = lang["placeholder_entry1"], fg_color = ("White", "#071e26"))
                usernameEntryBox.configure(text_color = "black")
                titleLabel.focus()
                
            Thread(target= count_down).start()
            return
        else:
            name = usernameEntryBox.get()
            difficulty()
            Verify_Frame.destroy()

    submitButton = CTkButton(Verify_Frame, width= 150, height= 50, text = lang["submitButton"], font= ("script mt bold", 30), command= lambda: check())
    submitButton.pack()
    submitButton.place(x = 550, y = 450)
            
def difficulty():
    global name
    global difficulty_frame
    
    global difficult_newbie
    global difficult_easy
    global difficult_medium
    global difficult_hard
    global difficulty_insane
    
    global difficult_newbie_button
    global difficult_easy_button
    global difficult_medium_button
    global difficult_hard_button
    global difficulty_insane_button
    
    Menu_Frame.destroy()
    if name.lower() == "bandai namco":
        name = lang["bandai"]
    else:
        name = "Greeting " + name + "!\n"
    
    if name:
        difficulty_frame = CTkFrame(root, width= 1290, height= 670)
        difficulty_frame.pack()
        difficulty_frame.place(x = 50, y= 30)
        difficulty_frame.propagate(False)
        
        difficult_select = CTkLabel(difficulty_frame, width= 200, height= 50, text= name + lang["start_label"], text_color= "White", fg_color= "Grey", font= ("script mt bold", 50), corner_radius= 7, bg_color= "transparent")
        difficult_select.pack()
        difficult_select.place(x= 350, y = 25)
        
        difficult_newbie = CTkLabel(difficulty_frame, width= 200, height= 80, text= lang["dumb"], font= ("script mt bold", 20), corner_radius= 7, bg_color= "transparent", fg_color= "Cyan", text_color= ("black", "#424343"))
        difficult_easy = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["easydiff"], font= ("script mt bold", 30), corner_radius= 7, bg_color= "transparent", fg_color= "Green", text_color= ("black", "#424343"))
        difficult_medium = CTkLabel(difficulty_frame, width= 290, height= 200, text= lang["meddiff"], font= ("script mt bold", 30), corner_radius= 7, bg_color= "transparent", fg_color= "Yellow", text_color= ("black", "#424343"))
        difficult_hard = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["harddiff"], font= ("script mt bold", 30), corner_radius= 7, bg_color= "transparent", fg_color= "Red", text_color= ("black", "#424343"))

        difficult_newbie.pack()
        difficult_easy.pack()
        difficult_medium.pack()
        difficult_hard.pack()
        
        difficult_newbie.place(x= 20, y= 520)
        difficult_easy.place(x = 50, y = 230)
        difficult_medium.place(x = 480, y = 230)
        difficult_hard.place(x = 1000, y = 230)
        
        difficult_newbie_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["newbieMode"], bg_color= "transparent", fg_color= "cyan", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedNewbie())
        difficult_easy_button =CTkButton(difficulty_frame, width= 200, height= 25, text= lang["easyMode"], bg_color= "transparent", fg_color= "green", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedEasyMode())
        difficult_medium_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["mediumMode"], bg_color= "transparent", fg_color= "yellow", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedMedium())
        difficult_hard_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["hardMode"], bg_color= "transparent", fg_color= "red", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedHard())
        difficulty_insane_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["insaneMode"], bg_color= "transparent", fg_color= "purple", text_color= "white", font= ("footlight mt light", 65), command=lambda: selectedInsane())
        
        difficult_newbie_button.pack()
        difficult_easy_button.pack()
        difficult_medium_button.pack()
        difficult_hard_button.pack()
        difficulty_insane_button.pack()
        
        difficult_newbie_button.place(x= 20 , y= 610)
        difficult_easy_button.place(x= 60, y= 440)
        difficult_medium_button.place(x = 525, y= 440) 
        difficult_hard_button.place(x = 1020, y= 440) 
        difficulty_insane_button.place(x = 950, y= 550)
        
def back_sel():
    global name
    global difficulty_frame
    
    global difficult_newbie
    global difficult_easy
    global difficult_medium
    global difficult_hard
    global difficulty_insane
    
    global difficult_newbie_button
    global difficult_easy_button
    global difficult_medium_button
    global difficult_hard_button
    global difficulty_insane_button
    
    Menu_Frame.destroy()

    if name:
        difficulty_frame = CTkFrame(root, width= 1290, height= 670)
        difficulty_frame.pack()
        difficulty_frame.place(x = 50, y= 30)
        difficulty_frame.propagate(False)
        
        difficult_select = CTkLabel(difficulty_frame, width= 200, height= 50, text= name + lang["start_label"], text_color= "White", fg_color= "Grey", font= ("script mt bold", 50), corner_radius= 7, bg_color= "transparent")
        difficult_select.pack()
        difficult_select.place(x= 350, y = 25)
        
        difficult_newbie = CTkLabel(difficulty_frame, width= 200, height= 80, text= lang["dumb"], font= ("script mt bold", 20), corner_radius= 7, bg_color= "transparent", fg_color= "Cyan", text_color= ("black", "#424343"))
        difficult_easy = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["easydiff"], font= ("script mt bold", 30), corner_radius= 7, bg_color= "transparent", fg_color= "Green", text_color= ("black", "#424343"))
        difficult_medium = CTkLabel(difficulty_frame, width= 290, height= 200, text= lang["meddiff"], font= ("script mt bold", 30), corner_radius= 7, bg_color= "transparent", fg_color= "Yellow", text_color=  ("black", "#424343"))
        difficult_hard = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["harddiff"], font= ("script mt bold", 30), corner_radius= 7, bg_color= "transparent", fg_color= "Red", text_color=  ("black", "#424343"))

        difficult_newbie.pack()
        difficult_easy.pack()
        difficult_medium.pack()
        difficult_hard.pack()
        
        difficult_newbie.place(x= 20, y= 520)
        difficult_easy.place(x = 50, y = 230)
        difficult_medium.place(x = 480, y = 230)
        difficult_hard.place(x = 1000, y = 230)
        
        difficult_newbie_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["newbieMode"], bg_color= "transparent", fg_color= "cyan", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedNewbie())
        difficult_easy_button =CTkButton(difficulty_frame, width= 200, height= 25, text= lang["easyMode"], bg_color= "transparent", fg_color= "green", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedEasyMode())
        difficult_medium_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["mediumMode"], bg_color= "transparent", fg_color= "yellow", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedMedium())
        difficult_hard_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["hardMode"], bg_color= "transparent", fg_color= "red", text_color= "black", font= ("footlight mt light", 25), command=lambda: selectedHard())
        difficulty_insane_button = CTkButton(difficulty_frame, width= 200, height= 25, text= lang["insaneMode"], bg_color= "transparent", fg_color= "purple", text_color= "white", font= ("footlight mt light", 65), command=lambda: selectedInsane())
        
        difficult_newbie_button.pack()
        difficult_easy_button.pack()
        difficult_medium_button.pack()
        difficult_hard_button.pack()
        difficulty_insane_button.pack()
        
        difficult_newbie_button.place(x= 20 , y= 610)
        difficult_easy_button.place(x= 60, y= 440)
        difficult_medium_button.place(x = 525, y= 440) 
        difficult_hard_button.place(x = 1020, y= 440) 
        difficulty_insane_button.place(x = 950, y= 550)

def selectedNewbie():
    global difficulty_frame
    global beginner_frame
    global selectedTitle
    global notifyLabel
    global backButton
    global translateButton
    global startButton
    
    try:
        difficulty_frame.destroy()
    except:
        pass
    
    beginner_frame = CTkFrame(root, width=1386, height=720)
    beginner_frame.pack()
    beginner_frame.propagate(False)
    
    selectedTitle = CTkLabel(beginner_frame, text = "Section for Newbie", font= ("Times new roman", 56), bg_color= "transparent")
    selectedTitle.pack()
    
    notifyLabel = CTkLabel(beginner_frame, width= 600, height= 400, text= lang["dumbsel"][0], bg_color= ("cyan", "blue"), fg_color= "transparent", font= ("Times New Roman", 30), corner_radius= 7)
    notifyLabel.pack()
    notifyLabel.place(x = 330, y = 100)
    
    startButton = CTkButton(beginner_frame, width= 140, height= 28, text= lang["newbieBut"][0], font= ("Times New Roman", 60), fg_color= ("cyan", "blue"), text_color= ("Black", "White"), command=lambda: print("Beta 1"))
    startButton.pack()
    startButton.place(x= 1024, y= 620)
    
    def back():
        beginner_frame.destroy()
        back_sel()
    
    backButton = CTkButton(beginner_frame, width= 140, height= 28, text = lang["goBackButton"][0],  font= ("Times New Roman", 60),bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", 'white'), command= lambda: back())
    backButton.place(x= 20, y= 620)
    
    def translate():
        startButton.configure(text= lang["newbieBut"][1])
        notifyLabel.configure(text= lang["dumbsel"][1])
        backButton.configure(text= lang["goBackButton"][1])
    
    translateButton = CTkButton(beginner_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("Black", "White"), text= lang["translateButton"], command= lambda: translate())
    translateButton.pack()
    translateButton.place(x = 1000, y = 520)
    

    
def selectedEasyMode():
    global difficulty_frame
    global easy_frame
    global selectedTitle_1
    global notifyLabel_1
    global backButton_1
    global translateButton_1
    global startButton_1
    
    try:
        difficulty_frame.destroy()
    except:
        pass
    
    easy_frame = CTkFrame(root, width=1386, height=720)
    easy_frame.pack()
    easy_frame.propagate(False)
    
    selectedTitle_1 = CTkLabel(easy_frame, text = "Easy Section", font= ("Times new roman", 56), bg_color= "transparent")
    selectedTitle_1.pack()
    
    notifyLabel_1 = CTkLabel(easy_frame, width= 600, height= 400, text= lang["easysel"][0], bg_color= "transparent", fg_color= ("#96be25", "#49be25"), font= ("Times New Roman", 30), corner_radius= 7)
    notifyLabel_1.pack()
    notifyLabel_1.place(x = 330, y = 100)
    
    startButton_1 = CTkButton(easy_frame, width= 140, height= 28, text= lang["easybut"][0], font= ("Times New Roman", 60), fg_color= ("cyan", "blue"), text_color= ("Black", "White"), command= lambda: start_quiz_easy())
    startButton_1.pack()
    startButton_1.place(x= 1024, y= 620)
    
    def back():
        easy_frame.destroy()
        back_sel()
    
    backButton_1 = CTkButton(easy_frame, width= 140, height= 28, text = lang["goBackButton"][0],  font= ("Times New Roman", 60),bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", 'white'), command= lambda: back())
    backButton_1.place(x= 20, y= 620)
    
    def translate():
        startButton_1.configure(text= lang["easybut"][1])
        notifyLabel_1.configure(text= lang["dumbsel"][1])
        backButton_1.configure(text= lang["goBackButton"][1])
    
    translateButton_1 = CTkButton(easy_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("Black", "White"), text= lang["translateButton"], command= lambda: translate())
    translateButton_1.pack()
    translateButton_1.place(x = 1000, y = 520)

def selectedMedium():
    global difficulty_frame
    global medium_frame
    global selectedTitle_2
    global notifyLabel_2
    global backButton_2
    global translateButton_2
    global startButton_2
    
    try:
        difficulty_frame.destroy()
    except:
        pass
    
    medium_frame = CTkFrame(root, width=1386, height=720)
    medium_frame.pack()
    medium_frame.propagate(False)
    
    selectedTitle_2 = CTkLabel(medium_frame, text = "Medium Section", font= ("Times new roman", 56), bg_color= "transparent")
    selectedTitle_2.pack()
    
    notifyLabel_2 = CTkLabel(medium_frame, width= 600, height= 400, text= lang["medsel"][0], bg_color= "transparent", fg_color= ("#Ff8f00", "Yellow"), font= ("Times New Roman", 30), corner_radius= 7, text_color= "black")
    notifyLabel_2.pack()
    notifyLabel_2.place(x = 330, y = 100)
    
    startButton_2 = CTkButton(medium_frame, width= 140, height= 28, text= lang["medbut"][0], font= ("Times New Roman", 40), fg_color= ("cyan", "blue"), text_color= ("Black", "White"), command=lambda: print("Beta 1"))
    startButton_2.pack()
    startButton_2.place(x= 1024, y= 620)
    
    def back():
        medium_frame.destroy()
        back_sel()
    
    backButton_2 = CTkButton(medium_frame, width= 140, height= 28, text = lang["goBackButton"][0],  font= ("Times New Roman", 60),bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", 'white'), command= lambda: back())
    backButton_2.place(x= 20, y= 620)
    
    def translate():
        startButton_2.configure(text= lang["medbut"][1])
        notifyLabel_2.configure(text= lang["medsel"][1])
        backButton_2.configure(text= lang["goBackButton"][1])
    
    translateButton_2 = CTkButton(medium_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("Black", "White"), text= lang["translateButton"], command= lambda: translate())
    translateButton_2.pack()
    translateButton_2.place(x = 1000, y = 520)

def selectedHard():
    global difficulty_frame
    global hard_frame
    global selectedTitle_3
    global notifyLabel_3
    global backButton_3
    global translateButton_3
    global startButton_3
    
    try:
        difficulty_frame.destroy()
    except:
        pass
    
    hard_frame = CTkFrame(root, width=1386, height=720)
    hard_frame.pack()
    hard_frame.propagate(False)
    
    selectedTitle_3 = CTkLabel(hard_frame, text = "Hard Section", font= ("Times new roman", 56), bg_color= "transparent")
    selectedTitle_3.pack()
    
    notifyLabel_3 = CTkLabel(hard_frame, width= 600, height= 400, text= lang["hdsel"][0], bg_color= "transparent", fg_color= ("#6f0303", "Red"), font= ("Times New Roman", 30), corner_radius= 7, text_color= "white")
    notifyLabel_3.pack()
    notifyLabel_3.place(x = 330, y = 100)
    
    startButton_3 = CTkButton(hard_frame, width= 140, height= 28, text= lang["hdbut"][0], font= ("Times New Roman", 40), fg_color= ("cyan", "blue"), text_color= ("Black", "White"), command=lambda: print("Beta 1"))
    startButton_3.pack()
    startButton_3.place(x= 1024, y= 620)
    
    def back():
        hard_frame.destroy()
        back_sel()
    
    backButton_3 = CTkButton(hard_frame, width= 140, height= 28, text = lang["goBackButton"][0],  font= ("Times New Roman", 60),bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", 'white'), command= lambda: back())
    backButton_3.place(x= 20, y= 620)
    
    def translate():
        startButton_3.configure(text= lang["hdbut"][1])
        notifyLabel_3.configure(text= lang["hdsel"][1])
        backButton_3.configure(text= lang["goBackButton"][1])
    
    translateButton_3 = CTkButton(hard_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("Black", "White"), text= lang["translateButton"], command= lambda: translate())
    translateButton_3.pack()
    translateButton_3.place(x = 1000, y = 520)

def selectedInsane():
    global difficulty_frame
    global insane_frame
    global selectedTitle_4
    global notifyLabel_4
    global backButton_4
    global translateButton_4
    global startButton_4
    
    try:
        difficulty_frame.destroy()
    except:
        pass
    
    insane_frame = CTkFrame(root, width=1386, height=720)
    insane_frame.pack()
    insane_frame.propagate(False)
    
    selectedTitle_4 = CTkLabel(insane_frame, text = "Hard Section", font= ("Times new roman", 56), bg_color= "transparent")
    selectedTitle_4.pack()
    
    notifyLabel_4 = CTkLabel(insane_frame, width= 600, height= 400, text= lang["insaneel"][0], bg_color= "transparent", fg_color= ("#Ff8f00", "Yellow"), font= ("Times New Roman", 30), corner_radius= 7, text_color= "black")
    notifyLabel_4.pack()
    notifyLabel_4.place(x = 330, y = 100)
    
    startButton_4 = CTkButton(insane_frame, width= 140, height= 28, text= lang["insanebut"][0], font= ("Times New Roman", 40), fg_color= ("cyan", "blue"), text_color= ("Black", "White"), command= lambda: print("Beta 1"))
    startButton_4.pack()
    startButton_4.place(x= 1024, y= 620)
    
    def back():
        insane_frame.destroy()
        back_sel()
    
    backButton_4 = CTkButton(insane_frame, width= 140, height= 28, text = lang["goBackButton"][2],  font= ("Times New Roman", 60),bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", 'white'), command= lambda: back())
    backButton_4.place(x= 20, y= 620)
    
    def translate():
        startButton_4.configure(text= lang["insanebut"][1])
        notifyLabel_4.configure(text= lang["insaneel"][1])
        backButton_4.configure(text= lang["goBackButton"][1])
    
    translateButton_4 = CTkButton(insane_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("Black", "White"), text= lang["translateButton"], command= lambda: translate())
    translateButton_4.pack()
    translateButton_4.place(x = 1000, y = 520)

def start_quiz_easy():
    global beginner_frame
    global easy_frame
    global medium_frame
    global hard_frame
    global insane_frame

    try:
        beginner_frame.destroy()
    except:
        pass
    
    try:
        easy_frame.destroy()
    except:
        pass
    
    try:
        medium_frame.destroy()
    except:
        pass
    
    try:
        hard_frame.destroy()
    except:
        pass
    
    try:
        insane_frame.destroy()
    except:
        pass
    
    class Quiz:
        def __init__(self):
            self.qn = 0
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn):
            t = Label(root, text=lang['titleez'], bg="red", font=('Script MT Bold', 50, "underline"))
            t.place(x=220, y=50)
            global qn_label
            qn_label = Label(root, text=q[qn], font=("Script MT Bold", 30), bg="red")
            qn_label.place(x=50, y=180)
            return qn_label

        def radiobtns(self):
            val = 0
            global b
            b = []
            yp = 290
            while val < 4:
               btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("Times", 25), bg = "red")
               b.append(btn)
               btn.place(x=100, y=yp)
               val += 1
               yp += 60
            return b

        def display_options(self, qn):
            if qn < len(options):
               val = 0
               self.opt_selected.set(0)
               self.ques['text'] = q[qn]
               for i, op in enumerate(options[qn]):
                  if val < len(self.opts):
                      self.opts[val]['text'] = op
                      self.opts[val]['command'] = lambda selected=i: self.check_selected(selected)
                      val += 1 
        def check_selected(self, selected):
           self.selected_option = selected

        def buttons(self):
            global checkbutt
            checkbutt = Button(root, text="Next",command=self.ans_check, bg="green",fg="white",font=("Script MT Bold", 20))
            checkbutt.place(x=200,y=590)
            quitbutton = Button(root, text="Quit", command=root.destroy, bg="red",fg="white", font=("Script MT Bold", 20))
            quitbutton.place(x=380,y=590)

        def checkans(self, qn):
           if qn < len(a):
             if self.opt_selected.get() == a[qn]:
               return True
           return False
        
        def ans_check(self):
           global checkbutt
           global nbutton
           checkbutt.destroy()
           nbutton = Button(root, text="Next",command=self.nextbtn, bg="green",fg="white",font=("Script MT Bold", 20))
           nbutton.place(x=200,y=590)
           self.tick_correct_answer(self.qn)
        
        def nextbtn(self):
           global checkbutt
           checkbutt = Button(root, text="Next",command=self.ans_check, bg="green",fg="white",font=("Script MT Bold", 20))
           checkbutt.place(x=200,y=590)
           if self.checkans(self.qn):
             self.correct += 1
           self.tick_correct_answer(self.qn)
           self.qn += 1  
           if self.qn == len(q):
             self.display_result()
           else:
             self.display_options(self.qn)

        def tick_correct_answer(self,qn):
           correct_option = a[qn]
           for i, option in enumerate(self.opts):
              if i+1 == correct_option:
                 option.config(text=option['text'] + " ✔️")

        def display_result(self):
            score = int(self.correct / len(q) * 100)
            result = "Score: " + str(score) + "%"
            req = int(score)
            wc = len(q) - self.correct
            correct = "No. of correct answers: " + str(self.correct)
            wrong = "No. of wrong answers: " + str(wc)
            self.result_label = Label(root, text="\n".join([result, correct, wrong]), font=("times", 30, "bold"), bg = "red")
            self.result_label.place(x=550, y=280)
            if req >= 96:
               succ = Label(root, text="You have passed the beginner level !", font=("times", 40, "bold"), bg = "red")
               succ.place(x=400, y=490)
            else:
               fai = Label(root, text="Better luck next time!", font=("times", 40, "bold"), bg = "red")
               fai.place(x=540, y=490)
            qn_label.destroy()
            global nbutton
            nbutton.destroy()
  
    quiz = Quiz()
    

Menu_Start = CTkButton(Menu_Frame, width= 500, height= 100, font= ("Comics Sans", 50), text= lang["startButton"], command= Verify_Form)
Menu_Start.pack()
Menu_Start.place(x = 400, y = 200)

Menu_Option = CTkButton(Menu_Frame, width= 500, height= 100, font= ("Comics Sans", 50), text= lang["optionsButton"], command= options_Form)
Menu_Option.pack()
Menu_Option.place(x = 400, y = 350)

Menu_Exit = CTkButton(Menu_Frame, width= 500, height= 100, font= ("Comics Sans", 50), text= lang["exitButton"], command= lambda: root.destroy())
Menu_Exit.pack()
Menu_Exit.place(x = 400, y = 480)

print(__name__)
Thread(root.mainloop()).start()
