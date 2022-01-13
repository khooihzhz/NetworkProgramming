from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/show_login', methods=["POST"])
def show_login():
    roles = request.form.get("roles")
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("success_login.html",
                           roles=roles,
                           username=username,
                           password=password)


@app.route('/show_signup', methods=["POST"])
def show_signup():
    student_id = request.form.get("student_id")
    student_name = request.form.get("student_name")
    email = request.form.get("email")
    date = request.form.get("date")
    gender = request.form.get("gender")
    education = request.form.get("education")
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("success_signup.html",
                           student_id=student_id,
                           student_name=student_name,
                           email=email,
                           date=date,
                           gender=gender,
                           education=education,
                           username=username,
                           password=password)
