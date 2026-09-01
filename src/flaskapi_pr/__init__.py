from flask import Flask, request, render_template

app = Flask(__name__)


@app.post("/handle_post")
def handle_post():
    data = request.json
    print(data)
    return data


if __name__ == "__main__":
    app.run(debug=True)
