from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/')
def front_page():
    df = pd.read_csv("C:/Users/bengi/PycharmProjects/QG_Project/Downloads/ItJobsWatchTop30.csv", encoding= 'unicode_escape')
    return df.to_html()


if __name__ == "__main__":
    app.run()
