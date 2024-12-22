from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('home-page.html')

# Membership page route
@app.route('/membership')
def membership():
    return render_template('membership-page.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

