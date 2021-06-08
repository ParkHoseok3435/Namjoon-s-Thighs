from tkinter import *
import random
from PIL import ImageTk, Image


names_list = []
asked =[]
score =0
questions_answers = { 
  1: ["What is an effect of climate change?", 
  'A. yes', 'B. Increased Heat', 'C. change in climate patterns','D. World domination',
   2],
  2: ["What do you think is creating climate change?", 
  'A. My interent use', 'B. Over-production of greenhouse gases','C. Melting Ice bergs','D. Cooking onions',
   2],
  3:["What is the ozone layer?", 
  'A. a blanket for the world', 'B. NOPE','C. The layer that protects the world', 'D. melted ice bergs',
   1],
  4:["How do you think we can prevent this from continuing?",
  'A. Staying home','B. Not using a private vehicle','C. making popcorn', 'D. cooking rice',
   1],
}

def randomiser():
  global qnum
  qnum = random.randint(1,4)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum not in asked:
    randomiser()

class Quizstarter:
  def __init__ (self, parent):
    background_color="#a4c2f4"

    #frame set up
    self.quiz_frame = Frame( parent, bg = background_color,padx=125,pady=99)
    self.quiz_frame.grid()
    

    self.bg_images= Image.open("cookingearth.jpg")#need to use image if need to resize
    self.bg_image = self.bg_images.resize( (250,177), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    #label for image
    self.image_label= Label(self.quiz_frame, image=self.bg_image)
    #self.image_label.grid(row=09, colum=1,) #on the right side
    self.image_label.place(x=0, y=0, relwidth=1, relheight=1) #make label 1 to fit the parent window always
    #widgets go below
    self.heading_label = Label(self.quiz_frame, text="Building Climate Awareness",bg="#f1b9b9")
    self.heading_label.grid(row=0, padx=20)

    # label to ask for Name
    self.user_label = Label(self.quiz_frame, text="Enter your first name:", bg="#f1b9b9")
    self.user_label.grid(row=1, padx=20, pady=10)

    #entry box
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row=2, padx=20, pady=10)

    #create a Button
    self.continue_button = Button(self.quiz_frame, text="Continue", font=("Happy hell", "13", "normal"), bg="#f1b9b9", command=self.name_collection)
    self.continue_button.grid(row=7, padx=15, pady=15)
  
  def name_collection(self):
    name=self.entry_box.get()
    names_list.append(name)
    print(names_list) #testing
    self.quiz_frame.destroy()
    #we destroy starter quiz_frame and open the questions quiz_frame isntead which will be part of the Quiz object
    Quiz(root)

class Quiz:
  def __init__ (self, parent):
    background_color="#a4c2f4"
    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    #randomiser will randomly pick a question number which is qnum
    randomiser()
     #label widget for our heading
    self.question_label = Label(self.quiz_frame, text = questions_answers[qnum][0], font=("Helvetica", "12"), bg="#f1b9b9",padx=10,pady=10)
    self.question_label.grid(row=0)

    #holds the value of the radio buttons
    self.varl1=IntVar()

    #radio button 1
    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg='#f1b9b9', value=1, variable=self.varl1, padx=5,pady=5)
    self.rb1.grid(row=2)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg='#f1b9b9', value=2, variable=self.varl1, padx=5, pady=5)
    self.rb2.grid(row=4)
   
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg='#f1b9b9', value=3, variable=self.varl1, padx=5, pady=5)
    self.rb3.grid(row=6)

    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg='#f1b9b9', value=4, variable=self.varl1, padx=5, pady=5)
    self.rb4.grid(row=8)
    #confirm answer button
    self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="#f1b9b9")
    self.confirm_button.grid(row=10)
  #Editing the question label and radio buttons to show the next questions data
  def questions_setup(self):
    randomiser()

#Entry
if __name__=="__main__":
    root = Tk() #creating a window
    root.title("Building Climate Awareness")
    quiz_object=Quizstarter(root)
    root.mainloop()
    #keep looping so window stays on
