from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["POST","GET"])
def index():
    note = request.args.get("note")
    notes.append(note)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True,port=5004)