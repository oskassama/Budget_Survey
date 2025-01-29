
# Income & Spending Survey Tool

**A Flask web application for collecting and analyzing spending data of users.**

---

## Requirements

- **Python 3.10+** ([Download Here](https://www.python.org/downloads/))

- **MongoDB Community Server** ([Download Here](https://www.mongodb.com/try/download/community))

### 2. Python Packages

Install all required packages using the command:

```bash
pip install -r requirements.txt
```plaintext

Contents of `requirements.txt`:

  ```plaintext

Flask==3.0.0
pymongo==4.5.0
pandas==2.1.1
matplotlib==3.7.1
seaborn==0.12.2
jupyter==1.0.0
python-dotenv==1.0.0

  ```plaintext

---

## 🚀 How to Run the Application

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
  ```plaintext

### 2. Set Up MongoDB

1. Install MongoDB from the [official website](https://www.mongodb.com/try/download/community).
2. Start the MongoDB server:
   - On Windows, run: `mongod` in the command prompt.
   - On macOS/Linux, use: `brew services start mongodb-community@6.0` (if installed via Homebrew).

### 3. Configure Environment Variables

- Create a `.env` file in the project root directory with the following content:

  ```
  MONGO_URI=mongodb://localhost:27017
  DATABASE_NAME=survey_tool
  COLLECTION_NAME=participants
  ```

### 4. Run the Flask Application

```bash
python main.py
```

- Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the survey form.

---

## 📊 Analyzing Data

### Export Data to CSV

1. Open a Python terminal or script.
2. Run the following code snippet to export the data from MongoDB to a CSV file:

   ```python
   from data_processing import User

   user = User()
   user.export_to_csv(filename="user_data.csv")
   ```

### Visualize Data

1. Open a Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Load the provided `visualization.ipynb` file.
3. Run the notebook to generate visualizations:
   - **Ages with the highest income**
   - **Gender distribution across spending categories**
4. Export charts as PNG files for further use.

---

## 🌐 Deploying to AWS

### Prerequisites (Windows User)

- IAWS EC2 Instance
- IPuTTY for SSH connection
- IWinSCP for file transfer
- IFlask application ready

### 1. Initial Setup

- Launch an **AWS EC2 instance** with Amazon Linux or Ubuntu.

- Convert .pem key to .ppk using PuTTYgen
- Connect to EC2 instance via PuTTY
- Transfer project files using WinSCP

### 2. Environment Preparation

```bash
# Navigate to project directory
cd ~/flask-app

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn
```

### 3. Environment Preparation

- Open required ports (80, 8000) in AWS EC2 security group

- Allow inbound traffic from 0.0.0.0/0

### 4. Application Deployment

```bash
# Run application with Gunicorn
sudo nohup gunicorn --bind 0.0.0.0:80 main:app > gunicorn.log 2>&1 &
```

### 5. Verification

- Access application via EC2 public DNS

- Check gunicorn.log for any deployment issues
- Verify application is running using ps aux | grep gunicorn

### 6. View Application

- [http://ec2-13-60-240-107.eu-north-1.compute.amazonaws.com:8000/](http://ec2-13-60-240-107.eu-north-1.compute.amazonaws.com:8000/)

---

## 📁 Project Structure

```plaintext
.
├── main.py                 # Flask application
├── surver_form/
│   └── survey.html        # HTML template for survey form
├── data.py                # Python class for data export
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── visualization.ipynb    # Jupyter notebook for data visualization
