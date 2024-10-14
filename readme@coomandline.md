--This system allows users to book and manage train seats efficiently. The system is designed to be user-friendly and easy to navigate in Command line Running.


**Problem Description**:

1. There are 80 seats in a coach of a train with only 7 seats in a row and last row of only 3
seats. For simplicity, there is only one coach in this train.
2. One person can reserve up to 7 seats at a time.
3. If a person is reserving seats, the priority will be to book them in one row.
4. If seats are not available in one row then the booking should be done in such a way that the
nearby seats are booked.
5. User can book as many tickets as s/he wants until the coach is full.
6. You don’t have to create login functionality for this application.

**Features**:

--Book seats on a train coach
--View available seats on a coach


**How to Use**:

--Run the seat_reservation.py script to start the system.
--Follow the prompts to book  seat reservations.
--Use the view_seats function to view available seats on a coach.

**Technical Details**:

--The system uses a simple in-memory data structure to manage seat reservations.
--Each train coach is represented by a TrainCoach object, which contains a 2D list of seats.
--seat reservations are managed using a combination of lists and dictionaries.

**Future Development**:

--Implement a database to store seat reservation data for persistence.
--Add user authentication and authorization to restrict access to certain features.
--Enhance the user interface to provide a more intuitive experience.
