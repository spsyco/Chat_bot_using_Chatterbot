from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import tkinter
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()

voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")
#  creating some convo's
convo = [
    'hello',
    'hi there',
    'what is your name',
    'My name is Friday1.0 , i am created by Karan',
    'how are you?',
    'I am doing great  ',
    'Thank you',
    'In which city you live',
    'I am from Serampore',
    'I am learning now but i can speak english very well!'

]
trainer = ListTrainer(bot)
# # now training the bot with the help of trainer
trainer.train(convo)

# answer = bot.get_response("What is your name?")
# print(answer)
# now creating a series of question and answer session
# print("Ask the Bot")
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer=bot.get_response(query)
#     print("bot: ",answer)
# now making the code graphical using tkinter

main = Tk()
main.geometry("500x650")  # setting the hight and width of the window
main.title("Jarvis")  # title of the window

#takes query : It takes audio as input adn gives it to the bot
def takequery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("I am listening boss! please speak")

    with s.Microphone() as m:
        try:

            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("101 Error boss")



def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)

    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = tkinter.Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


# binding main window with enter key
main.bind('<Return>',enter_function)
def repeatl():
    while True:
        takequery()

t=threading.Thread(target=repeatl)
t.start()


main.mainloop()
