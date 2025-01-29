# Source : https://flask.palletsprojects.com/en/3.0.x/
# Source : https://pymongo.readthedocs.io/en/stable/
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__, template_folder='survey_form')

# MongoDB Setup tutorial
# Source : https://www.mongodb.com/docs/manual/tutorial/
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client.user_data  # Database name
users_collection = db.users  # Collection name

@app.route("/")
def show_survey():
    """Display the survey form"""
    # Source : https://flask.palletsprojects.com/en/3.0.x/api/#flask.render_template
    return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def handle_submission():
    """Process form submission and store in MongoDB"""
    # Source : https://flask.palletsprojects.com/en/3.0.x/reqcontext/
    
    # Get basic user information
    age = int(request.form["age"])
    gender = request.form["gender"]
    income = float(request.form["income"])
    
    # Process expense data
    expenses = {
        "utilities": float(request.form["utilities"]),
        "entertainment": float(request.form["entertainment"]),
        "school_fees": float(request.form["school_fees"]),
        "shopping": float(request.form["shopping"]),
        "healthcare": float(request.form["healthcare"])
    }

      # Source : https://pymongo.readthedocs.io/en/stable/tutorial.html#inserting-a-document
    user_data = {
        "age": age,
        "gender": gender,
        "income": income,
        "expenses": expenses
    }
    
    # Insert into MongoDB collection
    users_collection.insert_one(user_data)
    
    return redirect(url_for("show_survey"))

if __name__ == "__main__":
    # Run Flask server
    # Source :https://flask.palletsprojects.com/en/3.0.x/quickstart/
    app.run(debug=True)