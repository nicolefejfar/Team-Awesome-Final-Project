# Import the functions we need from flask
from flask import Flask
from flask import render_template 
from flask import jsonify
# from config import password

# Instantiate the Flask application. 
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching

# Define application Routes
@app.route("/")
def IndexRoute():

    webpage = render_template("index.html")
    return webpage

@app.route("/about")
def AboutRoute():
    webpage = render_template("about.html", title_we_want="About Us")
    return webpage

@app.route("/visualizations")
def VisRoute():
    webpage = render_template("visualizations.html", title_we_want="Visualizations")
    return webpage

# final required code for flask server
if __name__ == '__main__':
    app.run(debug=True)