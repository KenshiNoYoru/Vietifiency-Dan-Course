from tkinter import *
from tkinter import messagebox as mb
from customtkinter import *
import json
from xml.etree.ElementTree import QName
import pygame

root = Tk()
root.title('Vietifiency Dan Course')
root['bg'] = 'red'
root.geometry("1386x720")
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
    readybutt = Button(root, text=label_data['easybut'], font=('Comic Sans MS', 25), bg="red", command=start_quiz)
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
    readybutt = Button(root, text=label_data['easybut'], font=('Comic Sans MS', 25), bg="red", command=start_quiz)
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
    readybutt = Button(root, text=label_data['hdbut'], font=('Comic Sans MS', 25), bg="red", command=start_quiz)
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
         pygame.mixer.music.load("./\\Sound\\A.mp3")
         pygame.mixer.music.play()  
      def play_sound2():
         pygame.mixer.init()
         pygame.mixer.music.load("./\\Sound\\Ă.mp3")
         pygame.mixer.music.play() 
      def play_sound3():
         pygame.mixer.init()
         pygame.mixer.music.load("./\\Sound\\Â.mp3")
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
      def alph_tec():
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
         abcdown = Label(root, text=word_data['theAlphabet'], font=('Comic Sans MS', 25), bg="red")
         abcdown.place(x=300, y=150)
         nonvowel = Label(root, text="Non-vowel Character:", font=('Comic Sans MS', 25, "bold", "underline"), bg="red")
         nonvowel.place(x=20, y=250)
         font_size = 25
         def play_sound4():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\B.mp3")
            pygame.mixer.music.play()  
         def play_sound5():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\C.mp3")
            pygame.mixer.music.play() 
         def play_sound6():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\D.mp3")
            pygame.mixer.music.play()
         def play_sound7():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Đ.mp3")
            pygame.mixer.music.play()  
         def play_sound8():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\E.mp3")
            pygame.mixer.music.play() 
         def play_sound9():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Ê.mp3")
            pygame.mixer.music.play()  
         def play_sound10():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\G.mp3")
            pygame.mixer.music.play()  
         def play_sound11():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\H.mp3")
            pygame.mixer.music.play() 
         def play_sound12():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\I.mp3")
            pygame.mixer.music.play()  
         def play_sound13():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\K.mp3")
            pygame.mixer.music.play()  
         def play_sound14():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\L.mp3")
            pygame.mixer.music.play() 
         def play_sound15():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\M.mp3")
            pygame.mixer.music.play()  
         def play_sound16():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\N.mp3")
            pygame.mixer.music.play()  
         def play_sound17():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\O.mp3")
            pygame.mixer.music.play() 
         def play_sound18():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Ô.mp3")
            pygame.mixer.music.play()
         def play_sound19():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Ơ.mp3")
            pygame.mixer.music.play()
         def play_sound20():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\P.mp3")
            pygame.mixer.music.play()
         def play_sound21():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Q.mp3")
            pygame.mixer.music.play()
         def play_sound22():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\R.mp3")
            pygame.mixer.music.play() 
         def play_sound23():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\S.mp3")
            pygame.mixer.music.play()
         def play_sound24():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\T.mp3")
            pygame.mixer.music.play() 
         def play_sound25():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\U.mp3")
            pygame.mixer.music.play()
         def play_sound26():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Ư.mp3")
            pygame.mixer.music.play() 
         def play_sound27():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\V.mp3")
            pygame.mixer.music.play()
         def play_sound28():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\X.mp3")
            pygame.mixer.music.play() 
         def play_sound29():
            pygame.mixer.init()
            pygame.mixer.music.load("./\\Sound\\Y.mp3")
            pygame.mixer.music.play()
         letter1 = Button(root, text="A", font=('Times', font_size), bg="red", command=play_sound1)
         letter1.place(x=30, y=300)
         expl1 = Label(root, text="/α:/‘a’ as in father", font=('Arial', 20), bg="red")
         expl1.place(x=100, y=310)
         letter2 = Button(root, text="Ă", font=('Times', font_size), bg="red", command=play_sound2)
         letter3 = Button(root, text="Â", font=('Times', font_size), bg="red", command=play_sound3)
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
         letter7 = Button(root, text="Đ", font=('Times', font_size), bg="red", command=play_sound7)
         letter8 = Button(root, text="E", font=('Times', font_size), bg="red", command=play_sound8)
         letter8.place(x=30, y=380)
         expl5 = Label(root, text="/ε/ ‘e’ as in get", font=('Arial', 20), bg="red")
         expl5.place(x=100, y=390)
         letter9 = Button(root, text="Ê", font=('Times', font_size), bg="red", command=play_sound9)
         letter10 = Button(root, text="G", font=('Times', font_size), bg="red", command=play_sound10)
         letter10.place(x=320, y=380)
         expl6 = Label(root, text="/ɣ/ ‘g’ as in good", font=('Arial', 20), bg="red")
         expl6.place(x=390, y=390)
         letter11 = Button(root, text="H", font=('Times', font_size), bg="red", command=play_sound11)
         letter11.place(x=620, y=380)
         expl7 = Label(root, text="/ɣ/ ‘g’ as in good", font=('Arial', 20), bg="red")
         expl7.place(x=690, y=390)
         
         letter12 = Button(root, text="I", font=('Times', font_size), bg="red", command=play_sound12)
         letter13 = Button(root, text="K", font=('Times', font_size), bg="red", command=play_sound13)
         letter14 = Button(root, text="L", font=('Times', font_size), bg="red", command=play_sound14)
         letter15 = Button(root, text="M", font=('Times', font_size), bg="red", command=play_sound15)
         letter16 = Button(root, text="N", font=('Times', font_size), bg="red", command=play_sound16)
         letter17 = Button(root, text="O", font=('Times', font_size), bg="red", command=play_sound17)
         letter18 = Button(root, text="Ô", font=('Times', font_size), bg="red", command=play_sound18)
         letter19 = Button(root, text="P", font=('Times', font_size), bg="red", command=play_sound20)
         letter20 = Button(root, text="Q", font=('Times', font_size), bg="red", command=play_sound21)
         letter21 = Button(root, text="R", font=('Times', font_size), bg="red", command=play_sound22)
         letter22 = Button(root, text="S", font=('Times', font_size), bg="red", command=play_sound23)
         letter23 = Button(root, text="T", font=('Times', font_size), bg="red", command=play_sound24)
         letter24 = Button(root, text="U", font=('Times', font_size), bg="red", command=play_sound25)
         letter25 = Button(root, text="Ư", font=('Times', font_size), bg="red", command=play_sound26)
         letter26 = Button(root, text="V", font=('Times', font_size), bg="red", command=play_sound27)
         letter27 = Button(root, text="S", font=('Times', font_size), bg="red", command=play_sound28)
         letter28 = Button(root, text="Y", font=('Times', font_size), bg="red", command=play_sound29)
         letter29 = Button(root, text="Ơ", font=('Times', font_size), bg="red", command=play_sound19)


      global next_page   
      next_page = Button(root, text="Next >>", font=('Times', 30), bg="red", command=alph_tec)
      next_page.place(x=1220, y=590)

    foundation = Foundation()


def start_quiz():
    global readybutt
    readybutt.destroy()
    global ready1
    ready1.destroy()
    global back
    back.destroy()
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
  
    quiz = Quiz()

entry1 = Entry(root, font=('Arial', 30))
entry1.place(x=500, y=250)
button1 = Button(root, text='SUBMIT', font=('Arial', 30), command=comm1)
button1.place(x=600, y=350)

root.mainloop()