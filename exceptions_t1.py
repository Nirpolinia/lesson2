def ask():
    try:
        while True:
            user_say = input ("How are you? ")
            if user_say == "OK":
                print ("I'm so happy, have a nice day!")
                break
            else:
                print ("Not, you are OK")
    except(KeyboardInterrupt):
        print("Bye-Bye")
ask()