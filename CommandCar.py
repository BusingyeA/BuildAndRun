#imports
import emoji
#initialising varriables

command = ""
started = False


#setting a condition
while True:
    command = input(">").lower()
    print(command)

    if command=="start":
        if started:
            print("please, please you cannot start, the car is already started")
            print(emoji.emojize(":grinning_face_with_big_eyes:"))
        else:
            started =True
            print("The car is started....")

    elif command =="stop":
        if not started:
            print("my dear the car is already in static mode,,,")
        else:
            started = True
            print("the car is stopped:X")

    elif command == "help":
        print(""""
        start: -to start the car
        stop: -to stop the car
        quit: -to quit the program
        """)
    elif command =="quit":
        break
    else:
        print("What you have done is not right!!!!!")





