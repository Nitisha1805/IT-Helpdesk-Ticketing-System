from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ---------------- #

def init_db():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            issue_type TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Open'
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# ---------------- USER PAGE ---------------- #

@app.route('/')
def home():
    return render_template('index.html')

# ---------------- SUBMIT TICKET ---------------- #

@app.route('/submit', methods=['POST'])
def submit_ticket():

    name = request.form['name']
    issue_type = request.form['issue_type']
    description = request.form['description']

    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tickets (name, issue_type, description)
        VALUES (?, ?, ?)
    ''', (name, issue_type, description))

    conn.commit()
    conn.close()

    return redirect('/')

# ---------------- ADMIN PANEL ---------------- #

@app.route('/admin')
def admin():

    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()

    conn.close()

    return render_template('admin.html', tickets=tickets)

# ---------------- UPDATE STATUS ---------------- #

@app.route('/update/<int:id>', methods=['POST'])
def update_status(id):

    status = request.form['status']

    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    ''', (status, id))

    conn.commit()
    conn.close()

    return redirect('/admin')

# ---------------- RUN APP ---------------- #

if __name__ == '__main__':
    app.run(debug=True)