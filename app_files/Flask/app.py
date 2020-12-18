from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/')
def front_page():
    file_location = input("Enter file location")
    df = pd.read_csv(f"{file_location}/ItJobsWatchTop30.csv", encoding= 'unicode_escape')
    return df.to_html()


if __name__ == "__main__":
    app.run()
