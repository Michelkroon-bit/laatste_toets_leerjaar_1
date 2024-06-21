import sqlite3

def list_sahara_cars(destination_name: str) -> list:
    cars = []
    conn = sqlite3.connect('travel_db.db')
    cursor = conn.cursor()
        
    cursor.execute('SELECT distance FROM destinations WHERE name = ?', (destination_name,))
    resultaat = cursor.fetchone()
    if resultaat == None:
        return cars
    
    afstand = resultaat[0]
    
    cursor.execute('''select brand, model, usage, tankvolume from cars''')
    car_data = cursor.fetchall()
    
    for brand, model, usage, tankvolume in car_data:
        max_afstand = (tankvolume / usage) *100 
        if max_afstand >= afstand:
            cars.append(f"{brand} {model}")
            return cars
    



print(f"Test 1 {list_sahara_cars('Tunis')}\n")
print(f"Test 2 {list_sahara_cars('Tripoli')}\n")
print(f"Test 3 {list_sahara_cars('Cairo')}\n")
print(f"Test 4 {list_sahara_cars('Bamako')}\n")
print(f"Test 5 {list_sahara_cars('Khartoum')}\n")

# code om de cars te selecteren die de afstand in één keer kunnen overbruggen
        