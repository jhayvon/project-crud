from flask import Flask, render_template, request, url_for, redirect, flash
import sqlite3
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    conn = sqlite3.connect('flights_reservation.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_detail(id):
    conn = get_db_connection()
    detail = conn.execute('SELECT * FROM flight_details WHERE flight_id = ?',
                             (id,)).fetchone()
    
    if detail is None:
        abort(404)
    return detail

@app.route('/')
def home():
    conn = get_db_connection()
    details = conn.execute('SELECT * FROM flight_details').fetchall()
    conn.close()
    return render_template('home.html', details = details)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':

        passenger_name = request.form['passenger_name']
        contact = request.form['contact']
        fight_date = request.form['contact']
        gate = request.form['gate']
        boarding_time = request.form['boarding_time']
        departure = request.form['departure']
        arrival = request.form['arrival']
        seat = request.form['seat']
        fare_class = request.form['fare_class']

        conn = get_db_connection()
        conn.execute("""INSERT INTO flight_details 
        (           passenger_name,
                    contact,
                    fight_date,
                    gate,
                    boarding_time,
                    departure,
                    arrival,
                    seat,
                    fare_class
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (           
                    passenger_name,
                    contact,
                    fight_date,
                    gate,
                    boarding_time,
                    departure,
                    arrival,
                    seat,
                    fare_class
        )
                    )
        
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    detail = get_detail(id)


    if request.method == 'POST':
        passenger_name = request.form['passenger_name']
        contact = request.form['contact']
        fight_date = request.form['contact']
        gate = request.form['gate']
        boarding_time = request.form['boarding_time']
        departure = request.form['departure']
        arrival = request.form['arrival']
        seat = request.form['seat']
        fare_class = request.form['fare_class']


        conn = get_db_connection()
        conn.execute('''UPDATE flight_details SET passenger_name = ?, contact = ? ,fight_date = ?, gate = ?, boarding_time = ?,
                        departure = ?, arrival= ?, seat = ?, fare_class= ?
                        WHERE flight_id = ?''',
                        (passenger_name, contact, fight_date, gate, boarding_time, departure, arrival, seat, fare_class, id))
        flash('{} was successfully edited!'.format(detail['passenger_name']))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    return render_template('edit.html', details=detail)

@app.route('/<int:id>/delete', methods=('GET', 'POST'))
def delete(id):
    detail = get_detail(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM flight_details WHERE flight_id = ?', (id,))
    conn.commit()
    conn.close()
    flash('{} was successfully deleted!'.format(detail['passenger_name']))
    return redirect(url_for('home')) 

