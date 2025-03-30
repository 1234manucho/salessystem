from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('daily_management.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        description TEXT,
        outcome REAL,
        sales REAL
    )
    ''')
    conn.commit()
    conn.close()

# Route to display records
@app.route('/')
def index():
    conn = sqlite3.connect('daily_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM daily_records')
    records = cursor.fetchall()
    conn.close()
    return render_template('index.html', records=records)

# Route to add a record
@app.route('/add', methods=['POST'])
def add_record():
    date = request.form['date']
    description = request.form['description']
    outcome = request.form['outcome']
    sales = request.form['sales']
    conn = sqlite3.connect('daily_management.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO daily_records (date, description, outcome, sales)
    VALUES (?, ?, ?, ?)
    ''', (date, description, float(outcome), float(sales)))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to delete a record
@app.route('/delete/<int:record_id>')
def delete_record(record_id):
    conn = sqlite3.connect('daily_management.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM daily_records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
