from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dictionary.html")


@app.route("/api/v1/<word>")
def api(word):
    df = pd.read_csv("dictionary.csv")
    return {"description": df.loc[df['word'] == word]['definition'].squeeze(),
            "word": word}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
