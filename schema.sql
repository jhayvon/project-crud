

CREATE TABLE IF NOT EXISTS flight_details(
    flight_id INTEGER PRIMARY KEY,
    passenger_name TEXT NOT NULL,
    contact TEXT NOT NULL,
    fight_date TEXT NOT NULL,
    gate TEXT NOT NULL,
    boarding_time TEXT NOT NULL,
    departure TEXT NOT NULL,
    arrival TEXT NOT NULL,
    seat TEXT NOT NULL,
    fare_class TEXT NOT NULL
);