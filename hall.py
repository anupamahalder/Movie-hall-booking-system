from star_cinema import Star_Cinema

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows 
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        tpl = (id, movie_name, time)
        self.show_list.append(tpl)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def book_seats(self, id, tpl):
        if id in self.seats:
            row, col = tpl
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(f'Seat booked successfully on seat({row}, {col})!')
                else:
                    print('Seat already booked!')
            else:
                print(f"Sorry this seat({row}, {col}) is not available!")
        else:
            print("Invalid id!")

    @classmethod
    def view_show_list(cls):
        for hall in Star_Cinema.get_hall_list():
            for id, movie_name, time in hall.show_list:
                print(f'Show ID: {id}, Movie Name: {movie_name},  Time: {time}')
    
    def view_available_seats(self, id):
        if id in self.seats:
            print("See the available seats with index of row and column:")
            for row_index, row in enumerate(self.seats[id]):
                for col_index, seat in enumerate(row):
                    if seat == 0:
                        print(f"Seat ({row_index}, {col_index})")
            # print in the matrix form
            print("Show the available seats in matrix form:") 
            for row in self.seats[id]:
                print(row)
        else:
            print("Invalid id")
