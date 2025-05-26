while True:

    print("\033[1;34;40m Functions:")     
    print("\033[1;34;40m cm to in" )    
    print("\033[1;34;40m in to cm" )    
    print("\033[1;34;40m kg to pounds" )         
    print("\033[1;34;40m pounds to kg" )      
    print("\033[1;34;40m f to c (Fahrenheit to Celsius)" )      
    print("\033[1;34;40m c to f (Celsius to Fahrenheit)" )
    print("At any time, type exit all to leave the program" )
    print(" ")
    
    user_input = input("\033[1;37;40m You:  ")

    if user_input.lower() == "exit all":
        break

    elif user_input.lower() == "c to f":
        print("\033[1;34;40m Please enter your temperature in degrees Celsius to convert them to Fahrenheit") 
        while True:
            user_input = input("\033[1;37;40m Celsius (or type exit to quit): ")
            if type(eval(user_input) or user_input.lower() == "exit") == int:
                print("\033[1;34;40m")
                print(f"{int(user_input)* 9/5 + 32} °F")
            elif user_input.lower() == "exit":
                break
            else:
                print("\033[1;34;40m Enter integers please")

    if user_input.lower() == "f to c":
        print("\033[1;34;40m Please enter your temperature in degrees Fahrenheit to convert them to Celsius") 
        while True:
            user_input = input(" \033[1;37;40m Fahrenheit (or type exit to quit): ")
            if type(eval(user_input) or user_input.lower() == "exit") == int:
                print("\033[1;34;40m")
                print(f"{(int(user_input)-32)/ 9*5:.1f} °C")
            elif user_input.lower() == "exit":
                break
            else:
                print("\033[1;34;40m Enter integers please")

    if user_input.lower() == "in to cm":
        print("\033[1;34;40m Please enter your length in inches to convert them to centimetres") 
        while True:
            user_input = input("\033[1;37;40m Inches (or type exit to quit): ")
            if type(eval(user_input) or user_input.lower() == "exit") == int:
                print("\033[1;34;40m")
                print(f"{int(user_input)*2.54} cm")
            elif user_input.lower() == "exit":
                break
            else:
                print("\033[1;34;40m Enter integers please")
            
    if user_input.lower() == "cm to in":
        print("\033[1;34;40m Please enter your length in centimetres to convert them to inches") 
        while True:
            user_input = input("\033[1;37;40m Centimetres (or type exit to quit): ")
            if type(eval(user_input) or user_input.lower() == "exit") == int:
                print("\033[1;34;40m")
                print(f"{int(user_input)/2.54:.1f} inches")
            elif user_input.lower() == "exit":
                break
            else:
                print("\033[1;34;40m Enter integers please")

    if user_input.lower() == "pounds to kg":
        print("\033[1;34;40m Please enter your weight in pounds to convert them to kilograms") 
        while True:
            user_input = input("\033[1;37;40m Pounds (or type exit to quit): ")
            if type(eval(user_input) or user_input.lower() == "exit") == int:
                print("\033[1;34;40m")
                print(f"{int(user_input)/2.205:.1f} kg")
            elif user_input.lower() == "exit":
                break
            else:
                print("\033[1;34;40m Enter integers please")

    if user_input.lower() == "kg to pounds":
        print("\033[1;34;40m Please enter your weight in kilograms to convert them to pounds") 
        while True:
            user_input = input("\033[1;37;40m Kilograms (or type exit to quit): ")
            if user_input.lower() == "exit":
                print("\033[1;34;40m")
                print(f"{int(user_input)*2.205:.1f} pounds")
            elif user_input.lower() == "exit":
                break
            else:
                print("\033[1;34;40m Enter integers please")