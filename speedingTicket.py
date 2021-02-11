

# List of who should be arrested
criminal = ['Sashin', 'Josiah', 'Ethan']

# Asks for the name of the driver, if it is a wanted driver it will print something out.
def name():
    print('What is the name of the driver?')
    while True:
        global name
        name = input()
        if name in criminal:
            print('ARREST THEM! THEY ARE WANTED!')
            sys.exit()
        if name.isnumeric():
            print('Only enter letters')
        else:
            break

# Calculates the fine based on the speed of the driver
def calculatefine():
    while True:
        try:
            # Variables to be used
            global fine1
            fine1 = 0
            global fine2
            fine2 = 0
            global fine3
            fine3 = 0
            global fine4
            fine4 = 0

            # Asks for the speed limit and speed of the driver
            print('What is the speed limit of the area?')
            speed_limit = int(input(''))      
            print('What is the speed of {}?' . format(name)) 
            speed_driver = int(input(''))

            # Calculates the new speed after the driver's speed minus the limit. Then putting it into variables
            global over_speed
            over_speed = speed_driver - speed_limit
            if over_speed > 1 and over_speed < 50:
                over_speed *= 10
                fine1 = over_speed
                break
            elif over_speed >= 50 and over_speed < 80:
                fine2 = over_speed
                break
            elif over_speed >= 80:
                fine3 = over_speed
                break
        except ValueError:
            print("Please only enter a whole number, eg. 120 or 150 for the speed of the driver and limit.")
        
# Prints out what the driver gets depending on their speed
def summary():
    if fine1:
        print("The fine is ${}." .format(fine1))
    elif fine2:
        print("Collect {} licence." .format(name))           
    elif fine3:
         print("Send {} to jail." .format(name))
    else:
        print("{} free of charge". format(name))

# Calls the name first, calculatefine second, then calls the summary
name()
calculatefine()
summary()

    
        
    
  