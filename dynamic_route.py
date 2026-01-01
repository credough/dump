from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return f"hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)

    # try http://127.0.0.1:5000/hello/Pogi