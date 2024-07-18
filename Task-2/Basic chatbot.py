import nltk
# installing ntlk library and reuired libraries
from nltk.chat.util import Chat, reflections
# logic for the ntlk chatbot questions and answers
pairs = [
[r'hi|hello' ,
['Hello', 'Hey there']
],
[ 
        r"my name is",
        ["Hello, How are you today ?"]
   ],
   [
     r"what is your name ?",
   ["I am a chatbot . you can call me Chatbot."]
   ],
   [
      r"How are you?",
     [
      "I'm good . How about you?"
     ]
   ],
   [
      r"who are you?",
     [
        "I'm your personal assistant chatbot"
     ]
   ],
   [
      r"what do you do ?",
      [
         "I can answer your simple questions"  
      ]
   ],
   [
       r"can you recommend me some books?",
       [
         "yes , Atomic Habits by James Clear"   
       ]
   ],
   [
      r"quit",
      ["Bye! Take care."]
    
   ],
   [
      r"(.*)",
      ["sorry, Ididn't understand that."]
   ]
]
# /creating Chat bot
chatbot = Chat(pairs, reflections)
while True:
    user_input = input("you :")
    # answer to user input
    response = chatbot.respond(user_input)
    print('Chatbot: ' , response)


