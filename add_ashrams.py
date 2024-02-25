import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('ashrams.db')
cursor = conn.cursor()

# Create a table for ashrams if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ashrams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        time_of_day TEXT NOT NULL,
        estimated_delivery_time TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

# Sample data for ashrams
locations = ['Nit Jalandhar', 'Jalandhar', 'Phagwara', 'Ludhiana']
times_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
delivery_times = ['9:00 AM', '1:00 PM', '5:00 PM', '8:00 PM']

# Generate random ashram data
ashram_data = []
for i in range(35):
    name = f'Ashram {i + 4}'  # Start with 4 to continue from existing ashram numbers
    location = random.choice(locations)
    time_of_day = random.choice(times_of_day)
    estimated_delivery_time = random.choice(delivery_times)
    quantity = random.randint(20, 150)  # Random quantity between 20 and 150
    ashram_data.append((name, location, time_of_day, estimated_delivery_time, quantity))

# Insert sample data into the ashrams table
cursor.executemany('''
    INSERT INTO ashrams (name, location, time_of_day, estimated_delivery_time, quantity)
    VALUES (?, ?, ?, ?, ?)
''', ashram_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Additional ashrams added to the database successfully.")
