from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods = ["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    
    return render_template("result.html", name=name, email=email)
    
    # return f"details submitted successfully with name - {name} and given email - {email}"
    

if __name__=="__main__":
    app.run(debug=True)
    