"""
Venus starter and main loop.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/healthcheck")
def healthcheck():
    """
    Return "Atchim!" if service is running.
    """
    return "Atchim!"


if __name__ == "__main__":
    app.run()
