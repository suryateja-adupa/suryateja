command = ""
while True:
    command = input(">>>")
    if command.lower() == "start":
        print("car has started")
    elif command.lower() == "stop":
        print("car has stopped")
    elif command.lower() == "help":
        print('''
start = start to start car
stop = stop the car
quit = skip the game
        ''')
    elif command.lower() =="quit":
        break
    else:
        print("I didn't understand")
