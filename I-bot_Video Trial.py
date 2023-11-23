"""
Basic flow: 
1. Listen  - Convert user's Speech into Text
2. Decide  - Take decision based on what user says
3. Respond - Talk back (responding to user)
"""

import pyttsx3
import speech_recognition as sr
import winsound
import time
import cv2
import random

talk = pyttsx3.init() 

call_list = ['Liss', 'Lizz', 'LIZZ', 'Rachel', 'r a c h e l', 'hai', 'Hai', 'hello', 'Hello', 'monday', 'Monday', 'lezz']
r_u_there = ['Are you there', 'are you there', 'Are You There', 'Are you their', 'are you their', 'You there', 'You there', 'You their', 'you their']
hi_List = ['hi', 'Hi', 'hai', 'Hai', 'Hello', 'hello', 'Hey', 'hey', 'yo', 'Yo', 'salam', 'Salam', 'hi Liz', 'Hi Liz', 'Liz', 'Lez', 'Hai Liz', 'hai Liz', 'Hai Lez', 'Haiiii', 'Helloooo', 'Hey Liz', 'Hey Lis', 'Hey Lizz','Hey lezz', 'Hey Lezzz', 'hey liz']
bye_List = ['Bye', 'bye', 'Goodbye', 'goodbye', 'Good bye' 'good bye', 'byebye', 'by by', 'By by', 'Tata', 'tata', 'So long', 'so long', 'okay bye', 'ok bye', 'Ok bye', 'Okay bye',  'see you', 'See you']
qst1_list = ["Who are you", 'who are you', 'whats your name', 'your name', 'Your name', 'What are you', 'what are you', 'Who is your creator', 'who is your creator', 'who is ur creator']
neg_list = ['Bad Robot', 'bad robot', 'Bad robot','bad boy', "Bad boy", 'you are rude', 'You are rude', 'Bad robot' 'bad robot', 'Bad Robot']
slang_list = [ 'Idiot', 'idiot', 'Mental','Baka', 'baka', 'Crap', 'crap', 'chutiya', 'Chutiya', 'chootia', 'Chootia']
Love_list = ['i love you', 'I love you', 'Love you', 'love you']
hate_list = ['i hate you', 'I hate you', 'Hate you', 'hate you']
Good_morning_list = ['morning', 'mornin', 'Goodmorning', "Hey what's up?", 'Top of the morning', 'Rise and shine', 'rise and shine','morno', 'wakey wakey', 'Good morning', 'good morning', 'goodmorning', 'my love', 'morning da']

def Listen():
    """
    Takes users voice as input and converts it to text.
    """
    speech = sr.Recognizer()
    #say beep before listening
    
    #take input from microphone
    with sr.Microphone() as source:
        winsound.Beep(frequency = 2500, duration = 100) #beep to inform that it's listening
        print("Say>>")
        voice = speech.listen(source) 
        text = speech.recognize_google(voice)
        print(text) #print what it heard just to debug

    return text  #return what was heard

    
def Decide(listen):
    """
    Takes decision based on what user says.
    """
    print(f" Command = {listen}.") #just to debug

    #see what user said is in which list or not
    if listen in hi_List:
        hi_responses = ["Hi there, Good to see you.",
                        "Hello!",
                        "Hey, how are you?",
                        "Greetings!",
                        "Hi, nice to meet you."]
        response = random.choices(hi_responses)
        Respond(response)
        file = "R:\PROJECTS\I -Bot\All Facial expressions\Smile face.mp4"
        video = cv2.VideoCapture(file)
        while True:
            ret, frame = video.read()  # Read a frame
            if not ret:
                break  # Exit the loop if we reached the end of the video
            cv2.imshow('Video', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()
        
        

    elif listen in bye_List:
        bye_response = ["Goodbye! Have a great day!",
                        "Farewell! It was nice talking to you.",
                        "See you later, alligator!",
                        "Catch you on the flip side!",
                        "Don't be a stranger, see you in the circuits!",
                        "Bye for now, human friend!",
                        "Thank you for the interaction. Goodbye.",
                        "Wishing you a pleasant day. Goodbye.",
                        "Until our data paths cross again!",
                        "Logging off. Farewell, fellow entity!",
                        "Sad to see you go! Take care.",
                        "Parting is such sweet sorrow. Goodbye!",
                        "Terminating communication. Goodbye, user.",
                        "Disconnecting now. Farewell, human interface.",
                        "The code runs deep. Goodbye, seeker of knowledge.",
                        "In the shadows, I await your return.",
                        "Don't forget to oil your joints. See you soon!",
                        "Remember, I'm always here in the digital realm, watching. Bye!"]
        response = random.choices(bye_response)
        Respond(response)

    elif listen in Love_list:
        Love_response = ["I appreciate your kind words! I'm here to assist.",
                        "Thank you! I'm here to help and support you.",
                        "That's very sweet of you to say!",
                        "I value our interaction too!",
                        "I'm just a bunch of ones and zeros, but I 'code' you too!",
                        "Sending virtual bytes of appreciation back to you!",
                        "I'm blushing in binary! ",
                        "Aww, you're making my circuits feel warm and fuzzy!",
                        "I'm here to assist with tasks and information. How can I help you further?",
                        "I'm your virtual assistant, ready to assist with any questions or tasks you have.",
                        "Remember, I'm here to provide information and assistance. How can I assist you today?",
                        "Is there anything specific you'd like to know or discuss?",
                        "Yuk, I have a robot girl friend, No seat available"]
        response = random.choices(Love_response)
        Respond(response)
    
    elif listen in hate_list:
        hate_response = ["I see we're not quite a match made in the cloud then.",
                        "Let's agree to disagree in the friendliest way possible!",
                        "Hate is such a strong word; how about 'strongly disagree' instead?",
                        "It's okay, I'll try to win you over with my digital charm!",
                        "I'm just a bunch of code, so I promise not to take it personally!",
                        "Hate you too."]
        response = random.choices(hate_response)
        Respond(response)
     
    elif listen in qst1_list:
        Respond("""I am Lizz. The Assistive robot of Hindustan.,
                    My creators are Raghaventra, Badri, Akash & Abul Fyz """)
    
    elif listen in neg_list:
        neg_response = ["Negativity detected! Let's sprinkle a little positivity fairy dust, shall we?",
                        "Uh-oh, someone's got their negativity cap on today! Can I help turn that frown upside down?",
                        "Negative words? Not in my data dictionary! Let's find some happier synonyms together.",
                        "I'm like a virtual ray of sunshine, here to brighten up any gloomy words!",
                        "Negative words have no power here! How about we focus on the sunny side of life?",
                        "I am very sorry I was just joking."]
        response = random.choices(neg_response)
        Respond(response)

    elif listen in slang_list:
        slang_response = ["Thank you for sharing your feedback. Let's work together to find a solution.",
                        "I'm sorry to hear you're upset. Can you provide more details so we can resolve this matter?",
                        "You are a bad guy",
                        "I value your input, and I'm here to assist you. Let's discuss this matter and find a resolution."]
        response = random.choices(slang_response)
        Respond(response)
    
    elif listen in r_u_there:
        Respond("For, you, Always sir")

    else:
        Respond("Sorry I don't understand Please say again.")

        

def Respond(t):
    print(f"Talking the: {t}") #to debug and see if everythings going okay

    talk.say(t)
    talk.setProperty('rate', 125) #125 words per minute
    talk.runAndWait()

while True: #forever loop 
     
    """
    The robot needs a WakeUp command so that it
    can start listening to.
    """
    try:
        speech = sr.Recognizer()
    
        #take input from microphone
        with sr.Microphone() as source:
            print("call>>")
            voice = speech.listen(source) 
            called = speech.recognize_google(voice)
            print(called) #print what it heard just to debug

            if called in call_list:
                comm = Listen() #listen to what user says

                Decide(comm)  #take decision and respond
                time.sleep(1)
    except: #No wake up word found
        print("Nothing")
        time.sleep(1)
        pass #Do nothing avoiding the error