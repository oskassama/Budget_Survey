# Source : https://docs.python.org/3/library/csv.html
import csv

# Source : https://pymongo.readthedocs.io/en/stable/
# Source : https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient

def export_to_csv():
    """Export MongoDB data to CSV file"""
    
    # MongoDB Make a connection reference
    # Source : https://pymongo.readthedocs.io/en/stable/tutorial.html#making-a-connection
    mongo = MongoClient("mongodb://localhost:27017/")
    db = mongo.user_data
    
    # Find more than one document on MongoDB
    # Source :https://pymongo.readthedocs.io/en/stable/tutorial.html#querying-for-more-than-one-document
    users = db.users.find()

    # CSV writer reference
    # Source : https://docs.python.org/3/library/csv.html#writer-objects
    with open("user_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        # Write CSV header
        writer.writerow([
            "Age", "Gender", "Income",
            "Utilities","Utilities", "Entertainment",
            "School Fees", "Shopping", "Healthcare"
        ])
        
        # Write data rows
        for user in users:
            writer.writerow([
                user["age"],
                user["gender"],
                user["income"],
                user["expenses"]["utilities"],
                user["expenses"]["entertainment"],
                user["expenses"]["school_fees"],
                user["expenses"]["shopping"],
                user["expenses"]["healthcare"]
            ])
    
    print("Data exported to user_data.csv")

if __name__ == "__main__":
    export_to_csv()