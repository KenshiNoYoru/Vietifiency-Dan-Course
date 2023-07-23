from tkinter import * 
from tkinter import messagebox as mb
from customtkinter import *
import json
from xml.etree.ElementTree import QName
import pygame
from threading import Thread
from time import time, sleep

print(f"This program run in: {time()}")

with open("Data\\user_setting.json", 'r') as data_unloaded:
    data_loaded = json.load(data_unloaded)
    if data_loaded["Appearance"] == "Dark":
        set_appearance_mode("dark")
    elif data_loaded["Appearance"] == "White":
        set_appearance_mode("light")

with open("Data\\Lang.json", encoding='utf-8') as f:
    global lang
    lang = json.load(f)

with open("Data\\foundation.json", encoding='utf-8') as fA1:
    global foundation
    foundation = json.load(fA1)

q = (lang['ques'])
options = (lang['options'])
a = (lang['ans'])

root = CTk()
root.title(lang['title'])
root.geometry("1386x720")
count = 0
root.resizable(0, 0)
root.iconbitmap(".\\Resource\\Iconv2.ico")

#load_data_again
with open("Data\\user_setting.json", 'r') as data_unloaded:
    data_loaded = json.load(data_unloaded)
    if data_loaded["Resizable"] == True:
        root.resizable(1, 1)
    elif data_loaded["Resizable"] == False:
        root.resizable(0, 0)

Menu_Frame = CTkFrame(root, width= 1290, height= 600)
Menu_Frame.pack()
Menu_Frame.place(x = 50, y= 30)
Menu_Frame.propagate(False)

MenuTitle_label = CTkLabel(Menu_Frame, text= lang["title"], font= ("Times new roman", 60), bg_color = "transparent")
MenuTitle_label.pack()
MenuTitle_label.place(x = 360, y = 20)

def options_Form():
    global options_Frame
    global Appearance
    global Resize
    global goBack
    global resolutionString
    global resolutionVar
    
    resolution = []

    with open("Data\\user_setting.json", 'r') as reso:
        resolutionString = json.load(reso)
    
    
    Appearance_var = IntVar(value= 0)
    Resize_Var = BooleanVar(value = False)
    resolutionVar = StringVar()

    #LoadSetting
    with open("Data\\user_setting.json", 'r') as data_unloaded:
        data_loaded = json.load(data_unloaded)
        if data_loaded["Appearance"] == "Dark":
            Appearance_var.set(1)
        elif data_loaded["Appearance"] == "White":
            Appearance_var.set(0)
        
        if data_loaded["Resizable"] == True:
            Resize_Var.set(value = True)
            root.resizable(1, 1)
        elif data_loaded["Resizable"] == False:
            Resize_Var.set(value = False)
            root.resizable(0, 0)
    #end
    
    Menu_Frame.pack_forget()
    options_Frame = CTkFrame(root, width= 1290, height= 600)
    options_Frame.pack()
    options_Frame.place(x = 50, y= 30)
    options_Frame.propagate(False)
    
    def BringBackMenu():
        global root
        root.update()
        options_Frame.destroy()
        Menu_Frame.pack()
        Menu_Frame.place(x = 50, y= 30)
        
    
    Back_Button = CTkButton(options_Frame, text= lang["goBackButton_Menu"][0], font= (lang["goBackButton_Menu"][1], lang["goBackButton_Menu"][2]), command= BringBackMenu)
    Back_Button.pack()
    Back_Button.place(x= 1040, y= 520)
    
    def checkAppearance_Mode():
        with open("Data\\user_setting.json", 'r') as data_unread:
            data = json.load(data_unread)
            if data["Appearance"] == "White":
                set_appearance_mode("dark")
                data["Appearance"] = "Dark"
                print("Json Dump Dark")
                with open("Data\\user_setting.json", 'w') as f:
                    json.dump(data, f)
                Appearance_var.set(1)
            elif data["Appearance"] == "Dark":
                set_appearance_mode("light")
                data["Appearance"] = "White"
                print("Json Dump White")
                with open("Data\\user_setting.json", 'w') as f:
                    json.dump(data, f)
                Appearance_var.set(0)
                
    def check_Resizable():
        with open("Data\\user_setting.json", 'r') as data_unread:
            data = json.load(data_unread)
            if data["Resizable"] == True:
                root.resizable(0, 0)
                data["Resizable"] = False
                print("Resizable: On")
                with open("Data\\user_setting.json", 'w') as f:
                    json.dump(data, f)
                Resize_Var.set(False)
                
            elif data["Resizable"] == False:
                root.resizable(1, 1)
                data["Resizable"] = True
                print("Resizable: Off")
                with open("Data\\user_setting.json", 'w') as f:
                    json.dump(data, f)
                Resize_Var.set(True)
    
    def change_Resolution():
        for i in lang["Resolution"]:
            if resolutionVar.get() == lang["ComboResolutionBox"][i]:
                root.geometry(f"{resolutionVar.get()}")
        
    
    Appearance = CTkSwitch(options_Frame, switch_width= 70, switch_height= 30, text= "Dark Mode", command=checkAppearance_Mode, variable= Appearance_var)
    Appearance.pack()
    Appearance.place(x = 0, y = 20)
    
    resoComboBox = CTkComboBox(options_Frame, width= 500, height= 50, values = lang["ResolutionComboBox"], font= ("Times new roman", 50), variable= resolutionVar, command= lambda: change_Resolution())
    resoComboBox.pack()
    resoComboBox.place(x = 0, y = 140)
    
    Resize = CTkSwitch(options_Frame, switch_width= 70, switch_height= 30, text= "Resizable", command=check_Resizable, variable= Resize_Var)
    Resize.pack()
    Resize.place(x = 0, y = 90)


def Verify_Form():
    global Verify_Frame
    global titleLabel
    global descriptionLabel
    global usernameEntryBox
    global submitButton
    global name
    global Back_Button_VF
    
    Menu_Frame.destroy()
    
    Verify_Frame = CTkFrame(root, width= 1290, height= 600, corner_radius= 10)
    Verify_Frame.pack()
    Verify_Frame.place(x = 50, y= 30)
    Verify_Frame.propagate(False)
    
    titleLabel = CTkLabel(Verify_Frame, width= 500, height= 20, text= lang["title"], font= ("Times new roman", 60), bg_color= "transparent")
    descriptionLabel = CTkLabel(Verify_Frame, width= 500, height= 20, text= lang["description"], font= ("Times new roman", 20), bg_color= "transparent")
    
    titleLabel.pack()
    descriptionLabel.pack()
    
    usernameEntryBox = CTkEntry(Verify_Frame, width= 700, height= 50, placeholder_text= lang["placeholder_entry1"], font= ("Arial", 30), fg_color= "#071e26", text_color= "white")
    usernameEntryBox.pack()
    usernameEntryBox.place(x = 320, y = 250)

    def back_mn_from_vf():
        global root
        root.update()
        options_Frame.destroy()
        Menu_Frame.pack()
        Menu_Frame.place(x = 50, y= 30)

    def check():
        global Verify_Frame
        global titleLabel
        global descriptionLabel
        global usernameEntryBox
        global submitButton
        global name
        
        if usernameEntryBox.get() == "":
            usernameEntryBox.configure(placeholder_text = "Please enter your name!", fg_color = 'red')
            titleLabel.focus()
            def count_down():
                sleep(1.2)
                usernameEntryBox.configure(placeholder_text = lang["placeholder_entry1"], fg_color= "#071e26", text_color= "white")
                usernameEntryBox.configure(text_color = "white")
                titleLabel.focus()
                
            Thread(target= count_down).start()
            return
        
        else:
            name = usernameEntryBox.get()
            difficulty()
            Verify_Frame.destroy()

    submitButton = CTkButton(Verify_Frame, width= 150, height= 50, text = lang["submitButton"], font= ("Times new roman", 30), command= lambda: check())
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
        
        difficult_select = CTkLabel(difficulty_frame, width= 200, height= 50, text= name + lang["start_label"], text_color= "White", fg_color= "Grey", font= ("Times new roman", 50), corner_radius= 7, bg_color= "transparent")
        difficult_select.pack()
        difficult_select.place(x= 350, y = 25)
        
        difficult_newbie = CTkLabel(difficulty_frame, width= 200, height= 80, text= lang["dumb"], font= ("Times new roman", 20, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Cyan", text_color= "black")
        difficult_easy = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["easydiff"], font= ("Times new roman", 30, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Green", text_color= "black")
        difficult_medium = CTkLabel(difficulty_frame, width= 290, height= 200, text= lang["meddiff"], font= ("Times new roman", 30, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Yellow", text_color= "black")
        difficult_hard = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["harddiff"], font= ("Times new roman", 30, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Red", text_color= "black")

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
        
        #Load Data
        with open("Data\\user_achievement.json") as data_unloaded:
            data_loaded = json.load(data_unloaded)
            if data_loaded["NewbieMode"] == True:
                difficult_newbie_button.configure(text = lang["newbieMode"] + "✔")

            if data_loaded["EasyMode"] == True:
                difficult_easy_button.configure(text = lang["easyMode"] + "✔")
                
            if data_loaded["MediumMode"] == True:
                difficult_medium_button.configure(text = lang["mediumMode"] + "✔")
                
            if data_loaded["HardMode"] == True:
                difficult_hard_button.configure(text = lang["hardMode"] + "✔")

            if data_loaded["InsaneMode"] == True:
                difficulty_insane_button.configure(text = lang["insaneMode"] + "✔")
        
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
        
        difficult_select = CTkLabel(difficulty_frame, width= 200, height= 50, text= name + lang["start_label"], text_color= "White", fg_color= "Grey", font= ("Times new roman", 50), corner_radius= 7, bg_color= "transparent")
        difficult_select.pack()
        difficult_select.place(x= 350, y = 25)
        
        difficult_newbie = CTkLabel(difficulty_frame, width= 200, height= 80, text= lang["dumb"], font= ("Times new roman", 20, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Cyan", text_color= "black")
        difficult_easy = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["easydiff"], font= ("Times new roman", 30, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Green", text_color= "black")
        difficult_medium = CTkLabel(difficulty_frame, width= 290, height= 200, text= lang["meddiff"], font= ("Times new roman", 30, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Yellow", text_color=  "black")
        difficult_hard = CTkLabel(difficulty_frame, width= 200, height= 200, text= lang["harddiff"], font= ("Times new roman", 30, "bold"), corner_radius= 7, bg_color= "transparent", fg_color= "Red", text_color=  "black")

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
        
        #Load Data
        with open("Data\\user_achievement.json") as data_unloaded:
            data_loaded = json.load(data_unloaded)
            if data_loaded["NewbieMode"] == True:
                difficult_newbie_button.configure(text = lang["newbieMode"] + "✔")

            if data_loaded["EasyMode"] == True:
                difficult_easy_button.configure(text = lang["easyMode"] + "✔")
                
            if data_loaded["MediumMode"] == True:
                difficult_medium_button.configure(text = lang["mediumMode"] + "✔")
                
            if data_loaded["HardMode"] == True:
                difficult_hard_button.configure(text = lang["hardMode"] + "✔")

            if data_loaded["InsaneMode"] == True:
                difficulty_insane_button.configure(text = lang["insaneMode"] + "✔")

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
    
    startButton = CTkButton(beginner_frame, width= 140, height= 28, text= lang["newbieBut"][0], font= ("Times New Roman", 60), fg_color= ("cyan", "blue"), text_color= ("black", "white"), command=lambda: Newbie_Mode())
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
    
    translateButton = CTkButton(beginner_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", "white"), text= lang["translateButton"], command= lambda: translate())
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
    
    startButton_1 = CTkButton(easy_frame, width= 140, height= 28, text= lang["easybut"][0], font= ("Times New Roman", 60), fg_color= ("cyan", "blue"), text_color= ("black", "white"), command= lambda: start_quiz_easy())
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
    
    translateButton_1 = CTkButton(easy_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", "white"), text= lang["translateButton"], command= lambda: translate())
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
    
    startButton_2 = CTkButton(medium_frame, width= 140, height= 28, text= lang["medbut"][0], font= ("Times New Roman", 40), fg_color= ("cyan", "blue"), text_color= ("black", "white"), command=lambda: print("Beta 1"))
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
    
    translateButton_2 = CTkButton(medium_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", "white"), text= lang["translateButton"], command= lambda: translate())
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
    
    startButton_3 = CTkButton(hard_frame, width= 140, height= 28, text= lang["hdbut"][0], font= ("Times New Roman", 40), fg_color= ("cyan", "blue"), text_color= ("black", "white"), command=lambda: print("Beta 1"))
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
    
    translateButton_3 = CTkButton(hard_frame, width= 140, height= 28, bg_color= "transparent", fg_color= ("cyan", "blue"), text_color= ("black", "white"), text= lang["translateButton"], command= lambda: translate())
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
    
    startButton_4 = CTkButton(insane_frame, width= 140, height= 28, text= lang["insanebut"][0], font= ("Times New Roman", 40), fg_color= ("cyan", "blue"), text_color= ("black", "white"), command= lambda: print("Beta 1"))
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
    
    translateButton_4 = CTkButton(insane_frame, width= 140, height= 28, bg_color= "red", fg_color= ("cyan", "blue"), text_color= ("black", "white"), text= lang["translateButton"], command= lambda: translate())
    translateButton_4.pack()
    translateButton_4.place(x = 1000, y = 520)

def Newbie_Mode():
    #Frame
    global NB_Page1
    global NB_Page2
    global NB_Page3
    global beginner_frame
    global Newbie_Frame
    global small_Newbie_Frame
    global Newbie_Title_Mode
    global Newbie_label_Mode
    global Next_Page_1
    
    beginner_frame.destroy()
    
    NB_Page1 = CTkFrame(root, width=1386, height= 1000, bg_color= "transparent")
    NB_Page1.pack()
    NB_Page1.propagate(False)
    
    Newbie_Frame = CTkFrame(NB_Page1, width= 1290, height= 600, corner_radius= 10)
    Newbie_Frame.pack()
    Newbie_Frame.place(x = 50, y = 20)
    Newbie_Frame.propagate(False)
    
    #Move the location of the main window and increase it's height. 1386x100 = width and height, +350 and +0 = the location of the window
    first_location = f"+{root.winfo_x()}+{root.winfo_y()}"
    print(first_location)
    root.geometry("1386x720+350+0")

    small_Newbie_Frame = CTkFrame(NB_Page1, width= 1290, height= 200, corner_radius= 10)
    small_Newbie_Frame.pack()
    small_Newbie_Frame.place(x = 50, y = 500)
    small_Newbie_Frame.propagate(False)
    
    #Question or label
    Newbie_Title_Mode = CTkLabel(Newbie_Frame, font= ("Times New Roman", 40), bg_color= "transparent", text_color= ("black", "white"), text= "Newbie session")
    Newbie_Title_Mode.pack()
    
    Newbie_label_Mode = CTkLabel(Newbie_Frame, font= ("Times New Roman", 40), bg_color= ("Grey", "White"), text_color= ("White", "Black"), text= foundation["theAlphabet"], width= 1024, height= 320)
    Newbie_label_Mode.pack()
    Newbie_label_Mode.place(x= 150,y= 150)
    
    
    class Sound:
        pygame.mixer.init()
        def play_sound1():
            pygame.mixer.music.load("./\\Sound\\Letters\\A.mp3")
            pygame.mixer.music.play()  
        def play_sound2():
            pygame.mixer.music.load("./\\Sound\\Letters\\Ă.mp3")
            pygame.mixer.music.play() 
        def play_sound3():
            pygame.mixer.music.load("./\\Sound\\Letters\\Â.mp3")
            pygame.mixer.music.play()
        def play_sound4(): 
            pygame.mixer.music.load("./\\Sound\\Letters\\B.mp3")
            pygame.mixer.music.play()  
        def play_sound5():
            pygame.mixer.music.load("./\\Sound\\Letters\\C.mp3")
            pygame.mixer.music.play() 
        def play_sound6():
            pygame.mixer.music.load("./\\Sound\\Letters\\D.mp3")
            pygame.mixer.music.play()
        def play_sound7():
            pygame.mixer.music.load("./\\Sound\\Letters\\Đ.mp3")
            pygame.mixer.music.play()  
        def play_sound8():
            pygame.mixer.music.load("./\\Sound\\Letters\\E.mp3")
            pygame.mixer.music.play() 
        def play_sound9():
            pygame.mixer.music.load("./\\Sound\\Letters\\Ê.mp3")
            pygame.mixer.music.play()  
        def play_sound10():
            pygame.mixer.music.load("./\\Sound\\Letters\\G.mp3")
            pygame.mixer.music.play()  
        def play_sound11():
            pygame.mixer.music.load("./\\Sound\\Letters\\H.mp3")
            pygame.mixer.music.play() 
        def play_sound12(): 
            pygame.mixer.music.load("./\\Sound\\Letters\\I.mp3")
            pygame.mixer.music.play()  
        def play_sound13():
            pygame.mixer.music.load("./\\Sound\\Letters\\K.mp3")
            pygame.mixer.music.play()  
        def play_sound14():
            pygame.mixer.music.load("./\\Sound\\Letters\\L.mp3")
            pygame.mixer.music.play() 
        def play_sound15():
            pygame.mixer.music.load("./\\Sound\\Letters\\M.mp3")
            pygame.mixer.music.play()  
        def play_sound16():
            pygame.mixer.music.load("./\\Sound\\Letters\\N.mp3")
            pygame.mixer.music.play()  
        def play_sound17():
            pygame.mixer.music.load("./\\Sound\\Letters\\O.mp3")
            pygame.mixer.music.play() 
        def play_sound18():
            pygame.mixer.music.load("./\\Sound\\Letters\\Ô.mp3")
            pygame.mixer.music.play()
        def play_sound19():
            pygame.mixer.music.load("./\\Sound\\Letters\\Ơ.mp3")
            pygame.mixer.music.play()
        def play_sound20():
            pygame.mixer.music.load("./\\Sound\\Letters\\P.mp3")
            pygame.mixer.music.play()
        def play_sound21():
            pygame.mixer.music.load("./\\Sound\\Letters\\Q.mp3")
            pygame.mixer.music.play()
        def play_sound22():
            pygame.mixer.music.load("./\\Sound\\Letters\\R.mp3")
            pygame.mixer.music.play() 
        def play_sound23():
            pygame.mixer.music.load("./\\Sound\\Letters\\S.mp3")
            pygame.mixer.music.play()
        def play_sound24():
            pygame.mixer.music.load("./\\Sound\\Letters\\T.mp3")
            pygame.mixer.music.play() 
        def play_sound25():
            pygame.mixer.music.load("./\\Sound\\Letters\\U.mp3")
            pygame.mixer.music.play()
        def play_sound26():
            pygame.mixer.music.load("./\\Sound\\Letters\\Ư.mp3")
            pygame.mixer.music.play() 
        def play_sound27():
            pygame.mixer.music.load("./\\Sound\\Letters\\V.mp3")
            pygame.mixer.music.play()
        def play_sound28():
            pygame.mixer.music.load("./\\Sound\\Letters\\X.mp3")
            pygame.mixer.music.play() 
        def play_sound29(): 
            pygame.mixer.music.load("./\\Sound\\Letters\\Y.mp3")
            pygame.mixer.music.play()
        
    sound = Sound
    
    #Button and Page
    global Next_Button
    global A1_Button
    global A2_Button
    global A3_Button
    global B_Button
    global C_Button
    global D1_Button
    global D2_Button
    global E1_Button
    global E2_Button
    to_P1 = CTkButton(Newbie_Frame, width= 140, height= 28, bg_color= "red", fg_color= ("cyan", "blue"), text_color= ("black", "white"), text= "Next >>", command= Next_Page_1)
    to_P1.pack()
    
    letter = foundation["Letters"]
    
    def Next_Page_1():
        global Next_Button_P2
        global A2_Button_P2
        global A3_Button_P2
        global D2_Button_P2
        global E2_Button_P2
        global O2_Button_P2
        global O3_Button_P2
        global U1_Button_P2
        
        global U_Button_P2
        global V_Button_P2
        global X_Button_P2
        global Y_Button_P2
        global Back_Button_P2
        global Next_Page_2
        
        NB_Page1.destroy()
        NB_Page2 = CTkFrame(root, width=1386, height= 1000, bg_color= "transparent")
        NB_Page2.pack()
        NB_Page2.propagate(False)
        
        Frame1 = CTkFrame(NB_Page2, width= 1286, height= 100)
        Frame2 = CTkFrame(NB_Page2, width= 1286, height = 300)
        Frame3 = CTkFrame(NB_Page2, width= 1286, height= 300)
        
        Frame1.propagate(False)
        Frame2.propagate(False)
        Frame3.propagate(False)
        
        Frame1.pack()
        Frame2.pack()
        Frame3.pack()
        
        TitleLabel = CTkLabel(Frame1, bg_color = "transparent", text_color = ("black", "white"), text = lang["titledumb"], font = ("Times new roman", 60))
        Vowel_Label = CTkLabel(NB_Page2, text = foundation["Vowel"][1], bg_color = "transparent", fg_color = "transparent", text_color = ("black", "white"), font = ("Times new roman", 20))
        Non_Vowel_Label =  CTkLabel(NB_Page2, text = foundation["Vowel"][0], bg_color = "transparent", fg_color = "transparent", text_color = ("black", "white"), font = ("Times new roman", 20))
        
        TitleLabel.pack()
        Vowel_Label.pack()
        
        Vowel_Label.place(x = 55, y = 165)
        Non_Vowel_Label.place(x = 45, y = 525)
        
        Frame1.place(x = 50, y= 30)
        Frame2.place(x = 50, y= 200)
        Frame3.place(x = 50, y= 560)
        
        #Vowel Letters
        A1_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][0], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command = lambda: sound.play_sound2())
        A2_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][1], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command = lambda: sound.play_sound3())
        D1_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][2], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound7())
        E2_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][3], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound9())
        O2_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][4], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound18())
        O3_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][5], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound19())
        U1_Button_P2 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][6], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound26())
        
        A1_Button_P2.pack()
        A2_Button_P2.pack()
        D1_Button_P2.pack()
        E2_Button_P2.pack()
        O2_Button_P2.pack()
        O3_Button_P2.pack()
        U1_Button_P2.pack()
        
        A1_Button_P2.place(x = 20, y = 20)
        A2_Button_P2.place(x = 500, y = 20)
        D1_Button_P2.place(x = 980, y = 20)
        E2_Button_P2.place(x = 20, y = 130)
        O2_Button_P2.place(x = 500, y = 130)
        O3_Button_P2.place(x = 980, y = 130)
        U1_Button_P2.place(x = 20, y = 240)
        
        #Non-Vowel Letters
        U_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][0], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound25())
        V_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][1], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound27())
        X_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][2], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound28())
        Y_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][3], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound29())

        U_Button_P2.pack()
        V_Button_P2.pack()
        X_Button_P2.pack()
        Y_Button_P2.pack()
        
        U_Button_P2.place(x = 20, y = 20)
        V_Button_P2.place(x = 500, y = 20)
        X_Button_P2.place(x = 980, y = 20)
        Y_Button_P2.place(x = 20, y = 130)
        
        Next_Button_P2 = CTkButton(NB_Page2, font= ("Times new roman", 40), bg_color= "transparent", fg_color= ("cyan", "#154c79"), text_color= "black", text= lang["NextBut"],command= lambda: Next_Page_2())
        Next_Button_P2.pack()
        Next_Button_P2.place(x = 1160, y = 940)
        
        Back_Button_P2 = CTkButton(NB_Page2, font= ("Times new roman", 40), bg_color= "transparent", fg_color= ("cyan", "#154c79"), text_color= "black", text= lang["goBackButton"][1])
        Back_Button_P2.pack()
        Back_Button_P2.place(x = 50, y = 940)
        
        def Next_Page_2():
            global Next_Button_P3
            global A2_Button_P3
            global A3_Button_P3
            global D2_Button_P3
            global E2_Button_P3
            global O2_Button_P3
            global O3_Button_P3
            global U1_Button_P3
            
            global U_Button_P3
            global V_Button_P3
            global X_Button_P3
            global Y_Button_P3
            global Back_Button_P3
            global Next_Page_P3
            
            NB_Page2.destroy()
            NB_Page3 = CTkFrame(root, width=1386, height= 1000, bg_color= "transparent")
            NB_Page3.pack()
            NB_Page3.propagate(False)
            
            Frame1 = CTkFrame(NB_Page3, width= 1286, height= 100)
            Frame2 = CTkFrame(NB_Page3, width= 1286, height = 300)
            Frame3 = CTkFrame(NB_Page3, width= 1286, height= 300)
            
            Frame1.propagate(False)
            Frame2.propagate(False)
            Frame3.propagate(False)
            
            Frame1.pack()
            Frame2.pack()
            Frame3.pack()
            
            TitleLabel = CTkLabel(Frame1, bg_color = "transparent", text_color = ("black", "white"), text = lang["titledumb"], font = ("Times new roman", 60))
            Vowel_Label = CTkLabel(NB_Page3, text = foundation["Vowel"][1], bg_color = "transparent", fg_color = "transparent", text_color = ("black", "white"), font = ("Times new roman", 20))
            Non_Vowel_Label =  CTkLabel(NB_Page3, text = foundation["Vowel"][0], bg_color = "transparent", fg_color = "transparent", text_color = ("black", "white"), font = ("Times new roman", 20))
            
            TitleLabel.pack()
            Vowel_Label.pack()
            
            Vowel_Label.place(x = 55, y = 165)
            Non_Vowel_Label.place(x = 45, y = 525)
            
            Frame1.place(x = 50, y= 30)
            Frame2.place(x = 50, y= 200)
            Frame3.place(x = 50, y= 560)
            
            #Vowel Letters
            A1_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][0], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command = lambda: sound.play_sound2())
            A2_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][1], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command = lambda: sound.play_sound3())
            D1_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][2], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound7())
            E2_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][3], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound9())
            O2_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][4], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound18())
            O3_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][5], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound19())
            U1_Button_P3 = CTkButton(Frame3, font = ("Times new roman", 40, "bold"), text= foundation["Vowel_Letters"][6], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound26())
            
            A1_Button_P3.pack()
            A2_Button_P3.pack()
            D1_Button_P3.pack()
            E2_Button_P3.pack()
            O2_Button_P3.pack()
            O3_Button_P3.pack()
            U1_Button_P3.pack()
            
            A1_Button_P3.place(x = 20, y = 20)
            A2_Button_P3.place(x = 500, y = 20)
            D1_Button_P3.place(x = 980, y = 20)
            E2_Button_P3.place(x = 20, y = 130)
            O2_Button_P3.place(x = 500, y = 130)
            O3_Button_P3.place(x = 980, y = 130)
            U1_Button_P3.place(x = 20, y = 240)
            #Non-Vowel Letters
            U_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][0], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound25())
            V_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][1], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound27())
            X_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][2], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound28())
            Y_Button_P2 = CTkButton(Frame2, font = ("Times new roman", 40, "bold"), text= foundation["Non-Vowel_Letters"][3], text_color= ("White", "Black"), bg_color= "transparent", fg_color = "red", command= lambda: sound.play_sound29())

            U_Button_P2.pack()
            V_Button_P2.pack()
            X_Button_P2.pack()
            Y_Button_P2.pack()
            
            U_Button_P2.place(x = 20, y = 20)
            V_Button_P2.place(x = 500, y = 20)
            X_Button_P2.place(x = 980, y = 20)
            Y_Button_P2.place(x = 20, y = 130)
            
            Next_Button_P2 = CTkButton(NB_Page3, font= ("Times new roman", 40), bg_color= "transparent", fg_color= ("cyan", "#154c79"), text_color= "black", text= lang["NextBut"],command= lambda: Complete_Foundation())
            Next_Button_P2.pack()
            Next_Button_P2.place(x = 1160, y = 940)
            
            Back_Button_P2 = CTkButton(NB_Page3, font= ("Times new roman", 40), bg_color= "transparent", fg_color= ("cyan", "#154c79"), text_color= "black", text= lang["goBackButton"][1], command = lambda: Get_Back())
            Back_Button_P2.pack()
            Back_Button_P2.place(x = 50, y = 940)
        
            def Get_Back():
                Next_Page_1()
                NB_Page3.destroy()
        
            def Complete_Foundation():
                with open("Data\\user_achievement.json", 'r') as f:
                    Achievement = json.load(f)
                    Achievement["NewbieMode"] = True
                    with open("Data\\user_achievement.json", 'w') as f2:
                        json.dump(Achievement, f2)
                
                back_sel()
                root.geometry(f"1386x720{first_location}")
                NB_Page3.destroy()
            
        def Get_Back():
            Newbie_Mode()
            NB_Page2.destroy()
        
        Back_Button_P2.configure(command= lambda: Get_Back())
    
    Next_Button = CTkButton(NB_Page1, font= ("Times new roman", 40), bg_color= "transparent", fg_color= ("cyan", "#154c79"), text_color= "black", text= lang["NextBut"],command= lambda: Next_Page_1())
    Next_Button.pack()
    Next_Button.place(x = 1160, y = 940)
    
    A1_Button = CTkButton(small_Newbie_Frame, width= 200, height= 100, text= letter[0], bg_color= "transparent", fg_color= "red", corner_radius= 7, font= ("Times new roman", 32), command= lambda: sound.play_sound1())
    A2_Button = CTkButton(small_Newbie_Frame, width= 200, height= 100, text= letter[1], bg_color= "transparent", fg_color= "red", corner_radius= 7, font= ("Times new roman", 32), command= lambda: sound.play_sound2())
    A3_Button = CTkButton(small_Newbie_Frame, width= 200, height= 100, text= letter[2], bg_color= "transparent", fg_color= "red", corner_radius= 7, font= ("Times new roman", 32), command= lambda: sound.play_sound3())
    
    A1_Button.pack()
    A2_Button.pack()
    A3_Button.pack()
    
    A1_Button.place(x= 20, y = 50)
    A2_Button.place(x= 520, y = 50)
    A3_Button.place(x= 1000, y = 50)
    
    
    
#Easy Mode
def start_quiz_easy():
    global beginner_frame
    global easy_frame
    global medium_frame
    global hard_frame
    global insane_frame

    #Remove Frame
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
    #___________________________    

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
            t = Label(root, text=lang['titleez'], bg="red", font=('Times new roman', 50, "underline"))
            t.place(x=220, y=50)
            global qn_label
            qn_label = Label(root, text=q[qn], font=("Times new roman", 30), bg="red")
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
            checkbutt = Button(root, text="Next",command=self.ans_check, bg="green",fg="white",font=("Times new roman", 20))
            checkbutt.place(x=200,y=590)
            quitbutton = Button(root, text="Quit", command=root.destroy, bg="red",fg="white", font=("Times new roman", 20))
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
           nbutton = Button(root, text="Next",command=self.nextbtn, bg="green",fg="white",font=("Times new roman", 20))
           nbutton.place(x=200,y=590)
           self.tick_correct_answer(self.qn)
        
        def nextbtn(self):
           global checkbutt
           checkbutt = Button(root, text="Next",command=self.ans_check, bg="green",fg="white",font=("Times new roman", 20))
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
    

Menu_Start = CTkButton(Menu_Frame, width= 500, height= 100, font= ("Comics Sans", 50), text= lang["startButton"], command= lambda: Verify_Form())
Menu_Start.pack()
Menu_Start.place(x = 400, y = 200)

Menu_Option = CTkButton(Menu_Frame, width= 500, height= 100, font= ("Comics Sans", 50), text= lang["optionsButton"], command= lambda: options_Form())
Menu_Option.pack()
Menu_Option.place(x = 400, y = 350)

Menu_Exit = CTkButton(Menu_Frame, width= 500, height= 100, font= ("Comics Sans", 50), text= lang["exitButton"], command= lambda: root.destroy())
Menu_Exit.pack()
Menu_Exit.place(x = 400, y = 480)

print(__name__)
Thread(root.mainloop(), daemon = True).start()
