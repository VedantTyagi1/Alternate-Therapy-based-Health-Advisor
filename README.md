# Alternate Therapy Based Health Advisor

A Flask-based machine learning web application that predicts Ayurvedic doshas (`Vata`, `Pitta`, `Kapha`) based on user-selected symptoms.

## Features

* Predicts dosha using a Decision Tree Machine Learning model
* Clean and responsive web interface
* Users can select up to 3 symptoms
* Built using Flask and scikit-learn
* Lightweight and easy to deploy

---

# Tech Stack

## Frontend

* HTML
* CSS
* Bootstrap (optional)

## Backend

* Flask

## Machine Learning

* scikit-learn
* pandas
* NumPy

---

# Project Structure

```text
Alternate-Therapy-based-Health-Advisor/
│
├── app.py
├── d1.csv
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/VedantTyagi1/Alternate-Therapy-based-Health-Advisor.git
```

## Navigate to Project Folder

```bash
cd Alternate-Therapy-based-Health-Advisor
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Machine Learning Workflow

```text
User selects symptoms
        ↓
Symptoms converted into feature vector
        ↓
Decision Tree model predicts dosha
        ↓
Prediction displayed on webpage
```

---


# Deployment

This project can be deployed using:

* Render
* Railway
* Heroku

---

# Future Improvements

* Add user authentication
* Add REST API endpoints
* Improve UI using Bootstrap/React
* Add prediction confidence score
* Add multiple ML models
* Store prediction history in database
* Deploy using Docker

---

# Author

Vedant Tyagi

GitHub:
[https://github.com/VedantTyagi1](https://github.com/VedantTyagi1)
