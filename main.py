"""
Private booking system

you can pick the day (mon-sun)
you can pick a time (9am-5pm / lessons start on the hour)
Each hour has 1 slot
You can add a booking, remove a booking, or view all bookings
a .txt file acts as a database.


"""
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sys
from os.path import exists

def main_menu():
    print("\n~~Booking System~~\n")
    print("Please pick an option:\n")
    print("1. Create a booking.\n")
    print("2. Remove a booking.\n")
    print("3. View all bookings.\n")
    print("4. Exit.\n")

def add_booking():
    print("\nPick a day (Monday - Sunday).")
    print("Or type exit to return to menu.\n")
    day = input()
    #Check if valid day
    dayList = ['monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday', 'exit']
    dayTest = [ele for ele in dayList if(ele in day.lower())]
    if bool(dayTest) == False:
        print("Invalid day. Please use valid dates and timings.")
        add_booking()
        return
    elif day.lower()=='exit':
        main()
        return
    print("\nPick a time (9am - 3pm).")
    print("Or type exit to return to menu.\n")
    time = input()
    timeList = ['9am', '10am', '11am', '12pm',
                '1pm', '2pm', '3pm', 'exit']
    timeTest = [ele for ele in timeList if(ele in time.lower())]
    if bool(timeTest) == False:
        print("Invalid time. Please use valid days and timings. Example: '9am'\n")
        add_booking()
        return
    elif time.lower()=='exit':
        main()
        return
    print("\nType your name.")
    print("Or type exit to return to menu.\n")
    name = input()
    if name.lower()=='exit':
        main()
        return
    elif len(name) > 25:
        print("Name must be under 25 characters long.")    

    bookData = day.lower()+"|"+time.lower()+"|"+name.lower()

    #Check availability
    with open("database.txt", "r") as database:
        noDayAvailability = False
        noTimeAvailability = False 
        i = 0
        if exists("database.txt"):
            with open("database.txt", "r") as db:
                for line in db:
                    linelist = line.split('|')
                    #print(linelist[0])
                    #Count occurences of day
                    if linelist[0] == day:
                        i = i+1
                        #print(i)
                        if i==3:
                            noDayAvailability = True
                        elif time==linelist[1]:
                            noTimeAvailability = True


    if exists("database.txt"):
        with open("database.txt", "a") as database:
            if noDayAvailability == True:
                print('\n'+ day + " is fully booked - please try another day.")
                add_booking()
            elif noDayAvailability == False and noTimeAvailability == True:
                print('\n'+ time + " is booked on " + day + " - please try another time.")
                add_booking()
            else:
                database.write(str(bookData) + "\n")
                print("Booking created. See you soon!\n")
                print("\nMake another booking? Y/N")
                addOption = input()
        if addOption.lower() == 'y':
            add_booking()
            return
        else:
            main()
            return
    else: 
        print ("\nFile does not exist! Creating...\n")
        with open("database.txt", "w") as database:
            database.write(str(bookData))
            print("Booking created. See you soon!\n")
            print("\nMake another booking? Y/N")
            addOption = input()
        if addOption.lower() == 'y':
            add_booking()
            return
        else:
            main()
            return
        

def remove_booking():
    if exists("database.txt"):
        print("Please enter the day you wish to remove a booking from.\n")
        print("Or type exit to return to menu.\n")
        remDay = input()

        if remDay.lower()=='exit':
            main()
            return

        dayList = ['monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday', 'exit']
        dayTest = [ele for ele in dayList if(ele in remDay.lower())]
        if bool(dayTest) == False:
            print("\nInvalid day. Please use a valid day.\n")
            remove_booking()
            return

        print("\nBookings occuring on " + remDay + ":\n")
        with open("database.txt", "r") as db:
            dayFound=False
            for line in db:
                linelist = line.split('|')
                
                if linelist[0] == remDay.lower():
                    print(line)
                    dayFound=True

        if dayFound==False:    
            print("\nNo bookings found on " + remDay)
            print("\nReturn to menu? Y/N")
            remOption = input()
            if remOption.lower() == 'y':
                main()
                return
            else:
                sys.exit()
        else:
            with open("database.txt", "r") as db:
                print("\nPlease choose a time to remove a booking on " + remDay + "\n")
                remTime = input()
                timeList = ['9am', '10am', '11am', '12pm',
                        '1pm', '2pm', '3pm', 'exit']
                timeTest = [ele for ele in timeList if(ele in remTime.lower())]
            if bool(timeTest) == False:
                print("Invalid time. Please use valid days and timings. Example: '9am'\n")
                remove_booking()
                return
        i = 0 
        with open("database.txt", "r") as remDbR:   
            for line in remDbR:
                linelist = line.split('|')
                i = i+1
                if linelist[0] == remDay.lower() and linelist[1] == remTime.lower():
                    dayDel = remDay.lower()
                    timeDel = remTime.lower()

        with open("database.txt", "r+") as remDb:
            lines = remDb.readlines()
            remDb.seek(0)
            for line in lines:
                if (dayDel+"|"+timeDel) not in line:
                    remDb.write(line)
            remDb.truncate()
            print("\nBooking removed.")
            print("\nRemove another booking? Y/N")
            remOption = input()
        if remOption.lower() == 'y':
            remove_booking()
            return
        else:
            main()
            return

                            
    else:
        print("No bookings exist. Return to menu? Y/N.\n")
        remOption = input()
        if remOption.lower() == 'y':
            main()
            return
        else:
            sys.exit()

def view_bookings():
    print("\n")
    if exists("database.txt"):
        with open("database.txt", "r") as db:
            for line in db:
                print(line)
            print("Return to menu? Y/N")
            viewOption = input()
        if viewOption.lower() == 'y':
            main()
            return
        else:
            sys.exit()
    else:
        print("File does not exist - you need at least 1 booking to create it.\n")
        main()
        return


def debug():
    with open('database.txt', 'r') as dbfile:
        while True:
            file_EOF = dbfile.read()
            for i in range (0, file_EOF):
                print(i)
 
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Black", font=("Helvetica", 18))
        self.label.place(x=50,y=80)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Report Issue", command=self.popupwin)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Admin", menu=fileMenu)

    def exitProgram(self):
        exit()

    def popupwin(self):
        tkinter.messagebox.showinfo("Sorry", "Too bad")

def gui():
    root = Tk()
    app = Window(root)
    root.wm_title("System")
    root.geometry("320x200")

    add_button = ttk.Button(
        root,
        text='Add Booking',
        command=lambda: add_booking()
    )

    add_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    rem_button = ttk.Button(
        root,
        text='Remove Booking',
        command=lambda: exit()
    )

    rem_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    view_button = ttk.Button(
        root,
        text='View All Bookings',
        command=lambda: exit()
    )

    view_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )


    exit_button = ttk.Button(
        root,
        text='Exit',
        command=lambda: exit()
    )

    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop()


def main():
    #gui()
    main_menu()
    option = input()

    if option == '1':
        add_booking()
    elif option == '2':
        remove_booking()
    elif option == '3':
        view_bookings()
    elif option == '4':
        print("\nExiting...\n")
    else:
        print("Invalid option! Exiting...\n")
        sys.exit()

    


main()


