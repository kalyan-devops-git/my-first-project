from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <h1>Sample Python Project2 jenkins</h1>
        <form action="/greet" method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    """)

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    greeting = f"Hello, {name}! Welcome to the sample Python project."
    return render_template_string(f"""
        <h1>{greeting}</h1>
        <form action="/add" method="post">
            <label for="num1">Enter the first number:</label>
            <input type="number" id="num1" name="num1" step="any" required>
            <br>
            <label for="num2">Enter the second number:</label>
            <input type="number" id="num2" name="num2" step="any" required>
            <br>
            <button type="submit">Add Numbers</button>
        </form>
    """)

@app.route("/add", methods=["POST"])
def add():
    num1 = float(request.form.get("num1"))
    num2 = float(request.form.get("num2"))
    result = num1 + num2
    return render_template_string(f"""
        <h1>The sum is: {result}</h1>
        <a href="/">Go back to home</a>
    """)

if __name__ == "__main__":
    app.run(debug=True)