from tkinter import *
from tkinter import messagebox as mb
from customtkinter import *
import json
from xml.etree.ElementTree import QName
import pygame

root = Tk()
root.title('Vietifiency Dan Course')
root['bg'] = 'red'
root.geometry("1386x750")
count = 0

with open('./test1.json', encoding='utf-8') as f:
    label_data = json.load(f)
q = (label_data['ques'])
options = (label_data['options'])
a = (label_data['ans'])

label_t = Label(root, text=label_data['title'], font=('Arial', 50), bg='red')
label_t.place(x=350, y=50)
label_des = Label(root, text=label_data['description'], font=('Arial', 20), bg='red')
label_des.place(x=350, y=140)
label1 = Label(root, text=label_data['username_label'], font=('Arial', 30), bg='red')
label1.place(x=250, y=250)

def comm1():
    global name
    name = entry1.get()
    if name:
        greeting = "Xin chào, " + name + "!"
        global label2
        global label3
        global diffeasy
        global easytext
        global medtext
        global diffmed
        global diffhard
        global hdtext
        global dumb
        global dumbstart
        global diffe
        label2 = Label(root, text=greeting, font=('Arial', 30), bg="red")
        label2.place(x=520, y=50)
        label3 = Label(root, text=label_data['start_label'], font=('Arial', 40, "underline"), bg="red")
        label3.place(x=360, y=120)
        diffeasy = Button(root, text=label_data['button_text'], font=('Arial', 30), bg="red", command=selecteddiffez)
        diffeasy.place(x=150, y=520)
        easytext = Label(root, text=label_data['easydiff'], font=('Comic Sans MS', 25), bg="red")
        easytext.place(x=60, y=220)
        diffmed = Button(root, text=label_data['button_textm'], font=('Arial', 30), bg="red", command=selecteddiffnm)
        diffmed.place(x=490, y=520)
        medtext = Label(root, text=label_data['meddiff'], font=('Comic Sans MS', 25), bg="red")
        medtext.place(x=380, y=220)
        diffhard = Button(root, text=label_data['button_texth'], font=('Arial', 30), bg="red", command=selecteddiffhd)
        diffhard.place(x=890, y=520)
        hdtext = Label(root, text=label_data['harddiff'], font=('Comic Sans MS', 25), bg="red")
        hdtext.place(x=800, y=220)
        diffe = Button(root, text=label_data['button_textex'], font=('Arial', 30), bg="red")
        diffe.place(x=1150,y=330)
        dumb = Label(root, text=label_data['dumb'], font=('Comic Sans MS', 30), bg="red")
        dumb.place(x=320, y=640)
        dumbstart = Button(root, text=label_data['dumbstart'], font=('Arial', 25), bg ="red", command=selecteddumb)
        dumbstart.place(x=720, y=640)
        label_des.destroy()
        label1.destroy()
        entry1.destroy()
        button1.destroy()
        label_t.destroy()

def back_sel():
   global readybutt
   readybutt.destroy()
   global ready1
   ready1.destroy()
   global name
   greeting = "Xin chào, " + name + "!"
   global label2
   global label3
   global diffeasy
   global easytext
   global medtext
   global diffmed
   global diffhard
   global hdtext
   global dumb
   global dumbstart
   global diffe
   label2 = Label(root, text=greeting, font=('Arial', 30), bg="red")
   label2.place(x=520, y=50)
   label3 = Label(root, text=label_data['start_label'], font=('Arial', 40, "underline"), bg="red")
   label3.place(x=360, y=120)
   diffeasy = Button(root, text=label_data['button_text'], font=('Arial', 30), bg="red", command=selecteddiffez)
   diffeasy.place(x=150, y=520)
   easytext = Label(root, text=label_data['easydiff'], font=('Comic Sans MS', 25), bg="red")
   easytext.place(x=60, y=220)
   diffmed = Button(root, text=label_data['button_textm'], font=('Arial', 30), bg="red", command=selecteddiffnm)
   diffmed.place(x=490, y=520)
   medtext = Label(root, text=label_data['meddiff'], font=('Comic Sans MS', 25), bg="red")
   medtext.place(x=380, y=220)
   diffhard = Button(root, text=label_data['button_texth'], font=('Arial', 30), bg="red", command=selecteddiffhd)
   diffhard.place(x=890, y=520)
   hdtext = Label(root, text=label_data['harddiff'], font=('Comic Sans MS', 25), bg="red")
   hdtext.place(x=800, y=220)
   dumb = Label(root, text=label_data['dumb'], font=('Comic Sans MS', 30), bg="red")
   dumb.place(x=320, y=640)
   dumbstart = Button(root, text=label_data['dumbstart'], font=('Arial', 25), bg ="red", command=selecteddumb)
   dumbstart.place(x=720, y=640)
   diffe = Button(root, text=label_data['button_textex'], font=('Arial', 30), bg="red")
   diffe.place(x=1150,y=330)
   global back
   back.destroy()
   global t
   t.destroy()

def selecteddumb():
    global label2
    label2.destroy()
    global label3
    label3.destroy()
    global diffeasy
    diffeasy.destroy()
    global easytext
    easytext.destroy()
    global medtext
    medtext.destroy()
    global diffmed
    diffmed.destroy()
    global diffhard
    diffhard.destroy()
    global hdtext
    hdtext.destroy()
    global dumb
    dumb.destroy()
    global dumbstart
    dumbstart.destroy()
    global diffe
    diffe.destroy()
    global back
    back = Button(root, text="<< Back", font=('Arial', 20), bg="red", command=back_sel)
    back.place(x=30, y=600)
    global t
    t = Label(root, text=label_data['titledumb'], bg="red", font=('Arial', 50, "underline"))
    t.place(x=350, y=50)
    global ready1
    global readybutt
    ready1 = Label(root, text=label_data['dumbsel'], font=('Comic Sans MS', 25), bg="red")
    ready1.place(x=200, y=290)
    readybutt = Button(root, text=label_data['easybut'], font=('Comic Sans MS', 25), bg="red", command=foundation_lev)
    readybutt.place(x=600, y=490)

def selecteddiffez():
    global label2
    label2.destroy()
    global label3
    label3.destroy()
    global diffeasy
    diffeasy.destroy()
    global easytext
    easytext.destroy()
    global medtext
    medtext.destroy()
    global diffmed
    diffmed.destroy()
    global diffhard
    diffhard.destroy()
    global hdtext
    hdtext.destroy()
    global dumb
    dumb.destroy()
    global dumbstart
    dumbstart.destroy()
    global diffe
    diffe.destroy()
    global back
    back = Button(root, text="<< Back", font=('Arial', 20), bg="red", command=back_sel)
    back.place(x=30, y=600)
    global t
    t = Label(root, text=label_data['titleez'], bg="red", font=('Arial', 50, "underline"))
    t.place(x=220, y=50)
    global ready1
    global readybutt
    ready1 = Label(root, text=label_data['easysel'], font=('Comic Sans MS', 25), bg="red")
    ready1.place(x=170, y=290)
    readybutt = Button(root, text=label_data['easybut'], font=('Comic Sans MS', 25), bg="red", command=start_quiz_ez)
    readybutt.place(x=600, y=490)

def selecteddiffnm():
    global label2
    label2.destroy()
    global label3
    label3.destroy()
    global diffeasy
    diffeasy.destroy()
    global easytext
    easytext.destroy()
    global medtext
    medtext.destroy()
    global diffmed
    diffmed.destroy()
    global diffhard
    diffhard.destroy()
    global hdtext
    hdtext.destroy()
    global dumb
    dumb.destroy()
    global dumbstart
    dumbstart.destroy()
    global diffe
    diffe.destroy()
    global back
    back = Button(root, text="<< Back", font=('Arial', 20), bg="red", command=back_sel)
    back.place(x=30, y=600)
    global t
    t = Label(root, text=label_data['titlenm'], bg="red", font=('Arial', 50, "underline"))
    t.place(x=220, y=50)
    global ready1
    global readybutt
    ready1 = Label(root, text=label_data['medsel'], font=('Comic Sans MS', 25), bg="red")
    ready1.place(x=170, y=290)
    readybutt = Button(root, text=label_data['easybut'], font=('Comic Sans MS', 25), bg="red", command=start_quiz_ez)
    readybutt.place(x=600, y=490)

def selecteddiffhd():
    global label2
    label2.destroy()
    global label3
    label3.destroy()
    global diffeasy
    diffeasy.destroy()
    global easytext
    easytext.destroy()
    global medtext
    medtext.destroy()
    global diffmed
    diffmed.destroy()
    global diffhard
    diffhard.destroy()
    global hdtext
    hdtext.destroy()
    global dumb
    dumb.destroy()
    global dumbstart
    dumbstart.destroy()
    global diffe
    diffe.destroy()
    global back
    back = Button(root, text="<< Back", font=('Arial', 20), bg="red", command=back_sel)
    back.place(x=30, y=600)
    global t
    t = Label(root, text=label_data['titlehd'], bg="red", font=('Arial', 50, "underline"))
    t.place(x=220, y=50)
    global ready1
    global readybutt
    ready1 = Label(root, text=label_data['hdsel'], font=('Comic Sans MS', 25), bg="red")
    ready1.place(x=170, y=290)
    readybutt = Button(root, text=label_data['hdbut'], font=('Comic Sans MS', 25), bg="red", command=start_quiz_ez)
    readybutt.place(x=600, y=490)

def foundation_lev():
    global readybutt
    readybutt.destroy()
    global ready1
    ready1.destroy()
    global back
    back.destroy()
    class Foundation:
      with open("./foundation.json", encoding='utf-8') as f:
           global word_data
           word_data = json.load(f)

      global intro
      global abc
      global abcintro
      intro = Label(root, text=word_data['intro'], font=('Comic Sans MS', 25), bg="red")
      intro.place(x=200, y=130)
      abc = Label(root, text=word_data['intro1'], font=('Comic Sans MS', 25, "bold"), bg="red")
      abc.place(x=110, y=220)
      abcintro = Label(root, text=word_data['abcintro'], font=('Comic Sans MS', 25), bg="red")
      abcintro.place(x=250, y=400)
      global play_sound1
      global play_sound2
      global play_sound3
      def play_sound1():
         pygame.mixer.init()
         pygame.mixer.music.load("./\\Sound\\Letter\\A.mp3")
         pygame.mixer.music.play()  
      def play_sound2():
         pygame.mixer.init()
         pygame.mixer.music.load("./\\Sound\\Letter\\Ă.mp3")
         pygame.mixer.music.play() 
      def play_sound3():
         pygame.mixer.init()
         pygame.mixer.music.load("./\\Sound\\Letter\\Â.mp3")
         pygame.mixer.music.play()  
      global sample1
      global sample2
      global sample3 
      sample1 = Button(root, text="A", font=('Times', 72), bg="red", command=play_sound1)
      sample2 = Button(root, text="Ă", font=('Times', 72), bg="red", command=play_sound2)
      sample3 = Button(root, text="Â", font=('Times', 72), bg="red", command=play_sound3)
      sample1.place(x=290, y=520)
      sample2.place(x=590, y=520)
      sample3.place(x=890, y=520)
      global alph_tech
      def alph_tech():
         global intro
         intro.destroy()
         global abc
         abc.destroy()
         global abcintro
         abcintro.destroy()
         global sample1
         sample1.destroy()
         global sample2
         sample2.destroy()
         global sample3 
         sample3.destroy()
         global next_page
         next_page.destroy()
         abcdown = Label(root, text=word_data['thealph'], font=('Comic Sans MS', 25), bg="red")
         abcdown.place(x=300, y=150)
         global nonvowel
         nonvowel = Label(root, text="Non-vowel Character:", font=('Comic Sans MS', 25, "bold", "underline"), bg="red")
         nonvowel.place(x=20, y=250)
         font_size = 25
         def play_sound4():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\B.mp3")
            pygame.mixer.music.play()  
         def play_sound5():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\C.mp3")
            pygame.mixer.music.play() 
         def play_sound6():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\D.mp3")
            pygame.mixer.music.play()
         def play_sound7():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Đ.mp3")
            pygame.mixer.music.play()  
         def play_sound8():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\E.mp3")
            pygame.mixer.music.play() 
         def play_sound9():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Ê.mp3")
            pygame.mixer.music.play()  
         def play_sound10():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\G.mp3")
            pygame.mixer.music.play()  
         def play_sound11():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\H.mp3")
            pygame.mixer.music.play() 
         def play_sound12():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\I.mp3")
            pygame.mixer.music.play()  
         def play_sound13():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\K.mp3")
            pygame.mixer.music.play()  
         def play_sound14():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\L.mp3")
            pygame.mixer.music.play() 
         def play_sound15():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\M.mp3")
            pygame.mixer.music.play()  
         def play_sound16():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\N.mp3")
            pygame.mixer.music.play()  
         def play_sound17():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\O.mp3")
            pygame.mixer.music.play() 
         def play_sound18():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Ô.mp3")
            pygame.mixer.music.play()
         def play_sound19():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Ơ.mp3")
            pygame.mixer.music.play()
         def play_sound20():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\P.mp3")
            pygame.mixer.music.play()
         def play_sound21():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Q.mp3")
            pygame.mixer.music.play()
         def play_sound22():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\R.mp3")
            pygame.mixer.music.play() 
         def play_sound23():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\S.mp3")
            pygame.mixer.music.play()
         def play_sound24():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\T.mp3")
            pygame.mixer.music.play() 
         def play_sound25():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\U.mp3")
            pygame.mixer.music.play()
         def play_sound26():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Ư.mp3")
            pygame.mixer.music.play() 
         def play_sound27():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\V.mp3")
            pygame.mixer.music.play()
         def play_sound28():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\X.mp3")
            pygame.mixer.music.play() 
         def play_sound29():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Letter\\Y.mp3")
            pygame.mixer.music.play()
         letter1 = Button(root, text="A", font=('Times', font_size), bg="red", command=play_sound1)
         letter1.place(x=30, y=300)
         expl1 = Label(root, text="/α:/‘a’ as in father", font=('Arial', 20), bg="red")
         expl1.place(x=100, y=310)
         letter4 = Button(root, text="B", font=('Times', font_size), bg="red", command=play_sound4)
         letter4.place(x=350, y=300)
         expl2 = Label(root, text="/ɓ/ ‘b’ as in big", font=('Arial', 20), bg="red")
         expl2.place(x=420, y=310)
         letter5 = Button(root, text="C", font=('Times', font_size), bg="red", command=play_sound5)
         letter5.place(x=640, y=300)
         expl3 = Label(root, text="/k/ ‘c’ as in cat", font=('Arial', 20), bg="red")
         expl3.place(x=710, y=310)
         letter6 = Button(root, text="D", font=('Times', font_size), bg="red", command=play_sound6)
         letter6.place(x=950, y=300)
         expl4 = Label(root, text="/z/,/j/ ‘z’ as in zoo (north),\n‘y’ as in yes (south)", font=('Arial', 20), bg="red")
         expl4.place(x=1020, y=300)
         letter8 = Button(root, text="E", font=('Times', font_size), bg="red", command=play_sound8)
         letter8.place(x=30, y=380)
         expl5 = Label(root, text="/ε/ ‘e’ as in get", font=('Arial', 20), bg="red")
         expl5.place(x=100, y=390)
         letter10 = Button(root, text="G", font=('Times', font_size), bg="red", command=play_sound10)
         letter10.place(x=320, y=380)
         expl6 = Label(root, text="/ɣ/ ‘g’ as in good", font=('Arial', 20), bg="red")
         expl6.place(x=390, y=390)
         letter11 = Button(root, text="H", font=('Times', font_size), bg="red", command=play_sound11)
         letter11.place(x=620, y=380)
         expl7 = Label(root, text="/h/ ‘h’ as in house", font=('Arial', 20), bg="red")
         expl7.place(x=690, y=390)
         letter12 = Button(root, text="I", font=('Times', font_size), bg="red", command=play_sound12)
         letter12.place(x=940, y=380)
         expl8 = Label(root, text="/i/ ‘i’ as in machine", font=('Arial', 20), bg="red")
         expl8.place(x=1000, y=390)
         letter13 = Button(root, text="K", font=('Times', font_size), bg="red", command=play_sound13)
         letter13.place(x=30, y=460)
         expl9 = Label(root, text="/k/ ‘c’ as in cat", font=('Arial', 20), bg="red")
         expl9.place(x=90, y=470)
         letter14 = Button(root, text="L", font=('Times', font_size), bg="red", command=play_sound14)
         letter14.place(x=300, y=460)
         expl10 = Label(root, text="/l/ ‘l’ as in life", font=('Arial', 20), bg="red")
         expl10.place(x=360, y=470)
         letter15 = Button(root, text="M", font=('Times', font_size), bg="red", command=play_sound15)
         letter15.place(x=550, y=460)
         expl11 = Label(root, text="/m/ ‘m’ as in man", font=('Arial', 20), bg="red")
         expl11.place(x=610, y=470)
         letter16 = Button(root, text="N", font=('Times', font_size), bg="red", command=play_sound16)
         letter16.place(x=850, y=460)
         expl12 = Label(root, text="/n/ ‘n’ as in nice", font=('Arial', 20), bg="red")
         expl12.place(x=910, y=470)
         letter17 = Button(root, text="O", font=('Times', font_size), bg="red", command=play_sound17)
         letter17.place(x=1130, y=460)
         expl13 = Label(root, text="/ɔ/ ‘o’ as in hot", font=('Arial', 20), bg="red")
         expl13.place(x=1190, y=470)
         letter20 = Button(root, text="P", font=('Times', font_size), bg="red", command=play_sound20)
         letter20.place(x=30, y=550)
         expl14 = Label(root, text="/p/ ‘p’ as in pet", font=('Arial', 20), bg="red")
         expl14.place(x=100, y=560)
         letter21 = Button(root, text="Q", font=('Times', font_size), bg="red", command=play_sound21)
         letter21.place(x=300, y=550)
         expl15 = Label(root, text="/q/ ‘q’ as in queue", font=('Arial', 20), bg="red")
         expl15.place(x=390, y=560)
         letter22 = Button(root, text="R", font=('Times', font_size), bg="red", command=play_sound22)
         letter22.place(x=630, y=550)
         expl16 = Label(root, text="/z/, /ɹ/ ‘z’ as in zoo (north), ‘r’ as in ring (south)", font=('Arial', 20), bg="red")
         expl16.place(x=690, y=560)
         letter23 = Button(root, text="S", font=('Times', font_size), bg="red", command=play_sound23)
         letter23.place(x=30, y=640)
         expl17 = Label(root, text="/s/, /∫/ ‘s’ as in sore (north), ‘s’ as in sure (south)", font=('Arial', 20), bg="red")
         expl17.place(x=100, y=650)
         letter24 = Button(root, text="T", font=('Times', font_size), bg="red", command=play_sound24)
         letter24.place(x=720, y=640)
         expl18 = Label(root, text="/t/ ‘t’ as in stop", font=('Arial', 20), bg="red")
         expl18.place(x=790, y=650)
         letter26 = Button(root, text="Ư", font=('Times', font_size), bg="red", command=play_sound26)

         def ending_0():
             for widget in root.winfo_children():
                 if widget != t:
                     widget.destroy()
         
         def to_page_2():
             ending_0()
             page_2()

         global nextpbutt
         nextpbutt = Button(root, text="Next >>", font=('Times', font_size), bg="red", command=to_page_2)
         nextpbutt.place(x=1200, y=650)

         global page_2
         def page_2():

            def back_alpha_tech():
                for widget in root.winfo_children():
                    if widget != t:
                        widget.destroy()
                    alph_tech()
            
            back_button = Button(root, text="<< Back", font=('Times', 30), bg="red")
            back_button.place(x=20, y=20)
            back_button['command'] = back_alpha_tech

            nonvowel = Label(root, text="Non-vowel Character:", font=('Comic Sans MS', 25, "bold", "underline"), bg="red")
            nonvowel.place(x=20, y=250)
            nonvowel.place(x=20, y=150)
            letter25 = Button(root, text="U", font=('Times', font_size), bg="red", command=play_sound25)
            letter25.place(x=20, y=220)
            expl19 = Label(root, text="/ʊ/ ‘oo’ as in boot", font=('Arial', 20), bg="red")
            expl19.place(x=80, y=230)
            letter27 = Button(root, text="V", font=('Times', font_size), bg="red", command=play_sound27)
            letter27.place(x=360, y=220)
            expl20 = Label(root, text="/v/, /j/ ‘v’ as in van (north), ‘y’ as in yes (south)", font=('Arial', 20), bg="red")
            expl20.place(x=420, y=230)
            letter28 = Button(root, text="X", font=('Times', font_size), bg="red", command=play_sound28)
            letter28.place(x=1020, y=220)
            expl21 = Label(root, text="/s/ ‘s’ as in sore", font=('Arial', 20), bg="red")
            expl21.place(x=1070, y=230)
            letter29 = Button(root, text="Y", font=('Times', font_size), bg="red", command=play_sound29)
            letter29.place(x=20, y=320)
            expl22 = Label(root, text="/i/ ‘I’ as in pin", font=('Arial', 20), bg="red")
            expl22.place(x=80, y=330)
            vowel = Label(root, text="Vowel Character:", font=('Comic Sans MS', 25, "bold", "underline"), bg="red")
            vowel.place(x=20, y=400) 
            letter2 = Button(root, text="Ă", font=('Times', font_size), bg="red", command=play_sound2)
            letter2.place(x=20, y=450)
            expl23 = Label(root, text="/ɜ/ ‘u’ as in but", font=('Arial', 20), bg="red")
            expl23.place(x=80, y=460)
            letter3 = Button(root, text="Â", font=('Times', font_size), bg="red", command=play_sound3)
            letter3.place(x=320, y=450)
            expl24 = Label(root, text="/α/ ‘a’ as in hat", font=('Arial', 20), bg="red")
            expl24.place(x=380, y=460)
            letter7 = Button(root, text="Đ", font=('Times', font_size), bg="red", command=play_sound7)
            letter7.place(x=620, y=450)
            expl25 = Label(root, text="/ɗ/ ‘d’ as in done", font=('Arial', 20), bg="red")
            expl25.place(x=680, y=460)
            letter9 = Button(root, text="Ê", font=('Times', font_size), bg="red", command=play_sound9)
            letter9.place(x=920, y=450)
            expl26 = Label(root, text="/e/ ‘a’ as in mate", font=('Arial', 20), bg="red")
            expl26.place(x=980, y=460)
            letter18 = Button(root, text="Ô", font=('Times', font_size), bg="red", command=play_sound18)
            letter18.place(x=20, y=550)
            expl27 = Label(root, text="/o/ ‘oa’ as in boat", font=('Arial', 20), bg="red")
            expl27.place(x=80, y=560)
            letter19 = Button(root, text="Ơ", font=('Times', font_size), bg="red", command=play_sound19)
            letter19.place(x=320, y=550)
            expl28 = Label(root, text="/ɜ:/ ‘u’ as in fur", font=('Arial', 20), bg="red")
            expl28.place(x=380, y=560)
            letter26 = Button(root, text="Ư", font=('Times', font_size), bg="red", command=play_sound26)
            letter26.place(x=620, y=550)
            expl29 = Label(root, text="/ɨ/ ‘oo’ as in boot", font=('Arial', 20), bg="red")
            expl29.place(x=680, y=560)

            def ending1():
                for widget in root.winfo_children():
                    if widget != t:
                        widget.destroy()
            
            def to_the_next():
                ending1()
                word_tech()

            global towordtech
            towordtech = Button(root, text="Next >>", font=('Times', font_size), bg="red", command=to_the_next)
            towordtech.place(x=1200, y=650)

      global word_tech
      def word_tech():
            global title_tone
            title_tone = Label(root, text="Tones and Vocabulary", font=('Comic Sans MS', 30, "underline", "bold"), bg="red")
            title_tone.place(x=480, y=140)
            global tonal_intro
            tonal_intro = Label(root, text=word_data["tonal"], font=('Comic Sans MS', 20, "bold"), bg="red")
            tonal_intro.place(x=80, y=200)

            def back_page_2():
                for widget in root.winfo_children():
                    if widget != t:
                        widget.destroy()
                    page_2()
            
            back_button = Button(root, text="<< Back", font=('Times', 30), bg="red")
            back_button.place(x=20, y=20)
            back_button['command'] = back_page_2

            def play_tone1():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Tone\\Á.mp3")
                pygame.mixer.music.play()
            def play_tone2():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Tone\\À.mp3")
                pygame.mixer.music.play()
            def play_tone3():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Tone\\Ả.mp3")
                pygame.mixer.music.play()
            def play_tone4():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Tone\\Ã.mp3")
                pygame.mixer.music.play()
            def play_tone5():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Tone\\Ạ.mp3")
                pygame.mixer.music.play()

            tone1 = Button(root, text="Á", font=('Times', 36), bg="red", command=play_tone1)
            tone1.place(x=100, y=450)
            tonesym1 = Label(root, text="Accute Accent", font=('Arial', 20, "bold"), bg="red")
            tonesym1.place(x=50, y=400)
            expltone1 = Label(root, text="high rising, ˧˥", font=('Arial', 20), bg="red")
            expltone1.place(x=60, y=560)
            
            tone2 = Button(root, text="À", font=('Times', 36), bg="red", command=play_tone2)
            tone2.place(x=350, y=450)
            tonesym2 = Label(root, text="Grave Accent", font=('Arial', 20, "bold"), bg="red")
            tonesym2.place(x=300, y=400)
            expltone2 = Label(root, text="low falling, ˨˩", font=('Arial', 20), bg="red")
            expltone2.place(x=310, y=560)

            tone3 = Button(root, text="Ả", font=('Times', 36), bg="red", command=play_tone3)
            tone3.place(x=600, y=450)
            tonesym3 = Label(root, text="Hook Above", font=('Arial', 20, "bold"), bg="red")
            tonesym3.place(x=550, y=400)
            expltone3 = Label(root, text="mid falling, ˧˩", font=('Arial', 20), bg="red")
            expltone3.place(x=560, y=560)

            tone4 = Button(root, text="Ã", font=('Times', 36), bg="red", command=play_tone4)
            tone4.place(x=830, y=450)
            tonesym4 = Label(root, text="Tilde", font=('Arial', 20, "bold"), bg="red")
            tonesym4.place(x=830, y=400)
            expltone4 = Label(root, text="glottalized rising, ˧˥ˀ", font=('Arial', 20), bg="red")
            expltone4.place(x=760, y=560)

            tone5 = Button(root, text="Ạ", font=('Times', 36), bg="red", command=play_tone5)
            tone5.place(x=1100, y=450)
            tonesym5 = Label(root, text="Dot Below", font=('Arial', 20, "bold"), bg="red")
            tonesym5.place(x=1060, y=400)
            expltone5 = Label(root, text="glottalized falling, ˧˨ˀ", font=('Arial', 20), bg="red")
            expltone5.place(x=1040, y=560)

            def ending_3():
                for widget in root.winfo_children():
                    if widget != t:
                        widget.destroy()

            def to_vocab_page():
                ending_3()
                to_vocab()
                back_button.destroy()

            vocab_to = Button(root, text="Next >>", font=('Times', 30), bg="red", command=to_vocab_page)
            vocab_to.place(x=1190, y=620)

      global to_vocab
      def to_vocab():
            global vocab_intro
            vocab_intro = Label(root, text=word_data["vocab"], font=('Comic SANS MS', 20, "bold"), bg="red")
            vocab_intro.place(x=350, y=140)

            def back_word_tech():
                for widget in root.winfo_children():
                    if widget != t:
                        widget.destroy()
                    word_tech()
            
            back_button = Button(root, text="<< Back", font=('Times', 30), bg="red", command=back_word_tech)
            back_button.place(x=20, y=20)

            def play_word1():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Chair.mp3")
                pygame.mixer.music.play()

            def play_word2():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Price.mp3")
                pygame.mixer.music.play()

            def play_word3():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Hard.mp3")
                pygame.mixer.music.play()

            def play_word4():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Corn.mp3")
                pygame.mixer.music.play()

            def play_word5():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Listen.mp3")
                pygame.mixer.music.play()

            def play_word6():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\House.mp3")
                pygame.mixer.music.play()

            def play_word7():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Street.mp3")
                pygame.mixer.music.play()

            def play_word8():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Gift.mp3")
                pygame.mixer.music.play()

            def play_word9():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Poem.mp3")
                pygame.mixer.music.play()

            def play_word10():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Tea.mp3")
                pygame.mixer.music.play()

            def play_word11():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\Bird.mp3")
                pygame.mixer.music.play()

            gh = Label(root, text="gh -", font=('Times', 30), bg="red")
            gh.place(x=20, y=260)
            wordgh = Button(root, text="Ghế", font=('Times', 30), bg="red", command=play_word1)
            wordgh.place(x=100, y=250)
            explgh = Label(root, text=": Chair /ɣ/ (Note: gh only goes with e, ê and i)", font=('Times', 20), bg="red")
            explgh.place(x=200, y=270)

            gi = Label(root, text="gi -", font=('Times', 30), bg="red")
            gi.place(x=20, y=360)
            wordgi = Button(root, text="Giá", font=('Times', 30), bg="red", command=play_word2)
            wordgi.place(x=100, y=350)
            explgi = Label(root, text=": Price /ɣ/", font=('Times', 20), bg="red")
            explgi.place(x=200, y=370)
         
            kh = Label(root, text="kh -", font=('Times', 30), bg="red")
            kh.place(x=20, y=460)
            wordkh = Button(root, text="Khó", font=('Times', 30), bg="red", command=play_word3)
            wordkh.place(x=100, y=450)
            explkh = Label(root, text=": Hard /kh/", font=('Times', 20), bg="red")
            explkh.place(x=230, y=470)

            ng = Label(root, text="ng -", font=('Times', 30), bg="red")
            ng.place(x=20, y=560)
            wordng = Button(root, text="Ngô", font=('Times', 30), bg="red", command=play_word4)
            wordng.place(x=100, y=550)
            explng = Label(root, text=": Corn /ŋ/", font=('Times', 20), bg="red")
            explng.place(x=230, y=570)

            ngh = Label(root, text="ngh -", font=('Times', 30), bg="red")
            ngh.place(x=20, y=660)
            wordngh = Button(root, text="Nghe", font=('Times', 30), bg="red", command=play_word5)
            wordngh.place(x=100, y=650)
            explngh = Label(root, text=": Listen /ŋ/ (Note: ngh only goes with i, e and ê)", font=('Times', 20), bg="red")
            explngh.place(x=230, y=670)

            nh = Label(root, text="nh -", font=('Times', 30), bg="red")
            nh.place(x=470, y=360)
            wordnh = Button(root, text="Nhà", font=('Times', 30), bg="red", command=play_word6)
            wordnh.place(x=540, y=350)
            explnh = Label(root, text=": House /ɲ/", font=('Times', 20), bg="red")
            explnh.place(x=650, y=370)

            ph = Label(root, text="ph -", font=('Times', 30), bg="red")
            ph.place(x=470, y=460)
            wordph = Button(root, text="Phố", font=('Times', 30), bg="red", command=play_word7)
            wordph.place(x=540, y=450)
            explph = Label(root, text=": Street /f/", font=('Times', 20), bg="red")
            explph.place(x=650, y=470)

            qu = Label(root, text="qu -", font=('Times', 30), bg="red")
            qu.place(x=470, y=560)
            wordqu = Button(root, text="Quà", font=('Times', 30), bg="red", command=play_word8)
            wordqu.place(x=540, y=550)
            explqu = Label(root, text=": Gift /kw/", font=('Times', 20), bg="red")
            explqu.place(x=670, y=570)

            th = Label(root, text="th -", font=('Times', 30), bg="red")
            th.place(x=890, y=360)
            wordth = Button(root, text="Thơ", font=('Times', 30), bg="red", command=play_word9)
            wordth.place(x=960, y=350)
            explth = Label(root, text=": Poem /th/", font=('Times', 20), bg="red")
            explth.place(x=1070, y=370)

            tr = Label(root, text="tr -", font=('Times', 30), bg="red")
            tr.place(x=890, y=560)
            wordtr = Button(root, text="Trà", font=('Times', 30), bg="red", command=play_word10)
            wordtr.place(x=960, y=550)
            expltr = Label(root, text=": Tea /ʈɽ/", font=('Times', 20), bg="red")
            expltr.place(x=1070, y=570)

            ch = Label(root, text="ch -", font=('Times', 30), bg="red")
            ch.place(x=890, y=460)
            wordch = Button(root, text="Chim", font=('Times', 30), bg="red", command=play_word11)
            wordch.place(x=960, y=450)
            explch = Label(root, text=": Bird /c/", font=('Times', 20), bg="red")
            explch.place(x=1070, y=470)

            def ending4():
                for widget in root.winfo_children():
                    if widget != t:
                        widget.destroy()

            def to_final_found():
                ending4()
                final_found()
                back_button.destroy()

            to_final = Button(root, text="Next >>", font=('Times', 30), bg="red", command=to_final_found)
            to_final.place(x=1190, y=620)

      global final_found
      def final_found():
            dandd_intro = Label(root, text="Vietnamese Diphthongs & Triphthongs", font=('Comic SANS MS', 30, "bold", "underline"), bg="red")
            dandd_intro.place(x=340, y=140)

            def back_to_vocab():
                dandd_intro.destroy()
                for widget in root.winfo_children():
                    if widget != t:
                       widget.destroy()
                to_vocab()
            
            back_button = Button(root, text="<< Back", font=('Times', 30), bg="red", command=back_to_vocab)
            back_button.place(x=20, y=20)        

            def play_dip1():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ai.mp3")
                pygame.mixer.music.play()

            def play_dip2():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ay.mp3")
                pygame.mixer.music.play()

            def play_dip3():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ây.mp3")
                pygame.mixer.music.play()

            def play_dip4():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ao.mp3")
                pygame.mixer.music.play()

            def play_dip5():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\au.mp3")
                pygame.mixer.music.play()

            def play_dip6():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\âu.mp3")
                pygame.mixer.music.play()

            def play_dip7():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\eo.mp3")
                pygame.mixer.music.play()

            def play_dip8():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ia.mp3")
                pygame.mixer.music.play()

            def play_dip9():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\iê.mp3")
                pygame.mixer.music.play()

            def play_dip10():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\iêu.mp3")
                pygame.mixer.music.play()

            def play_dip11():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\iu.mp3")
                pygame.mixer.music.play()

            def play_dip12():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\oa.mp3")
                pygame.mixer.music.play()

            def play_dip13():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\oai.mp3")
                pygame.mixer.music.play()

            def play_dip14():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\oă.mp3")
                pygame.mixer.music.play()

            def play_dip15():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\oe.mp3")
                pygame.mixer.music.play()

            def play_dip16():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\oi.mp3")
                pygame.mixer.music.play()

            def play_dip17():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ôi.mp3")
                pygame.mixer.music.play()

            def play_dip18():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ơi.mp3")
                pygame.mixer.music.play()

            def play_dip19():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ua.mp3")
                pygame.mixer.music.play()

            def play_dip20():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ưa.mp3")
                pygame.mixer.music.play()

            def play_dip21():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\uô.mp3")
                pygame.mixer.music.play()

            def play_dip22():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ươ.mp3")
                pygame.mixer.music.play()

            def play_dip23():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ui.mp3")
                pygame.mixer.music.play()

            def play_dip24():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\uôi.mp3")
                pygame.mixer.music.play()

            def play_dip25():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\uâ.mp3")
                pygame.mixer.music.play()

            def play_dip26():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\uê.mp3")
                pygame.mixer.music.play()

            def play_dip27():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\uy.mp3")
                pygame.mixer.music.play()

            def play_dip28():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\uyê.mp3")
                pygame.mixer.music.play()

            def play_dip29():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ưi.mp3")
                pygame.mixer.music.play()

            def play_dip30():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ươi.mp3")
                pygame.mixer.music.play()

            def play_dip31():
                pygame.mixer.init()
                pygame.mixer.music.load("./\\Sound\\Word\\ưu.mp3")
                pygame.mixer.music.play()

            dandd_list = [
            ("ai", "[aĭ]", play_dip1),
            ("ay", "[ɛi]", play_dip2),
            ("ây", "[ei]", play_dip3),
            ("ao", "[ɑu̯]", play_dip4),
            ("au", "[au̯]", play_dip5),
            ("âu", "[əu̯]", play_dip6),
            ("eo", "[ɛu̯]", play_dip7),
            ("ia", "[iə]", play_dip8),
            ("iê", "[iə]", play_dip9),
            ("iêu", "[iəu̯]", play_dip10),
            ("iu", "[iu̯]", play_dip11),
            ("oa", "[wɑ]", play_dip12),
            ("oai", "[wɑĭ]", play_dip13),
            ("oă", "[wa]", play_dip14),
            ("oe", "[wɛ]", play_dip15),
            ("oi", "[ɔi]", play_dip16),
            ("ôi", "[oi]", play_dip17),
            ("ơi", "[ɤĭ]", play_dip18),
            ("ua", "[uə]", play_dip19),
            ("ưa", "[ɯə]", play_dip20),
            ("uô", "[uə]", play_dip21),
            ("ươ", "[ɯə]", play_dip22),
            ("ui", "[uĭ]", play_dip23),
            ("uôi", "[uəĭ]", play_dip24),
            ("uâ", "[wə]", play_dip25),
            ("uê", "[we]", play_dip26),
            ("uy", "[wi]", play_dip27),
            ("uyê", "[wiə]", play_dip28),
            ("ưi", "[ɯĭ]", play_dip29), 
            ("ươi", "[ɯəi]", play_dip30),
            ("ưu", "[ɯu̯]", play_dip31)
            ]

            column_1_x = 250
            column_2_x = 550
            column_3_x = 800
            column_4_x = 1050
            start_y = 250
            y_increment = 60

            for i, (dandd, pronunciation, sound_command) in enumerate(dandd_list):
                if i < 8:
                    label_x = column_1_x
                elif i < 16:
                    label_x = column_2_x
                elif i < 24:
                    label_x = column_3_x
                else:
                    label_x = column_4_x
    
                dandd_label = Button(root, text=dandd, font=('Times', 24), bg="red", command=sound_command)
                dandd_label.place(x=label_x, y=start_y + (i % 8) * y_increment)

                pronunciation_label = Label(root, text=pronunciation, font=('Arial', 20), bg="red")
                pronunciation_label.place(x=label_x + 60, y=start_y + (i % 8) * y_increment)
           
            def the_end():
                dandd_intro.destroy()
                for widget in root.winfo_children():
                    if widget != t:
                      widget.destroy()
                foundation_end()

            vocab_to = Button(root, text="Next >>", font=('Times', 30), bg="red", command=the_end)
            vocab_to.place(x=1190, y=620)
      
      global foundation_end
      def foundation_end():
         fouend_text = Label(root, text=word_data['fouend'], font=('Comic Sans MS', 25), bg="red")
         fouend_text.place(x=340, y=290)

         def agree_beg():
             for widget in root.winfo_children():
                 widget.destroy()
             selecteddiffez()
         
         def menu_sc():
             for widget in root.winfo_children():
                 widget.destroy()
             back_sel()
             
         def failure():
             for widget in root.winfo_children():
                 widget.destroy()
             sys.exit()

         agree_begin = Button(root, text="Đi nào!", font=('Comic Sans MS', 25), bg="red", command=agree_beg)
         agree_begin.place(x=430, y=450)

         main_menu = Button(root, text="Main Menu", font=('Comic Sans MS', 25), bg="red", command=menu_sc)
         main_menu.place(x=750, y=450)

         the_end = Button(root, text="The End", font=('Comic Sans MS', 25), bg="red", command=failure)
         the_end.place(x=600, y=560)
   
    foundation = Foundation()

    global next_page   
    next_page = Button(root, text="Next >>", font=('Times', 30), bg="red", command = alph_tech)
    next_page.place(x=1220, y=590)


def start_quiz_ez():
    global readybutt
    readybutt.destroy()
    global ready1
    ready1.destroy()
    global back
    back.destroy()
    class Quiz:
        def __init__(self, quiz_data):
            self.quiz_data = quiz_data
            self.qn = 0
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn):
            t = Label(root, text=label_data['titleez'], bg="red", font=('Arial', 50, "underline"))
            t.place(x=220, y=50)
            global qn_label
            qn_label = Label(root, text=q[qn], font=("Arial", 30), bg="red")
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
            if qn == 10 or qn == 11:  # Questions 11 and 15
                self.play_button = Button(root, text="🔊", font=('Arial', 30), bg="red", command=self.play_sound)
                self.play_button.place(x=800, y=180)
            else:
                self.play_button = None

        def play_sound(self):
            if self.qn in [10, 11]:  # Questions 11 and 15 (indexes 10 and 14)
                sound_index = [10, 11].index(self.qn)  # Index of the sound file corresponding to the question
                sound_file = self.quiz_data['sound_files'][sound_index]
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

        def check_selected(self, selected):
           self.selected_option = selected

        def buttons(self):
            global checkbutt
            checkbutt = Button(root, text="Next",command=self.ans_check, bg="green",fg="white",font=("Arial", 20))
            checkbutt.place(x=200,y=590)
            quitbutton = Button(root, text="Quit", command=root.destroy, bg="red",fg="white", font=("Arial", 20))
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
           nbutton = Button(root, text="Next",command=self.nextbtn, bg="green",fg="white",font=("Arial", 20))
           nbutton.place(x=200,y=590)
           self.tick_correct_answer(self.qn)
        
        def nextbtn(self):
           global checkbutt
           checkbutt = Button(root, text="Next",command=self.ans_check, bg="green",fg="white",font=("Arial", 20))
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
  
    quiz = Quiz(label_data)

entry1 = Entry(root, font=('Arial', 30))
entry1.place(x=500, y=250)
button1 = Button(root, text='SUBMIT', font=('Arial', 30), command=comm1)
button1.place(x=600, y=350)

root.mainloop()