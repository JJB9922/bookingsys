"""
BJJ Private booking system

you can pick the day (mon-sun)
you can pick a time (9am-5pm / lessons start on the hour)
Each hour has 1 slot
You can add a booking, remove a booking, or view all bookings
a .txt file acts as a database.


"""
import sys
from os.path import exists

def main_menu():
    print("~~BJJClub Booking System~~\n")
    print("Please pick an option:\n")
    print("1. Create a booking.\n")
    print("2. Remove a booking.\n")
    print("3. View all bookings.\n")
    print("4. Exit.\n")

def add_booking():
    print("\nPick a day (Monday - Sunday).")
    print("Or type exit to return to menu.\n")
    day = input()
    if day==exit:
        main_menu()
    print("\nPick a time (9am - 6pm).")
    print("Or type exit to return to menu.\n")
    time = input()
    if time==exit:
        main_menu()
    print("\nType your name.")
    print("Or type exit to return to menu.\n")
    name = input()
    if name==exit:
        main_menu()

    bookData = day+"|"+time+"|"+name

    #Check availability
    with open("database.txt", "r") as database:
        #Check availability   
        noDayAvailability = False
        noTimeAvailability = False 
        i = 0
        if exists("database.txt"):
            with open("database.txt", "r") as db:
                for line in db:
                    linelist = line.split('|')
                    #print(linelist[0])
                    #Count occurences of monday
                    if linelist[0] == day:
                        i = i+1
                        #print(i)
                        if i==3:
                            noDayAvailability = True
                        elif time==linelist[1]:
                            noTimeAvailability = True    

    if day == 'Monday' or day == 'monday':
        day = 'Monday'
        if exists("database.txt"):
            with open("database.txt", "a") as database:
                if noDayAvailability == True:
                    print('\n'+ day + " is fully booked - please try another day.")
                    add_booking()
                elif noDayAvailability == False and noTimeAvailability == True:
                    print('\n'+ time + " is fully booked - please try another time.")
                    add_booking()
                else:
                    day = 'Monday'
                    database.write(str(bookData) + "\n")
                    print("Booking created. See you soon!\n")
        else: 
            print ("\nFile does not exist! Creating...\n")
            with open("database.txt", "w") as database:
                database.write(str(bookData))
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
    with open('database.txt', 'r') as dbfile:
        while True:
            file_EOF = dbfile.read()
            for i in range (0, file_EOF):
                print(i)
 
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
        sys.exit()


main()
