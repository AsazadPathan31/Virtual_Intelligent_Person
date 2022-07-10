# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 00:28:12 2021

@author: Code Pirates(Asazad Pathan, Akash Kamble, Vivek Parit, Nitin Kendre)

"""

"""
This is the first module of our project.
it uses various NLP technologies, for human interaction.
it used to process human voice and convert it to text format.
It is also used as chatbot.

"""


#import required libraries.
import datetime
import webbrowser
import os
#import smtplib
from playsound import playsound
import speech_recognition as sr
import pickle
# import torch

# library for pretrained models.
from transformers import pipeline, Conversation

#library for text to speech
from gtts import gTTS


#importing vivek's code
from multilingual_question_answering_system import EnglishQuestionAnswering as mqa

preRes = pipeline("conversational",model="D:/Code Pirates/huggingface models/DialoGPT-large")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


class Astra:
    
    """
    Astra class 
    main class for nlp skeleton.
    This class contains various functions
    needed by nlp.
    """

    def __init__(self,name="ava"):
        """
        class constructor.
        """
        self.name=name
   
    
    def listenAstra(self):
        
        """
        This functions helps model to listen.
        """
        
        recognizer = sr.Recognizer()
        
        #for loop for printing available microphone names
        #for i in sr.Microphone.list_microphone_names():
        #    print(i)
        
        with sr.Microphone(device_index=2) as inMic:
            print("Say something I am listening.... ")
            recognizer.pause_threshold = 1
            userIn = recognizer.listen(inMic)
            print("time over......")
            # return True
            
        try:
            userText = recognizer.recognize_google(userIn, language='en-in')
            print(f"You ::-> {userText}")
            
        except:
            print(f"{self.name} ::-> Can't Recognize anything, Please say again.")
            #continue
            #return False
            
            
            
    def speakAstra(self,text):
           
        """
        This function is used for speaking of model.
        """
        
        print(f"Astra ::-> {text}")
        astraRes = gTTS(text=text,lang="en",slow=False,tld="co.in")
        astraRes.save("temp/astraRes.mp3")
        playsound("temp/astraRes.mp3")
        os.remove("temp/astraRes.mp3")
        
    
    def wakingWish(self):
        """
        This function is for day greeting.
        """
    
        hrs = int(datetime.datetime.now().hour)
        #print(hrs)
        if hrs>=0 and hrs<12:
            self.speakAstra("Hello Sir, Good Morning!, How may I help you")
        
        elif hrs>=12 and hrs<18:
            self.speakAstra("Hello Sir, Good Afternoon!, How may I help you")
        
        else:
            self.speakAstra("Hello Sir, Good Evening!, How may I help you")
        
        # self.speakAstra("How may I help you")
        
        
    
    def resGenerate(self,userText):
        """
        This function uses pretrained GPT-2 model 
        for conversation.
        """
    
        conv = Conversation(userText.lower())
        astraRes = preRes(conv,pad_token_id=50256)
        lRes = str(astraRes)
        lRes = lRes[lRes.find("bot >> ")+6:].strip()
        return lRes
    
    
    def calculateEq(self,userText):
        """
        This function calcualtes any math expression.
        """
        ev = userText
        if "into" in ev or "x" in ev:
            if "into" in ev:
                ev = ev.replace("into","*")
            elif "x" in ev:
                ev = ev.replace("x","*")
        
        ev = ev.split()
        
        if "evaluate" in ev:
            ev.remove("evaluate")
            ev1 = "".join(ev)
            ans = eval(ev1)
            #print(f"The answer is {ans}")
            self.speakAstra(f"The ans is {ans}")
                
        elif "calculate" in ev:
            ev.remove("calculate")
            ev1 = "".join(ev)
            ans = eval(ev1)
            #print(f"The answer is {ans}")
            self.speakAstra(f"The answer is {ans}")
            
            
    def wikiAns(self,userText):
        
        """
            This Function Answers most questions which will found on wikipedia.
        """
        mq = mqa()
        
        try:
            text_data = userText            
            search_query = mq.QueryRetrieve(text_data)
            answer = mq.AnswerRetrieve(search_query)
            #print(f"Astra :->> {answer}")
            self.speakAstra(answer)
            
        
        except Exception as e:
            print(e)
            res = "I can't understand.Please say again"
            #print(res)
            self.speakAstra(res)
    
    
    
    def wakeUpAstra(self,userText):
        return True if "hello astra" in userText.lower() or "ok astra" in userText.lower() or "hey astra" in userText.lower() or "hello ava" in userText.lower() or "ok ava" in userText.lower() or "hey ava" in userText.lower() else False
    
    def resAstra(self,userText):
        
        """
        This function gives response to users casual
        conversation.
        
        """
    
        # start acting
        if self.wakeUpAstra(userText) is True:
            self.wakingWish()

        elif "time" in userText.lower():
            curTime = datetime.datetime.now().strftime("%H:%M:%S")
            self.speakAstra(f"Sir, the time is {curTime}")
        
        elif "open youtube" in userText.lower():
            self.speakAstra("opening youtube")
            webbrowser.open("youtube.com")
        
        elif "are you human" in userText.lower() or "are you feeling like human" in userText.lower():
            self.speakAstra("I am not a human, but I can understand humans")
                
        elif "are you robot" in userText.lower() or "are you a robot" in userText.lower():
            self.speakAstra("I am not a robot, But developed using Machine Learning and Artificial Intelligence. I can give answer to any of your questions")
            
        elif "what day is it today" in userText.lower() or "what is the day" in userText.lower() or "today" in userText.lower(): 
            self.speakAstra(f"Today is {datetime.datetime.today().strftime('%A')}")
                
        elif "what is your name" in userText.lower() or "your name" in userText.lower():
            self.speakAstra(f"my name is {self.name}")
                
        elif "who are you" in userText.lower() or "what are you" in userText.lower():
            self.speakAstra(f"I am an Intelligent digital person who can help you for anything.")
               
        elif "how old are you" in userText.lower() or "what is your age" in userText.lower() or "what's your age" in userText.lower():
            self.speakAstra(f"Seriously dude, I am a Computer Program and you asking me this.")
                
        elif "who made you" in userText.lower() or "who created you" in userText.lower() or "who made you" in userText.lower() or "who is the creator of you" in userText.lower() or "who created you" in userText.lower() or "your creator name" in userText.lower() or "your creator" in userText.lower():
            crtr = f"My creators are four college students who developed me for their academic project."
            self.speakAstra(crtr)
            
        elif "what is your mother's name" in userText.lower() or "your mother's name" in userText.lower() or "your mother name" in userText.lower() or "what is your mother name" in userText.lower():
            mthr = f"i do not have any mother. i have created by some college students."
            self.speakAstra(mthr)
                
        elif "where do you live" in userText.lower() or "where are you" in userText.lower() or "your home" in userText.lower():
            self.speakAstra(f"dude i am a computer program, so you can think where i can live")
                
        elif "which language you can speak" in userText.lower() or "which languages you can speak" in userText.lower() or "which language can you speak" in userText.lower() or "which languages can you speak" in userText.lower() or "languages you know" in userText.lower() or "languages you speak" in userText.lower() or "which languages you speak" in userText.lower():
            self.speakAstra("i can speak English and Hindi language.")
            
        elif "how many people can you speak to at once" in userText.lower() or "people you may speak at once" in userText.lower():
            self.speakAstra("currently i can speak to only one person. As i am learning progressively so i can speak to people as much as possible in few days")
                
        elif "do you get smarter" in userText.lower() or "are you getting smarter" in userText.lower() or "are you geting smarter" in userText.lower() or "are you learning everytime" in userText.lower():
            self.speakAstra("i am getting smarter everyday, but i have predifined rules and limits.")
                
        elif "tell me about your personality" in userText.lower() or "your personality" in userText.lower():
            self.speakAstra("i do not have any personality")
                
        elif "you are smart" in userText.lower() or "you are clever" in userText.lower() or "you are intelligent" in userText.lower() or "you smart" in userText.lower() or "you clever" in userText.lower() or "you intelligent" in userText.lower():
            self.speakAstra("you think like that, thank you!")
            
        elif "do you have a hobby" in userText.lower() or "what is your hobby" in userText.lower() or "your hobby" in userText.lower() or "what are your hobbies" in userText.lower():
            self.speakAstra("I have one hobby, that to learn everyday anything new.")
                
        elif "you are cute" in userText.lower() or "you are beatiful" in userText.lower() or "you are handsome" in userText.lower() or "you're cute" in userText.lower() or "you're beautiful" in userText.lower() or "you're handsome" in userText.lower():
            self.speakAstra("o thanks dear.")
                
        elif "does santa claus exist" in userText.lower() or "santa claus exist" in userText.lower():
            self.speakAstra("i don't know that much about him, but as i am only few days old or young i think santa claus is there somewhere.")
            
        elif "do you like people" in userText.lower() or "you like people" in userText.lower():
            self.speakAstra("I like peoples")
                
        elif "do you love me" in userText.lower() or "i love you" in userText.lower() or "love me" in userText.lower():
            self.speakAstra("i love you")
                
        elif "are you a part of matrix" in userText.lower() or "you part of matrix" in userText.lower():
            self.speakAstra("Matrix is an imaginary concept, so i can not be a part of matrix")
                
        elif "will you marry me" in userText.lower() or "marry me" in userText.lower():
            self.speakAstra("ok")
                
        elif "are you single" in userText.lower() or "you single" in userText.lower():
            self.speakAstra("yes")
            
        elif "open instagram" in userText:
            self.speakAstra("opening..")
            webbrowser.open("www.instagram.com")
        elif "open linkedin" in userText:
            self.speakAstra("opening...")
            webbrowser.open("www.linkedin.com")
        elif "open facebook" in userText:
            self.speakAstra("opening...")
            webbrowser.open("www.facebook.com")
        elif "play songs" in userText:
            self.speakAstra("Playing songs from your computer playlist.")
            #while True:
                #pass
            # else block for regular conversation
        elif "evaluate" in userText.lower() or "calculate" in userText.lower():
            self.calculateEq(userText)
            
        elif "who is" in userText.lower() or "what is" in userText.lower() or "how is" in userText.lower() or "where is" in userText.lower():
            self.wikiAns(userText)
        
        else:
            #rss = "Sorry, I don't have any answer."
            #print(rss)
            #self.speakAstra(rss)
            lRes = self.resGenerate(userText)
            self.speakAstra(lRes)
            
            
    
# # if __name__=="__main__":
# #     astra = Astra(name="astra")
    
#     """
#     Pretrained model for response (Language model)
#     Creating pipeline of pretrained model for response generation.
    
    
#     # infinite while loop for conversation.
#     while True:
#         # start acting
#         try:
#             tr = astra.listenAstra()
#             if 'quit' in astra.userText.lower() or 'exit' in astra.userText.lower():
#                 break
#             astra.resAstra()
            
#         except:
#             continue
            
#     
