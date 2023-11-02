# Import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data to simulate seat availability
available_seats = {
    "Train1": 50,
    "Train2": 30,
    "Train3": 20,
}

# Sample data to store reservations
reservations = []

# Define a dictionary for fare information
fare_info = {
    "Train1": {"FirstClass": 50, "SecondClass": 30},
    "Train2": {"FirstClass": 40, "SecondClass": 20},
    "Train3": {"FirstClass": 60, "SecondClass": 35},
}

# Define a reservation form
class Reservation:
    def __init__(self, train, passenger_name, num_tickets, travel_class, fare):
        self.train = train
        self.passenger_name = passenger_name
        self.num_tickets = num_tickets
        self.travel_class = travel_class
        self.fare = fare

# Route for the reservation form
@app.route('/')
def reservation_form():
    return render_template('reservation_form.html', available_seats=available_seats)

# Handle form submission
@app.route('/reserve', methods=['POST'])
def reserve():
    train = request.form['train']
    passenger_name = request.form['passenger_name']
    num_tickets = int(request.form['num_tickets'])
    travel_class = request.form['travel_class']

    if available_seats[train] >= num_tickets:
        fare = fare_info[train][travel_class] * num_tickets
        available_seats[train] -= num_tickets
        reservations.append(Reservation(train, passenger_name, num_tickets, travel_class, fare))
        return render_template('reservation_confirmation.html', reservation=reservations[-1])

    return "Sorry, not enough seats available for this train."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
