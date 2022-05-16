"""
BJJ Private booking system

you can pick the day (mon-sun)
you can pick a time (9am-5pm / lessons start on the hour)
Each hour has 1 slot
You can add a booking, remove a booking, or view all bookings
a .txt file acts as a database.


"""


def main_menu():
    print("~~BJJClub Booking System~~\n")
    print("Please pick an option:\n")
    print("1. Create a booking.\n")
    print("2. Remove a booking.\n")
    print("3. View all bookings.\n")
    print("4. Exit.\n")

def add_booking():
    database = open("database.txt", "w")
    print("\nPick a day (Monday - Sunday.")
    print("Or type exit to return to menu.\n")
    day = input()
    print("\nPick a time (9am - 6pm).")
    print("Or type exit to return to menu.\n")
    time = input()
    print("\nType your name.")
    print("Or type exit to return to menu.\n")
    name = input()

    #check if date and time are in use:
        #Placeholder

    if day == 'Monday' or day == 'monday': 
        database.write("Monday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Tuesday' or day == 'tuesday': 
        database.write("Tuesday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Wednesday' or day == 'wednesday': 
        database.write("Wednesday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Thursday' or day == 'thursday': 
        database.write("Thursday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Friday' or day == 'friday': 
        database.write("Friday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Saturday' or day == 'saturday': 
        database.write("Saturday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Sunday' or day == 'sunday': 
        database.write("Sunday|" + time + "|" + name + "\n")
        print("Booking created. See you soon!\n")
    elif day == 'Exit' or day == 'exit': main()
    else: 
        print("Invalid option! Please try again.\n") 
        add_booking()
        

def remove_booking():
    print("Placeholder\n")

def view_bookings():
    print("Placeholder\n")

def debug():
    print("OPTION VAR: " + option)

def main():
    main_menu()
    option = input()

    if option == '1':
        add_booking()
    elif option == '2':
        remove_booking()
    elif option == '3':
        view_bookings()
    elif option == '4':
        print("Exiting...\n")
    else:
        print("Invalid option! Exiting...\n")

main()