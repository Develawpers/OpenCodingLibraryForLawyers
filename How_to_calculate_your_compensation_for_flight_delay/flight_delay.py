def my_func():
    print("How much can you claim in compensation for your delayed flight? Type here the delay and the distance to find out")
   
    delay = float(input("How many hours of delay?: "))
    distance = float(input("How many kilometers away?: "))
   
    if delay<3:
        print("You are not entitled to any compensation, sorry")
    elif delay>=3:
        if distance<1500:
            print("You shall receive a compensation amounting to 250€")
        elif distance>3500:
            if delay<4:
                print("You shall receive a compensation amounting to 300€")
            else:
                print("Great, you are entitled to a compensation amounting to 600€")
        else:
            print("That's right, your compensation shall be 400€")
    answer = str(input("Would you like to calculate your compensation again?"))
    if ((answer == "yes") or ( answer == "Yes")):
      my_func()
    else:
      print("Have a good day!")          

my_func()
