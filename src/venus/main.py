"""
Venus starter and main loop.
"""
from flask import Flask
from venus.resources import numbers


app = Flask(__name__)
# app.debug = True
app.register_blueprint(numbers.numbers_blueprint)


@app.route("/healthcheck")
def healthcheck():
    """
    Return "Atchim!" if service is running.
    """
    return "Atchim!"


if __name__ == "__main__":
    app.run()
