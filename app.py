from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="myhope@123",
    database="school"
)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Add stud
@app.route('/add', methods=['POST'])
def add_stud():
    name = request.form['name']

    cursor = db.cursor()
    cursor.execute("INSERT INTO stud (name) VALUES (%s)", (name,))
    db.commit()

    return redirect('/stud')

# Show all stud
@app.route('/stud')
def stud():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM stud")
    data = cursor.fetchall()

    return render_template('stud.html', stud=data)

app.run(debug=True)
