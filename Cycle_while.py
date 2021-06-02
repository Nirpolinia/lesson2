while True:
    user_say = input("Wrigh smth: ")
    if user_say == "Buy":
        print("Buy-buy")
        break
    else:
        print("You are a {}".format(user_say))
