# 🧠 Health AI Prediction System

A Django-based web application that predicts multiple health conditions (Diabetes, Heart Disease, Stress) and provides AI-powered insights with a clean and modular backend structure.

---

## 📁 Project Structure

```
HEALTH_AI_PROJECT/
│
├── app/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── base.html
│   │   ├── chat.html
│   │   ├── diabetes.html
│   │   ├── heart.html
│   │   ├── index.html
│   │   └── stress.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── ai.py
│   ├── apps.py
│   ├── chat_memory.py
│   ├── context_processor.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── core/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── models/
│   ├── diabetes_features.pkl
│   ├── diabetes_model.pkl
│   ├── diabetes.csv
│   ├── heart_features.pkl
│   ├── heart_model.pkl
│   ├── heart.csv
│   ├── stress_features.pkl
│   ├── stress_model.pkl
│   └── student-mental-health.csv
│
├── venv/
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Features

* 🩺 Diabetes Prediction
* ❤️ Heart Disease Prediction
* 🧠 Stress Detection
* 💬 AI Chat Support
* 📊 ML Model Integration using `.pkl` files
* 🌐 Dynamic Templates with Django

---

## 🧩 Tech Stack

* Backend: Django
* Machine Learning: Scikit-learn (Pickle models)
* Frontend: HTML, CSS
* Database: SQLite
* AI Integration: OpenAI API

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd project-folder
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start Server

```bash
python manage.py runserver
```

---

## 📡 Application Routes

| Route        | Description              |
| ------------ | ------------------------ |
| `/`          | Home Page                |
| `/diabetes/` | Diabetes Prediction      |
| `/heart/`    | Heart Disease Prediction |
| `/stress/`   | Stress Prediction        |
| `/chat/`     | AI Chat Interface        |

---

## 🧠 How It Works

1. User inputs health data
2. Django processes request via views
3. ML model (.pkl) predicts result
4. AI module generates insights
5. Response rendered on UI

---

## 🔒 Best Practices Used

* Modular Django app structure
* Separation of logic (views, utils, AI)
* Environment variable security
* Reusable templates

---

## 🚀 Future Improvements

* Add user authentication
* Dashboard with analytics
* Model accuracy improvements
* REST API support
* React frontend integration

---

## 👨‍💻 Author

Utkarsh

---

## ⭐ Support

If you found this helpful, give it a ⭐ on GitHub!
