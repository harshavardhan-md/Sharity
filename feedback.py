from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import time

app = Flask(__name__)

# MongoDB Configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/contactFormDB'
mongo = PyMongo(app)

# Route to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        fullName = request.form['fullName']
        email = request.form['email']
        message = request.form['message']

        # Save form data to MongoDB
        mongo.db.contacts.insert_one({
            'fullName': fullName,
            'email': email,
            'message': message
        })

        # Delayed response to simulate feedback
        time.sleep(1.2)
        return '<script>alert("Feedback received"); window.location="/";</script>'
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
