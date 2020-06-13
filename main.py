from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")


@app.route("/portfolio/hairsalon")
def hairsalon():
    return render_template("hairsalon.html")


@app.route("/portfolio/hairsalon2")
def hairsalon2():
    return render_template("hairsalon2.html")


@app.route("/portfolio/stars")
def stars():
    return render_template("stars.html")


if __name__ == "__main__":
    app.run()