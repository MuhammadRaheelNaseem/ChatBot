from tkinter import *
import datetime
x=datetime.datetime.now()
chat = {
    'How are you?':'I\'m Good.',
    'How are you doing':'I\'m doing good.',
    'Good morning':"Good Morning",
    'Good evening':'Good Evening',
    'Good afternoon':'Good Afternoon',
    'Good night':'Good Night',
    'Tell me something':'I dont have any thing about to tell you somthing!',
    'what can you do?':'I can do anything what you want',
    'Happy birthday!':'Today is not my birthday',
    'I have a question':'Yes! you ask me',
    'can you help me?':'Yes! I can help you',
    'Are you human? / Are you a robot?':'I\'m Robt',
    'What is your name?':'My name is Bot',
    'How old are you? / What’s your age?':'Sorry! I can\'t tell you',
    'What day is it today?':f"Today is {x.strftime('%A')}",
    'Who made you?':'Raheel made me using python language',
    'Which languages can you speak?':'English',
    "Do you have a job for me? / Where can I apply?":'Yes! I have a job for you must be apply on Nasa',
    'Do you get smarter?':'Yes! I\'m more smarter then you',
    'what is your name?':'my name is chatbot',
    'whats your name?':'my name is chatbot',
    'In which navttc provided course do you study?':'I study in course internet of things',
    'what is the duration of this course':'6 months?',
    'how many months are left to complete this course?':'almost 3 months',
    'what will do you do after completing this course?':'I will do my own business on freelancing',
    'how do you see yourself after 5 years?':'Enterprenuer'
}
bot=Tk()
bot.geometry('1000x670+50+20')
bot.minsize(1000,670)
bot.maxsize(1000,670)
bot.configure(bg='#73B6FE')
bot.title('ChatBot')

#_______Open image______
photo_1=PhotoImage(file='user.png')
user=Label(image=photo_1,
          bg='#73B6FE')
user.place(x=170,
          y=0)
#__________heading_______
heading=Label(bot,
             text='Chat With Bot',
             font='Times 48 bold italic',
             bg='#73B6FE')
heading.place(x=310,
             y=6)
#_________open 2nd image________
photo_2=PhotoImage(file='bot5.png')
Bot=Label(image=photo_2,
         bg='#73B6FE')
Bot.place(x=720,
         y=-25)

#______set stringvar___
variable = StringVar()
variable.set('Select Qustion for Bot')

#______define function_____
def replace():
    box1.insert(0.0,variable.get(),'center')
def clear():
    box1.delete('1.0',END)
    box2.configure(text='')
def answer():
    print(chat[variable.get()])
    box2.configure(text=chat[variable.get()])
#________frame_______
bot_frame=Frame(bot,
               bg='#73B6FE')
bot_frame.place(x=0,
               y=100,
               width=1000,
               height=569)
#_______image______
photo=PhotoImage(file='user.png')
img=Label(bot_frame,
          image=photo,
          bg='#73B6FE')
img.place(x=40,
         y=80)
#________text box_____
box1=Text(bot_frame,
         font='vardana 22')
box1.place(x=160,
         y=90,
          width=400,
          height=85)

#________option menu for qustion_______
options=OptionMenu(bot_frame,
                    variable,
                   *chat)
options.configure(font='Times')
options.place(x=590,
             y=99,
             width=300,
             height=70)
#________replace Button_____
replacebtn = Button(bot_frame,
                   text='Replace',
                   command=replace,
                   font='Times 20')
replacebtn.place(x=590,
                y=180,
                width=150,
                height=70)
#__________clear Button__________
clearbtn=Button(bot_frame,
               text='Clear',
               command=clear,
               font='Times 20')
clearbtn.place(x=740,
              y=180,
              width=150,
              height=70)
#____________image______________
photo_3=PhotoImage(file='chatbot.png')
image_label=Label(bot_frame,
                 image=photo_3,
                 bg='#73B6FE')
image_label.place(x=180,
                   y=240)
#____________image for bot______
photo2=PhotoImage(file='bot5.png')
img2=Label(bot_frame,
           image=photo2,
          bg='#73B6FE')
img2.place(x=15,
          y=365)
#________text box_____
box2=Label(bot_frame,
          font='vardana 22 italic')
box2.place(x=160,
          y=390,
          width=800,
          height=85)
#_________Answer Button________
answerbtn=Button(bot_frame,
                text="Answer",
                font='Times 25',
                command=answer)
answerbtn.place(x=350,
               y=488,
               width=300,
               height=79)


bot.mainloop()
