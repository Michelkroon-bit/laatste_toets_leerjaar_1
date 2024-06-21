import sqlite3

def get_all_cars():
    
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        usage REAL NOT NULL,  -- Changed to REAL to reflect kilometers per liter
        tankvolume REAL NOT NULL
    )
''')
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    
    conn.close()

    return cars

all_cars = get_all_cars()

for car in all_cars:
    print(f"ID: {car[0]}, Brand: {car[1]}, Model: {car[2]}, Usage: {car[3]} km/l, Tank Volume: {car[4]} liters")
