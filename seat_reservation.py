
class TrainCoach:
    def __init__(self, total_seats, seats_per_row):
        self.total_seats = total_seats
        self.seats_per_row = seats_per_row
        self.rows = self.calculate_rows()
        self.seats = self.initialize_seats()

    def calculate_rows(self):
        full_rows = self.total_seats // self.seats_per_row
        remaining_seats = self.total_seats % self.seats_per_row
        if remaining_seats > 0:
            full_rows += 1
        return full_rows

    def initialize_seats(self):
        seats = []
        for i in range(self.rows):
            if i == self.rows - 1 and self.total_seats % self.seats_per_row != 0:
                seats.append([False] * (self.total_seats % self.seats_per_row))
            else:
                seats.append([False] * self.seats_per_row)
        return seats

    def reserve_seats(self, num_seats):
        if num_seats > 7:
            return []
        reserved_seats = []
        for i in range(self.rows):
            for j in range(len(self.seats[i])):
                if not self.seats[i][j] and len(reserved_seats) < num_seats:
                    self.seats[i][j] = True
                    reserved_seats.append((i, j))
        return reserved_seats

    def display_seats(self, reserved_seats):
        print("Coach Seat Layout:")
        for i in range(self.rows):
            for j in range(len(self.seats[i])):
                if (i, j) in reserved_seats:
                    print("R", end="\t")
                elif self.seats[i][j]:
                    print("B", end="\t")
                else:
                    print("A", end="\t")
            print()
        print("R: Reserved, B: Booked, A: Available")

def main():
    coach = TrainCoach(80, 7)
    while True:
        num_seats = int(input("Enter the number of seats to reserve (0 to exit): "))
        if num_seats == 0:
            break
        reserved_seats = coach.reserve_seats(num_seats)
        if len(reserved_seats) < num_seats:
            print("Sorry, not enough seats available.")
        else:
            print("Reserved seats:")
            for seat in reserved_seats:
                print(f"Row {seat[0]+1}, Seat {seat[1]+1}")
            coach.display_seats(reserved_seats)

if __name__ == "__main__":
    main()

 