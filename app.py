from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import os
import yagmail

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Home_page.html")


@app.route("/home")
def home():
    return render_template("Home_page.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    sender_email = os.getenv('CLUB_ID')
    password = os.getenv('CLUB_PASSWORD')
    receiver_email = email
    president_email = 'simratsingh261@gmail.com'

    body_to_contacter = """\
    <html>
    <body>
        <h2>Thank you for reaching out to us :)</h2>
        <h3>We will be contacting you soon!</h3>
    </body>
    </html>
    """
    body_to_president = f"{name} has contacted {sender_email}.\n\n\nEmail: {receiver_email}\n\n\nSubject: {subject}\n\n\nMessage -\n\n{message}"
    body_to_self = f"{name} has contacted.\n\n\nEmail: {receiver_email}\n\n\nSubject: {subject}\n\n\nMessage -\n\n{message}"

    yag = yagmail.SMTP(sender_email, password)

    yag.send(
        to=receiver_email,
        subject="Reply to Contact Form",
        contents=body_to_contacter
    )

    yag.send(
        to=president_email,
        subject="Contact Form Entry",
        contents=body_to_president
    )

    yag.send(
        to=sender_email,
        subject="Contact Form Entry",
        contents=body_to_self
    )

    return redirect(url_for("home"))


@app.route("/blog")
def blog():
    return render_template("blog_page.html")

@app.route("/team")
def team():
    return render_template("teampage.html")


@app.route("/projects")
def projects():
    return render_template("Home_page.html")


@app.route("/blog/Humanoids-are-a-boon-or-a-bane")
def blog1():
    return render_template("Blogs/blog1.html")


@app.route("/blog/Future-of-humanoids")
def blog2():
    return render_template("Blogs/blog2.html")


@app.route("/blog/Humanoid-robots-One-step-closer-to-holistic-automation")
def blog3():
    return render_template("Blogs/blog3.html")


@app.route("/blog/Sophia-The-humanoid-robot")
def blog4():
    return render_template("Blogs/blog4.html")


@app.route("/blog/Humanoid-robot-applications-in-COVID-19")
def blog5():
    return render_template("Blogs/blog5.html")    


if __name__ == "__main__":
    app.run(debug=True)
