loopy=1
print("Traffic Light Simulation Programme System")
while True:
    if loopy == 1:
        print("Input signal to run program :")
        print("Input red for : STOP")
        print("Input yellow for : READY TO STOP")
        print("Input green for : GO")
        print("Input stop for : END PROGRAMME")
        print("-------------------------------")
    else:
        print("Input signal to run program : ")
        print("-------------------------------")
    signal = input()
    if signal == "red":
        print("color = RED")
        print("Stop behind the line")
        print("Next 60 seconds")
        print("---------------------")
    else:
        if signal == "yellow":
            print("color = YELLOW")
            print("Get ready to stop your vehicle")
            print("Next 60 seconds")
            print("---------------------------------")
        else:
            if signal == "green":
                print("Color = GREEN")
                print("You can move forward now.Drive safely.")
                print("Next 60 seconds")
                print("---------------------------------------")
            else:
                if signal == "stop":
                    print("You choose to end this programme.")
                    print("----------------------------------")
                else:
                    print("Please insert the right signals(red,yellow,green & stop) only.")
                    print("--------------------------------------------------------------")
    loopy=2
    if not(signal !="stop"): break     #Exit loop
print("End Simulation Programme")                            

