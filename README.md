# Flask-MLops-Project
A Machine Learning based web application that predicts house prices based on user inputs such as Living Area, Number of Rooms, and Postal Code.
## 🚀 Features
- Predicts house prices using a trained Machine Learning model
- Flask REST API backend
- Simple and responsive HTML/CSS frontend
- Dockerized application for easy deployment
- JSON-based API communication
## 🛠️ Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS
- Docker
- Git & GitHub
## ⚙️ Installation
Clone the repository:

```bash
git clone https://github.com/rakshitakanwar/House-Price-Prediction.git
```

Move into the project folder:

```bash
cd House-Price-Prediction
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the Flask backend:

```bash
python backend/app.py
```

Open the frontend:

```
frontend/index.html
```

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t house-price-app .
```

Run the container:

```bash
docker run -d -p 5000:5000 house-price-app
```

Backend will be available at:

```
http://127.0.0.1:5000
```

## 📥 Input Features

- Living Area (sq ft)
- Number of Rooms
- Postal Code

## 📤 Output

Predicted House Price

## 📌 Future Improvements

- Add more house features for better prediction
- Improve model accuracy
- Deploy on AWS or Render
- Build a React frontend

## 👩‍💻 Author

**Rakshita Kanwar**

GitHub: https://github.com/rakshitakanwar
