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




# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)