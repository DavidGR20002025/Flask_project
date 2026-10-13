import smtplib
import os
from flask import Flask, render_template, request


my_email=os.environ.get("MY_EMAIL")
my_password=os.environ.get("MY_PASSWORD")

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("David´s portfolio.html")

@app.route("/contact", methods=["POST"])
def contact():
    name=request.form.get("name")
    email=request.form.get("email")
    subject=request.form.get("subject")
    message=request.form.get("message")
    print(name)
    print(email)
    print(subject)
    print(message)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:{subject}\n\n{name} is trying to contact you his email is {email} and his/her message: {message}")
    return "Message received!"






#Run the app through the code not the terminal
if __name__=="__main__":
    app.run(debug=True)
