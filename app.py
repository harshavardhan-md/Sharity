from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def create_table():
    conn = sqlite3.connect('donations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            location TEXT NOT NULL,
            time_of_day TEXT NOT NULL,
            estimated_delivery_time TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        location = request.form['location']
        time_of_day = request.form['time_of_day']
        estimated_delivery_time = request.form['estimated_delivery_time']
        quantity = request.form['donationAmount']

        conn = sqlite3.connect('donations.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO donations (name, phone, location, time_of_day, estimated_delivery_time, quantity)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, phone, location, time_of_day, estimated_delivery_time, quantity))
        conn.commit()
        conn.close()

        return redirect(url_for('thank_you'))  # Redirect to thank_you route after form submission

@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create the contacts table
def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Create the contacts table
create_table()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for submitting the contact form
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        message = request.form['message']

        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contacts (full_name, email, message)
            VALUES (?, ?, ?)
        ''', (full_name, email, message))
        conn.commit()
        conn.close()

        return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
