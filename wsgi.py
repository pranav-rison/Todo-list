# flask run     to run directly  or app.py
# python -m venv flaskvenv
# flaskvenv\Scripts\activate

# ! sqlite viewer  to view live changes happning in db in instance folder todo.db

# http://127.0.0.1:5000/

# from flask import Flask,render_template
# app=Flask(__name__)

# decorator  extending the code so addition adding 
# @app.route("/")    
# def hello_world():
#     return "Hello, World!"

# @app.route("/next")
# def next_page():
#     return "Next, World!"

# @app.route("/") 
# def hello_world():
#     return render_template('home.html')

# if __name__=='__main__':
#     app.run(debug=True)
    # app.run(debug=True,port=8000)   to change the port 


from flask import Flask, render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Good practice to suppress warnings

db = SQLAlchemy(app)

# Database model (table)
class Todo(db.Model):
    # Note: Integer and String must be capitalized
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    # Passing datetime.utcnow without () so it executes when the record is created
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Todo {self.id}>"
    
# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/",methods=["GET",'POST'])
def home():
    if request.method=='POST':
        t = request.form['title']
        d = request.form['desc']

        todo=Todo(title=t,desc=d)    # class of todo class
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    
    all_todo = Todo.query.all()
    return render_template('home.html', all_todo=all_todo)

@app.route("/delete/<int:id>")
def delete(id):
    todo=Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)