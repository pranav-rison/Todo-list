# 🖤 Black & White Flask To-Do List

A minimal, black-and-white **Flask To-Do List web app** with a retro/industrial UI.  
Tasks are stored using **SQLite + SQLAlchemy**, and the interface is optimized for both desktop and mobile.

---

## ✨ Features

- ➕ Add tasks with title & description
- 🗑️ Delete tasks instantly
- 🕒 Automatic timestamp for each task
- 🗄️ Persistent storage using SQLite
- 🎨 Modern black & white brutalist UI
- 📱 Mobile-friendly layout

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **HTML / CSS (B&W Brutalist Theme)**

---

## 📁 Project Structure

project/
│
├── app.py
├── instance/
│ └── todo.db
├── templates/
│ └── home.html
└── README.md



## 🚀 Getting Started

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app

2️⃣ Create Virtual Environment
python -m venv flaskvenv

Activate it:

Windows
flaskvenv\Scripts\activate
Mac / Linux
source flaskvenv/bin/activate

3️⃣ Install Dependencies
pip install flask flask-sqlalchemy

4️⃣ Run the App
flask run
or
http://127.0.0.1:5000/

🗃️ Database

Uses SQLite

Database file: instance/todo.db

Tables are automatically created on first run

💡 You can inspect the database using SQLite Viewer to see live task changes.
| Route          | Method | Description       |
| -------------- | ------ | ----------------- |
| `/`            | GET    | Display all tasks |
| `/`            | POST   | Add a new task    |
| `/delete/<id>` | GET    | Delete a task     |

📸 UI Preview

Black & white brutalist design

Bold borders & hard shadows

Monospace industrial font

Mobile-responsive
📌 Notes

Tasks are permanently deleted once removed

Debug mode is enabled by default

Port can be changed in app.py if needed

🧑‍💻 Author

Built with rison ❤️ using Flask
Feel free to fork, improve, or customize

📜 License

This project is open-source and free to use.

---

If you want, I can:
- Add **screenshots section**
- Write a **short GitHub description**
- Add **requirements.txt**
- Or make it look more “open-source pro” 😎



