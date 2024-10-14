from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

# Initialize the TrainCoach instance
coach = TrainCoach(80, 7)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    reserved_seats = []
    if request.method == 'POST':
        try:
            num_seats = int(request.form.get('num_seats', 0))
            if num_seats > 0:
                reserved_seats = coach.reserve_seats(num_seats)
                if len(reserved_seats) < num_seats:
                    message = "Sorry, not enough seats available."
                else:
                    message = f"Successfully reserved {num_seats} seat(s)."
            else:
                message = "Please enter a valid number of seats."
        except ValueError:
            message = "Invalid input. Please enter a number."
    return render_template('index.html', coach=coach, message=message, reserved_seats=reserved_seats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81,debug =True)
