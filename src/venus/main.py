"""
Venus starter and main loop.
"""
from flask import Flask

from venus.resources import numbers
from venus.utils import middleware

app = Flask(__name__)
app.register_blueprint(numbers.api_numbers)

app.debug = True
# app.wsgi_app = middleware.LogMiddleware(app)


@app.route("/healthcheck")
def healthcheck():
    """
    Return "Atchim!" if service is running.
    """
    return "Atchim!"


if __name__ == "__main__":
    app.run()
