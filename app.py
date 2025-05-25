from flask import Flask, render_template
from analysis import analyze_jobs

app = Flask(__name__)

@app.route('/')
def index():
    data = analyze_jobs("jobs.csv")  # Or "data/indeed_jobs.csv"
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)