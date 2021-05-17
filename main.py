from tkinter import *
import random
from PIL import ImageTK, Image

global questions_answers
names_list = []
asked =[]
score =0
questions_answers = {

}

def randomiser():
global qnum
qnum = random.randint(1,10)
if qnum not in asked:
asked.append(qnum)
elif qnum not in asked:
randomiser()


class Quizstarter:
def __init__ (self, parent):
background_color="#AC77E9"
#frame set up
self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
self.quiz_frame.grid()
background_color="OldLace"# to set it as as background for all the widgets

self.bg_images= Images .open("smoke.jfif")#need to use image if need to resize
self.bg_image = self.bg_images.resize( 450, 350, Image.ANTIALIAS)
self.bg_image = ImageTk.PhotoImage(self.bg_image)

#widgets go below
self.heading_label = Label(self.quiz_frame, text="Welcome to Mythology
Quiz", bg="#9982E6")
self.heading_label.grid(row=0, padx=20)

#label for image
self.image_label= Label(self.quiz_frame, images=self.bg_image)
#self.image_label.grid(row=09, colum=1,) #on the right side
self.image_label.place(x=0, y=0, relwidth=1, relheight=1) #make label
1 to fit the parent window always


# label to ask for Name
self.user_label = Label(self.quiz_frame, text="Enter your name
below:", bg="#9982E6")
self.user_label.grid(row=1, padx=20, pady=10)

#entry box
self.entry_box = Entry(self.quiz_frame)
self.entry_box.grid(row=2, padx=20, pady=10)

#create a Button
self.continue_button = Button(self.quiz_frame, text="Continue",
font=("mishka family", "13", "normal"), bg="#878CE3",
command=self.name_collection)
self.continue_button.grid(row=3, padx=20, pady=20)



def name_collection(self):
name=self.entry_box.get()
names_list.append(name)
print(names_list) #testing
self.quiz_frame.destroy()
Quiz(root) #we destroy starter quiz_frame and open the questions
quiz_frame isntead which will be part of the Quiz object

class Quiz:
def __init__ (self, parent):
background_color="#c299ff"
#frame set up
self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
self.quiz_frame.grid()

#randomiser will randomly pick a question number which is qnum
randomiser()
#label widget for our heading
self.question_label = Label(self.quiz_frame, text =
questions_answers[qnum][0], font=("Garamond", "14") , bg="#ccf5ff")
self.question_label.grid(row=0)

#holds the value of the radio buttons
self.varl=IntVar()

#radio button 1
self.rb1 = RadioButton (self.quiz_frame, text =
questions_answers[qnum][1], font=("Helvetica", "12"),
bg=background_color, value=1, variable=self.varl1, padx=10,pady=10)
self.rb1.grid(row=1, sticky=W)

#radio button 2
self.rb2 = RadioButton (self.quiz_frame, text =
questions_answers[qnum][2], font=("Helvetica", "12"),
bg=background_color, value=2, variable=self.varl1, padx=10, pady=10)
self.rb2.grid(row=2, sticky=W)

#radio button 3
self.rb3 = RadioButton (self.quiz_frame, text =
questions_answers[qnum][3], font=("Helvetica", "12"),
bg=background_color, value=3, variable=self.varl1, padx=10,pady=10)
self.rb3.grid(row=3, sticky=W)

#radio button 4
self.rb4 = RadioButton (self.quiz_frame, text =
questions_answers[qnum][4], font=("Helvetica", "12"),
bg=background_color, value=4, variable=self.varl1, padx=10, pady=10)
self.rb4.grid(row=4, sticky=W)

#confirm answer button
self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="white")
slef.confirm_button.grid(row=5)

#Entry
if __name__=="__main__":
root = Tk() #creating a window
root.title("Mythyology")
quiz_object= Quizstarter(root)
root.mainloop()
#keep looping so window stays on
