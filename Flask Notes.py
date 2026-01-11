"""
========================================================
FLASK – THEORY, KEY CONCEPTS & PRACTICAL EXAMPLES
Author: Vatsal Negi
========================================================

Flask is a lightweight web application framework written in Python.
It is developed by Armin Ronacher and maintained by the Pocco team.

Flask is based on:
1. Werkzeug – WSGI toolkit
2. Jinja2 – Template engine

Both are Pocco projects.
========================================================
"""

# ======================================================
# INTRODUCTION TO FLASK
# ======================================================

"""
THEORY:
Flask is called a micro web framework because it does not require
particular tools or libraries. It is simple, flexible, and gives
developers full control over application design.

KEY CONCEPTS:
- Lightweight and minimal
- Easy to learn
- Highly extensible
- Ideal for APIs and small-to-medium web apps
"""

# ======================================================
# INSTALLING FLASK
# ======================================================

"""
THEORY:
Flask can be installed using pip, Python's package manager.

KEY CONCEPTS:
- Virtual environment recommended
- Cross-platform support

COMMAND:
pip install flask
"""

# ======================================================
# CREATING FIRST FLASK APPLICATION
# ======================================================

"""
THEORY:
A Flask application starts by creating an instance of the Flask class.

KEY CONCEPTS:
- Flask app object
- app.run() starts development server
"""

from flask import Flask, request, redirect, url_for, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Web Framework 🚀"

# ======================================================
# FLASK ROUTING
# ======================================================

"""
THEORY:
Routing connects URLs to Python functions.

KEY CONCEPTS:
- @app.route decorator
- Each route must return a response
"""

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/contact")
def contact():
    return "Contact: support@example.com"

# ======================================================
# HTTP METHODS – GET AND POST
# ======================================================

"""
THEORY:
HTTP methods define how data is sent between client and server.

KEY CONCEPTS:
- GET: fetch data
- POST: submit data securely
- request object
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return f"Login successful for {username}"
    
    return """
        <form method="post">
            <input type="text" name="username" placeholder="Enter Username">
            <input type="submit">
        </form>
    """

# ======================================================
# VARIABLE RULES (DYNAMIC URLS)
# ======================================================

"""
THEORY:
Flask allows dynamic URLs using variable rules.

KEY CONCEPTS:
- <variable_name>
- Type converters: int, float, string
"""

@app.route("/user/<username>")
def user_profile(username):
    return f"Welcome {username}"

@app.route("/product/<int:product_id>")
def product(product_id):
    return f"Product ID: {product_id}"

# ======================================================
# HTML PAGE RENDERING
# ======================================================

"""
THEORY:
Flask uses Jinja2 for rendering HTML templates.

KEY CONCEPTS:
- render_template
- render_template_string
"""

@app.route("/dashboard")
def dashboard():
    html = """
    <h1>Dashboard</h1>
    <p>You are logged in</p>
    <a href="/logout">Logout</a>
    """
    return render_template_string(html)

# ======================================================
# URL REDIRECTION
# ======================================================

"""
THEORY:
Redirection sends users from one route to another.

KEY CONCEPTS:
- redirect()
- url_for()
"""

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

# ======================================================
# FLASK API CREATION
# ======================================================

"""
THEORY:
Flask is widely used for building REST APIs.

KEY CONCEPTS:
- jsonify()
- JSON data exchange
- REST principles
"""

@app.route("/api/info", methods=["GET"])
def api_info():
    return jsonify({
        "framework": "Flask",
        "language": "Python",
        "type": "Web Framework"
    })

@app.route("/api/sum", methods=["POST"])
def api_sum():
    data = request.get_json()
    result = data["a"] + data["b"]
    return jsonify({"sum": result})

# ======================================================
# APPLICATION EXECUTION
# ======================================================

"""
HOW TO RUN:
1. Install Flask
2. Run: python flask_notes_with_examples.py
3. Open browser:
   http://127.0.0.1:5000/
"""

if __name__ == "__main__":
    app.run(debug=True)

