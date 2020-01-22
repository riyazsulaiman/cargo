from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("/")

@app.route("/aboutus.html")
def aboutus():
   return render_template("aboutus.html")

@app.route("/airlines.html")
def airlines():
   return render_template("airlines.html")

@app.route("/customers.html")
def customers():
   return render_template("customers.html")

@app.route("/signup.html")
def signup():
   return render_template("signup.html")

@app.route("/login.html")
def login():
   return render_template("login.html")

@app.route("/blog.html")
def blog():
   return render_template("blog.html")

@app.route("/blog-details.html")
def blogdetails():
   return render_template("blog-details.html")

if __name__ == '__main__':
   app.run(debug = True)