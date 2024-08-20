from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Define a route for the home page

@app.route('/')
def home():
    return render_template('index.html')



# Define a route for the Login page 
@app.route('/login')
def login():
    return render_template('dashboard.html')

# Define a route for the dashboard page 
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/userdetails')
def user_details():
    return render_template('userdetails.html')

# Define a route for the view all ticket 
@app.route('/viewticket')
def viewticket():
    return render_template('viewticket.html')


@app.route('/deleteticket')
def delete_ticket():
    # ticket_id = request.form['ticket_id']
   
    return render_template('deleteticket.html')



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
