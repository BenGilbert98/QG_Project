from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/')
def front_page():
    df = pd.read_csv("~Downloads\ItJobsWatchTop30.csv")
    return df.to_html()

if __name__ == "__main__":
    app.run()
