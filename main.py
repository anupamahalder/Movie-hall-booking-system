    
from star_cinema import Star_Cinema
from hall import Hall

# Create instances of Hall class to represent different halls
hall1 = Hall(5, 4, 101)
hall2 = Hall(6, 5, 102)
hall3 = Hall(7, 6, 103)

# Perform operations on each hall
hall1.entry_show(777, "Jawan", "24/04/2024 12:00 PM")
hall1.entry_show(888, "Maidaan", "24/04/2024 12:00 PM")
hall2.entry_show(111, "Pathan", "24/04/2024 1:00 PM")
hall3.entry_show(222, "Tiger", "24/04/2024 2:00 PM")

flag = True
while flag:
    print("\n------Welcome to Star Cinema------\n")
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        Hall.view_show_list()

    elif option == 2:
        show_id = int(input("Enter show ID: "))
        for hall in Hall.get_hall_list():
            if show_id in hall.seats:
                hall.view_available_seats(show_id)
                break
        else:
            print("Invalid show ID!")

    elif option == 3:
        show_id = int(input("Enter show ID: "))

        valid_show_id = False
        for hall in Hall.get_hall_list():
            if show_id in hall.seats:
                valid_show_id = True
                break

        if valid_show_id:
            num_seats = int(input("Enter number of seats to book: "))
            for hall in Hall.get_hall_list():
                if show_id in hall.seats:
                    for _ in range(num_seats):
                        # get row and col as input 
                        row = int(input("Enter the row number:"))
                        col = int(input("Enter the column number:"))
                        hall.book_seats(show_id, (row, col))
                    break
        else:
            print("Invalid show ID!")

    elif option == 4:
        flag = False
    else:
        print("You have entered a wrong choice!")
