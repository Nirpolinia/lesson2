dictionary = {
    "How are you?":"I'm Ok", 
    "What are you doing?":"Programming",
    "What is youf favourite color?":"black"}
def ask_user ():  
    while True:
        user_say = input ("Ask me a question: ")
        if dictionary.get(user_say,0)!=0:
            print(dictionary.get(user_say))
            break
        else:
            print ("I am not going to answer such a stupid question")
ask_user()

    