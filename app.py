from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persons = db.Column(db.String(15), nullable=True)
    todos = db.relationship('Todo', backref='name')

    def __repr__(self):
        return f'{self.persons}'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=True)
    complete = db.Column(db.Boolean)
    name_id = db.Column(db.Integer, db.ForeignKey('name.id'))

    def __repr__(self):
        return f"Todo('{self.id}', '{self.task}')"
db.create_all()

@app.route("/")
def home():
    todo_list = Todo.query.all()
    name_list = Name.query.all()
    return render_template("home.html", todo_list=todo_list,name_list=name_list)

@app.route("/add", methods=['POST', 'GET'])
def add():

    task = request.form.get("task")
    persons = request.form.get("new_person")
    new_person = Name(persons=persons)
    db.session.add(new_person)
    db.session.commit()
    new_task = Todo(task=task, complete=False)
    db.session.add(new_person)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:Todo_id>")
def update(Todo_id):
    todo = Todo.query.filter_by(id=Todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:Todo_id>")
def delete(Todo_id):
    task = Todo.query.filter_by(id=Todo_id).first()
    name = Name.query.all()
    db.session.delete(name[-1])
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    
#webhook
