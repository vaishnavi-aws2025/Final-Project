from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample tour data
tours = [
    {"id": 1, "name": "Goa Beach Tour", "location": "Goa", "price": 5000, "description": "Enjoy sun and sand!"},
    {"id": 2, "name": "Himalaya Trek", "location": "Himalayas", "price": 15000, "description": "Adventure trekking in the mountains!"}
]

# Store bookings
bookings = []

@app.route('/')
def index():
    return render_template('index.html', tours=tours)

@app.route('/tour/<int:tour_id>')
def tour_detail(tour_id):
    tour = next((t for t in tours if t["id"] == tour_id), None)
    return render_template('tour.html', tour=tour)

@app.route('/tour/<int:tour_id>/booking', methods=['GET', 'POST'])
def booking(tour_id):
    tour = next((t for t in tours if t["id"] == tour_id), None)
    if request.method == 'POST':
        booking_info = {
            "tour": tour["name"],
            "name": request.form["name"],
            "email": request.form["email"],
            "people": request.form["people"]
        }
        bookings.append(booking_info)
        return redirect(url_for('index'))
    return render_template('booking.html', tour=tour)

if __name__ == '__main__':
    app.run(debug=True)
