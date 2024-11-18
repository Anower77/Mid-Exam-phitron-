class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)




class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []



    def entry_show(self, show_id, movie_name, show_time):
        show_details = (show_id, movie_name, show_time)
        self.show_list.append(show_details)

        # 2D Matrix
        seats_matrix = []
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                row.append(0)
            seats_matrix.append(row)

        self.seats[show_id] =seats_matrix




    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            raise ValueError("Invalid show ID..")
        
        for row, col in seat_list:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                raise ValueError(f"Invalid seat position: ({row}, {col}).")
            if self.seats[show_id][row][col] == 1:
                raise ValueError(f"Seat ({row}, {col}) is already booked.")

            self.seats[show_id][row][col] = 1 # book the seat




    def view_show_list(self):
        if not self.show_list:
            print("No shows Availble...")
            return

        print("List of Shows: ")
        for show_id, movie_name, show_time in self.show_list:
            print(f"ID: {show_id}, Movie: {movie_name}, Time: {show_time}")




    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            raise ValueError("Invalid show ID,,,")
        

        print(f"Availble seats for show ID {show_id}:")
    
    
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[show_id][row][col] == 0:
                    seat_status = "0"
                else:
                    seat_status = "1"
                    
                print(seat_status, end=" ")
            print()

    
        
        

def main():
    cinema = Star_Cinema()
    hall_1 = Hall(5, 8, 101)
    hall_2 = Hall(6, 6, 102)


    cinema.entry_hall(hall_1)
    cinema.entry_hall(hall_2)


    hall_1.entry_show(1, "Movie A", "10.00 AM")
    hall_1.entry_show(2, "Movie B", "1.00 PM")
    hall_2.entry_show(3, "Movie C", "12.00 PM")

    while True:
        print("\n-----Chose Option-----")
        print("1. View all show")
        print("2. View Available Seats in a Show")
        print("3. Book Seats for a Show")
        print("4. Logout")

        try:
            option = int(input("Enter your choice : "))
            
            if option==1: # view all option
                for hall in cinema.hall_list:
                    hall.view_show_list()

            elif option==2: # view avalible seats
                show_id = int(input("Enter show ID: "))
                hall_no = int(input("Enter hall number (101 or 102): "))
                
                hall = None
                for i in cinema.hall_list:
                    if i.hall_no == hall_no:
                        hall = i
                        break

                if hall is not None:
                    hall.view_available_seats(show_id)
                else:
                    print("Invalid Hall Number.")

            elif option==3: # book seats
                show_id = int(input("Enter show ID: "))
                hall_no = int(input("Enter hall number (101 or 102): "))

                hall = None
                for i in cinema.hall_list:
                    if i.hall_no == hall_no:
                        hall = i
                        break
                
                if hall is not None:
                    seat_list = []
                    num_seats = int(input("How many seats to book? "))

                    for _ in range(num_seats):
                        row = int(input("Enter row number: "))
                        col = int(input("Enter colum number: "))
                        seat_list.append((row, col))

                    try:
                        hall.book_seats(show_id, seat_list)
                        print("Seats booked successfully!!!")
                    except ValueError:
                        print("Value Error!!!")
                         
                else:
                    print("Invalid Hall Number.")
            
            elif option==4: # logout
                print("Exiting the system...")
                break


            else:
                print("Invalid option. Please choose between 1 and 4.")

        except ValueError:
            print("Please enter a valid number.")



if __name__ == "__main__": 
    main()
