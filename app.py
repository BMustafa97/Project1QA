from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)          #print this
    task = db.Column(db.String(100))                      #print this
    complete = db.Column(db.Boolean)
    tasks = db.relationship('Name', backref="Todo")
    def __repr__(self):
        return f"Todo('{self.id}', '{self.task}')"

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))
    persons = db.Column(db.String(15))
    def __repr__(self):
        return f"Name('{self.persons}')"

@app.route("/")
def home():
    todo_list = Todo.query.all()
    new_person = Name.query.all()
    return render_template("home.html", todo_list=todo_list, new_person=new_person)


@app.route("/add", methods=["POST", "GET"])
def add():
    task = request.form.get("task")   #maybe change title to task?
    new_todo = Todo(task=task, complete=False)
    persons = request.form.get("persons")
    new_person = Name(persons=persons)
    db.session.add(new_todo)
    db.session.add(new_person)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)