from tkinter import *
import random
from PIL import ImageTk, Image
global questions_answers


names_list = []
global questions_answers
__placeholder__ = False
asked =[]
names=[]
score =0
questions_answers = { 
  1: ["What is an effect of climate change?", 
  'A. yes', 
  'B. Increased Heat', 
  'C. change in climate patterns',
  'D. World domination',
  'Increasing tempertures', 
    2],
  2: ["What do you think is creating climate change?", 
  'A. My interent use',
  'B. Over-production of greenhouse gases',
  'C. Melting Ice bergs',
  'D. Cooking onions',
  'Over-production of greenhouse gases',
    2],
  3:["What is the ozone layer?", 
  'A. a blanket for the world', 
  'B. NOPE',
  'C. The layer that protects the world', 
  'D. melted ice bergs',
  'A layer that protects the world', 
    3],
  4:["Why should we care about climate change?",
  'A. its not important',
  'B. I told you to',
  'C. For the future of humanity',
  'D. Just cause',
  'For the future of humanity',
    3],
  5:["What is the type of gas that is causing climate change?",
   'A. Greenhouse gases',
   'B. Carbon dioxide',
   'C. solar electricity',
   'D. petrol',
   'Greenhouses gases',
    1],
  6:["Who/What is responsible for the over production of green house gases?",
  'A. cars',
  'B. gas stations',
  'C.Factories, power plants..etc',
  'D. oceans waste',
  'Factories, power plants..etc',
    3],
  7:["What is climate change directly affecting?",
  'A. Water levels',
  'B. gas stations',
  'C.Donald. J. Trump',
  'D. You',
  'Water levels',
    1],
  8:["Is the ozone hole causing climate change? ",
  'A. No',
  'B. Maybe',
  'C. very unlikey',
  'D. yes',
  'Yes',
    4],
  9:["Is climate change caused by humans?",
  'A. Maybe',
  'B. No',
  'C.Yes',
  'D. Possibly',
  'Yes, we are the reason to our own destruction',
    3],
  10:["Does deforestation contribute to climate change?",
  'A. No, they are seperate',
  'B. Maybe, they are linked',
  'C.Yes deforestation contributes in multiple ways',
  'D. Possibly they are linked , but there is no evidence',
  'Yes, They are linked in a way, that you can find out.',
    3],
}

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
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
    #Entry

  
  def name_collection(self):
    name=self.entry_box.get()
    global names_list
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
    self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="#f1b9b9",command=self.test_progress)
    self.confirm_button.grid(row=10)
    
    #score label to show score (test result so far)
    self.score_label=Label(self .quiz_frame, text="SCORE", font=("Helvetica""14"),bg=background_color,)
    self.score_label.grid(row=12,pady=1)

  
  
  #Editing the question label and radio buttons to show the next questions data
  def questions_setup(self):
    randomiser()
    self.varl1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])
  

#confirm button for the questions window to be better
  def test_progress(self):#pass the users choice
    global score#this score us there to be accessed to everyone
    scr_label = self.score_label#shhowing the score because it will be different each time a question is answered
    choice = self.varl1.get()#get the users choice

    if len(asked)>9:#to determine it's the last question to end the quiz after
      if choice == questions_answers[qnum][6]:#cheking the qnum has the correct answer that is stored in index 6
        score+=1#adding a point after each correct answer
        scr_label.configure(text=score)#it will change the score to the new score each time
        self.confirm_button.config(text="confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed
      else:
        print(choice)
        score+=0#score will stay the same if the questions is answered inccorectly
        scr_label.configure(text="Incorrect the answer was: " + questions_answers[qnum][5])#sayin the incorrect answer the the question that the end user put wrong
        self.confirm_button.config(text="Confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed
    else:
        if choice == 0:#if the user doesn't select and option
          self.confirm_button.config(text="Pick an option")#then the confirm button will say please try again until the questions is answered and an option is selected
          choice=self.varl1.get()#still get the answer if they chose it
        else:#if choice is correct
          if choice == questions_answers[qnum][6]:#if the choice is correct
            score+=1
            scr_label.configure(text=score)
            self.confirm_button.config(text="Confirm")
            self.questions_setup()#to move on to the next question

          else:#if the choice was incorrect
            print(choice)
            score+=0
            scr_label.configure(text="Incorrect! The answer was: " + questions_answers[qnum][5])#telling the correct answer
            self.confirm_button.config(text="Confirm")
            self.questions_setup()#moving to the next question


  def endScreen(self, *args):
    root.withdraw()
    name = names_list[0]
    file = open("leaderBoard.txt", "a")#opens highscores, text file in append mode
    if name == "admin_reset":#to wipe scores in the list, admin enters with the name
      file = open("leaderBoard.txt", "w")
    else:
      file.write(str(score))#turns the success rate into a string
      file.write(" - ")#writes into the text file
      file.write(name+"\n")#writes the names into the text files and goes to a new line (\n)
      file.close()#closes the file

      inputFile = open("leaderBoard.txt", 'r')#opens the high score files in read mode
      lineList = inputFile.readlines()#linelist equals the each lines in the lists
      lineList.sort()#sorts the line alphabetically
      top=[]#display top scores
      top5=(lineList[-5:])#the last 10 values in the list for top 10
      for line in top5:
        point=line.split(" - ")
        top.append((int(point[0]), point[1]))
        file.close()#closes the files
        top.sort()
        top.reverse()
        return_string = "Your final score is: "
        for i in range (len(top)): return_string += "{} - {}\n".format(top[i][0], top[i][1])
        print(return_string)#for testing to show on the console
      open_endscreen = End(root)
      open_endscreen.listLabel.config(text=return_string)#this will config the label in the end screen class which is displaying the names of the top 5
 
class End:
  def __init__(self, parent): # this function is called every time the class is being used to create a new object
    background ="#a4c2f4"
    self.end_box = Toplevel(root)
    self.end_box.title("Congratulations, You have completed the quiz")
    self.end_frame = Frame(self.end_box, pady=70, padx=45, bg=background)
    self.end_frame.grid()
  #end heading
    end_heading = Label (self.end_frame, text='I hope you have learnt something,Thanks. Sayonara :)', font=("Helvetica", "14"),bg='#f1b9b9', pady=15)
    end_heading.grid(row=0)
    #exit button to end the quiz
    exit_button = Button (self.end_frame, text='Exit quiz>>', width=10,font=("Helvetica", "14"),bg='#f1b9b9', command=self.close_end, pady=10, padx=10)
    exit_button.grid(row=4, pady=20, padx=5, sticky=E)

  #if 1st place is available/ what they got
    self.listLabel = Label(self.end_frame, text="You are in 1st place",font=("Helvetica", "14"), width=40, bg=background, padx=10,pady=10)
    self.listLabel.grid(row=2)
  
  def close_end(self):
    exit()


if __name__=="__main__":
  root = Tk() #creating a window
  root.title("Building Climate Awareness")
  Quizstarter_object=Quizstarter(root)
  root.mainloop()
  #keep looping so window stays on
 
  
  

